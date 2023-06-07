import os
import sys
import subprocess
from .writing import printnlog, typewriter
from time import sleep
import glob
from threading import Thread
import copy


def run_database_project():
    if os.path.exists("database_project"):
        typewriter(
            printnlog(
                f"\nChecking for updates\nRunning command\nRunning command: git -C database_project pull\n",
                toprint=False,
            ),
            ttime=0.01,
        )
        subprocess.call(["git", "-C", "database_project", "pull"])
        database_project()
    else:
        while True:
            vstup = input(
                printnlog(
                    "\nTo install database_project run this command 'git clone https://github.com/GrenManSK/database_project.git'\nDo you want to complete this action automatically (Y/n) > ",
                    toprint=False,
                )
            ).lower()
            if vstup in ["", "y"]:
                break
            elif vstup == "n":
                return
            else:
                printnlog("Wrong character")
        os.system("git clone https://github.com/GrenManSK/database_project.git")
        typewriter(
            printnlog(
                f"\nDownloading pip requirements\nRunning command: {sys.executable} -m pip install -r database_project/requirements.txt --no-warn-script-location\n",
                toprint=False,
            ),
            ttime=0.01,
        )
        sleep(1)
        os.system(
            sys.executable
            + " -m pip install -r database_project/requirements.txt --no-warn-script-location"
        )
        print("\n")
        os.system(f"{sys.executable} database_project/install.py")

        database_project()


def database_project():
    printnlog(
        "This will only work with my own set of database located in 'database_project\\anime.sql'"
    )
    with open(".env", "a", encoding="utf-8") as dotenv:
        dotenv.write("DAT_PORT=3306\nHOST_NAME=localhost\n")
        printnlog("Add your password > ", end="")
        dotenv.write(f"PASSWORD={input()}\n")
        printnlog("Add your database name > ", end="")
        dotenv.write(f"DATABASE={input()}\n")
        printnlog("Add your user name > ", end="")
        dotenv.write(f"DAT_USER={input()}\n")
    print("Check '.env' file for configuration")
    input("Enter to continue")
    os.system(f"{sys.executable} database_project/main.py")
