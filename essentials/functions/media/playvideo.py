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
        vstup = input('Use sponsorblock (y/N) >')
        if vstup in ['y', 'Y']:
            _sponsorblock = True
            break
        elif vstup in ['', 'n', 'N']:
            _sponsorblock = False
            break

    while True:
        videovstup: str = input(
            '1) Search your own video\n2) back\n> ')
        if videovstup == '1':
            music_name: str = str(input('Name of the video> '))
            if not validators.url(music_name):
                query_string = urllib.parse.urlencode({"search_query": music_name})
                formatUrl = urllib.request.urlopen(
                    "https://www.youtube.com/results?" + query_string)
                logging.debug(
                    "Searched in: https://www.youtube.com/results?" + query_string)
                search_results = re.findall(
                    r"watch\?v=(\S{11})", formatUrl.read().decode())
                # deepcode ignore Ssrf: <User input to video on Youtube>
                clip = requests.get("https://www.youtube.com/watch?v=" +
                                    "{}".format(search_results[0]))
                clip2 = "https://www.youtube.com/watch?v=" + \
                    "{}".format(search_results[0])
                logging.debug("Found: https://www.youtube.com/watch?v=" +
                            "{}".format(search_results[0]))
                inspect = BeautifulSoup(clip.content, "html.parser")
                yt_title = inspect.find_all("meta", property="og:title")
                for concatMusic1 in yt_title:
                    pass
            else:
                clip2 = music_name
            try:
                mixer.music.pause()
            except Exception:
                pass
            DownloadVideo(clip2)
            os.system('Title ZnámE')
            if _sponsorblock:
                sponsorblock(clip2)
            PlayVideo()
            try:
                mixer.music.unpause()
            except Exception:
                pass
        elif videovstup == '2':
            break
