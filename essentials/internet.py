import requests
from time import sleep
import os
from .writing import printnlog
import sys
from threading import Thread
import inspect


def get_line_number(goback: int = 0, relative_frame: int = 1) -> int:
    """
    The get_line_number function returns the line number of the caller.

        The get_line_number function is a helper function that returns the line number of 
        where it was called from. This can be useful for debugging purposes, or to help 
        identify where an error occurred in your code. It also allows you to go back a few lines if needed, which can be helpful when using this function inside loops and other functions that may have multiple calls on one line (such as list comprehensions).

    :param goback: int: Go back a certain number of lines in the stackconfig.
    :param relative_frame: int: Specify the frame in the stack to get the line number from
    :return: The line number of the function call
    """
    return int(inspect.stack()[relative_frame][0].f_lineno)-int(goback)

def internet(args, datelog):
    number = 0
    while True:
        sleep(1)
        if os.path.isfile('INTERNET_CHECK_CORRECT'):
            os.remove('INTERNET_CHECK_CORRECT')
            break
        number += 1
        if 10 >= number >= 5:
            if args.language == "SK":
                printnlog(
                    "Zdá sa, že máme problém s internetovým pripojením")
            elif args.language == "EN":
                printnlog(
                    "Seems like we're having trouble with internet connection")
            elif args.language == "JP":
                printnlog(
                    "インターネット接続に問題があるようです\nIf you don't see any of characters watch 'help.txt'")
            break
        if number >= 10:
            break

def internet_check(args, datelog) -> None:
    try:
        global requests
        import requests
        timeout: int = 10
        Thread(target=internet, args=(args, datelog)).start()
        requests.head("http://www.google.com/", timeout=timeout)
        try:
            open('INTERNET_CHECK_CORRECT', 'x')
        except FileExistsError:
            pass
    except requests.ConnectionError:  # type: ignore
        line_number: int = get_line_number()
        if __name__ == '__main__':
            if args.language == "SK":
                printnlog("Vaše internetové pripojenie nefunguje")
            elif args.language == "EN":
                printnlog("The internet connection is down")
            elif args.language == "JP":
                printnlog(
                    "インターネット接続がダウンしています\nIf you don't see any of characters watch 'help.txt'")
            sleep(2)
            sys.exit(1)