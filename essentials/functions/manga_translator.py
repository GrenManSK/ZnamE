import os
import subprocess
from .writing import printnlog, typewriter
from time import sleep
from ..system.file_operations import mkdir
import shutil
from PIL import Image
from tkinter import filedialog


def run_manga_image_translator(env):
    """
    The run_manga_image_translator function is used to install and run the manga-image-translator program.
    
    :param env: Run the program in a specific environment
    :return: The following:
    """
    if os.path.exists("manga-image-translator"):
        typewriter(
            printnlog(
                f"\nChecking for updates\nRunning command\nRunning command: git -C manga-image-translator pull\n",
                toprint=False,
            ),
            ttime=0.01,
        )
        subprocess.call(["git", "-C", "manga-image-translator", "pull"])
        print("")
    else:
        while True:
            vstup = input(
                printnlog(
                    "\nTo install manga-image-translator run this command 'git clone https://github.com/zyddnys/manga-image-translator.git'\nDo you want to complete this action automatically (Y/n) > ",
                    toprint=False,
                )
            ).lower()
            if vstup in ["", "y"]:
                break
            elif vstup == "n":
                return
            else:
                printnlog("Wrong character")
        os.system("git clone https://github.com/zyddnys/manga-image-translator.git")
        typewriter(
            printnlog(
                f"\nDownloading pip requirements\nRunning command: {env} -m pip install -r manga-image-translator/requirements.txt --no-warn-script-location\n",
                toprint=False,
            ),
            ttime=0.01,
        )
        sleep(1)
        os.system(
            env
            + " -m pip install -r manga-image-translator/requirements.txt --no-warn-script-location"
        )
        typewriter(
            printnlog(
                f"\nRunning command: {env} -m pip install -r manga-image-translator/requirements.txt --no-warn-script-location\n",
                toprint=False,
            ),
            ttime=0.01,
        )
        os.system(
            env
            + " -m pip install git+https://github.com/lucasb-eyer/pydensecrf.git --no-warn-script-location"
        )

        mkdir("manga_translator_temp")
        img = Image.new("RGB", (800, 1280), (255, 255, 255))
        img.save("manga_translator_temp/image.png", "PNG")
        os.chdir("manga-image-translator")
        os.system(
            f"{env} -m manga_translator -v --mode batch --translator=google -l ENG -i ../manga_translator_temp"
        )
        os.chdir("..")
        shutil.rmtree("manga_translator_temp")
        shutil.rmtree("manga_translator_temp-translated")

    manga_image_translator(env)


def manga_image_translator(env):
    """
    The manga_image_translator function is a command line interface for the manga_image_translator_command function.
    It allows you to specify the folder and language of your choice, then it calls the manga_image_translator command with those parameters.
    
    :param env: Get the environment variables
    :return: The manga_image_translator function
    """
    folder = None
    lang = "ENG"
    typewriter(
        printnlog(
            "Folder must contains image files\n'folder' to define folder with which you will be working with\n'lang' to define language which will be translated to\n'start' to start program",
            toprint=False,
        ),
        ttime=0.01,
    )
    while True:
        vstup = input("> ")
        if vstup == "folder":
            folder = filedialog.askdirectory(
                initialdir="./", mustexist=True, title="Select manga folder with images"
            )
        if vstup == "lang":
            while True:
                typewriter(
                    printnlog(
                        """CHS: Chinese (Simplified)
CHT: Chinese (Traditional)
CSY: Czech
NLD: Dutch
ENG: English
FRA: French
DEU: German
HUN: Hungarian
ITA: Italian
JPN: Japanese
KOR: Korean
PLK: Polish
PTB: Portuguese (Brazil)
ROM: Romanian
RUS: Russian
ESP: Spanish
TRK: Turkish
UKR: Ukrainian
VIN: Vietnames""",
                        toprint=False,
                    ),
                    ttime=0.01,
                )
                vstup = input("Select language")
                if vstup not in [
                    "CHS",
                    "CHT",
                    "CSY",
                    "NLD",
                    "ENG",
                    "FRA",
                    "DEU",
                    "HUN",
                    "ITA",
                    "JPN",
                    "KOR",
                    "PLK",
                    "PTB",
                    "ROM",
                    "RUS",
                    "ESP",
                    "TRK",
                    "UKR",
                    "VIN",
                ]:
                    print("Wrong language")
                    continue
                lang = vstup
                break
        if vstup == "start":
            if folder is None:
                print("No folder specified")
                continue
            manga_image_translator_command(env, folder, lang)


def manga_image_translator_command(env, folder, lang):
    """
    The manga_image_translator_command function is a wrapper for the manga-image-translator package.
    It takes in three arguments: env, folder, and lang.
    env is the environment variable that points to your Python executable (e.g., /usr/bin/python3).
    folder is the path to your manga image directory (e.g., /home/user/manga_images). 
    lang is the language you want translated into (e.g., ENG for English).
    
    :param env: Specify the environment for the script to run in
    :param folder: Specify the folder where the images are located
    :param lang: Determine the language of the translated text
    :return: The following:
    """
    os.system(
        f"{env} -m manga-image-translator.manga_translator -v --mode batch  --translator=google -l {lang} -i {folder}"
    )
