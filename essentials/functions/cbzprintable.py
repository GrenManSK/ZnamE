import os
import sys
import subprocess
from .writing import printnlog, typewriter
from time import sleep
from tkinter import filedialog
import argparse


def run_cbz():
    """
    The run_cbz function is used to run the cbzPrintable program.
    It checks if the cbzPrintable folder exists and if it does, it updates it using git pull.
    If not, then it asks you whether you want to install the program automatically or not.

    :return: None
    """
    if os.path.exists("cbzPrintable"):
        typewriter(
            printnlog(
                f"\nChecking for updates\nRunning command\nRunning command: git -C cbzPrintable pull\n",
                toprint=False,
            ),
            ttime=0.01,
        )
        subprocess.call(["git", "-C", "cbzPrintable", "pull"])
    else:
        while True:
            vstup = input(
                printnlog(
                    "\nTo install cbzPrintable run this command 'git clone https://github.com/GrenManSK/cbzPrintable.git'\nDo you want to complete this action automatically (Y/n) > ",
                    toprint=False,
                )
            ).lower()
            if vstup in ["", "y"]:
                break
            elif vstup == "n":
                return
            else:
                printnlog("Wrong character")
        os.system("git clone https://github.com/GrenManSK/cbzPrintable.git")
        typewriter(
            printnlog(
                f"\nDownloading pip requirements\nRunning command: {sys.executable} -m pip install -r cbzPrintable/requirements.txt --no-warn-script-location\n",
                toprint=False,
            ),
            ttime=0.01,
        )
        sleep(1)
        os.system(
            sys.executable
            + " -m pip install -r cbzPrintable/requirements.txt --no-warn-script-location"
        )

    cbz()


def cbz():
    """
    The cbz function is the main function of this program. It asks the user whether they want to use CLI or GUI, and then calls either cbz_cli() or cbz_gui() accordingly.

    :return: The cbz_cli function or the cbz_gui function&lt;/code&gt;
    """
    while True:
        vstup = input("Do you wanna use CLI or GUI? (c/g)")
        if vstup.lower() in ["c", "g"]:
            break
        else:
            print("Please specify an option")
    if vstup == "c":
        cbz_cli()
    elif vstup == "g":
        cbz_gui()


def run_cbz_command(args):
    """
    The run_cbz_command function is a wrapper for the cbzPrintable.py script, which
    is used to create printable PDF files from CBZs. The run_cbz_command function takes
    a single argument, args, which is a string containing all of the arguments that
    would normally be passed to cbzPrintable.py on the command line.

    :param args: Pass in the arguments that will be used by cbzprintable
    :return: The result of the cbzprintable
    """
    typewriter(
        printnlog(
            f"{sys.executable} cbzPrintable/cbzPrintable/cbzPrintable.py {args}",
            toprint=False,
        ),
        ttime=0.01,
    )
    sleep(1)
    os.system(f"{sys.executable} cbzPrintable/cbzPrintable/cbzPrintable.py {args}")


def parse_cbz_command(command):
    """
    The parse_cbz_command function takes a command string as input and parses it into an argparse.ArgumentParser object.
    The function then uses the parsed arguments to run the cbz_command function with appropriate parameters.

    :param command: Pass the command to be run in the terminal
    :return: The command to run the cbz script
    """
    parser = argparse.ArgumentParser()
    parser.add_argument("input", type=str)
    parser.add_argument("-fp", "--file_pattern", type=str, default=None, nargs="?")
    args = parser.parse_args(command.split(" "))
    directory = args.input.replace("#", " ")
    if args.file_pattern is not None:
        pattern = args.file_pattern
        run_cbz_command(f'"{directory}" --file_pattern {pattern}')
    else:
        run_cbz_command(f'"{directory}"')


def cbz_cli():
    """
    The cbz_cli function is a command line interface for the cbzPrintable program.
    It allows users to interact with the program in a more user-friendly way than
    using command line arguments. It also provides an easy way to test out different
    arguments without having to retype them every time.

    :return: Nothing
    """
    typewriter(
        printnlog(
            "Here you will put arguments for program\nSee README here 'https://github.com/GrenManSK/cbzPrintable/blob/main/README.md'\nYou will add only arguments | Wihtout 'cbzPrintable'",
            toprint=False,
        ),
        ttime=0.01,
    )
    while True:
        vstup = input("> ")
        if vstup in ["q", "quit", "exit", "-q"]:
            break
        if "#" in vstup or "&" in vstup or ":" in vstup or ";" in vstup:
            print("Unallowed characters\n")
        parse_cbz_command(vstup)


def cbz_gui():
    """
    The cbz_gui function is a simple command line interface for the parse_cbz_command function.
    It allows you to select a directory and file pattern using glob, then it calls the parse_cbz_command function with those arguments.

    :return: The parse_cbz_command function with the directory and pattern arguments
    """
    pattern = None
    typewriter(
        printnlog(
            "'dir' for selecting directory\n'pattern' for file pattern\n'complete' for final result\nFile pattern using glob",
            toprint=False,
        ),
        ttime=0.01,
    )
    while True:
        vstup = input("> ")
        if vstup in ["q", "quit", "exit", "-q"]:
            break
        if vstup == "dir":
            directory = filedialog.askdirectory(
                initialdir="./", mustexist=True, title="Select directory with cbz files"
            ).replace(" ", "#")
        if vstup == "pattern":
            while True:
                pattern = input("Pattern > ")
                if "#" in pattern or "&" in pattern:
                    print("Unallowed characters\n")
                    pattern = None
                    continue
                break
        if vstup == "complete":
            if pattern is None:
                parse_cbz_command(f"{directory}")
            else:
                parse_cbz_command(f"{directory} --file_pattern {pattern}")
