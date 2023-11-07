import contextlib
import zipfile
from tqdm import tqdm
import os
from ..functions.writing import log, typewriter, printnlog
import subprocess
import sys
import shutil
import stat
import time
from dotenv import load_dotenv

load_dotenv(".env")

try:
    quiet = eval(os.getenv("QUIET"))
except TypeError:
    quiet = False


def unpack(datelog, args, cachename: str) -> None:
    """
    The unpack function unpacks the downloaded zip file and extracts the data from it.
    It then moves all of the files to their appropriate locations, deletes any unneeded folders,
    and removes the zip file. It also prints out a progress bar for each step.

    :param cachename: Determine the name of the file to extract from
    :return: :
    """
    with zipfile.ZipFile(cachename, mode="r") as zip:
        for member in tqdm(
            iterable=zip.namelist(), total=len(zip.namelist()), desc="Extracting "
        ):
            with contextlib.suppress(zipfile.error):
                zip.extract(member)
                if not quiet:
                    tqdm.write(
                        f"{os.path.basename(member)}({str(os.path.getsize(member))}B)"
                    )
                log(f"{os.path.basename(member)}({str(os.path.getsize(member))}B)")
        zip.close()
    typewriter(printnlog("Done\n", toprint=False))
    typewriter(printnlog("Unpacking second part...\n", toprint=False))
    """
    Extract the data from the xp3 file.
    @param xp3_file - the xp3 file to extract from
    @param output_folder - the folder to extract to
    @param extract_name - the name of the file to extract
    """
    if not quiet:
        subprocess.call(
            [sys.executable, "xp3.py", "data.xp3", "data1", "-e", "neko_vol0_steam"]
        )
    if quiet:
        subprocess.call(
            [
                sys.executable,
                "xp3.py",
                "data.xp3",
                "data1",
                "-e",
                "neko_vol0_steam",
                "-silent",
            ]
        )
    with contextlib.suppress(Exception):
        shutil.move("data1/data", "data")
    mkdir("apphtml")
    mkdir("assets")
    if cachename == "data.xp2":
        move_apphtml()
    remove(cachename)
    remove("data.xp3")


def move_apphtml():
    for r, d, f in os.walk("data1/apphtml/"):
        for file in f:
            shutil.move(
                os.path.join("data1/apphtml/", file), os.path.join("apphtml/", file)
            )
    for r, d, f in os.walk("data1/assets/"):
        for file in f:
            shutil.move(
                os.path.join("data1/assets/", file), os.path.join("assets/", file)
            )
    shutil.rmtree("data1/apphtml")
    shutil.rmtree("data1/assets")
    for i in os.listdir("data1"):
        shutil.move(f"data1/{i}", i)
    shutil.rmtree("data1")


def extract(args, datelog):
    """
    The extract function is used to extract the data files from the game.
    It does this by first finding all of the .xp2 files in your current directory, and then unpacking them using unpack().
    After that, it copies &quot;data&quot; into a backup file called &quot;data_backup&quot;. It then opens up both data and a new file called
    &quot;data_dummy&quot;, which will be used to replace data. The reason for this is because there are some characters in data that
    are not allowed on Windows (such as ':'). This function replaces those characters with ones that are allowed on Windows.

    :param args: Pass the arguments from the command line to this function
    :param datelog: Write to the log file
    :return: A list of the files that have been extracted
    """
    typewriter(printnlog("\nStarting to extract\n", toprint=False))
    with contextlib.suppress(FileNotFoundError):
        datafiles: list = [
            file
            for file in os.listdir("./")
            if file.startswith("data") and file.endswith(".xp2")
        ]
        for i in range(1, len(datafiles) + 1):
            unpack(datelog, args, datafiles[-i])
        shutil.copy("data", "data_backup")
        printnlog("\nDone\n")
        with open("data", "r") as check:
            check_new = open("data_dummy", "w")
            for i in check.read():
                if i == "G":
                    check_new.write("[")
                else:
                    check_new.write(i)
        check_new.close()
        os.mkdir("temp")
        shutil.move("data_dummy", "temp/")
        os.remove("data")
        shutil.move("temp/data_dummy", "data")
        shutil.rmtree("temp")
        os.rename("data_dummy", "data")


def delete(file):
    """
    The delete function is used to delete a file or directory.
        It will attempt to remove the file/directory, and if it fails,
        it will call on_rm_error() which attempts to change permissions of the
        file/directory before attempting removal again.

    :param file: Specify the file to be deleted
    :return: Nothing
    """
    with contextlib.suppress(Exception):
        shutil.rmtree(file, onerror=on_rm_error)


def on_rm_error(func, path, exc_info):
    """
    The on_rm_error function is a callback function that will be called by the shutil.rmtree() function
    if an error occurs while attempting to remove a file or directory. The on_rm_error() function will attempt
    to change the permissions of the file or directory so that it can be removed, and then it will try again.

    :param func: Pass the function that raised the exception
    :param path: Specify the directory to be removed
    :param exc_info: Pass information about the exception that caused the error
    :return: A function that handles the error
    """
    os.chmod(path, stat.S_IWRITE)
    os.unlink(path)


def file_to_datafolder():
    """
    The file_to_datafolder function moves all the files in the current directory to a new folder called datafolder.
    The function also creates subfolders for assets, apphtml.

    :return: A list of files that are in the datafolder
    """
    source_dir = move_to_datafolder("assets/")
    source_dir = move_to_datafolder("apphtml/")
    files: list = [
        "downloadmusic.py",
        "mouse.py",
        "path.py",
        "endscreen.py",
        "login.py",
        "settings.py",
        "game_assets.py",
        "completer.py",
    ]
    for i in files:
        shutil.move(i, f"datafolder/{i}")


def move_to_datafolder(arg0):
    result: str = arg0
    os.mkdir(f"datafolder/{result}")
    for file_name in os.listdir(result):
        shutil.move(os.path.join(result, file_name), f"datafolder/{result}")
    return result


def xp3_finalization():
    """
    The xp3_finalization function is used to repack the data.xp3 file after all of the necessary changes have been made.
    It also deletes any temporary folders that were created during the process.

    :return: None
    """
    if not quiet:
        subprocess.call(
            [
                sys.executable,
                "xp3.py",
                "datafolder",
                "data.xp3",
                "-mode",
                "repack",
                "-e",
                "neko_vol0_steam",
            ]
        )
    if quiet:
        subprocess.call(
            [
                sys.executable,
                "xp3.py",
                "datafolder",
                "data.xp3",
                "-mode",
                "repack",
                "-e",
                "neko_vol0_steam",
                "-silent",
            ]
        )
    shutil.rmtree("datafolder")
    shutil.rmtree("apphtml")
    shutil.rmtree("assets")


def to_zip(logger, cachename, start):
    """
    The to_zip function takes a logger, cachename, and start as arguments.
    It then creates two lists of strings: zipfiles and zipfileswopath.
    The first list contains the names of files to be zipped; the second is identical but without paths.
    Then it creates a list called folders which contains one string: &quot;structs&quot;.  It loops through this list with an index i from 0 to len(folders).  For each value of i, it walks through the folder named by folders[i] (which is always &quot;structs&quot;) and adds all files in that folder to both lists created earlier.

    :param logger: Print the progress of the packing process
    :param cachename: Specify the name of the zip file
    :param start: Calculate the elapsed time of packing
    :return: Nothing
    """
    zipfiles: list[str] = [
        "tests.py",
        "xp3.py",
        "xp3reader.py",
        "xp3writer.py",
        "data.xp3",
    ]
    zipfileswopath: list[str] = [
        "tests.py",
        "xp3.py",
        "xp3reader.py",
        "xp3writer.py",
        "data.xp3",
    ]
    folders: list[str] = ["structs"]
    for folder in folders:
        for path, directories, files in os.walk(folder):
            for file in files:
                file_name: str = os.path.join(path, file)
                zipfiles.append(file_name)
                zipfileswopath.append(file)
    logger.next("")
    with zipfile.ZipFile(cachename, mode="w", compresslevel=5) as zip:
        _extracted_from_to_zip_36(zipfiles, zip, logger, zipfileswopath)
    for folder_ in folders:
        shutil.rmtree(folder_)
    end = time.time()
    logger.stay(f"Elapsed time of packing: {str(end - start)}" + "\n")


def _extracted_from_to_zip_36(zipfiles, zip, logger, zipfileswopath):
    zipfilesnumber: int = len(zipfiles)
    bar = tqdm(range(len(zipfiles)), desc="Packing ")
    zip_kb_old: int = 0
    for i in bar:
        zip.write(zipfiles[i])
        filesizeen: int = sum(zinfo.file_size for zinfo in zip.filelist)
        if not quiet:
            tqdm.write(
                logger.stay(
                    f"{zipfileswopath[i]}({str(os.path.getsize(zipfiles[i]))} KB) -> {str(round(filesizeen - zip_kb_old, 2))} KB",
                    end="",
                    toprint=False,
                )
            )
        zip_kb_old: int = filesizeen
        os.remove(zipfiles[i])
        if i == len(zipfiles) - 1 and not quiet:
            tqdm.write("\n")
    filesizeenend: int = sum(zinfo.file_size for zinfo in zip.filelist)
    logger.prev("\nPacked data have > " + str(filesizeenend) + " KB")
    zip.close()


def del_wn():
    """
    The del_wn function deletes the following files:
        - neko.png
        - waifu.png
        - waifu.gif
        - waifu.mp4

    :return: Nothing
    """
    remove("assets/neko.png")
    remove("assets/waifu.png")
    remove("assets/waifu.gif")
    remove("assets/waifu.mp4")
    remove("assets/video.mp4")


def remove(file: str | list[str]):
    """
    The remove function is a wrapper for the os.remove function that allows you to pass in either a single filepath or
    a list of filepaths and will attempt to remove each one. If an exception occurs, it will be caught and ignored.

    :param file: str | list[str]: Specify the file or files to be removed
    :return: None, which is not a valid return type for the function
    """
    if isinstance(file, str):
        with contextlib.suppress(Exception):
            return os.remove(file)
    elif isinstance(file, list):
        for filepath in file:
            with contextlib.suppress(Exception):
                return os.remove(filepath)


def mkdir(path):
    """
    The mkdir function creates a directory at the specified path.
        If the directory already exists, it will not raise an error.

    :param path: Specify the path of the directory to be created
    :return: None
    """
    os.makedirs(path, exist_ok=True)


def change_quiet_file_op(to):
    """
    The change_quiet_file_op function changes the global variable quiet to True or False.
        This is used in the file_op function to determine whether or not a message should be printed.

    :param to: Set the global quiet variable to true or false
    :return: Nothing
    """
    global quiet
    if to in [True, False]:
        quiet = to
