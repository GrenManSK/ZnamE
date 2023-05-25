import os
import sys
import subprocess
from .writing import printnlog, typewriter
from time import sleep


def run_kayopy():
    if os.path.exists('KayoPy'):
        typewriter(printnlog(
            f'\nChecking for updates\nRunning command\nRunning command: git -C KayoPy pull\n', toprint=False), ttime=0.01)
        subprocess.call(['git', '-C', 'KayoPy', 'pull'])
        kayopy()
    else:
        while True:
            vstup = input(printnlog(
                "\nTo install KayoPy run this command \'git clone https://github.com/GrenManSK/KayoPy.git\'\nDo you want to complete this action automatically (Y/n) > ", toprint=False)).lower()
            if vstup in ['', 'y']:
                break
            elif vstup == 'n':
                return
            else:
                printnlog('Wrong character')
        os.system('git clone https://github.com/GrenManSK/KayoPy.git')
        typewriter(printnlog(
            f'\nDownloading pip requirements\nRunning command: {sys.executable} -m pip install -r KayoPy/requirements.txt\n', toprint=False), ttime=0.01)
        sleep(1)
        os.system(sys.executable +
                  ' -m pip install -r KayoPy/requirements.txt')

        kayopy()


def kayopy():
    while True:
        vstup = input('Do you want to download anime in anime folder? (y/n): ')
        if vstup == 'y':
            arg = ' -ad -of Anime'
            break
        if vstup == 'n':
            arg = ''
            break
    os.system(f"{sys.executable} KayoPy/kayopy/kayopy.py {arg}")
