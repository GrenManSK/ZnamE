import os
import sys
import subprocess
from .writing import printnlog, typewriter
from time import sleep
from tkinter import filedialog
import argparse


def run_cbz():
    if os.path.exists('cbzPrintable'):
        typewriter(printnlog(
            f'\nChecking for updates\nRunning command\nRunning command: git -C cbzPrintable pull\n', toprint=False), ttime=0.01)
        subprocess.call(['git', '-C', 'cbzPrintable', 'pull'])
        cbz()
    else:
        while True:
            vstup = input(printnlog(
                "\nTo install cbzPrintable run this command \'git clone https://github.com/GrenManSK/cbzPrintable.git\'\nDo you want to complete this action automatically (Y/n) > ", toprint=False)).lower()
            if vstup in ['', 'y']:
                break
            elif vstup == 'n':
                return
            else:
                printnlog('Wrong character')
        os.system('git clone https://github.com/GrenManSK/cbzPrintable.git')
        typewriter(printnlog(
            f'\nDownloading pip requirements\nRunning command: {sys.executable} -m pip install -r cbzPrintable/requirements.txt\n', toprint=False), ttime=0.01)
        sleep(1)
        os.system(sys.executable +
                  ' -m pip install -r cbzPrintable/requirements.txt')

        cbz()


def cbz():
    while True:
        vstup = input('Do you wanna use CLI or GUI? (c/g)')
        if vstup.lower() in ['c', 'g']:
            break
        else:
            print('Please specify an option')
    if vstup == 'c':
        cbz_cli()
    elif vstup == 'g':
        cbz_gui()


def run_cbz_command(args):
    typewriter(printnlog(
        f'{sys.executable} cbzPrintable/cbzPrintable/cbzPrintable.py {args}', toprint=False), ttime=0.01)
    sleep(1)
    os.system(
        f'{sys.executable} cbzPrintable/cbzPrintable/cbzPrintable.py {args}')


def parse_cbz_command(command):
    parser = argparse.ArgumentParser()
    parser.add_argument('input', type=str)
    parser.add_argument('-fp', '--file_pattern',
                        type=str, default=None, nargs='?')
    args = parser.parse_args(command.split(' '))
    directory = args.input.replace('#', ' ')
    if args.file_pattern is not None:
        pattern = args.file_pattern
        run_cbz_command(f"\"{directory}\" --file_pattern {pattern}")
    else:
        run_cbz_command(f"\"{directory}\"")


def cbz_cli():
    typewriter(printnlog('Here you will put arguments for program\nSee README here \'https://github.com/GrenManSK/cbzPrintable/blob/main/README.md\'\nYou will add only arguments | Wihtout \'cbzPrintable\'', toprint=False), ttime=0.01)
    while True:
        vstup = input('> ')
        if vstup in ['q', 'quit', 'exit', '-q']:
            break
        if "#" in vstup or "&" in vstup:
            print('Unallowed characters\n')
        parse_cbz_command(vstup)


def cbz_gui():
    dir = None
    pattern = None
    typewriter(printnlog(
        '\'dir\' for selecting directory\n\'pattern\' for file pattern\n\'complete\' for final result\nFile pattern using glob', toprint=False), ttime=0.01)
    while True:
        vstup = input('> ')
        if vstup in ['q', 'quit', 'exit', '-q']:
            break
        if vstup == 'dir':
            directory = filedialog.askdirectory(initialdir='./',
                                                mustexist=True,
                                                title='Select directory with cbz files').replace(' ', '#')
        if vstup == 'pattern':
            while True:
                pattern = input('Pattern > ')
                if "#" in pattern or "&" in pattern:
                    print('Unallowed characters\n')
                    pattern = None
                    continue
                break
        if vstup == 'complete':
            if pattern is None:
                parse_cbz_command(f"{directory}")
            else:
                parse_cbz_command(f"{directory} --file_pattern {pattern}")
