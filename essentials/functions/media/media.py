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



def DownloadVideo(link: str, name: str = 'video', directory: str = 'assets') -> str:
    """
    The Download function downloads the video from YouTube.
    It takes in a link as an argument and then downloads the video.

    :param link: Download the video from youtube
    :return: The name of the file that has been downloaded
    """
    os.system(f"{sys.executable} -m yt_dl video -l \"{link}\" ")
    for out_file in glob.glob('Video_File_Save/*.mp4'):
        pass
    base, ext = os.path.splitext(out_file)
    base = os.path.basename(base)
    base.replace("[", "(")
    base.replace("]", ")")
    base.replace("'", "")
    base.replace("\"", "")
    new_file = 'video.mp4'
    print(os.path.join(out_file))
    print(os.path.join('assets\\' + new_file))
    shutil.copy(os.path.join(out_file) ,os.path.join('assets\\' + new_file))
    os.remove(out_file)
    print('Done\n')
    shutil.rmtree('Video_File_Save')
    
    return base


def PlayVideo(video_path: str = 'assets/video.mp4', repeat: bool = False) -> None:
    """
    The PlayVideo function plays a video from the specified path.
        The function will play the video in full screen mode and will not return until the user presses 'Q' to quit.


    :param video_path: Specify the path to the video file that should be played
    :return: Nothing
    """

    media_player = vlc.MediaPlayer()
    media_player.set_fullscreen(True)
    media = vlc.Media(video_path)
    media_player.set_media(media)
    sleep(1)
    print("Press 'Q' to stop video")
    input('Press enter to continue')
    media_player.play()
    try:
        sleep(0.25)
        window = pygetwindow.getWindowsWithTitle(
            'VLC (Direct3D11 output)')[0]
        window.activate()
        window.maximize()
    except Exception:
        pass
    while True:
        if keyboard.is_pressed('q'):
            media_player.stop()
            ctypes.windll.user32.keybd_event(0x8, 0, 0, 0)
            sleep(0.01)
            ctypes.windll.user32.keybd_event(0x8, 0, 2, 0)
            sleep(0.01)
            break


def play_loop():
    player = vlc.Instance('--input-repeat=999999')
    media_list = player.media_list_new()  # type: ignore
    media_player = player.media_list_player_new()  # type: ignore
    media = player.media_new(
        "assets/waifu.mp4")  # type: ignore
    media_list.add_media(media)
    media_player.set_media_list(media_list)
    player.vlm_set_loop(
        "waifu", True)  # type: ignore
    media_player.play()
    return media_player