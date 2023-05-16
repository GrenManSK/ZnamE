from ..internet import download
import os
import shutil
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


def textractor(lang):
    lang = lang.lower()
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
    sleep(2)

    window = pygetwindow.getWindowsWithTitle('Textractor')[1]
    window.activate()
    for i in range(3):
        pg.press('tab')
    pg.press('space')
    pg.write('python.exe')
    pg.press('tab')
    pg.press('enter')
    pg.keyDown('shift')
    pg.press('tab')
    pg.press('tab')
    pg.keyUp('shift')
    sleep(2)
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


def install_font():
    sleep(0.5)
    pg.press('i')
    sleep(5)
    pg.keyDown('alt')
    pg.press('f4')
    pg.keyUp('alt')
