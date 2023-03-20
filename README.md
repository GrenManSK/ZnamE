# **ZnamE**

Using [krkr-xp3](https://github.com/awaken1ng/krkr-xp3) as extraction tool

Rewritten to python3 and added some functions to work with ZnámE

Using [anime-chan](https://github.com/RocktimSaikia/anime-chan) for motivation function

Using [nekos-best](https://github.com/nekos-best) for NEKO photos

Using [waifu-api](https://github.com/Waifu-pics/waifu-api) for WAIFU photos

---

**Test login credentials:**
PID: 426738
Password: 123456

Program will make backup files and credentials saves in 'C:/Users/your_name/AppData/Local/ZnámE'

---

## Installation

If you have already installed pytube go to the pytube directory and cipher.py file ({your_python}/site-packages/pytube/cipher.py)

On line 411 remove all content of the line and change it to 'transform_plan_raw = js'

Without it download music function from yml file won't work

---

## **Config options**

```yaml
basic info:
  enviroment: [0-f][0-f]
  inactivelimit: [Any number]
  intro: [True/False]
  lang: ['SK', 'EN', 'JP']
  music: [disable/enable]
  musiclist: [Any Youtube video title, divided by comma]
  musicnumber: [Any number; Max is number of items in musiclist]
game settings:
  computer_power: [Any number; Lower the powerfull]
  goal_score: [Any number]
neko settings:
  server: ['nekos.best', 'waifu.pics', 'kyoko', 'nekos_api']
user history:
waifu settings:
  category (sfw): ['waifu', 'neko', 'shinobu', 'megumin', 'bully', 'cuddle', 'cry', 'hug', 'awoo', 'kiss', 'lick', 'pat', 'smug', 'bonk', 'yeet', 'blush', 'smile', 'wave', 'highfive', 'handhold', 'nom', 'bite', 'glomp', 'slap', 'kill', 'kick', 'happy', 'wink', 'poke', 'dance', 'cringe']
  category (nsfw): ['waifu', 'neko', 'trap', 'blowjob']
  type: [sfw/nsfw]
```

---

CLI Arguments

```plain
-lang --language {EN, SK, JP} # Select language of the aplication defaut to config option
-v --version {} # Show version of the app
-ef --endf {} # Will not automatically end program
-ni --nointro {} # Will not start intro
-co --configoptions {} # Will make a file with all config options, frankly speaking it will put previous text to file
-music --music {Any number} # Max is number of items in 'basic info' => 'musiclist' in config file
```
