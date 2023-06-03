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
            try:
                zip.extract(member)
                if not quiet:
                    tqdm.write(
                        f"{os.path.basename(member)}("
                        + str(os.path.getsize(member))
                        + "B)"
                    )
                log(
                    f"{os.path.basename(member)}(" + str(os.path.getsize(member)) + "B)"
                )
            except zipfile.error as e:
                pass
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
    try:
        shutil.move("data1/data", "data")
    except Exception:
        pass
    mkdir("apphtml")
    mkdir("assets")
    if cachename == "data.xp2":
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
    remove(cachename)
    remove("data.xp3")


def extract(args, datelog):
    typewriter(printnlog("\nStarting to extract\n", toprint=False))
    try:
        datafiles: list = []
        for file in os.listdir("./"):
            if file.startswith("data"):
                if file.endswith(".xp2"):
                    datafiles.append(file)
        for i in range(1, len(datafiles) + 1):
            unpack(datelog, args, datafiles[-i])
        shutil.copy("data", "data_backup")
        printnlog("\nDone\n")
        check = open("data", "r")
        check_new = open("data_dummy", "w")
        for i in check.read():
            if i == "G":
                check_new.write("[")
            else:
                check_new.write(i)
        check.close()
        check_new.close()
        os.mkdir("temp")
        shutil.move("data_dummy", "temp/")
        os.remove("data")
        shutil.move("temp/data_dummy", "data")
        shutil.rmtree("temp")
        os.rename("data_dummy", "data")
    except FileNotFoundError:
        pass


def delete(file):
    try:
        shutil.rmtree(file, onerror=on_rm_error)
    except:
        pass


def on_rm_error(func, path, exc_info):
    os.chmod(path, stat.S_IWRITE)
    os.unlink(path)


def file_to_datafolder():
    source_dir: str = "assets/"
    os.mkdir("datafolder/" + source_dir)
    for file_name in os.listdir(source_dir):
        shutil.move(os.path.join(source_dir, file_name), "datafolder/" + source_dir)
    source_dir: str = "apphtml/"
    os.mkdir("datafolder/" + source_dir)
    for file_name in os.listdir(source_dir):
        shutil.move(os.path.join(source_dir, file_name), "datafolder/" + source_dir)
    source_dir: str = "yt_dl/"
    os.mkdir("datafolder/" + source_dir)
    for file_name in os.listdir(source_dir):
        shutil.move(os.path.join(source_dir, file_name), "datafolder/" + source_dir)
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


def xp3_finalization():
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
    shutil.rmtree("yt_dl")
    shutil.rmtree("assets")


def to_zip(logger, cachename, start):
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
    for i in range(0, len(folders)):
        for path, directories, files in os.walk(folders[i]):
            for file in files:
                file_name: str = os.path.join(path, file)
                zipfiles.append(file_name)
                zipfileswopath.append(file)
    logger.next("")
    with zipfile.ZipFile(cachename, mode="w", compresslevel=5) as zip:
        zip_kb_old: int = 0
        zipfilesnumber: int = len(zipfiles)
        bar = tqdm(range(0, len(zipfiles)), desc="Packing ")
        for i in bar:
            zip.write(zipfiles[i])
            filesizeen: int = sum([zinfo.file_size for zinfo in zip.filelist])
            if not quiet:
                tqdm.write(
                    logger.stay(
                        zipfileswopath[i]
                        + "("
                        + str(os.path.getsize(zipfiles[i]))
                        + " KB) -> "
                        + str(round(filesizeen - zip_kb_old, 2))
                        + " KB",
                        end="",
                        toprint=False,
                    )
                )
            zip_kb_old: int = filesizeen
            os.remove(zipfiles[i])
            if i == len(zipfiles) - 1:
                if not quiet:
                    tqdm.write("\n")
        filesizeenend: int = sum([zinfo.file_size for zinfo in zip.filelist])
        logger.prev("\nPacked data have > " + str(filesizeenend) + " KB")
        zip.close()
    for i in range(0, len(folders)):
        shutil.rmtree(folders[i])
    end = time.time()
    logger.stay("Elapsed time of packing: " + str(end - start) + "\n")


def del_wn():
    remove("assets/neko.png")
    remove("assets/waifu.png")
    remove("assets/waifu.gif")
    remove("assets/waifu.mp4")
    remove("assets/video.mp4")


def remove(file: str | list[str]):
    if isinstance(file, str):
        try:
            return os.remove(file)
        except Exception:
            pass
    elif isinstance(file, list):
        for filepath in file:
            try:
                return os.remove(filepath)
            except Exception:
                pass


def mkdir(path):
    os.makedirs(path, exist_ok=True)


def change_quiet_file_op(to):
    global quiet
    if to in [True, False]:
        quiet = to
