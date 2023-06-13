import os
import sys
import subprocess
from .writing import printnlog, typewriter
from time import sleep
import glob
from threading import Thread
import copy


def run_database_project():
    """
    The run_database_project function is used to run the database_project.
        It checks if the database_project folder exists and if it does, it updates it using git pull.
        If not, then it asks you whether you want to install the project automatically or not.

    :return: None
    """
    if os.path.exists("Data-Dynamics"):
        typewriter(
            printnlog(
                f"\nChecking for updates\nRunning command\nRunning command: git -C Data-Dynamics pull\n",
                toprint=False,
            ),
            ttime=0.01,
        )
        subprocess.call(["git", "-C", "Data-Dynamics", "pull"])
        printnlog("")
        database_project()
    else:
        while True:
            vstup = input(
                printnlog(
                    "\nTo install Data-Dynamics run this command 'git clone https://github.com/GrenManSK/Data-Dynamics.git'\nDo you want to complete this action automatically (Y/n) > ",
                    toprint=False,
                )
            ).lower()
            if vstup in ["", "y"]:
                break
            elif vstup == "n":
                return
            else:
                printnlog("Wrong character")
        os.system("git clone https://github.com/GrenManSK/Data-Dynamics.git")
        typewriter(
            printnlog(
                f"\nDownloading pip requirements\nRunning command: {sys.executable} -m pip install -r Data-Dynamics/requirements.txt --no-warn-script-location\n",
                toprint=False,
            ),
            ttime=0.01,
        )
        sleep(1)
        os.system(
            sys.executable
            + " -m pip install -r Data-Dynamics/requirements.txt --no-warn-script-location"
        )
        print("\n")
        os.system(f"{sys.executable} Data-Dynamics/install.py")

        database_project()


def database_project():
    """
    The database_project function is a function that allows the user to create an .env file for the database_project folder.
    The .env file will contain all of the information needed to connect to a MySQL database, and it will be used by main.py in order
    to connect and interact with said database.

    :return: None
    """
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
