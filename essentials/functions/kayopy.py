import os
import sys
import subprocess
from .writing import printnlog, typewriter
from time import sleep
import glob
from threading import Thread
import copy


def run_kayopy():
    """
    The run_kayopy function is used to check if the KayoPy folder exists.
    If it does, then it will run a git pull command and then call the kayopy function.
    If not, then it will ask you if you want to install KayoPy automatically or manually.
    
    :return: The kayopy function
    """
    if os.path.exists("KayoPy"):
        typewriter(
            printnlog(
                f"\nChecking for updates\nRunning command\nRunning command: git -C KayoPy pull\n",
                toprint=False,
            ),
            ttime=0.01,
        )
        subprocess.call(["git", "-C", "KayoPy", "pull"])
    else:
        while True:
            vstup = input(
                printnlog(
                    "\nTo install KayoPy run this command 'git clone https://github.com/GrenManSK/KayoPy.git'\nDo you want to complete this action automatically (Y/n) > ",
                    toprint=False,
                )
            ).lower()
            if vstup in ["", "y"]:
                break
            elif vstup == "n":
                return
            else:
                printnlog("Wrong character")
        os.system("git clone https://github.com/GrenManSK/KayoPy.git")
        typewriter(
            printnlog(
                f"\nDownloading pip requirements\nRunning command: {sys.executable} -m pip install -r KayoPy/requirements.txt --no-warn-script-location\n",
                toprint=False,
            ),
            ttime=0.01,
        )
        sleep(1)
        os.system(
            sys.executable
            + " -m pip install -r KayoPy/requirements.txt --no-warn-script-location"
        )


    kayopy()


def kayopy():
    """
    The kayopy function is used to start the KayoPy program.
    It asks if you want to download anime in a folder called Anime, and then starts the KayoPy program with or without that argument.
    
    :return: This function
    """
    while True:
        vstup = input("\nDo you want to download anime in anime folder? (y/n): ")
        if vstup == "y":
            arg = " -ad -of Anime"
            Thread(target=anime_mole, daemon=True).start()
            break
        if vstup == "n":
            arg = ""
            break
    os.system(f"{sys.executable} KayoPy/kayopy/kayopy.py {arg}")
    open("kayopyEND", "x")


def anime_mole():
    """
    The anime_mole function is a daemon that runs in the background and monitors
    the Anime directory for new files. When it finds one, it adds the file to a set
    of anime files. It then writes this set of anime files to disk as an archive.
    
    :return: None
    """
    if os.path.exists("AnimeArchive"):
        with open("AnimeArchive", "r") as file:
            filer = file.readlines()
        anime_tmp: set = set(filer)
        anime: set = set(copy.deepcopy(anime_tmp))
        for item in anime_tmp:
            if not os.path.exists(item):
                anime.remove(item)

    else:
        anime: set = set()
    while True:
        sleep(1)
        if os.path.exists("kayopyEND"):
            break
        if os.path.exists("Anime"):
            for filename in set(glob.glob("Anime/**/**/*", recursive=True)):
                if filename.endswith("tmp") or os.path.isdir(filename):
                    continue
                anime.add(filename)

        anime_text = "".join(item + "\n" for item in anime)
        with open("AnimeArchive", "w") as file:
            file.write(anime_text)
    os.remove("kayopyEND")
