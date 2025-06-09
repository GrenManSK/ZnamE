import contextlib
import cv2
import glob
from .exceptions import error_get
from .system_info import get_line_number, get_screensize
from ..functions.writing import typewriter
from time import sleep
import pyautogui as pg
import pygetwindow
import os
import traceback
import sys
import ctypes
import win32gui
from dotenv import load_dotenv
from pygame import mixer
import moviepy as mp

load_dotenv(".env")


def get_music_menu(musiclistnew):
    """
    The get_music_menu function takes a list of music files as an argument and prints out the menu for the user to select from.
    It returns the number of items in that list.

    :param musiclistnew: Display the music list
    :return: The number of songs in the music list
    """
    for times, music_name in enumerate(musiclistnew):
        typewriter(f"{str(times + 1)}) {music_name}")
    typewriter(f"{str(times + 2)}) Delete audio")
    typewriter(f"{str(times + 3)}) Download music")
    typewriter(f"{str(times + 4)}) Back")
    return times


def altF4():
    """
    The altF4 function simulates the pressing of the Alt+F4 key combination.
    This is useful for closing windows in Windows.

    :return: Nothing
    """
    pg.keyDown("alt")
    pg.press("f4")
    pg.keyUp("alt")


def gif_to_vid():
    """
    The gif_to_vid function converts a gif to an mp4 video file.
        This is done because the discord.py library does not support uploading gifs, only videos.

    :return: Nothing
    """
    clip = mp.VideoFileClip("assets/waifu.gif")
    clip.write_videofile("assets/waifu.mp4")
    clip.close()


def delcache(config, cache_name: str, hist: str) -> None:
    """
    The delcache function deletes the cache file if it is empty.

    :param cache_name: cache_Name the file that is used to store the time
    :param hist: Check if the history file has changed
    :return: The value of the timer
    """
    time_got: int = int(config["basic info"]["inactivelimit"])
    timer = time_got
    filesize: int = os.path.getsize(hist)
    sizehist: int = filesize
    while True:
        try:
            for end_file in os.listdir():
                if end_file == "END":
                    raise SystemError
            if timer <= 0:
                os.remove(cache_name)
                open("INACTIVE", "x", encoding="utf-8")
                os.system("cls")
                pg.write("\n")
                break
            if filesize != sizehist:
                timer = time_got
                sizehist: int = filesize
            else:
                sizehist: int = filesize
                filesize: int = os.path.getsize(hist)
                sleep(1)
                timer -= 1
        except SystemError:
            break


def getWindow(args) -> bool:
    """
    The getWindow function is used to find the window of Známý (the game) and activate it.
    It also checks if the file 'banner.png' exists in the assets folder.

    :return: If error occured
    """
    dummy = None
    cv2.namedWindow("frame2", cv2.WND_PROP_FULLSCREEN)
    cv2.setWindowProperty("frame2", cv2.WND_PROP_FULLSCREEN, cv2.WINDOW_FULLSCREEN)
    test: str = "assets/banner.png"
    for file in glob.glob(test):
        dummy = cv2.imread(file)
    try:
        cv2.imshow("Image", dummy)
    except cv2.error:
        error_get(
            cv2.error("File is corrupt (probably 'banner.png')"),
            [get_line_number()],
            fname="system_operations.py",
        )
        return True
    cv2.waitKey(1)
    sleep(0.1)
    cv2.destroyWindow("Image")
    if args.test is not None:
        try:
            show_cmd(args)
            return False
        except IndexError as e:
            raise IndexError(
                "Possible solution; run in cmd or python application not ide or put arguments '--test'"
            ) from e
    return False


def set_image():
    """
    The set_image function is used to set the image of the banner.
        The function takes no arguments and returns nothing.

    :return: A tuple with the image and its size
    """
    screensize = get_screensize()[0]
    getImg(
        "assets/banner.png",
        "banner",
        0,
        0,
        screensize[0],
        int((round((322 / 1736) * screensize[0], 0))),
    )


def set_up(args):
    """
    The set_up function is used to set up the environment for the program.
    It sets up a screensize variable, which is used in other functions. It also
    sets an image as wallpaper and moves it to the right place on screen, so that
    the user can see it while using this program.

    :param args: Pass the arguments from the command line to this function
    :return: The screensize and the image of the screen
    """
    screensize = get_screensize()[0]
    set_image()
    move(
        "ZnámE",
        0,
        int((round((322 / 1736) * screensize[0], 0)) - 35),
        screensize[0],
        screensize[1] - int((round((322 / 1736) * screensize[0], 0))),
    )
    show_cmd(args)
    press_win()
    os.system("cls")


def isUserAdmin():
    """
    The isUserAdmin function checks to see if the user running this script is an admin.
    This is for Windows only.
    :return: A boolean value
    """
    if os.name == "nt":
        import ctypes

        # WARNING: requires Windows XP SP2 or higher!
        try:
            return ctypes.windll.shell32.IsUserAnAdmin()
        except:
            traceback.print_exc()
            print("Admin check failed, assuming not an admin.")
            return False
    elif os.name == "posix":
        # Check for root on Posix
        return os.getuid() == 0
    else:
        raise RuntimeError(f"Unsupported operating system for this module: {os.name}")


def runAsAdmin(cmdLine=None, wait=True):
    """
    The runAsAdmin function is a simple function that will run your python script as the Administrator.
    This function will attempt to do the following:
    :param cmdLine: Pass arguments to the executable
    :param wait: Determine whether the function should wait for the process to finish or not
    :return: The process handle of the elevated process
    """
    if os.name != "nt":
        raise RuntimeError("This function is only implemented on Windows.")

    import win32api
    import win32con
    import win32event
    import win32process
    from win32com.shell.shell import ShellExecuteEx  # type: ignore
    from win32com.shell import shellcon  # type: ignore

    python_exe = sys.executable

    if cmdLine is None:
        cmdLine = [python_exe] + sys.argv
    elif type(cmdLine) not in (ctypes.TupleType, ctypes.ListType):
        raise ValueError("cmdLine is not a sequence.")
    cmd = f'"{cmdLine[0]}"'
    params = " ".join([f'"{x}"' for x in cmdLine[1:]])
    cmdDir = ""
    showCmd = win32con.SW_SHOWNORMAL
    lpVerb = "runas"
    procInfo = ShellExecuteEx(
        nShow=showCmd,
        fMask=shellcon.SEE_MASK_NOCLOSEPROCESS,
        lpVerb=lpVerb,
        lpFile=cmd,
        lpParameters=params,
    )
    if wait:
        procHandle = procInfo["hProcess"]
        obj = win32event.WaitForSingleObject(procHandle, win32event.INFINITE)
        return win32process.GetExitCodeProcess(procHandle)
    else:
        return None


def checkAdmin():
    """
    The checkAdmin function checks if the user is an admin. If not, it will run the program as an admin.
    :return: 0 if the user is an admin, and returns 1 if the user is not an admin
    :doc-author: Trelent
    """
    rc = 0
    if not isUserAdmin():
        print("You're not an admin.", os.getpid(), "params: ", sys.argv)
        return runAsAdmin()
    else:
        print("You are an admin!", os.getpid(), "params: ", sys.argv)
        return 0


def getImg(imgSrc: str, name: str, x=None, y=None, width=None, length=None) -> None:
    """
    The getImg function displays an image from the source. If x, y, width, and length are specified, then the image will be displayed at those coordinates with the specified width and length. Otherwise, the image will be displayed at the default coordinates and default width and length.

    :param imgSrc: str: Specify the source of the image
    :param name: str: Name the window
    :param x: Set the x coordinate of the window
    :param y: Specify the y coordinate of the window
    :param width: Set the width of the window
    :param length: Set the length of the window
    :return: The image that is displayed
    """
    try:
        screensize = os.getenv("SCREENSIZE")[1:-1].split(", ")
        screensize = [int(i) for i in screensize]
    except TypeError:
        screensize = get_screensize()[0]
    path: str = imgSrc
    for file in glob.glob(path):
        global dummy
        dummy = cv2.imread(file)
        cv2.imshow(name, dummy)
        if x is not None and y is not None and width is not None and length is not None:
            appname: str = name
            xpos: int = x
            ypos: int = y
            if width is None:
                width = int((screensize[0] / 10) * 9)
            if length is None:
                length = int((screensize[1] / 10) * 9)

            def enumHandler(hwnd, lParam):
                if win32gui.IsWindowVisible(hwnd) and appname in win32gui.GetWindowText(hwnd):
                    win32gui.MoveWindow(hwnd, xpos, ypos, width, length, True)

            win32gui.EnumWindows(enumHandler, None)
        k = cv2.waitKey(33)
        cv2.setWindowProperty(name, cv2.WND_PROP_FULLSCREEN, cv2.WINDOW_FULLSCREEN)
        if k == 27:
            break
        elif k == -1:
            continue
        else:
            print(k)
            cv2.destroyAllWindows()


def pg_comb(operations: dict[str, str]):
    """
    The pg_comb function takes a dictionary of operations and keys as an argument.
    The function then iterates through the dictionary, performing each operation on the corresponding key.

    :param operations: dict[str: Define the operations that can be used in this function
    :param str]: Define the type of data that will be passed into the function
    :return: A dictionary with the keys being operations and the values being keys
    """
    for oper, key in operations.items():
        if oper == "p":
            pg.press(key)
        elif oper == "ku":
            pg.keyUp(key)
        elif oper == "kd":
            pg.keyDown(key)


def move(window: str, x: int, y: int, width, length) -> None:
    """
    The move function moves the specified window to a specified location.
    The move function takes four arguments:
        1) The name of the window as a string. This is case sensitive and should be enclosed in quotation marks if it contains spaces or special characters (e.g., &quot;Microsoft Word&quot;).
        2) The x-coordinate of the desired location on your screen, measured in pixels from the left edge of your screen to where you want your window located (e.g., 100).
        3) The y-coordinate of the desired location on your screen, measured in pixels from the top edge of your screen

    :param window: str: Specify the name of the window
    :param x: int: Set the x position of the window, y is used to set the y position
    :param y: int: Set the y position of the window, measured in pixels from the top edge of your screen
    :param width: Set the width of the window
    :param length: Set the height of the window
    :return: None
    """
    try:
        screensize = os.getenv("SCREENSIZE")[1:-1].split(", ")
        screensize = [int(i) for i in screensize]
    except TypeError:
        screensize = get_screensize()[0]
    appname: str = window
    xpos: int = x
    ypos: int = y
    if width is None:
        width: int = int((screensize[0] / 10) * 9)
    if length is None:
        length: int = int((screensize[1] / 10) * 9)

    def enumHandler(hwnd, lParam):
        if win32gui.IsWindowVisible(hwnd) and appname in win32gui.GetWindowText(hwnd):
            win32gui.MoveWindow(hwnd, xpos, ypos, width, length, True)

    win32gui.EnumWindows(enumHandler, None)


def intro_video(args, media_player):
    """
    The intro_video function is used to play the intro video and greeting audio.
        It also maximizes the VLC window if it's not already maximized.

    :param args: Pass the arguments from the command line to this function
    :param media_player: Play the intro video
    :return: Nothing
    """
    if args.restart is None:
        return
    with contextlib.suppress(Exception):
        sleep(0.1)
        window = pygetwindow.getWindowsWithTitle("VLC (Direct3D11 output)")[0]
        window.activate()
        window.maximize()
    sleep(2.5)
    mixer.init()
    mixer.music.load("assets/greeting.mp3")
    mixer.music.play()
    sleep(2.5)
    media_player.stop()


def show_cmd(args):
    """
    The show_cmd function is used to activate the window with the title 'Známé'
        if it exists. If it does not exist, then an IndexError will be raised and
        handled by error_get().

    :return: The window object
    """
    try:
        if args.test is not None:
            window = pygetwindow.getWindowsWithTitle("ZnámE")[0]
            window.activate()
            return window
    except IndexError:
        exit = True
        raise IndexError(
            "Possible solution; run in cmd or python application not ide or put arguments '--test'"
        )


def wait_for_file(path):
    """
    The wait_for_file function waits for a file to be created.
        It takes one argument, the path of the file to wait for.
        The function will loop until it finds that the file exists.

    :param path: Specify the path of the file you want to wait for
    :return: Nothing
    """
    while True:
        leave: bool = any(i == path for i in os.listdir())
        if leave:
            sleep(0.05)
            break


def double_alt_tab():
    """
    The double_alt_tab function is used to switch between windows.
    It does this by pressing the alt key, then tab, then releasing the alt key.
    Then it presses the alt key again and tabs once more before releasing it.

    :return: None
    """
    alt_tab()
    alt_tab()


def alt_tab():
    pg.keyDown("alt")
    pg.press("tab")
    pg.keyUp("alt")


def press_win():
    """
    The press_win function presses the Windows key twice.

    :return: Nothing
    """
    pg.press("win")
    sleep(0.25)
    pg.press("win")
