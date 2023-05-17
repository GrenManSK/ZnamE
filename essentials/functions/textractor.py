from ..internet import download
import os
from ..system.system_operations import move
from ..data.translate import t_languages
import pyautogui as pg
import zipfile
from tqdm import tqdm
from dotenv import load_dotenv
from .writing import log
from threading import Thread
from time import sleep
import win32gui
import win32con
import pygetwindow
load_dotenv()

quiet = os.getenv('QUIET')
screensize = os.getenv('SCREENSIZE')[1:-1].split(', ')
screensize = [int(x) for x in screensize]


def textractor(args, lang):
    if not lang in t_languages:
        return 0
    lang = lang.lower()
    if not os.path.exists('Textractor'):
        download('https://github.com/Artikash/Textractor/releases/download/v5.2.0/Textractor-5.2.0-Zip-Version-English-Only.zip', 'textractor.zip')
        with zipfile.ZipFile('textractor.zip', mode='r') as zip:
            for member in tqdm(iterable=zip.namelist(), total=len(zip.namelist()), desc='Extracting '):
                try:
                    zip.extract(member)
                    if not quiet:
                        tqdm.write(
                            f"{os.path.basename(member)}(" + str(os.path.getsize(member)) + "B)")
                    log(f"{os.path.basename(member)}(" +
                        str(os.path.getsize(member)) + "B)")
                except zipfile.error as e:
                    pass
            zip.close()
        os.remove('Textractor.zip')

        Thread(target=install_font).start()
        print('Close the program if already installed')
        os.system('INSTALL_THIS_UNICODE_FONT.ttf')
        os.remove('INSTALL_THIS_UNICODE_FONT.ttf')
    os.system('start Textractor/x64/Textractor.exe')
    sleep(5)

    window = pygetwindow.getWindowsWithTitle('Textractor')[1]
    window.activate()
    for i in range(3):
        pg.press('tab')
    pg.press('space')
    sleep(0.2)
    pg.write('python.exe')
    pg.press('tab')
    pg.press('enter')
    sleep(0.2)
    pg.keyDown('shift')
    pg.press('tab')
    pg.press('tab')
    pg.keyUp('shift')
    sleep(3)
    print('Hello, world')
    print('This is test')
    pg.press('down')
    pg.press('down')
    window = pygetwindow.getWindowsWithTitle('Google Translate')[0]
    window.activate()
    sleep(0.5)
    pg.press('tab')
    pg.press('space')
    pg.write('english')
    pg.press('enter')
    pg.keyDown('shift')
    pg.press('tab')
    pg.keyUp('shift')
    pg.press('space')
    pg.write(lang)
    pg.press('enter')
    window = pygetwindow.getWindowsWithTitle('Textractor')[1]
    window.activate()
    sleep(0.5)
    hwnd = win32gui.GetForegroundWindow()
    win32gui.SetWindowPos(hwnd, win32con.HWND_TOPMOST, 100, 100, 200, 200, 0)
    open('textractor_done', 'x')
    if args.test is not None:
        window = pygetwindow.getWindowsWithTitle('ZnámE')[0]
        window.activate()


def install_font():
    sleep(0.5)
    pg.press('i')
    sleep(5)
    pg.keyDown('alt')
    pg.press('f4')
    pg.keyUp('alt')


def run_textractor(args, lang):
    textractor(args, lang)

    while not os.path.exists('textractor_done'):
        sleep(0.5)
    os.remove('textractor_done')
    move('Textractor', 0, 0, int(
        screensize[0]/2), int((round((322/1736)*screensize[0], 0))-35))
