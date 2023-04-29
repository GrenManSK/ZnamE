import cv2
import glob
from .exceptions import error_get
from .system_info import get_line_number
from time import sleep
import pygetwindow
import os
import traceback
import sys
import ctypes
import win32gui


def getWindow(args) -> bool:
    """
    The getWindow function is used to find the window of Známý (the game) and activate it.
    It also checks if the file 'banner.png' exists in the assets folder.

    :return: If error occured
    """
    dummy = None
    cv2.namedWindow('frame2', cv2.WND_PROP_FULLSCREEN)
    cv2.setWindowProperty(
        'frame2', cv2.WND_PROP_FULLSCREEN, cv2.WINDOW_FULLSCREEN)
    test: str = "assets/banner.png"
    for file in glob.glob(test):
        dummy = cv2.imread(file)
    try:
        cv2.imshow("Image", dummy)
    except cv2.error:
        error_get(cv2.error('File is corrupt (probably \'banner.png\')'), [
            get_line_number()])
        return True
    cv2.waitKey(1)
    sleep(0.1)
    cv2.destroyWindow("Image")
    if args.test is not None:
        try:
            window = pygetwindow.getWindowsWithTitle('ZnámE')[0]
            window.activate()
            return False
        except IndexError:
            error_get(IndexError(
                'Possible solution; run in cmd or python aplication not ide or put arguments \'--test\''), [get_line_number()])
            return True
    return False


def isUserAdmin():
    """
    The isUserAdmin function checks to see if the user running this script is an admin.
    This is for Windows only.
    :return: A boolean value
    """
    if os.name == 'nt':
        import ctypes
        # WARNING: requires Windows XP SP2 or higher!
        try:
            return ctypes.windll.shell32.IsUserAnAdmin()
        except:
            traceback.print_exc()
            print("Admin check failed, assuming not an admin.")
            return False
    elif os.name == 'posix':
        # Check for root on Posix
        return os.getuid() == 0
    else:
        raise RuntimeError(
            "Unsupported operating system for this module: %s" % (os.name,))


def runAsAdmin(cmdLine=None, wait=True):
    """
    The runAsAdmin function is a simple function that will run your python script as the Administrator.
    This function will attempt to do the following:
    :param cmdLine: Pass arguments to the executable
    :param wait: Determine whether the function should wait for the process to finish or not
    :return: The process handle of the elevated process
    """
    if os.name != 'nt':
        raise RuntimeError(
            "This function is only implemented on Windows.")

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
    cmd = '"%s"' % (cmdLine[0],)
    params = " ".join(['"%s"' % (x,) for x in cmdLine[1:]])
    cmdDir = ''
    showCmd = win32con.SW_SHOWNORMAL
    lpVerb = 'runas'
    procInfo = ShellExecuteEx(nShow=showCmd,
                              fMask=shellcon.SEE_MASK_NOCLOSEPROCESS,
                              lpVerb=lpVerb,
                              lpFile=cmd,
                              lpParameters=params)
    if wait:
        procHandle = procInfo['hProcess']
        obj = win32event.WaitForSingleObject(
            procHandle, win32event.INFINITE)
        rc = win32process.GetExitCodeProcess(procHandle)
    else:
        rc = None
    return rc


def checkAdmin():
    """
    The checkAdmin function checks if the user is an admin. If not, it will run the program as an admin.
    :return: 0 if the user is an admin, and returns 1 if the user is not an admin
    :doc-author: Trelent
    """
    rc = 0
    if not isUserAdmin():
        print("You're not an admin.",
              os.getpid(), "params: ", sys.argv)
        rc = runAsAdmin()
    else:
        print("You are an admin!", os.getpid(),
              "params: ", sys.argv)
        rc = 0
    return rc


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
    screensize = os.getenv('SCREENSIZE')
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
                width = int((screensize[0]/10)*9)
            if length is None:
                length = int((screensize[1]/10)*9)

            def enumHandler(hwnd, lParam):
                if win32gui.IsWindowVisible(hwnd):  # type: ignore
                    # type: ignore
                    if appname in win32gui.GetWindowText(hwnd):
                        win32gui.MoveWindow(
                            hwnd, xpos, ypos, width, length, True)  # type: ignore
            win32gui.EnumWindows(enumHandler, None)  # type: ignore
        k = cv2.waitKey(33)
        cv2.setWindowProperty(
            name, cv2.WND_PROP_FULLSCREEN, cv2.WINDOW_FULLSCREEN)
        if k == 27:
            break
        elif k == -1:
            continue
        else:
            print(k)
            cv2.destroyAllWindows()
