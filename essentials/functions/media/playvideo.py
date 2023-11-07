import contextlib
import urllib
import requests
import re
from pygame import mixer
from bs4 import BeautifulSoup
from .media import DownloadVideo, PlayVideo
import logging
from .sponsorblock import sponsorblock
import os
import validators


def main():
    while True:
        vstup = input("Use sponsorblock (y/N) >")
        if vstup in ["y", "Y"]:
            _sponsorblock = True
            break
        elif vstup in ["", "n", "N"]:
            _sponsorblock = False
            break

    music_name: str = str(input("Name of the video> "))
    clip2 = music_name if validators.url(music_name) else get_url(music_name)
    with contextlib.suppress(Exception):
        mixer.music.pause()
    path = DownloadVideo(clip2, directory=".", sponsorblock=_sponsorblock)
    os.system("Title ZnámE")
    os.system(f"\"C:\\Program Files\\VideoLAN\\VLC\\vlc.exe\" {path}")
    with contextlib.suppress(Exception):
        mixer.music.unpause()

    print("")


def get_url(music_name):
    print("Refactoring to url-like string ...", end="\r")
    query_string = urllib.parse.urlencode({"search_query": music_name})
    print("Refactoring to url-like string DONE")
    print("Opening site ...", end="\r")
    formatUrl = urllib.request.urlopen(
        f"https://www.youtube.com/results?{query_string}"
    )
    logging.debug(f"Searched in: https://www.youtube.com/results?{query_string}")
    print("Opening site DONE")
    print("Finding video ...", end="\r")
    search_results = re.findall(r"watch\?v=(\S{11})", formatUrl.read().decode())
    print("Finding video DONE\n")
    result = f"https://www.youtube.com/watch?v={search_results[0]}"
    logging.debug(f"Found: https://www.youtube.com/watch?v={search_results[0]}")
    return result
