import contextlib
from pytube import YouTube
import os
import shutil
import vlc
import pygetwindow
import ctypes
import keyboard
from time import sleep
import glob
import sys


def DownloadVideo(
    link: str, name: str = "video", directory: str = "assets", sponsorblock=False
) -> str:
    """
    The Download function downloads the video from YouTube.
    It takes in a link as an argument and then downloads the video.

    :param link: Download the video from youtube
    :return: The name of the file that has been downloaded
    """
    if sponsorblock:
        os.system(
            f"yt-dlp {link} -o {directory}/{name} --restrict-filenames --sponsorblock-remove all --windows-filenames "
        )
    else:
        os.system(
            f"yt-dlp {link} -o {directory}/{name} --restrict-filenames --windows-filenames "
        )

    return glob.glob(f"{directory}/{name}.*")[0]


def play_loop():
    """
    The play_loop function creates a new instance of VLC, then creates a media list and player.
    It adds the video to the media list, sets it to loop infinitely, and plays it.

    :return: A media_player object
    """
    player = vlc.Instance("--input-repeat=999999")
    media_list = player.media_list_new()
    media_player = player.media_list_player_new()
    media = player.media_new("assets/waifu.mp4")
    media_list.add_media(media)
    media_player.set_media_list(media_list)
    player.vlm_set_loop("waifu", True)
    media_player.play()
    return media_player
