import subprocess
import os
from time import sleep
from .writing import printnlog, typewriter
from ..app_alternations import on_rm_error
import shutil


def get_size(start_path="."):
    """
    The get_size function returns the total size of a directory in bytes.
        It takes one argument, start_path, which is the path to be measured.
        The default value for start_path is &quot;.&quot; (the current working directory).
    
    :param start_path: Specify the path of the directory to be scanned
    :return: The total size of the directory in bytes
    """
    total_size = 0
    for dirpath, dirnames, filenames in os.walk(start_path):
        for f in filenames:
            fp = os.path.join(dirpath, f)
            # skip if it is symbolic link
            if not os.path.islink(fp):
                total_size += os.path.getsize(fp)

    return total_size


def run_voicevox(env):
    """
    The run_voicevox function is used to run the VOICEVOX program.
    It checks if the VOICEVOX folder exists and if it does, it runs a git pull command on that folder.
    If there are any updates, they will be downloaded and installed automatically.
    If there are no updates available or the folder doesn't exist, then it asks you whether you want to download 
    the latest version of VOICEVOX from GitHub using git clone command or not.
    
    :param env: Determine the python environment to run the program in
    :return: The value of the run_voicevox function
    """
    damaged = False
    if os.path.exists("VOICEVOX"):
        size = get_size("VOICEVOX") / 1024 / 1024
        if size < 1000:
            damaged = True
    if os.path.exists("VOICEVOX") and not damaged:
        typewriter(
            printnlog(
                f"\nChecking for updates\nRunning command\nRunning command: git -C VOICEVOX pull\n",
                toprint=False,
            ),
            ttime=0.01,
        )
        subprocess.call(["git", "-C", "VOICEVOX", "pull"])
        typewriter(
            printnlog(
                f"\nRunning VOICEVOX\nRunning command: {env} -m VOICEVOX\n",
                toprint=False,
            ),
            ttime=0.01,
        )
        sleep(1)
        subprocess.call([env, "-m", "VOICEVOX"])
    else:
        if os.path.exists("VOICEVOX"):
            delete_damaged_goods()
        else:
            printnlog("VOICEVOX not found")
        while True:
            vstup = input(
                printnlog(
                    "\nTo install VOICEVOX run this command 'git clone https://github.com/GrenManSK/VOICEVOX.git'\nDo you want to complete this action automatically (Y/n) > ",
                    toprint=False,
                )
            ).lower()
            if vstup in ["", "y"]:
                break
            elif vstup == "n":
                return
            else:
                printnlog("Wrong character")
        typewriter(printnlog("Downloading VOICEVOX\n", toprint=False), ttime=0.01)
        os.system("git clone https://github.com/GrenManSK/VOICEVOX.git")
        typewriter(
            printnlog(
                f"\nDownloading pip requirements\nRunning command: {env} -m pip install -r VOICEVOX/requirements.txt --no-warn-script-location\n",
                toprint=False,
            ),
            ttime=0.01,
        )
        sleep(1)
        os.system(
            env
            + " -m pip install -r VOICEVOX/requirements.txt --no-warn-script-location"
        )
        typewriter(
            printnlog(
                f"\nRunning VOICEVOX\nRunning command: {env} -m VOICEVOX --force-reinstall\n",
                toprint=False,
            ),
            ttime=0.01,
        )
        sleep(1)
        subprocess.call([env, "-m", "VOICEVOX", "--force-reinstall"])


def delete_damaged_goods():
    typewriter(
        printnlog(f"\nFound damaged VOICEVOX\nDeleting ...\n", toprint=False),
        ttime=0.01,
    )
    print("\nWaiting 2 seconds to clear Access Denied Error\n")
    sleep(2)
    for i in os.listdir("VOICEVOX"):
        if i.endswith("git"):
            tmp = os.path.join("VOICEVOX", i)
            while True:
                subprocess.call(["attrib", "-H", tmp])
                break
            shutil.rmtree(tmp, onerror=on_rm_error)
    print("\nWaiting 2 seconds to clear Access Denied Error\n")
    sleep(2)
    shutil.rmtree("VOICEVOX", onerror=on_rm_error)
