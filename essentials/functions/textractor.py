import win32api
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

try:
    quiet = eval(os.getenv('QUIET'))
except TypeError:
    quiet = False
screensize = os.getenv('SCREENSIZE')[1:-1].split(', ')
screensize = [int(x) for x in screensize]


def rclick(x, y):
    win32api.SetCursorPos((x, y))
    win32api.mouse_event(win32con.MOUSEEVENTF_RIGHTDOWN, x, y, 0, 0)
    win32api.mouse_event(win32con.MOUSEEVENTF_RIGHTUP, x, y, 0, 0)


def textractor(args, lang, translator):
    if not lang in t_languages:
        return 0
    lang = lang.lower()
    update = False
    if not os.path.exists('Textractor'):
        update = True
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
    if update:
        for i in range(13):
            pg.press('tab')
        pg.press('space')
        move('Extensions', 0, 0, 100, 300)
        rclick(50, 50)
        sleep(0.1)
        pg.press('tab')
        pg.press('enter')
        sleep(0.5)
        pg.write(f'{translator} Translate.xdll')
        pg.press('enter')
        sleep(0.25)
        window = pygetwindow.getWindowsWithTitle('Extensions')[0]
        window.activate()
        for i in range(7):
            pg.press('up')
        for i in range(3):
            pg.press('down')
        rclick(50, 200)
        sleep(0.1)
        pg.press('tab')
        pg.press('tab')
        pg.press('enter')
        sleep(0.25)
        window = pygetwindow.getWindowsWithTitle('Extensions')[0]
        window.activate()
        for i in range(7):
            pg.press('up')
        for i in range(3):
            pg.press('down')
        rclick(50, 200)
        sleep(0.1)
        pg.press('tab')
        pg.press('tab')
        pg.press('enter')
        sleep(0.25)
        window = pygetwindow.getWindowsWithTitle('Extensions')[0]
        window.activate()
        for i in range(7):
            pg.press('up')
        for i in range(3):
            pg.press('down')
        rclick(50, 200)
        sleep(0.1)
        pg.press('tab')
        pg.press('tab')
        pg.press('enter')
        sleep(0.5)
        window = pygetwindow.getWindowsWithTitle('Extensions')[0]
        window.activate()
        rclick(50, 50)
        sleep(0.1)
        pg.press('tab')
        pg.press('enter')
        sleep(0.5)
        pg.write('Extra Window.xdll')
        pg.press('enter')
        sleep(0.25)
        window = pygetwindow.getWindowsWithTitle('Extensions')[0]
        window.activate()
        rclick(50, 50)
        sleep(0.1)
        pg.press('tab')
        pg.press('enter')
        sleep(0.5)
        pg.write('Extra Newlines.xdll')
        pg.press('enter')
        sleep(0.25)

        window = pygetwindow.getWindowsWithTitle('Textractor')[0]
        window.activate()
        sleep(0.25)
        
        pg.keyDown('shift')
        for i in range(13):
            pg.press('tab')
        pg.keyUp('shift')
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
    window = pygetwindow.getWindowsWithTitle(f'{translator} Translate')[0]
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


def run_textractor(args, lang, translator):
    textractor(args, lang, translator)

    while not os.path.exists('textractor_done'):
        sleep(0.5)
    os.remove('textractor_done')
    sleep(0.1)
    move('Textractor', 0, 0, int(
        screensize[0]/2), int((round((322/1736)*screensize[0], 0))-35))
    sleep(0.1)


def change_quiet_textractor(to):
    global quiet
    if to in [True, False]:
        quiet = to
