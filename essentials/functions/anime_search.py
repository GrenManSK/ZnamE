from edupage import typewriter, download
from .media.media import PlayVideo
import os
import datetime
import shutil
import urllib.parse
from PIL import Image
import pyautogui as pg
from showinfm import show_in_file_manager
from time import sleep
import requests
import logging


def main():
    while True:
        anime_vstup: str = input('1) image upload\n2) url link\n3) back\n> ')
        if anime_vstup == '1':
            try:
                os.mkdir('anime_search/')
            except FileExistsError:
                pass
            input('Firstly you will be redirected to \'anime_search\' directory and you need to put your image to folder as \'anime.png\' click enter to continue> ')
            show_in_file_manager('anime_search/')
            logging.debug(os.path.abspath('anime_search/'))
            sleep(0.1)
            show_in_file_manager('./')
            logging.debug(os.path.abspath('./'))
            sleep(1)
            pg.hotkey('win', 'left')
            sleep(0.5)
            pg.press('enter')
            koniec: bool = False
            while not koniec:
                try:
                    for i in os.listdir('anime_search'):
                        if (name := i.split('.'))[1] == 'png':
                            sleep(0.5)
                            if name[0] == 'anime':
                                koniec: bool = True
                            else:
                                os.rename(
                                    f'anime_search/{i}', 'anime_search/anime.png')
                                koniec: bool = True
                        if (name := i.split('.'))[1] in ['jpg', 'jpeg', 'jpe', 'jif', 'jfif', 'jfi', 'gif', 'webp', 'tiff', 'tif', 'psd', 'raw', 'arw', 'cr2', 'nrw', 'k25', 'bmp', 'dib', 'heif', 'heic', 'ind', 'indd', 'jp2', 'j2k', 'jpf', 'jpx', 'jpm', 'mj2', 'svg', 'svgz', 'ai', 'eps', 'pdf']:
                            sleep(0.5)
                            os.rename(
                                f'anime_search/{i}', 'anime_search/anime.png')
                            koniec: bool = True
                except FileNotFoundError:
                    break
            if not koniec:
                continue
            try:
                anime = requests.post("https://api.trace.moe/search", data=open(
                    "anime_search/anime.png", "rb"), headers={"Content-Type": "image/jpeg"}).json()
            except FileNotFoundError:
                continue
            for i in anime['result']:
                anime_id: int = int(i['anilist'])
                anime_filename: str = i['filename']
                anime_episode: str = i['episode']
                anime_from: str = i['from']
                anime_to: str = i['to']
                anime_similarity: str = i['similarity']
                anime_video: str = i['video']
                anime_image: str = i['image']
                break
            print(f'Anime name: {anime_filename}')
            print(f'Episode: {anime_episode}')
            while True:
                anime_vstup_success: str = input(
                    '1) Play video\n2) Show image\n3) Timeline\n4) Similarity\n5) back\n> ')
                if anime_vstup_success == '1':
                    download(anime_video, 'anime_search/anime_video.mp4')
                    PlayVideo('anime_search/anime_video.mp4', repeat=True)
                    anime_vstup_video: str = input('Save (Y/n)> ').lower()
                    if anime_vstup_video in ['', 'y']:
                        imagetime: str = str(
                            datetime.datetime.now().strftime("%H-%M-%S"))
                        try:
                            os.mkdir('download/')
                            typewriter(
                                'Making directory \'download\'', end='\r')
                        except Exception:
                            pass
                        typewriter(
                            'Copying video to download folder', end='\r')
                        shutil.copy(
                            'anime_search/anime_video.mp4', 'download/anime_video-' + imagetime + '.mp4')
                        typewriter(
                            'Done                                            ')
                elif anime_vstup_success == '2':
                    download(anime_image, 'anime_search/anime_image.png')
                    img = Image.open('anime_search/anime_image.png')
                    typewriter('Opening image   ', end='\r')
                    img.show()
                    sleep(0.1)
                    pg.keyDown('win')
                    typewriter('......                        ', end='\r')
                    pg.press('up')
                    typewriter('.......', end='\r')
                    pg.keyUp('win')
                    typewriter('........', end='\r')
                    sleep(0.5)
                    typewriter('..........                  ', end='\r')
                    sleep(0.25)
                    typewriter('.............', end='\r')
                    typewriter('DONE           ')
                    anime_vstup_image: str = input('Save (Y/n)> ').lower()
                    if anime_vstup_image in ['', 'y']:
                        imagetime: str = str(
                            datetime.datetime.now().strftime("%H-%M-%S"))
                        try:
                            os.mkdir('download/')
                            typewriter(
                                'Making directory \'download\'', end='\r')
                        except Exception:
                            pass
                        typewriter(
                            'Copying video to download folder', end='\r')
                        shutil.copy(
                            'anime_search/anime_image.png', 'download/anime_image-' + imagetime + '.png')
                        typewriter(
                            'Done                                            ')
                elif anime_vstup_success == '3':
                    print(
                        f'It\'s in episode {anime_episode} from time {anime_from} to {anime_to}')
                elif anime_vstup_success == '4':
                    print(f'Similarity is {anime_similarity}')
                elif anime_vstup_success == '5':
                    break
        elif anime_vstup == '2':
            try:
                anime = requests.get("https://api.trace.moe/search?url={}".format(
                    urllib.parse.quote_plus(input("Paste here image url>")))).json()
            except FileNotFoundError:
                continue
            for i in anime['result']:
                anime_id: int = int(i['anilist'])
                anime_filename: str = i['filename']
                anime_episode: str = i['episode']
                anime_from: str = i['from']
                anime_to: str = i['to']
                anime_similarity: str = i['similarity']
                anime_video: str = i['video']
                anime_image: str = i['image']
                break
            print(f'Anime name: {anime_filename}')
            print(f'Episode: {anime_episode}')
            while True:
                anime_vstup_success: str = input(
                    '1) Play video\n2) Show image\n3) Timeline\n4) Similarity\n5) back\n> ')
                if anime_vstup_success == '1':
                    download(anime_video, 'anime_search/anime_video.mp4')
                    PlayVideo('anime_search/anime_video.mp4', repeat=True)
                    anime_vstup_video: str = input('Save (Y/n)> ').lower()
                    if anime_vstup_video in ['', 'y']:
                        imagetime: str = str(
                            datetime.datetime.now().strftime("%H-%M-%S"))
                        try:
                            os.mkdir('download/')
                            typewriter(
                                'Making directory \'download\'', end='\r')
                        except Exception:
                            pass
                        typewriter(
                            'Copying video to download folder', end='\r')
                        shutil.copy(
                            'anime_search/anime_video.mp4', 'download/anime_video-' + imagetime + '.mp4')
                        typewriter(
                            'Done                                            ')
                elif anime_vstup_success == '2':
                    download(anime_image, 'anime_search/anime_image.png')
                    img = Image.open('anime_search/anime_image.png')
                    typewriter('Opening image   ', end='\r')
                    img.show()
                    sleep(0.1)
                    pg.keyDown('win')
                    typewriter('......                        ', end='\r')
                    pg.press('up')
                    typewriter('.......', end='\r')
                    pg.keyUp('win')
                    typewriter('........', end='\r')
                    sleep(0.5)
                    typewriter('..........                  ', end='\r')
                    sleep(0.25)
                    typewriter('.............', end='\r')
                    typewriter('DONE           ')
                    anime_vstup_image: str = input('Save (Y/n)> ').lower()
                    if anime_vstup_image in ['', 'y']:
                        imagetime: str = str(
                            datetime.datetime.now().strftime("%H-%M-%S"))
                        try:
                            os.mkdir('download/')
                            typewriter(
                                'Making directory \'download\'', end='\r')
                        except Exception:
                            pass
                        typewriter(
                            'Copying video to download folder', end='\r')
                        shutil.copy(
                            'anime_search/anime_image.png', 'download/anime_image-' + imagetime + '.png')
                        typewriter(
                            'Done                                            ')
                elif anime_vstup_success == '3':
                    print(
                        f'It\'s in episode {anime_episode} from time {anime_from} to {anime_to}')
                elif anime_vstup_success == '4':
                    print(f'Similarity is {anime_similarity}')
                elif anime_vstup_success == '5':
                    break
        elif anime_vstup == '3':
            break
