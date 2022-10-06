import argparse, pkg_resources, sys, os, subprocess, configparser
from time import sleep
print('Reading config file (ini)\n')
sleep(0.25)
config = configparser.RawConfigParser()
config.read('config.ini')
print(config.get('basic info','lang').split(' ')[0])
print('\nDone')
global parser
parser = argparse.ArgumentParser()
UNSPECIFIED = object()
sleep(0.5)
os.system('cls')
parser.add_argument('-lang', '--language', choices=['SK','EN','JP'], help='Language selection', nargs='?')
parser.add_argument('-v', '--version', help='Show version of this program', default=UNSPECIFIED, nargs='?')
parser.add_argument('-ef', '--endf', help='Will not automatically end program', default=UNSPECIFIED, nargs='?')
parser.add_argument('-inactive', '--inactive', choices=[], help='!!! Argument for program to use', default=UNSPECIFIED, nargs='?')
parser.add_argument('-update', '--update', choices=[], help='!!! Argument for program to use (this command won\'t update this program, it does it automatically)', default=UNSPECIFIED, nargs='?')
args = parser.parse_args()
if args.language == None:
    args.language = config.get('basic info', 'lang').split(' ')[0]
if args.update == None:
    os.remove('update.py')
try:
    import requests
    timeout = 1
    requests.head("http://www.google.com/", timeout=timeout)
except requests.ConnectionError: # type: ignore
    if args.language == "SK":
        print("Vaše internetové pripojenie nefunguje")
    if args.language == "EN":
        print("The internet connection is down")
    if args.language == "JP":
        print("If you don't see any of characters watch 'help.txt'\nインターネット接続がダウンしています")
    sleep(2)
    quit()
potrebne = {'psutil', 'numpy','tqdm', 'semantic-version'}
nainstalovane = {pkg.key for pkg in pkg_resources.working_set}
nenajdene = potrebne - nainstalovane
if args.version == None:
    verzia = open('version', 'r')
    print(verzia.read())
    verzia.close()
    if nenajdene:
        if args.language == "SK":
            print('Aktualizácia je k dispozícií: ', *nenajdene)
        if args.language == "EN":
            print('Update is available: ', *nenajdene)
        if args.language == "JP":
            print('アップデートが利用可能です： ', *nenajdene)
    quit()
if nenajdene:
    if args.language == "SK":
        print('Aktualizácia je k dispozícií: ', *nenajdene)
    if args.language == "EN":
        print('Update is available: ', *nenajdene)
    if args.language == "JP":
        print('アップデートが利用可能です： ', *nenajdene)
    sleep(0.5)
    if args.language == "SK":
        print("Sťahujú sa aktualizácie")
    if args.language == "EN":
        print("Downloading updates")
    if args.language == "JP":
        print("アップデートのダウンロード")
    subprocess.check_call([sys.executable, '-m', 'pip', 'install', *nenajdene])
    if args.language == "SK":
        print("Program sa reštartuje!!!")
    if args.language == "EN":
        print("The program is restarting!!!")
    if args.language == "JP":
        print("番組再開！！！")
    sleep(1)
    subprocess.check_call('start python edupage.py -lang ' + args.language, shell=True)
    quit()
os.system('Title ' + 'ZnámE')
from threading import Thread
from tqdm import tqdm
from datetime import datetime
import shutil, zipfile
import semantic_version  
import requests
from pathlib import Path
url = 'https://raw.githubusercontent.com/GrenManSK/ZnamE/main/version'
page = requests.get(url)
verzia = open('version', 'r')

updateapp = str('import argparse, shutil, os, subprocess, configparser\nfrom time import sleep\nUNSPECIFIED = object()\nglobal parser\nparser = argparse.ArgumentParser()\nparser.add_argument(\'-ef\', \'--endf\', help=\'Will not automatically end program\', default=UNSPECIFIED, nargs=\'?\')\nparser.add_argument(\'-lang\', \'--language\', choices=[\'SK\',\'EN\',\'JP\'], help=\'Language selection\', nargs=\'?\')parser.add_argument(\'input\', help=\'Input folder\', nargs=\'?\')\nargs = parser.parse_args()\nconfig = configparser.RawConfigParser()\nconfig.read(\'config.ini\')\nargs.language = config.get(\'basic info\', \'lang\').split(\' \')[0]\nelif args.input != "":\n    sleep(0.5)\n    shutil.move(\'edupage.py\', \'old/edupage.py\')\n    shutil.move(args.input + \'/edupage.py\', \'edupage.py\')\n    sleep(0.2)\n    shutil.rmtree(args.input)\n    if args.endf == None:\n        subprocess.check_call(\'start python edupage.py -lang \' + args.language + \' -endf\', shell=True)\n    else:        subprocess.check_call(\'start python edupage.py -lang \' + args.language + \' -update\', shell=True)\n    shutil.rmtree(\'old\')\n    quit()')










if  semantic_version.Version(page.text[1:]) <= semantic_version.Version(verzia.read()[1:]):
    pass
else:
    if args.language == "SK":
        print("Bola nájdená nová aktualizacia: " + page.text)
    if args.language == "EN":
        print("Newer version was found: " + page.text)
    if args.language == "JP":
        print("新しいバージョンが見つかりました: " + page.text)
    verzia.close()
    sleep(0.5)
    url = 'https://api.github.com/repos/GrenManSK/ZnamE/zipball/main'
    r = requests.get(url)
    filename = "new.zip"
    with open(filename,'wb') as output_file:
        output_file.write(r.content)
    with zipfile.ZipFile("new.zip", mode='r') as zip:
        if args.language == "SK":
            for member in tqdm(iterable=zip.namelist(), total=len(zip.namelist()), desc='Rozbaľujem '):
                try:
                    zip.extract(member)
                    tqdm.write(f"{os.path.basename(member)}(" + str(os.path.getsize(member)) + "KB)")
                    sleep(0.05)
                except zipfile.error as e:
                    pass
        elif args.language == "EN":
            for member in tqdm(iterable=zip.namelist(), total=len(zip.namelist()), desc='Extracting '):
                try:
                    zip.extract(member)
                    tqdm.write(f"{os.path.basename(member)}(" + str(os.path.getsize(member)) + "KB)")
                    sleep(0.05)
                except zipfile.error as e:
                    pass
        elif args.language == "JP":
            for member in tqdm(iterable=zip.namelist(), total=len(zip.namelist()), desc='抽出中 '):
                try:
                    zip.extract(member)
                    tqdm.write(f"{os.path.basename(member)}(" + str(os.path.getsize(member)) + "KB)")
                    sleep(0.05)
                except zipfile.error as e:
                    pass
        zip.close()
    os.remove("new.zip")
    directory = None
    for path, currentDirectory, files in os.walk(Path.cwd()):
        for directory1 in currentDirectory:
            if directory1.startswith("GrenManSK-ZnamE-"):
                print(directory1)
                directory = directory1
    if directory == None:
        if args.language == "SK":
            print("CHYBA STAHOVANIA\nStiahnete manuálne novšiu verziu z\n'https://github.com/GrenManSK/ZnamE'")
        if args.language == "EN":
            print("DOWNLOADING ERROR\nManually download newer version from\n'https://github.com/GrenManSK/ZnamE'")
        if args.language == "JP":
            print("ダウンロード エラー\n'https://github.com/GrenManSK/ZnamE' から新しいバージョンを手動でダウンロードしてください")
        sleep(2)
        quit()
    os.mkdir('old')
    shutil.move('data.xp2','old/data.xp2')
    shutil.move('help.txt','old/help.txt')
    shutil.move('LICENSE','old/LICENSE')
    shutil.move('README.md','old/README.md')
    shutil.move('version','old/version')
    sleep(0.5)
    shutil.move(directory + "/data.xp2", 'data.xp2')
    shutil.move(directory + "/help.txt", 'help.txt')
    shutil.move(directory + "/LICENSE", 'LICENSE')
    shutil.move(directory + "/README.md", 'README.md')
    shutil.move(directory + "/version", 'version')
    crupdate = open("update.py", "w")
    crupdate.write(updateapp)
    crupdate.close()
    if args.endf == None:
        subprocess.check_call('start python update.py ' + directory + ' -lang ' + args.language + ' -endf', shell=True)
    else:
        subprocess.check_call('start python update.py ' + directory + ' -lang ' + args.language , shell=True)
    sleep(0.1)
    quit()

verzia.close()

codeapp = str('import sys\nPLOCHA = [[\"a\", \"b\", \"c\", \"d\", \"e\"], [\"f\", \"g\", \"h\", \"i\", \"j\"], [\n    \"k\", \"l\", \"m\", \"n\", \"o\", ], [\"p\", \"q\", \"r\", \"s\", \"t\"], [\n    \"u\", \"v\", \"w\", \"x\", \"y\"], [\"A\", \"B\", \"C\", \"D\", \"E\"], [\n    \"F\", \"G\", \"H\", \"I\", \"J\"], [\"K\", \"L\", \"M\", \"N\", \"O\", ], [\n    \"P\", \"Q\", \"R\", \"S\", \"T\"], [\"U\", \"V\", \"W\", \"X\", \"y\"], [\n    \"z\", \" \", \",\", \".\", \":\"], [\"!\", \"?\", \"\'\", \'\"\', \"`\"], [\n    \"1\", \"2\", \"3\", \"4\", \"5\"], [\"6\", \"7\", \"8\", \"9\", \"0\"], [\n    \"\\n\", \"<\", \">\", \";\", \"/\"], [\"\\\\", \"{\", \"}\", \"(\", \")\"],[\n    \"[\",\"]\",\"|\",\"-\",\"_\"],[\"=\",\"+\",\"@\",\"#\",\"$\"],[\"%\",\"^\",\"&\",\"*\",\"~\"]]\ndef read_file(file):\n    obsah = \"\"\n    obsah_list = []\n    for i in file:\n        obsah = \"\"\n        obsah += i\n        for i in obsah:\n            i.lower()\n            obsah_list.append(i)\n    return obsah_list\ndef encode(obsah):\n    sifra = []\n    for i in obsah:\n        riadok = 0\n        stlpec = 0\n        while True:\n            if riadok == 19 and stlpec == 0:\n                break\n            if i == PLOCHA[riadok][stlpec]:\n                sifra.append(str(riadok) + \" \" + str(stlpec))\n                break\n            if stlpec == 4:\n                riadok += 1\n                stlpec = 0\n            else:\n                stlpec += 1\n    return sifra\ndef output_file(file, name):\n    y = []\n    x = open(name + \"crypted\", \"w\")\n    for i in file:\n        y.append(i)\n    x.write(str(y))\n    x.close\n    return\ndef main():\n    name = sys.argv[1]\n    open_file = open(name, \"r\")\n    open_file.close\n    output_file(encode(read_file(open_file)), name)\nmain()\nx=open(\'DONE\',\'x\')\nx.close()')
decodeapp = str('import os\nos.system(\'Title \' + \'code\')\nimport sys\nPLOCHA = [[\"a\", \"b\", \"c\", \"d\", \"e\"], [\"f\", \"g\", \"h\", \"i\", \"j\"], [\n    \"k\", \"l\", \"m\", \"n\", \"o\", ], [\"p\", \"q\", \"r\", \"s\", \"t\"], [\n    \"u\", \"v\", \"w\", \"x\", \"y\"], [\"A\", \"B\", \"C\", \"D\", \"E\"], [\n    \"F\", \"G\", \"H\", \"I\", \"J\"], [\"K\", \"L\", \"M\", \"N\", \"O\", ], [\n    \"P\", \"Q\", \"R\", \"S\", \"T\"], [\"U\", \"V\", \"W\", \"X\", \"y\"], [\n    \"z\", \" \", \",\", \".\", \":\"], [\"!\", \"?\", \"\'\", \'"\', \"`"], [\n    \"1\", \"2\", \"3\", \"4\", \"5\"], [\"6\", \"7\", \"8\", \"9\", \"0\"], [\n    \"\\n\", \"<\", \">\", \";\", \"/\"], [\"\\\\", \"{\", \"}\", \"(\", \")\"],[\n    \"[\",\"]\",\"|\",\"-\",\"_\"],[\"=\",\"+\",\"@\",\"#\",\"$\"],[\"%\",\"^\",\"&\",\"*\",\"~\"]]\ndef read_file(file):\n    obsah = \"\"\n    obsah_list = []\n    for i in file:\n        obsah += i\n        for i in obsah:\n            obsah_list.append(i)\n    return obsah_list\ndef decode(obsah):\n    done = \"\"\n    sifra = []\n    for i in obsah:\n        done += str(i)\n        if i == \"[\" or i == \"\'\" or i == \",\" or i == \"]\":\n            done = \"\"\n            continue\n        if i == \" \":\n            sifra.append(i)\n        else:\n            sifra.append(i)\n    return sifra\ndef real_decode(obsah):\n    cislo = 0\n    pokracovanie = False\n    done = \"\"\n    vysledok = []\n    for i in obsah:\n        done += str(i)\n        cislo = 0\n        for i in done:\n            cislo += 1\n        if i == \" \":\n            done = \"\"\n            continue\n        if pokracovanie and done.isnumeric() and cislo == 1:\n            stlpec = int(done)\n            vysledok.append(PLOCHA[riadok][stlpec])\n            pokracovanie = False\n            done = \"\"\n            continue\n        if not pokracovanie or cislo == 2:\n            pokracovanie = True\n            riadok = int(done)\n            continue\n    return vysledok\ndef to_text(obsah):\n    text = \"\"\n    for i in obsah:\n        if i == \".\":\n            text += i + \"\\n\"\n            continue\n        text += i\n    return text\ndef create_file(obsah, name):\n    x = open(sys.argv[1], \"w\")\n    x.write(obsah)\n    x.close\n    return\ndef main():\n    if sys.argv[2] == \'False\':\n        name = \'data\'\n    else:\n        name = sys.argv[2]\n    open_file = open(name, \"r\")\n    code = list(decode(read_file(open_file)))\n    create_file(to_text(real_decode(code)), name)\nmain()\nx=open(\'DONE\',\'x\')\nx.close()')
findapp = str('import sys\ndecodename=str(sys.argv[1])\nicofind=int(sys.argv[2])\ndn=open(decodename,\'r\')\ndnr=dn.read()\nbracket,brackethist=0,0\nico=[]\nicocurrent=\'\'\nicoend=False\nrnii=False\nrniiend=False\nsubject=\'\'\nik=False\nuserdef=False\nwh=False\npassword=\'\'\npassend=False\nfor i in dnr:\n    if rnii:\n        wh=True\n        if i==\'[\':\n            bracket+=1\n        elif i==\']\':\n            bracket-=1\n        if passend:\n            user.write(password+\'\\n\')\n            passend=False\n        if ik:\n            if i!="," and bracket==4 and brackethist==4:\n                user.write(i)\n            if bracket==3:\n                subject=\'\'\n                ik=False\n                rniiend=False\n                user.write(\"\\n\")\n        if rniiend:\n            user.write(subject)\n            ik=True\n            rniiend=False\n            brackethist=bracket\n            continue\n        if userdef:\n            userdef=False\n            user=open(str(ico[0]),\'w\')\n        if bracket==3 and brackethist==3 and i!=\"\'\":\n            if i ==\',\':\n                rniiend=True\n                continue\n            subject+=str(i)\n        elif bracket==5 and brackethist==5 and i!=\"\'\":\n            if i ==\',\':\n                passend=True\n                continue\n            password+=str(i)\n        brackethist=bracket\n        if bracket<2 and brackethist<2:\n            break\n    else:\n        if i==\'[\':\n            bracket+=1\n        elif i==\']\':\n            bracket-=1\n        if icoend:\n            if icocurrent!=\'\':\n                if int(icocurrent)==icofind:\n                    ico.append(icocurrent)\n                    rnii=True\n                    continue\n                icocurrent=\'\'\n                icoend=False\n        if bracket==2 and brackethist==2:\n            if i ==\',\':\n                icoend=True\n                userdef=True\n                continue\n            icocurrent+=i\n        brackethist=bracket\nif not wh:\n    user=open(sys.argv[2], \'x\')\nuser.close()\nx=open(\'DONE\',\'x\')\nx.close()')
passwordapp = str('import sys\ndecodename=str(sys.argv[1])\ndn=open(decodename,\'r\')\ndnr=dn.readlines()\ntry:\n    number=int(dnr[0])\n    number=str(dnr[0])\n    number=dnr[0][:6]\nexcept Exception:\n    number=None\nx=open(\'DONE\',\'w\')\nx.write(number)\nx.close()')
addapp= str('import sys\ndecodename=str(sys.argv[1])\nicofind=int(sys.argv[2])\nsubjectfind = sys.argv[3]\nmarkadd = sys.argv[4]\ndn=open(decodename,\'r\')\ndnr=dn.read()\nbracket,brackethist=0,0\nico=[]\nicocurrent=\'\'\nicoend=False\nrnii=False\nrniiend=False\nsubject=\'\'\nik=False\nuserdef=False\nwh=False\npassword=\'\'\npassend=False\nik2=False\nadd=False\nuser=open(\'data1\',\'w\', newline=\'\')\nfor i in dnr:\n    user.write(i)\n    if rnii:\n        wh=True\n        if i==\'[\':\n            bracket+=1\n        elif i==\']\':\n            bracket-=1\n        if add and subject==subjectfind and bracket==4 and brackethist==4:\n            subjectfind=None\n            user.write(str(markadd) + \',\')\n            add=False\n        if passend:\n            passend=False\n        if ik:\n            if ik2:\n                ik2=False\n                add=True\n            if bracket==3:\n                subject=\'\'\n                ik=False\n                rniiend=False\n        if rniiend:\n            ik=True\n            ik2=True\n            rniiend=False\n            brackethist=bracket\n            continue\n        if userdef:\n            userdef=False\n        if bracket==3 and brackethist==3 and i!=\"\'\":\n            if i ==\',\':\n                rniiend=True\n                continue\n            subject+=str(i)\n        elif bracket==5 and brackethist==5 and i!=\"\'\":\n            if i ==\',\':\n                passend=True\n                continue\n            password+=str(i)\n        brackethist=bracket\n    else:\n        if i==\'[\':\n            bracket+=1\n        elif i==\']\':\n            bracket-=1\n        if icoend:\n            if icocurrent!=\'\':\n                if int(icocurrent)==icofind:\n                    ico.append(icocurrent)\n                    rnii=True\n                    continue\n                icocurrent=\'\'\n                icoend=False\n        if bracket==2 and brackethist==2:\n            if i ==\',\':\n                icoend=True\n                userdef=True\n                continue\n            icocurrent+=i\n        brackethist=bracket\nif not wh:\n    user=open(sys.argv[2], \'x\')\nuser.close()\nx=open(\'DONE\',\'x\')\nx.close()')

def delcache(name, hist):
    global timer
    time_got = 300
    timer = time_got
    size = os.path.getsize(hist)
    sizehist = size
    while True:
        try:
            for i in os.listdir():
                if i == "END":
                    raise Exception
            if timer <= 0:
                os.remove(name)
                x = open("INACTIVE", 'x')
                x.close()
                os.system('cls')
                if args.language == "SK":
                    print("Stlač 'enter'")
                if args.language == "EN":
                    print("Press 'enter'")
                if args.language == "JP":
                    print("「入力」を押してください")
                break
            if size != sizehist:
                timer = time_got
                sizehist = size
            else:
                sizehist = size
                size = os.path.getsize(hist)
                sleep(1)
                timer -= 1
        except Exception:
            pass


global progress_bar_check
progress_bar_check = 0
global progress_bar_end
progress_bar_end = False

cachename = 'data.xp2'

def inactive():
    global password
    leave = False
    for i in os.listdir():
        if i == 'INACTIVE':
            leave = True
            try:
                os.remove('INACTIVE')
                os.remove(password[1])  # type: ignore
            except Exception:
                pass
            break
    if leave:
        sleep(0.05)
        return True
    else:
        return False
    
def progress_bar(name, number):
    global progress_bar_check
    progress_bar_check = 0
    progress_bar_check_old = 0
    end = False
    for i in tqdm(range(0,number), desc=name +' '):
        if end:
            break
        while True:
            if progress_bar_check >= 100:
                end = True
                break
            if progress_bar_check == progress_bar_check_old:
                continue
            elif progress_bar_check != progress_bar_check_old:
                progress_bar_check_old = progress_bar_check
                break

def main():
    historyname = str(datetime.now().strftime("%H-%M-%S"))
    history = open(historyname, 'w')
    logged = False
    exit = False
    global password
    if args.language == "SK":
        print('Jazyk = SK\n\nZačínam rozbaľovať\n')
    if args.language == "EN":
        print('Language = EN\n\nStarting to extract\n')
    if args.language == "JP":
        print("言語 = 日本語\n\n抽出開始\n")
    sleep(0.25)
    try:
        with zipfile.ZipFile(cachename, mode='r') as zip:
            if args.language == "SK":
                for member in tqdm(iterable=zip.namelist(), total=len(zip.namelist()), desc='Rozbaľujem '):
                    try:
                        zip.extract(member)
                        tqdm.write(f"{os.path.basename(member)}(" + str(os.path.getsize(member)) + "B)")
                        sleep(0.01)
                    except zipfile.error as e:
                        pass
            elif args.language == "EN":
                for member in tqdm(iterable=zip.namelist(), total=len(zip.namelist()), desc='Extracting '):
                    try:
                        zip.extract(member)
                        tqdm.write(f"{os.path.basename(member)}(" + str(os.path.getsize(member)) + "B)")
                        sleep(0.01)
                    except zipfile.error as e:
                        pass
            elif args.language == "JP":
                for member in tqdm(iterable=zip.namelist(), total=len(zip.namelist()), desc='抽出中 '):
                    try:
                        zip.extract(member)
                        tqdm.write(f"{os.path.basename(member)}(" + str(os.path.getsize(member)) + "B)")
                        sleep(0.01)
                    except zipfile.error as e:
                        pass
            zip.close()
        if args.language == "SK":
            print('Hotovo\n')
            sleep(0.25)
            print("Rozbaľujem druhu časť...\n")
        if args.language == "EN":
            print('Done\n')
            sleep(0.25)
            print("Unpacking second part...\n")
        if args.language == "JP":
            print("2 番目の部分を解凍しています...\n")
        if args.language == "SK":
            subprocess.call([sys.executable, 'xp3.py', 'data.xp3', 'data1', '-e', 'neko_vol0_steam'])
        if args.language == "EN":
            subprocess.call([sys.executable, 'xp3.py', 'data.xp3', 'data1', '-e', 'neko_vol0_steam', '-lang', 'EN'])
        if args.language == "JP":
            subprocess.call([sys.executable, 'xp3.py', 'data.xp3', 'data1', '-e', 'neko_vol0_steam', '-lang', 'JP'])
        shutil.move('data1/data', 'data')
        shutil.rmtree('data1')
        os.remove(cachename)
        os.remove('data.xp3')
        if args.language == "SK":
            print('\nHotovo\n')
        if args.language == "EN":
            print('\nDone\n')
        if args.language == "JP":
            print('\n完了\n')
        sleep(0.5)
        check = open('data', 'r')
        check_new = open('data_dummy', 'w')
        for i in check.read():
                if i == "G":
                    check_new.write("[")
                else:
                    check_new.write(i)
        check.close()
        check_new.close()
        os.mkdir("temp")
        shutil.move("data_dummy", 'temp/')
        os.remove('data')
        shutil.move("temp/data_dummy", 'data')
        shutil.rmtree('temp')
        os.rename('data_dummy', 'data')
    except FileNotFoundError:
        pass
    verzia = open('version', 'r')
    if args.language == "SK":
        print('Používate ZnámE ' + verzia.read() + "\n")
    if args.language == "EN":
        print('You\'re using ZnámE ' + verzia.read() + "\n")
    if args.language == "JP":
        print('ZnámE を使用しています ' + verzia.read() + "\n")
    verzia.close()
    try:
        if args.inactive == None:
            sleep(0.25)
            if args.language == "SK":
                print('Bol si neaktívny, bol si odhlásený a program sa reštartoval!!!\n')
            if args.language == "EN":
                print('You were inactive, you were logged out and the program restarted!!!\n')
            if args.language == "JP":
                print('非アクティブでした。ログアウトし、プログラムを再起動しました!!!\n')
        if args.update == None:
            sleep(0.25)
            if args.language == "SK":
                print('Program bol aktualizovaný!!!\n')
            if args.language == "EN":
                print('Program was updated!!!\n')
            if args.language == "JP":
                print('プログラムが更新されました!!!\n')
    except Exception:
        pass
    tologin = False
    restart = False
    topassword = False
    topasswordhelp = False
    loggedhelp = False
    firstlogin = True
    vstup = None
    help = ['help','pomoc','-h','-help','?','-?']
    advhelp = ['advanced help','ah','-ah','-advanced help']
    while True:
        if not exit:
            global loginvstupuser
            if logged:
                if firstlogin:
                    firstlogin = False
                    shutil.copy2('data', 'data_backup')
                if loggedhelp:
                    if args.language == "SK":
                        print("'zz' pre zobrazenie známok\n'pz' pre pridanie známok")
                    if args.language == "EN":
                        print("'zz' to display marks\n'pz' to add marks")
                    if args.language == "JP":
                        print('「zz」でマークを表示\n「pz」でマークを追加')
                    loggedhelp = False
                vstup = input('> ')
                history.write(vstup + '\n')
                vstup.lower()
                history.close()
                history = open(historyname, 'a')
                help = ['help','pomoc','-h','-help','?','-?']
                for i in range(len(help)):
                    if vstup == help[i]:
                        loggedhelp = True
                if loggedhelp:
                    continue
                if vstup == "zz":
                    passwordfile = open(password[1], 'r')  # type: ignore
                    countersubject = 0
                    counter = 6
                    counterfirst = True
                    for i in passwordfile.read():
                        if counter != 0:
                            counter -= 1
                            continue
                        try:
                            if i == '\n':
                                print('\n', end="")
                                continue
                            int(i)
                            if counterfirst:
                                print(i, end="")
                            else:
                                print(','+i, end="")
                        except Exception:
                            if countersubject > 2:
                                countersubject = 0
                            counterfirst = True
                            countersubject += 1
                            print(i, end="")
                            if countersubject > 2:
                                print(" | ", end="")
                    passwordfile.close()
                if vstup == "pz":
                    if args.language == "SK":
                        subject = input('Predmet > ')
                        history.write(subject + '\n')
                        vstup.lower()
                        history.close()
                        history = open(historyname, 'a')
                        if subject == 'quit':
                            exit = True
                            continue
                        if subject == 'back':
                            continue
                        mark = input('Známka > ')
                        history.write(mark + '\n')
                        vstup.lower()
                        history.close()
                        history = open(historyname, 'a')
                    elif args.language == "EN":
                        subject = input('Subject > ')
                        history.write(subject + '\n')
                        vstup.lower()
                        history.close()
                        history = open(historyname, 'a')
                        if subject == 'quit':
                            exit = True
                            continue
                        if subject == 'back':
                            continue
                        mark = input('Mark > ')
                        history.write(mark + '\n')
                        vstup.lower()
                        history.close()
                        history = open(historyname, 'a')
                    elif args.language == "JP":
                        subject = input('主題 > ')
                        history.write(subject + '\n')
                        vstup.lower()
                        history.close()
                        history = open(historyname, 'a')
                        if subject == 'quit':
                            exit = True
                            continue
                        if subject == 'back':
                            continue
                        mark = input('マーク > ')
                        history.write(mark + '\n')
                        vstup.lower()
                        history.close()
                        history = open(historyname, 'a')
                    else:
                        subject = input('Subject > ')
                        history.write(subject + '\n')
                        vstup.lower()
                        history.close()
                        history = open(historyname, 'a')
                        if subject == 'quit':
                            exit = True
                            continue
                        if subject == 'back':
                            continue
                        mark = input('Mark > ')
                        history.write(mark + '\n')
                        vstup.lower()
                        history.close()
                        history = open(historyname, 'a')
                    if subject == 'quit' or mark == 'quit':
                        exit = True
                        continue
                    if subject == 'back' or mark == 'back':
                        continue
                    if args.language == "SK":
                        Thread(target=progress_bar, args=('Preverujem', 3,), daemon=True).start()
                    if args.language == "EN":
                        Thread(target=progress_bar, args=('Checking', 3,), daemon=True).start()
                    if args.language == "JP":
                        Thread(target=progress_bar, args=('チェック中', 3,), daemon=True).start()
                    code(add(decode(True, False), loginvstupuser, subject, mark), 'justcode')  # type: ignore
                    os.mkdir("temp")
                    shutil.move("data", 'temp/')
                    os.rename('data1crypted', 'data')
                    shutil.rmtree('temp')
                    os.remove('data1')
            if topassword:
                if args.language == "SK":
                    vstup = input('Heslo > ')
                elif args.language == "EN":
                    vstup = input('Password > ')
                elif args.language == "JP":
                    vstup = input('パスワード > ')
                else:
                    vstup = input('Password > ')
                history.write(vstup + '\n')
                vstup.lower()
                history.close()
                history = open(historyname, 'a')
                help = ['help','pomoc','-h','-help','?','-?']
                for i in range(len(help)):
                    if vstup == help[i]:
                        topasswordhelp = True
                if topasswordhelp:
                    if args.language == "SK":
                        print("6 číselne heslo\n 'back' pre menu\n 'quit' pre koniec")
                    if args.language == "EN":
                        print("6 numeric password\n 'back' for menu\n 'quit' for end")
                    if args.language == "JP":
                        print('6桁のパスワード\n メニューの「戻る」\n 終了の「終了」')
                    topasswordhelp = False
                    continue
                if vstup == "back":
                    if args.language == "SK":
                        print('Idem späť.')
                    if args.language == "EN":
                        print('Going back.')
                    if args.language == "JP":
                        print('戻る。')
                    topassword = False
                    os.remove(loginvstupuser + 'crypted')
                    continue
                elif vstup == "quit" or vstup == "koniec":
                    if args.language == "SK":
                        print("Idem späť a ukončujem program.")
                    if args.language == "EN":
                        print("Going back and ending program.")
                    if args.language == "JP":
                        print('戻ってプログラムを終了します。')
                    sleep(0.5)
                    os.remove(loginvstupuser + 'crypted')
                    exit = True
                    continue
                if args.language == "SK":
                    Thread(target=progress_bar, args=('Preverujem', 2,), daemon=True).start()
                if args.language == "EN":
                    Thread(target=progress_bar, args=('Checking', 2,), daemon=True).start()
                if args.language == "JP":
                    Thread(target=progress_bar, args=('チェック中', 2,), daemon=True).start()
                password = password(decode(loginvstupuser + 'crypted', True))  # type: ignore
                sleep(0.1)
                if vstup == password[0]:  # type: ignore
                    if args.language == "SK":
                        print('Si prihlaseny\n')
                    if args.language == "EN":
                        print('You\'re logged\n')
                    if args.language == "JP":
                        print('あなたはログインしています\n')
                    os.rename(loginvstupuser + 'crypted', loginvstupuser)
                    passwordfile = open(loginvstupuser, 'r')
                    passwordfile1 = open(loginvstupuser + "1", 'w')
                    counter = 0
                    for i in passwordfile.read():
                        passwordfile1.write(i)
                    passwordfile.close()
                    passwordfile1.close()
                    os.remove(loginvstupuser)
                    os.rename(loginvstupuser + '1', loginvstupuser)
                    topassword = False
                    logged = True
                    continue
                elif vstup != password[0]:  # type: ignore
                    topassword = False
                    os.remove(loginvstupuser + 'crypted')
                    os.remove(password[1])  # type: ignore
                    global progress_bar_check
                    progress_bar_check = 100
                    sleep(0.1)
                    if args.language == "SK":
                        print("ZLÉ HESLO")
                    if args.language == "EN":
                        print("WRONG PASSWORD")
                    if args.language == "JP":
                        print('間違ったパスワード')
            if not tologin and not logged:
                vstup = input('> ')
                history.write(vstup + '\n')
                vstup.lower()
                history.close()
                history = open(historyname, 'a')
            inactivelogout = inactive()
            if vstup == 'clear' or vstup == 'cls':
                os.system('cls')
            if inactivelogout:
                restart = True
                exit = True
            if logged and vstup == "logout" and not restart:
                logged = False
                os.remove(loginvstupuser)
                os.remove(password[1])  # type: ignore
                if args.language == "SK":
                    print("Si odhlásený")
                if args.language == "EN":
                    print("You\'re logged out")
                if args.language == "JP":
                    print('ログアウトしました')
                continue
            elif logged and inactivelogout and restart:
                logged = False
                if args.language == "SK":
                    print("Si odhlásený")
                if args.language == "EN":
                    print("You\'re logged out")
                if args.language == "JP":
                    print('ログアウトしました')
                continue
            elif not logged and vstup == "logout" or inactivelogout:
                logged = False
                if args.language == "SK":
                    print('Nie si prihlásený!!!')
                if args.language == "EN":
                    print("You\'re not logged in!!!")
                if args.language == "JP":
                    print('ログインしていません!!!')
                continue
            elif vstup == 'quit' or vstup == 'koniec' or vstup == 'end':
                exit = True
                continue
            history = open(historyname, 'a')
            if vstup != "" and not restart:
                for i in range(len(advhelp)):
                    if vstup == advhelp[i]:
                        advhelpfile = open('Help.txt', 'r', encoding='UTF-8')
                        print(advhelpfile.read())
                        advhelpfile.close()
                for i in range(len(help)):
                    if vstup == help[i]:
                        if args.language == "SK":
                            print("'login' pre prihlásenie\n'logout' pre odhlásenie\n'quit' alebo 'koniec' pre koniec\n\nKeď chceš zmeniť jazyk programu v terminalu do commandu pridaj '-lang EN' or '-lang SK'\n\nPre podrobnejšiu pomoc napíš '-ah' alebo '-advanced help' alebo 'ah' alebo 'advanced help'")
                        if args.language == "EN":
                            print("'login' for login\n'logout' for logout\n'quit' or 'end' for end\n\nWhen you want to change the language of the program in the terminal, add '-lang EN' or '-lang SK' to the command\n\nFor more detailed help, type '-ah' or '-advanced help' or 'ah' or 'advanced help'")
                        if args.language == "JP":
                            print("ログインの場合は「login」\nログアウトの場合は「logout」\n終了の場合は「quit」または「end」\n\nターミナルでプログラムの言語を変更する場合は、「-lang EN」または「-lang」を追加します コマンドに SK'\n\n詳細なヘルプを表示するには、'-ah' または '-advanced help' または 'ah' または 'advanced help' と入力してください'")
                        continue
                if vstup == 'login' and not logged or tologin and not logged:
                    loginvstupuser = ''
                    tologin = False
                    def add(name, ico, subject, mark):
                        global progress_bar_check
                        decodename = str(datetime.now().strftime("%H-%M-%S"))
                        crdecode = open(decodename + ".py", "w")
                        crdecode.write(addapp)
                        crdecode.close()
                        subprocess.check_output('start ' + decodename + '.py ' + str(name) + ' ' + str(ico) + ' ' + str(subject) + ' ' + str(mark), shell=True)
                        if args.language == "SK":
                            tqdm.write('Pridávam ...', end='\r')
                        if args.language == "EN":
                            tqdm.write('Adding ...', end='\r')
                        if args.language == "JP":
                            tqdm.write('追加する ...', end='\r')
                        while True:
                            leave = False
                            for i in os.listdir():
                                if i == 'DONE':
                                    leave = True
                                    break
                            if leave:
                                sleep(0.05)
                                break
                        if args.language == "SK":
                            tqdm.write('Pridávam Hotovo')
                        if args.language == "EN":
                            tqdm.write('Adding Complete')
                        if args.language == "JP":
                            tqdm.write('追加完了')
                        os.remove(decodename + '.py')
                        os.remove(name)
                        os.remove('DONE')
                        progress_bar_check += 1
                        name = ('data1', None)
                        return name
                    def decode(name, password):
                        global progress_bar_check
                        decodename = str(datetime.now().strftime("%H-%M-%S"))
                        decodename2 = 'False'
                        if password:
                            decodename2 = name
                        if name:
                            decodename1 = decodename
                        elif isinstance(name, str):
                            decodename1 = name
                        else:
                            decodename1 = "None"
                        crdecode = open(decodename + ".py", "w")
                        crdecode.write(decodeapp)
                        crdecode.close()
                        subprocess.check_output('start ' + decodename + '.py ' + str(decodename1) + ' ' + str(decodename2), shell=True)
                        if args.language == "SK":
                            tqdm.write('Odkoduvávam ...', end='\r')
                        if args.language == "EN":
                            tqdm.write('Encrypting ...', end='\r')
                        if args.language == "JP":
                            tqdm.write('暗号化 ...', end='\r')
                        while True:
                            leave = False
                            for i in os.listdir():
                                if i == 'DONE':
                                    leave = True
                                    break
                            if leave:
                                sleep(0.05)
                                break
                        if args.language == "SK":
                            tqdm.write('Odkoduvávam Hotovo')
                        if args.language == "EN":
                            tqdm.write('Encrypting Complete')
                        if args.language == "JP":
                            tqdm.write('暗号化完了')
                        os.remove(decodename + '.py')
                        os.remove('DONE')
                        progress_bar_check += 1
                        return decodename1
                    def password(name):
                        global progress_bar_check
                        passwordname = str(datetime.now().strftime("%H-%M-%S"))
                        crfind = open(passwordname + ".py", "w")
                        crfind.write(passwordapp)
                        crfind.close()
                        if args.language == "SK":
                            tqdm.write('Kontrolujem ...', end='\r')
                        if args.language == "EN":
                            tqdm.write('Controling ...', end='\r')
                        if args.language == "JP":
                            tqdm.write('制御する ...', end='\r')
                        subprocess.check_output('start ' + passwordname + '.py ' + str(name), shell=True)
                        while True:
                            leave = False
                            for i in os.listdir():
                                if i == 'DONE':
                                    leave = True
                                    break
                            if leave:
                                sleep(0.05)
                                break
                        os.remove(passwordname + '.py')
                        password = ''
                        for i in open('DONE', 'r').read():
                            password+=str(i)
                        if args.language == "SK":
                            tqdm.write('Kontrolujem Hotovo')
                        if args.language == "EN":
                            tqdm.write('Controling Complete')
                        if args.language == "JP":
                            tqdm.write('制御完了')
                        os.remove('DONE')
                        progress_bar_check += 1
                        return (password, name)
                    def find(name):
                        global progress_bar_check
                        findname = str(datetime.now().strftime("%H-%M-%S"))
                        crfind = open(findname + ".py", "w")
                        crfind.write(findapp)
                        crfind.close()
                        if args.language == "SK":
                            tqdm.write('Hľadám ...', end='\r')
                        if args.language == "EN":
                            tqdm.write('Finding ...', end='\r')
                        if args.language == "JP":
                            tqdm.write('発見 ...', end='\r')
                        subprocess.check_output('start ' + findname + '.py ' + str(name) + ' ' + str(loginvstupuser), shell=True)
                        while True:
                            leave = False
                            for i in os.listdir():
                                if i == 'DONE':
                                    leave = True
                                    break
                            if leave:
                                sleep(0.05)
                                break
                        os.remove(findname + '.py')
                        os.remove(name)
                        os.remove('DONE')
                        test = open(loginvstupuser, 'r')
                        end = False
                        pocitadlo = 0
                        for i in test.read():
                            pocitadlo += 1
                        if 0 <= pocitadlo <= 5:
                            test.close()
                            if args.language == "SK":
                                tqdm.write('Hľadám CHYBA')
                            if args.language == "EN":
                                tqdm.write('Finding ERROR')
                            if args.language == "JP":
                                tqdm.write('発見 エラー')
                            end = True
                        if end:
                            return (loginvstupuser, end)
                        test.close()
                        if args.language == "SK":
                            tqdm.write('Hľadám Hotovo')
                        if args.language == "EN":
                            tqdm.write('Finding Complete')
                        if args.language == "JP":
                            tqdm.write('発見完了')
                        progress_bar_check += 1
                        return (loginvstupuser, end)
                    def code(name, new):
                        global progress_bar_check
                        codename = str(datetime.now().strftime("%H-%M-%S"))
                        crcode = open(codename + ".py", "w")
                        crcode.write(codeapp)
                        crcode.close()
                        if args.language == "SK":
                            tqdm.write('Zakoduvávam ...', end='\r')
                        if args.language == "EN":
                            tqdm.write('Coding ...', end='\r')
                        if args.language == "JP":
                            tqdm.write('コーディング ...', end='\r')
                        subprocess.check_output('start ' + codename + '.py ' + str(name[0]), shell=True)
                        while True:
                            leave = False
                            for i in os.listdir():
                                if i == 'DONE':
                                    leave = True
                                    break
                            if leave:
                                sleep(0.05)
                                break
                        if args.language == "SK":
                            tqdm.write('Zakoduvávam Complete')
                        if args.language == "EN":
                            tqdm.write('Coding Complete')
                        if args.language == "JP":
                            tqdm.write('コーディング 完了')
                        os.remove(codename + '.py')
                        if new == 'justcode':
                            pass
                        elif new:
                            os.remove(loginvstupuser + 'crypted')
                            shutil.move(loginvstupuser + 'cryptedcrypted', loginvstupuser + 'crypted')
                        else:
                            os.remove(loginvstupuser)
                        progress_bar_check += 1
                        os.remove('DONE')
                        return name[1], new
                    if args.language == "SK":
                        loginvstupuser = input("Prihlasovacie číslo (PID) > ")
                    if args.language == "EN":
                        loginvstupuser = input("Login Number (PID) > ")
                    if args.language == "JP":
                        loginvstupuser = input("ログイン番号 (PID) > ")
                    history.write(loginvstupuser + "\n")
                    history.close()
                    history = open(historyname, 'a')
                    tologinhelp = False
                    if loginvstupuser == "back":
                        if args.language == "SK":
                            print('Idem späť.')
                        if args.language == "EN":
                            print('Going back.')
                        if args.language == "JP":
                            print('戻る。')
                        continue
                    elif loginvstupuser == "quit" or loginvstupuser == "koniec":
                        if args.language == "SK":
                            print("Idem späť a ukončujem program.")
                        if args.language == "EN":
                            print("Going back and exiting the program.")
                        if args.language == "JP":
                            print('戻ってプログラムを終了します。')
                        sleep(0.5)
                        exit = True
                        continue
                    help = ['help','pomoc','-h','-help','?','-?']
                    for i in range(len(help)):
                        if loginvstupuser == help[i]:
                            tologinhelp = True
                    if tologinhelp:
                        if args.language == "SK":
                            print("'back' pre menu\n'quit' alebo 'koniec' pre koniec")
                        if args.language == "EN":
                            print("'back' for menu\n'quit' or 'end' for end")
                        if args.language == "JP":
                            print("メニューの「戻る」\n 'quit' または 'end' で終了")
                        tologin = True
                        continue
                    elif not loginvstupuser.isnumeric():
                        if args.language == "SK":
                            print('PID neobsahuje písmená alebo znaky!!!')
                        if args.language == "EN":
                            print('The PID does not contain letters or characters!!!')
                        if args.language == "JP":
                            print('PID に文字が含まれていません!!!')
                        tologin = True
                        continue
                    history.write(loginvstupuser + '\n')
                    if len(str(loginvstupuser)) == 6:
                        exit = False
                        if args.language == "SK":
                            Thread(target=progress_bar, args=('Preverujem', 3,), daemon=True).start()
                        if args.language == "EN":
                            Thread(target=progress_bar, args=('Checking', 3,), daemon=True).start()
                        if args.language == "JP":
                            Thread(target=progress_bar, args=('チェック中', 3,), daemon=True).start()
                        icofind = code(find(decode(True, False)), False)
                        if icofind[0]:
                            logged = False
                            os.remove(loginvstupuser + 'crypted')
                            progress_bar_check = 100
                            sleep(0.1)
                            if args.language == "SK":
                                print("ZLÉ PID!!!")
                            if args.language == "EN":
                                print("WRONG PID!!!")
                            if args.language == "JP":
                                print('間違った PID !!!')
                            tologin = True
                            continue
                        Thread(target=delcache, args=(loginvstupuser,historyname,), daemon=True).start()
                        topassword = True
                    else:
                        if args.language == "SK":
                            print('PID má byt 6 čísel dlhé!!!')
                        if args.language == "EN":
                            print('The PID should be 6 numbers long!!!')
                        if args.language == "JP":
                            print('PID は 6 桁の長さでなければなりません!!!')
                        tologin = True
                elif logged and vstup == 'login':
                    if args.language == "SK":
                        print('Už si prihlasení!!!')
                    if args.language == "EN":
                        print('You are already logged in!!!')
                    if args.language == "JP":
                        print('すでにログインしています！！！')
        elif vstup == 'quit' or vstup == 'koniec' or vstup == 'end' or exit:
            try:
                open('END', 'x')
            except Exception:
                pass
            if logged:
                try:
                    sleep(0.25)
                    os.remove(loginvstupuser)
                    os.remove(password[1])  # type: ignore
                except Exception:
                    pass
                if args.language == "SK":
                    print("\nSi odhlásený\n")
                if args.language == "EN":
                    print('\nYou are logged out\n')
                if args.language == "JP":
                    print('\nログアウトしました\n')
                sleep(0.5)
            history.close()
            if args.language == "SK":
                print("ODSTRAŇOVANIE NEPOTREBNÝCH SÚBOROV\n")
            if args.language == "EN":
                print("DELETING UNNECESSARY FILES\n")
            if args.language == "JP":
                print('不要なファイルを削除しています\n')
            try:
                os.remove(historyname)
            except Exception:
                pass
            try:
                os.remove('data_backup')
            except Exception:
                pass
            print('.', end='\r')
            sleep(0.2)
            os.mkdir('datafolder')
            sleep(0.2)
            shutil.move('data', 'datafolder/')
            sleep(0.2)
            if args.language == "SK":
                print("ZABAĽUJEM DATA\n")
                sleep(0.2)
                subprocess.call([sys.executable, 'xp3.py', 'datafolder', 'data.xp3', '-mode', 'repack', '-e', 'neko_vol0_steam'])
            if args.language == "EN":
                print("PACKING DATA\n")
                sleep(0.2)
                subprocess.call([sys.executable, 'xp3.py', 'datafolder', 'data.xp3', '-mode', 'repack', '-e', 'neko_vol0_steam', '-lang', 'EN'])
            if args.language == "JP":
                print("梱包データ\n")
                sleep(0.2)
                subprocess.call([sys.executable, 'xp3.py', 'datafolder', 'data.xp3', '-mode', 'repack', '-e', 'neko_vol0_steam', '-lang', 'JP'])
            shutil.rmtree('datafolder')
            if args.language == "SK":
                print("HOTOVO\n")
                sleep(0.5)
                print("ZABAĽUJEM DRUHÚ ČASŤ DATA\n")
            if args.language == "EN":
                print("COMPLETE\n")
                sleep(0.5)
                print("PACKING SECOND PART OF DATA\n")
            if args.language == "JP":
                print("完了\n")
                sleep(0.5)
                print("データの 2 番目の部分のパッキング\n")
            zipfiles = ['tests.py', 'xp3.py', 'xp3reader.py', 'xp3writer.py', 'data.xp3']
            zipfileswopath = ['tests.py', 'xp3.py', 'xp3reader.py', 'xp3writer.py', 'data.xp3']
            for path, directories, files in os.walk('structs'):
                for file in files:
                    file_name = os.path.join(path, file)
                    zipfiles.append(file_name)
                    zipfileswopath.append(file)
            with zipfile.ZipFile(cachename, mode='w', compresslevel=5) as zip:
                if args.language == "SK":
                    bar = tqdm(range(0, len(zipfiles)), desc="Zabaľujem ")
                    zip_kb_old = 0
                    for i in bar:
                        zip.write(zipfiles[i])
                        size = sum([zinfo.file_size for zinfo in zip.filelist])
                        sleep(0.025)
                        tqdm.write(zipfileswopath[i] + "(" + str(os.path.getsize(zipfiles[i])) + " KB) -> " + str(round(size - zip_kb_old,2)) + " KB")
                        zip_kb_old = size
                        os.remove(zipfiles[i])
                        if i == len(zipfiles)-1:
                            tqdm.write("\n")
                    size = sum([zinfo.file_size for zinfo in zip.filelist])
                    tqdm.write("\nZabalené data majú > " + str(size)+ " KB")
                if args.language == "EN":
                    bar = tqdm(range(0, len(zipfiles)), desc="Packing ")
                    zip_kb_old = 0
                    for i in bar:
                        zip.write(zipfiles[i])
                        size = sum([zinfo.file_size for zinfo in zip.filelist])
                        sleep(0.02)
                        tqdm.write(zipfileswopath[i] + "(" + str(os.path.getsize(zipfiles[i])) + " KB) -> " + str(round(size - zip_kb_old,2)) + " KB")
                        zip_kb_old = size
                        os.remove(zipfiles[i])
                        if i == len(zipfiles)-1:
                            tqdm.write("\n")
                    size = sum([zinfo.file_size for zinfo in zip.filelist])
                    tqdm.write("\nPacked data have > " + str(size)+ " KB")
                if args.language == "JP":
                    bar = tqdm(range(0, len(zipfiles)), desc="梱包 ")
                    zip_kb_old = 0
                    for i in bar:
                        zip.write(zipfiles[i])
                        size = sum([zinfo.file_size for zinfo in zip.filelist])
                        sleep(0.02)
                        tqdm.write(zipfileswopath[i] + "(" + str(os.path.getsize(zipfiles[i])) + " KB) -> " + str(round(size - zip_kb_old,2)) + " KB")
                        zip_kb_old = size
                        os.remove(zipfiles[i])
                        if i == len(zipfiles)-1:
                            tqdm.write("\n")
                    size = sum([zinfo.file_size for zinfo in zip.filelist])
                    tqdm.write("\nパックされたデータは > " + str(size)+ " KB")
                zip.close()
            shutil.rmtree('structs')
            sleep(0.2)
            if args.language == "SK":
                print("\nHOTOVO\n")
            if args.language == "EN":
                print("\nCOMPLETE\n")
            if args.language == "JP":
                print('\n未完了\n')
            sleep(0.5)
            if restart:
                if args.language == "SK":
                    print('Program sa automaticky reštartuje.')
                if args.language == "EN":
                    print('The program will restart automatically.')
                if args.language == "JP":
                    print('プログラムが自動的に再起動します。')
            elif not restart:
                if args.endf == None:
                    pass
                else:
                    if args.language == "SK":
                        print('Program sa automaticky vypne.')
                    if args.language == "EN":
                        print('The program will automatically shut down.')   
                    if args.language == "JP":
                        print('プログラムは自動的にシャットダウンします。')
            sleep(0.5)
            os.remove('END')
            if args.endf != None:
                sleep(2.5)
            if restart:
                subprocess.check_call('start python edupage.py --inactive -lang ' + args.language, shell=True)
                quit()
            elif not restart:
                if args.endf == None:
                    if args.language == "SK":
                        input("'ENTER' NA KONIEC")
                    if args.language == "EN":
                        input("'ENTER' TO END")  
                    if args.language == "JP":
                        input("「ENTER」で終了")
                    quit()
                else:
                    quit()

if '__main__' == __name__:
    main()
