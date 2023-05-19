# **ZnamE**

![Commit activity](https://img.shields.io/github/commit-activity/m/GrenManSK/ZnamE)
![Lines of code](https://img.shields.io/tokei/lines/github/GrenManSK/ZnamE?label=lines%20of%20code)
![License](https://img.shields.io/github/license/GrenManSK/ZnamE)
![Contributors](https://img.shields.io/github/contributors/GrenManSK/ZnamE)
![Issues](https://img.shields.io/github/issues/GrenManSK/ZnamE)
![Language](https://img.shields.io/github/languages/top/GrenManSK/ZnamE)
![Code Size](https://img.shields.io/github/languages/code-size/GrenManSK/ZnamE)
![Star](https://img.shields.io/github/stars/GrenManSK/ZnamE?style=social)
![Last Commit](https://img.shields.io/github/last-commit/GrenManSK/ZnamE)

Using [krkr-xp3](https://github.com/awaken1ng/krkr-xp3) as extraction tool

Rewritten to python3 and added some functions to work with ZnámE

Using [spotDL](https://github.com/spotDL/spotify-downloader) for music function

Using [anime-chan](https://github.com/RocktimSaikia/anime-chan) for motivation function

Using [nekos-best](https://github.com/nekos-best) for NEKO photos

Using [waifu-api](https://github.com/Waifu-pics/waifu-api) for WAIFU photos

Using [ytdownload](https://github.com/KalebSchmidlkofer/ytdownload) for music from config

Using [manga-image-translator](https://github.com/zyddnys/manga-image-translator) for manga_translator function

Using [textractor](https://github.com/Artikash/Textractor) for translate function

---

**Test login credentials:**
PID: 426738
Password: 123456

Program will make backup files and credentials saves in 'C:/Users/your_name/AppData/Local/ZnámE'

---

## Installation

Firstly use the following command `pip install -r requirements.txt`

If in requirements.txt are some missing dependencies program will automatically install them

In file `choco_packages.json`, you can see the list of other dependencies which will be installed as part of first time installation

---

## Main functions

- waifu | neko
- VOICEVOX
- login
- music

---

### `config.yml` hereinafter as config or config file

---

## Important notice

### Works only on Windows

---

## waifu | neko

- Downloads image from API server and opens it
- neko - as title says, it will return cat-themed images
  - can define sevver from which image will be downloaded
- waifu - returns image on theme which is configured in config file
  - If image is gif then program converts it to video and opens it

---

## VOICEVOX

- Ability to choose from conda environments if installed or classic interpreter
- Downloads repository [VOICEVOX](https://github.com/GrenManSK/VOICEVOX), installs pip requirements, downloads engine [VOICEVOX_engine](https://github.com/VOICEVOX/voicevox_engine/releases/tag/0.14.4) (986mb) and run VOICEVOX
- First time install will also download medium.en and base.en model from [whisper](https://github.com/openai/whisper#available-models-and-languages) (Around 1.5gb)
- From microphone gets an input, AI process the audio file, get text from it, convert it to AI voice, play it through VB-Audio Virtual Cable as input device and current output device

---

## login

- From encrypted file check if user inputed username and password are correct
- if yes then proceed to login
- else print error message and retry

---

## Music

### Config file

- `basic info => music` - change to `enable` to enable music
- `basic info => musiclist` - From YouTube converts to mp3 file
- `basic info => musicnumber` - Define index of which music file to play

### Function

- Can select from existing music list which is configured in `basic info => musiclist`
- Can download music through `spot-dl`
- Also updates `basic info => musiclist` in config

---

## Manga_translator

- Choose from conda environments or classic interpreter
- Using [manga-image-translator](https://github.com/zyddnys/manga-image-translator) for this function
- Translate manga images

---

## Motivational

- Returns quote from anime

---

## KayoPy

- Downloads repository [KayoPy](https://github.com/GrenManSK/KayoPy), installs pip requirements and run KayoPy
- Parser of [kayoanime](https://kayoanime.com/) site for anime download

---

## cbzPrintable

- Downloads repository [cbzPrintable](https://github.com/GrenManSK/cbzPrintable), installs pip requirements and run KayoPy
- From cbz files return pdf of multiple cbz files with some formatting so it could be printed like a book (Duplex printing)

---

## PlayVideo

- Searches for video on YouTube and downloads it, then plays it

---

## Anime_search

- Upload image or input an url to search for episode which image is from
- Works on trace.moe API

---

## **Config options**

```yaml
basic info:
  environmentA: [0-f]
  environmentB: [0-f]
  inactivelimit: [Any number]
  intro: [True/False]
  music: [disable/enable]
  musiclist: [Any Youtube video title, divided by comma]
  musicnumber: [Any number; Max is number of items in musiclist]
  translate: [''|'Afrikaans','Albanian','Amharic','Arabic','Armenian','Assamese','Aymara','Azerbaijani','Bambara','Basque','Belarusian','Bengali','Bhojpuri','Bosnian','Bulgarian','Catalan','Cebuano','Chichewa','Chinese (Simplified)','Chinese (Traditional)','Corsican','Czech','Danish','Dhivehi','Dogri','Dutch','English','Esperanto','Estonian','Ewe','Filipino','Finnish','French','Frisian','Galician','Georgian','German','Greek','Guarani','Gujarati','Haitian Creole','Hausa','Hawaiian','Hindi','Hmong','Hungarian','Icelandic','Igbo','Ilocano','Indonesian','Irish','Italian','Japanese','Javanese','Kannada','Kazakh','Khmer','Kinyarwanda','Konkani','Korean','Krio','Kurdish (Kurmanji)','Kurdish (Sorani)','Kyrgyz','Lao','Latvian','Lingala','Lithuanian','Luganda','Luxembourgish','Macedonian','Maithili','Malagasy','Malay','Malayalam','Maltese','Maori','Marathi','Meiteilon (Manipuri)','Mizo','Mongolian','Myanmar (Burmese)','Nepali','Norwegian','Odia (Oriya)','Oromo','Pashto','Polish','Portuguese','Punjabi','Quechua','Romanian','Russian','Samoan','Sanskrit','Scots Gaelic','Sepedi','Serbian','Sesotho','Shona','Si ndhi','Sinhala','Slovak','Slovenian','Somali','Spanish','Sundanese','Swahili','Swedish','Tamil','Tatar','Telugu','Thai','Tigrinya','Tsonga','Turkish','Turkmen','Twi','Ukrainian','Urdu','Uyghur','Uzbek','Vietnamese','Welsh','Xhosa','Yiddish','Yoruba','Zulu']
  translator: [Bing|Google]
game settings:
  computer_power: [Any number; Lower the powerfull]
  goal_score: [Any number]
  offline_game: [True/False]
neko settings:
  server: ['nekos.best', 'waifu.pics', 'kyoko', 'nekos_api']
user history:
waifu settings:
  category (sfw): ['waifu', 'neko', 'shinobu', 'megumin', 'bully', 'cuddle', 'cry', 'hug', 'awoo', 'kiss', 'lick', 'pat', 'smug', 'bonk', 'yeet', 'blush', 'smile', 'wave', 'highfive', 'handhold', 'nom', 'bite', 'glomp', 'slap', 'kill', 'kick', 'happy', 'wink', 'poke', 'dance', 'cringe']
  category (nsfw): ['waifu', 'neko', 'trap', 'blowjob']
  type: [sfw/nsfw]
```

---

## CLI Arguments

```plain
-v --version {} # Show version of the app
-ef --endf {} # Will not automatically end program
-ni --nointro {} # Will not start intro
-co --configoptions {} # Will make a file with all config options, frankly speaking it will put previous text to file
-music --music {Any number} # Max is number of items in 'basic info' => 'musiclist' in config file
--quiet => Won't print any unnecessary logging
```
