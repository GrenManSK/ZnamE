# **ZnamE**

Using https://github.com/awaken1ng/krkr-xp3 as extraction tool

Rewritten to python3 and added some functions to work with ZnámE

Using https://github.com/RocktimSaikia/anime-chan for motivation function

Using https://github.com/nekos-best for NEKO photos

Using https://github.com/Waifu-pics/waifu-api for WAIFU photos

---

**Test login credentials:**
PID: 426738
Password: 123456

Program will make backup files and credentials saves in 'C:/Users/your_name/AppData/Local/ZnámE'

---

## **Config options**

```
[BASIC INFO]
lang = ['SK', 'EN', 'JP']
enviroment = [0-f][0-f]
intro = [True/False]
inactivelimit = [Any number]
music = [disable/enable]
musiclist = [Any Youtube video title, divided by comma]
musicnumber = [Any number; Max is number of items in musiclist]
[WAIFU SETTINGS]
type = [sfw/nsfw]
category (sfw) = ['waifu', 'neko', 'shinobu', 'megumin', 'bully', 'cuddle', 'cry', 'hug', 'awoo', 'kiss', 'lick', 'pat', 'smug', 'bonk', 'yeet', 'blush', 'smile', 'wave', 'highfive', 'handhold', 'nom', 'bite', 'glomp', 'slap', 'kill', 'kick', 'happy', 'wink', 'poke', 'dance', 'cringe']
category (nsfw) = ['waifu', 'neko', 'trap', 'blowjob']
[NEKO SETTINGS]
server = ['nekos.best', 'waifu.pics', 'kyoko', 'nekos_api']
[GAME SETTINGS]
goal_score = [Any number]
computer_power = [Any number; Lower the powerfull]

```
---

CLI Arguments

```
-lang --language {EN, SK, JP} # Select language of the aplication defaut to config option
-v --version {} # Show version of the app
-ef --endf {} # Will not automatically end program
-ni --nointro {} # Will not start intro
-co --configoptions {} # Will make a file with all config options, frankly speaking it will put previous text to file
-music --music {Any number} # Max is number of items in 'basic info' => 'musiclist' in config file
```