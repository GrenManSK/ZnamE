import webbrowser
import pyautogui as pg
from time import sleep
import pygetwindow
from ..system.system_operations import show_cmd


def playhtml(args, config, htmlFile: str, mode: int = 0, time: int = 0):
    """
    The playhtml function is used to open the html file containing the game's intro.
    It can be called in two ways:
        1) playhtml(htmlFile, mode=0, time=0):  # mode = 0 means that it will click through all of the intro automatically.
                                                # time = 0 means that it will not wait for a specific amount of time before clicking
                                                # through each part of the intro.

    :param htmlFile: str: Specify which html file to open
    :param mode: int: Determine whether the function is used to start a new game or load an existing one
    :param time: int: Specify how long the mouseclick function should wait before clicking
    :return: Nothing
    """
    from mouse import mouseclick  # type: ignore

    if args.nointro is None or args.nointrof is None:
        args.nointrof = object()
        if args.test is None and config["basic info"]["intro"] == True:
            webbrowser.open(htmlFile + ".html", 1)
            sleep(1)
            pg.press("f11")
            if mode == 0:
                mouseclick()
            elif mode == 1:
                mouseclick(time=time)
        else:
            pass
    else:
        if config["basic info"]["intro"] == True:
            webbrowser.open(htmlFile + ".html", 1)
            sleep(1.5)
            pg.press("f11")
            if mode == 0:
                mouseclick()
            elif mode == 1:
                mouseclick(time=time)
            show_cmd(args)
        else:
            pass
