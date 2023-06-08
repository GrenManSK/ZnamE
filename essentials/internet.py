import requests
from time import sleep
import os
from .functions.writing import printnlog
import sys
from threading import Thread
from tqdm import tqdm
import logging
from .system.system_info import get_line_number


def internet():
    """
    The internet function checks if the internet is working.
        It does this by checking if a file called INTERNET_CHECK_CORRECT exists.
        If it doesn't exist, then we know that there's no internet connection.
    
    :return: A boolean value, true if the internet is working and false if it's not
    """
    number = 0
    while True:
        sleep(1)
        if os.path.isfile("INTERNET_CHECK_CORRECT"):
            os.remove("INTERNET_CHECK_CORRECT")
            break
        number += 1
        if 10 >= number >= 5:
            printnlog("Seems like we're having trouble with internet connection")
            break
        if number >= 10:
            break


def internet_check() -> None:
    """
    The internet_check function checks if the internet is up and running.
    If it isn't, then the program will exit with an error code of 1.
    
    :return: Nothing
    """
    try:
        global requests
        import requests

        timeout: int = 10
        Thread(target=internet).start()
        requests.head("http://www.google.com/", timeout=timeout)
        try:
            open("INTERNET_CHECK_CORRECT", "x")
        except FileExistsError:
            pass
    except requests.ConnectionError:
        line_number: int = get_line_number()
        printnlog("The internet connection is down")
        sleep(2)
        sys.exit(1)


def download(url: str, fname: str, chunk_size: int = 1024) -> bool:
    """
    "Download a file from a URL to a local file."

    The first line is the function's signature. It's a single line of code that tells you everything
    you need to know about the function

    :param url: The URL of the file to download
    :type url: str
    :param fname: The name of the file to be downloaded
    :type fname: str
    :param chunk_size: The size of the chunks to download, defaults to 1024 (optional)
    """
    try:
        resp = requests.get(url, stream=True)
        total: int = int(resp.headers.get("content-length", 0))
        with open(fname, "wb") as file, tqdm(
            desc=fname,
            total=total,
            unit="iB",
            unit_scale=True,
            unit_divisor=1024,
        ) as bar:
            for data in resp.iter_content(chunk_size=chunk_size):
                size = file.write(data)
                bar.update(size)
    except ConnectionError:
        logging.warning("Connection error")
        return False
    return True
