import win32api
from ..internet import download
import os
from .writing import printnlog
from ..system.system_operations import move, show_cmd
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
    quiet = eval(os.getenv("QUIET"))
except TypeError:
    quiet = False
screensize = os.getenv("SCREENSIZE")[1:-1].split(", ")
screensize = [int(x) for x in screensize]


def rclick(x, y):
    win32api.SetCursorPos((x, y))
    win32api.mouse_event(win32con.MOUSEEVENTF_RIGHTDOWN, x, y, 0, 0)
    win32api.mouse_event(win32con.MOUSEEVENTF_RIGHTUP, x, y, 0, 0)


def textractor(args, lang: str, translator: str):
    if not lang in t_languages:
        return 39
    lang = lang.lower()
    update = False
    printnlog("Checking if Textractor is present")
    if not os.path.exists("Textractor"):
        printnlog("Textractor not found")
        update = True
        printnlog("Downloading Textractor")
        download(
            "https://github.com/Artikash/Textractor/releases/download/v5.2.0/Textractor-5.2.0-Zip-Version-English-Only.zip",
            "textractor.zip",
        )
        printnlog("Extracting downloaded package")
        with zipfile.ZipFile("textractor.zip", mode="r") as zip:
            for member in tqdm(
                iterable=zip.namelist(), total=len(zip.namelist()), desc="Extracting "
            ):
                try:
                    zip.extract(member)
                    if not quiet:
                        tqdm.write(
                            f"{os.path.basename(member)}("
                            + str(os.path.getsize(member))
                            + "B)"
                        )
                    log(
                        f"{os.path.basename(member)}("
                        + str(os.path.getsize(member))
                        + "B)"
                    )
                except zipfile.error as e:
                    pass
            zip.close()
        os.remove("Textractor.zip")
        printnlog("Installing font")
        Thread(target=install_font).start()
        os.system("INSTALL_THIS_UNICODE_FONT.ttf")
        os.remove("INSTALL_THIS_UNICODE_FONT.ttf")

    printnlog("Starting Textractor")
    os.system("start Textractor/x64/Textractor.exe")
    printnlog("Waiting for Textractor to start (5 sec)", end="\r")
    sleep(1)
    printnlog("Waiting for Textractor to start (5 sec) .", end="\r")
    sleep(1)
    printnlog("Waiting for Textractor to start (5 sec) ..", end="\r")
    sleep(1)
    printnlog("Waiting for Textractor to start (5 sec) ...", end="\r")
    sleep(1)
    printnlog("Waiting for Textractor to start (5 sec) ....", end="\r")
    sleep(1)
    printnlog("Waiting for Textractor to start (5 sec) DONE")

    window = pygetwindow.getWindowsWithTitle("Textractor")[1]
    window.activate()
    if update:
        printnlog("Opening extensions", end="\r")
        for i in range(13):
            pg.press("tab")
        pg.press("space")
        printnlog("Opening extensions DONE")
        move("Extensions", 0, 0, 100, 300)
        printnlog(f"Adding {translator} translator extension", end="\r")
        rclick(50, 50)
        sleep(0.1)
        pg.press("tab")
        pg.press("enter")
        sleep(1)
        pg.write(f"{translator} Translate.xdll")
        pg.press("enter")
        sleep(0.25)
        window = pygetwindow.getWindowsWithTitle("Extensions")[0]
        window.activate()
        printnlog(f"Adding {translator} translator extension DONE")
        printnlog("Removing Google Translator extension", end="\r")
        sleep(0.25)
        window = pygetwindow.getWindowsWithTitle("Extensions")[0]
        window.activate()
        for i in range(7):
            pg.press("up")
        for i in range(3):
            pg.press("down")
        rclick(50, 200)
        sleep(0.1)
        pg.press("tab")
        pg.press("tab")
        pg.press("enter")
        printnlog("Removing Google Translator extension DONE")
        printnlog("Removing Extra Window extension", end="\r")
        for i in range(7):
            pg.press("up")
        for i in range(3):
            pg.press("down")
        rclick(50, 200)
        sleep(0.1)
        pg.press("tab")
        pg.press("tab")
        pg.press("enter")
        sleep(0.25)
        window = pygetwindow.getWindowsWithTitle("Extensions")[0]
        window.activate()
        printnlog("Removing Extra Window extension DONE")
        printnlog("Removing Extra Newlines extension", end="\r")
        for i in range(7):
            pg.press("up")
        for i in range(3):
            pg.press("down")
        rclick(50, 200)
        sleep(0.1)
        pg.press("tab")
        pg.press("tab")
        pg.press("enter")
        sleep(0.5)
        window = pygetwindow.getWindowsWithTitle("Extensions")[0]
        window.activate()
        printnlog("Removing Extra Newlines extension DONE")
        printnlog("Adding Extra Window extension", end="\r")
        rclick(50, 50)
        sleep(0.1)
        pg.press("tab")
        pg.press("enter")
        sleep(1)
        pg.write("Extra Window.xdll")
        pg.press("enter")
        sleep(0.25)
        window = pygetwindow.getWindowsWithTitle("Extensions")[0]
        window.activate()
        printnlog("Adding Extra Window extension DONE")
        printnlog("Adding Extra Newlines extension", end="\r")
        rclick(50, 50)
        sleep(0.1)
        pg.press("tab")
        pg.press("enter")
        sleep(0.5)
        pg.write("Extra Newlines.xdll")
        pg.press("enter")
        printnlog("Adding Extra Newlines extension DONE")
        sleep(0.25)
        window = pygetwindow.getWindowsWithTitle("Textractor")[0]
        window.activate()
        sleep(0.25)

        pg.keyDown("shift")
        for i in range(13):
            pg.press("tab")
        pg.keyUp("shift")
        printnlog("Setup DONE")

    printnlog("Hooking python.exe")
    for i in range(3):
        pg.press("tab")
    pg.press("space")
    sleep(0.2)
    printnlog("Searching python.exe", end="\r")
    pg.write("python.exe")
    printnlog("Searching python.exe DONE")
    printnlog("Aknowledging confirmation", end="\r")
    pg.press("tab")
    pg.press("enter")
    printnlog("Aknowledging confirmation DONE")
    sleep(3)
    printnlog(
        "Selecting thread to 'MultiByteToWideChar (HS-4C@0:kernel32.dll:MultiByteToWideChar)'",
        end="\r",
    )
    pg.keyDown("shift")
    pg.press("tab")
    pg.press("tab")
    pg.keyUp("shift")
    pg.press("down")
    pg.press("down")
    printnlog(
        "Selecting thread to 'MultiByteToWideChar (HS-4C@0:kernel32.dll:MultiByteToWideChar)' DONE"
    )
    printnlog("Waiting for python.exe to hook (3 sec)", end="\r")
    sleep(1)
    printnlog("Waiting for python.exe to hook (3 sec) .", end="\r")
    sleep(1)
    printnlog("Waiting for python.exe to hook (3 sec) ..", end="\r")
    sleep(1)
    printnlog("Waiting for python.exe to hook (3 sec) DONE")
    pg.press("down")
    pg.press("down")
    printnlog("Setting source language to English", end="\r")
    window = pygetwindow.getWindowsWithTitle(f"{translator} Translate")[0]
    window.activate()
    sleep(0.5)
    pg.press("tab")
    pg.press("space")
    pg.write("english")
    pg.press("enter")
    printnlog("Setting source language to English DONE")
    printnlog(f"Setting target language to {lang.title()}", end="\r")
    pg.keyDown("shift")
    pg.press("tab")
    pg.keyUp("shift")
    pg.press("space")
    pg.write(lang)
    pg.press("enter")
    window = pygetwindow.getWindowsWithTitle("Textractor")[1]
    window.activate()
    printnlog(f"Setting target language to {lang.title()} DONE")
    sleep(0.5)
    printnlog("Setting window to always on top", end="\r")
    hwnd = win32gui.GetForegroundWindow()
    win32gui.SetWindowPos(hwnd, win32con.HWND_TOPMOST, 100, 100, 200, 200, 0)
    open("textractor_done", "x")
    show_cmd(args)
    printnlog("Setting window to always on top DONE")
    print("\n")
    return 0


def install_font():
    sleep(0.5)
    pg.press("i")
    pg.press("tab")
    sleep(0.5)
    pg.press("enter")
    sleep(3)
    pg.keyDown("alt")
    pg.press("f4")
    pg.keyUp("alt")


def run_textractor(args, lang, translator):
    return_code = textractor(args, lang, translator)

    if return_code == 39:
        printnlog(f"Incorrect language; Return Code: %s" % return_code)
        return return_code
    while not os.path.exists("textractor_done"):
        sleep(0.5)
    os.remove("textractor_done")
    sleep(0.1)
    move(
        "Textractor",
        0,
        0,
        int(screensize[0] / 2),
        int((round((322 / 1736) * screensize[0], 0)) - 35),
    )
    sleep(0.1)


def change_quiet_textractor(to):
    global quiet
    if to in [True, False]:
        quiet = to
