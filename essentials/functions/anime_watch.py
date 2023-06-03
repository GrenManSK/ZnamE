import os
import glob
import subprocess

vlc_path = "C:/Program Files/VideoLAN/VLC/vlc.exe"


def anime_menu(vlc_path_tmp=None):
    global vlc_path
    if vlc_path_tmp is not None:
        if not os.path.exists(vlc_path_tmp):
            return 1
        vlc_path = vlc_path_tmp
    if not os.path.exists("Anime"):
        if os.path.exists("AnimeArchive"):
            os.remove("AnimeArchive")
        return 1
    elif not os.path.exists("AnimeArchive"):
        anime: set = set()
        if os.path.exists("Anime"):
            for filename in set(glob.glob("Anime/**/**/*", recursive=True)):
                if filename.endswith("tmp") or os.path.isdir(filename):
                    continue
                anime.add(filename)
        anime_text = ""
        for item in anime:
            anime_text += item + "\n"
        with open("AnimeArchive", "w") as file:
            file.write(anime_text)
    else:
        anime: set = set()
        if os.path.exists("Anime"):
            for filename in set(glob.glob("Anime/**/**/*", recursive=True)):
                if filename.endswith("tmp") or os.path.isdir(filename):
                    continue
                anime.add(filename)

        anime = list(anime)

        while True:
            for times, filename in enumerate(anime):
                print(f"{times + 1}) {filename}")

            vstup = input("Which anime do you want to watch? > ")

            if vstup in ["q", "quit"]:
                return 0

            vstup = int(vstup)
            anime_file = anime[vstup - 1]

            anime_play(anime_file)


def anime_play(file_path):
    subprocess.check_output([vlc_path, file_path])
