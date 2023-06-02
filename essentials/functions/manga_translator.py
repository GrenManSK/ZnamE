import os
import sys
import subprocess
from .writing import printnlog, typewriter
from time import sleep
from tkinter import filedialog


def run_manga_image_translator(env):
    if os.path.exists('manga-image-translator'):
        typewriter(printnlog(
            f'\nChecking for updates\nRunning command\nRunning command: git -C manga-image-translator pull\n', toprint=False), ttime=0.01)
        subprocess.call(['git', '-C', 'manga-image-translator', 'pull'])
        print('')
        manga_image_translator(env)
    else:
        while True:
            vstup = input(printnlog(
                "\nTo install manga-image-translator run this command \'git clone https://github.com/zyddnys/manga-image-translator.git\'\nDo you want to complete this action automatically (Y/n) > ", toprint=False)).lower()
            if vstup in ['', 'y']:
                break
            elif vstup == 'n':
                return
            else:
                printnlog('Wrong character')
        os.system(
            'git clone https://github.com/zyddnys/manga-image-translator.git')
        typewriter(printnlog(
            f'\nDownloading pip requirements\nRunning command: {env} -m pip install -r manga-image-translator/requirements.txt\n', toprint=False), ttime=0.01)
        sleep(1)
        os.system(env +
                  ' -m pip install -r manga-image-translator/requirements.txt')
        os.system(env +
                  ' -m pip install git+https://github.com/lucasb-eyer/pydensecrf.git')

        manga_image_translator(env)


def manga_image_translator(env):
    folder = None
    lang = 'ENG'
    typewriter(printnlog('Folder must contains image files\n\'folder\' to define folder with which you will be working with\n\'lang\' to define language which will be translated to\n\'start\' to start program', toprint=False), ttime=0.01)
    while True:
        vstup = input('> ')
        if vstup == 'folder':
            folder = filedialog.askdirectory(initialdir='./',
                                             mustexist=True,
                                             title='Select manga folder with images')
        if vstup == 'lang':
            while True:
                typewriter(printnlog("""CHS: Chinese (Simplified)
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
VIN: Vietnames""", toprint=False), ttime=0.01)
                vstup = input("Select language")
                if not vstup in ['CHS', "CHT", 'CSY', 'NLD', 'ENG', 'FRA', 'DEU', 'HUN', 'ITA', 'JPN', 'KOR', 'PLK', 'PTB', 'ROM', 'RUS', 'ESP', 'TRK', 'UKR', 'VIN']:
                    print('Wrong language')
                    continue
                lang = vstup
                break
        if vstup == 'start':
            if folder is None:
                print('No folder specified')
                continue
            manga_image_translator_command(env, folder, lang)


def manga_image_translator_command(env, folder, lang):
    os.system(
        f"{env} -m manga-image-translator.manga_translator -v --mode batch  --translator=google -l {lang} -i {folder}")
