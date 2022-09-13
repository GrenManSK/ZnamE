import argparse, pkg_resources, sys, os, subprocess
global parser
parser = argparse.ArgumentParser()
UNSPECIFIED = object()
parser.add_argument('-lang', '--language', choices=['SK','EN'], help='Language selsection', nargs='?', default='SK')
parser.add_argument('-v', '--version', help='Show version of this program', default=UNSPECIFIED, nargs='?')
args = parser.parse_args()
if args.version == None:
    verzia = open('version', 'r')
    print(verzia.read())
    verzia.close()
    quit()
potrebne = {'psutil', 'numpy'}
nainstalovane = {pkg.key for pkg in pkg_resources.working_set}
nenajdene = potrebne - nainstalovane
if nenajdene:
    from time import sleep
    if args.language == "SK":
        print("Sťahujú sa aktualizácie")
    if args.language == "EN":
        print("Downloading updates")
    sleep(0.5)
    subprocess.check_call([sys.executable, '-m', 'pip', 'install', *nenajdene])
    if args.language == "SK":
        print("Program sa reštartuje!!!")
    if args.language == "EN":
        print("The program is restarting!!!")
    sleep(1)
    subprocess.check_call('start python edupage.py', shell=True)
    quit()
os.system('cls')
os.system('Title ' + 'ZnámE')
from time import sleep
from threading import Thread
from datetime import datetime
import shutil, zipfile

codeapp = str('import sys\nPLOCHA = [[\"a\", \"b\", \"c\", \"d\", \"e\"], [\"f\", \"g\", \"h\", \"i\", \"j\"], [\n    \"k\", \"l\", \"m\", \"n\", \"o\", ], [\"p\", \"q\", \"r\", \"s\", \"t\"], [\n    \"u\", \"v\", \"w\", \"x\", \"y\"], [\"A\", \"B\", \"C\", \"D\", \"E\"], [\n    \"F\", \"G\", \"H\", \"I\", \"J\"], [\"K\", \"L\", \"M\", \"N\", \"O\", ], [\n    \"P\", \"Q\", \"R\", \"S\", \"T\"], [\"U\", \"V\", \"W\", \"X\", \"y\"], [\n    \"z\", \" \", \",\", \".\", \":\"], [\"!\", \"?\", \"\'\", \'\"\', \"`\"], [\n    \"1\", \"2\", \"3\", \"4\", \"5\"], [\"6\", \"7\", \"8\", \"9\", \"0\"], [\n    \"\\n\", \"<\", \">\", \";\", \"/\"], [\"\\\\", \"{\", \"}\", \"(\", \")\"],[\n    \"[\",\"]\",\"|\",\"-\",\"_\"],[\"=\",\"+\",\"@\",\"#\",\"$\"],[\"%\",\"^\",\"&\",\"*\",\"~\"]]\ndef read_file(file):\n    obsah = \"\"\n    obsah_list = []\n    for i in file:\n        obsah = \"\"\n        obsah += i\n        for i in obsah:\n            i.lower()\n            obsah_list.append(i)\n    return obsah_list\ndef encode(obsah):\n    sifra = []\n    for i in obsah:\n        riadok = 0\n        stlpec = 0\n        while True:\n            if riadok == 19 and stlpec == 0:\n                break\n            if i == PLOCHA[riadok][stlpec]:\n                sifra.append(str(riadok) + \" \" + str(stlpec))\n                break\n            if stlpec == 4:\n                riadok += 1\n                stlpec = 0\n            else:\n                stlpec += 1\n    return sifra\ndef output_file(file, name):\n    y = []\n    x = open(name + \"crypted\", \"w\")\n    for i in file:\n        y.append(i)\n    x.write(str(y))\n    x.close\n    return\ndef main():\n    name = sys.argv[1]\n    open_file = open(name, \"r\")\n    open_file.close\n    output_file(encode(read_file(open_file)), name)\nmain()\nx=open(\'DONE\',\'x\')\nx.close()')
decodeapp = str('import os\nos.system(\'Title \' + \'code\')\nimport sys\nPLOCHA = [[\"a\", \"b\", \"c\", \"d\", \"e\"], [\"f\", \"g\", \"h\", \"i\", \"j\"], [\n    \"k\", \"l\", \"m\", \"n\", \"o\", ], [\"p\", \"q\", \"r\", \"s\", \"t\"], [\n    \"u\", \"v\", \"w\", \"x\", \"y\"], [\"A\", \"B\", \"C\", \"D\", \"E\"], [\n    \"F\", \"G\", \"H\", \"I\", \"J\"], [\"K\", \"L\", \"M\", \"N\", \"O\", ], [\n    \"P\", \"Q\", \"R\", \"S\", \"T\"], [\"U\", \"V\", \"W\", \"X\", \"y\"], [\n    \"z\", \" \", \",\", \".\", \":\"], [\"!\", \"?\", \"\'\", \'"\', \"`"], [\n    \"1\", \"2\", \"3\", \"4\", \"5\"], [\"6\", \"7\", \"8\", \"9\", \"0\"], [\n    \"\\n\", \"<\", \">\", \";\", \"/\"], [\"\\\\", \"{\", \"}\", \"(\", \")\"],[\n    \"[\",\"]\",\"|\",\"-\",\"_\"],[\"=\",\"+\",\"@\",\"#\",\"$\"],[\"%\",\"^\",\"&\",\"*\",\"~\"]]\ndef read_file(file):\n    obsah = \"\"\n    obsah_list = []\n    for i in file:\n        obsah += i\n        for i in obsah:\n            obsah_list.append(i)\n    return obsah_list\ndef decode(obsah):\n    done = \"\"\n    sifra = []\n    for i in obsah:\n        done += str(i)\n        if i == \"[\" or i == \"\'\" or i == \",\" or i == \"]\":\n            done = \"\"\n            continue\n        if i == \" \":\n            sifra.append(i)\n        else:\n            sifra.append(i)\n    return sifra\ndef real_decode(obsah):\n    cislo = 0\n    pokracovanie = False\n    done = \"\"\n    vysledok = []\n    for i in obsah:\n        done += str(i)\n        cislo = 0\n        for i in done:\n            cislo += 1\n        if i == \" \":\n            done = \"\"\n            continue\n        if pokracovanie and done.isnumeric() and cislo == 1:\n            stlpec = int(done)\n            vysledok.append(PLOCHA[riadok][stlpec])\n            pokracovanie = False\n            done = \"\"\n            continue\n        if not pokracovanie or cislo == 2:\n            pokracovanie = True\n            riadok = int(done)\n            continue\n    return vysledok\ndef to_text(obsah):\n    text = \"\"\n    for i in obsah:\n        if i == \".\":\n            text += i + \"\\n\"\n            continue\n        text += i\n    return text\ndef create_file(obsah, name):\n    x = open(sys.argv[1], \"w\")\n    x.write(obsah)\n    x.close\n    return\ndef main():\n    if sys.argv[2] == \'False\':\n        name = \'data\'\n    else:\n        name = sys.argv[2]\n    open_file = open(name, \"r\")\n    code = list(decode(read_file(open_file)))\n    create_file(to_text(real_decode(code)), name)\nmain()\nx=open(\'DONE\',\'x\')\nx.close()')
findapp = str('import sys\ndecodename=str(sys.argv[1])\nicofind=int(sys.argv[2])\ndn=open(decodename,\'r\')\ndnr=dn.read()\nbracket,brackethist=0,0\nico=[]\nicocurrent=\'\'\nicoend=False\nrnii=False\nrniiend=False\nsubject=\'\'\nik=False\nuserdef=False\nwh=False\npassword=\'\'\npassend=False\nfor i in dnr:\n    if rnii:\n        wh=True\n        if i==\'[\':\n            bracket+=1\n        elif i==\']\':\n            bracket-=1\n        if passend:\n            user.write(password+\'\\n\')\n            passend=False\n        if ik:\n            if i!="," and bracket==4 and brackethist==4:\n                user.write(i)\n            if bracket==3:\n                subject=\'\'\n                ik=False\n                rniiend=False\n                user.write(\"\\n\")\n        if rniiend:\n            user.write(subject)\n            ik=True\n            rniiend=False\n            brackethist=bracket\n            continue\n        if userdef:\n            userdef=False\n            user=open(str(ico[0]),\'w\')\n        if bracket==3 and brackethist==3 and i!=\"\'\":\n            if i ==\',\':\n                rniiend=True\n                continue\n            subject+=str(i)\n        elif bracket==5 and brackethist==5 and i!=\"\'\":\n            if i ==\',\':\n                passend=True\n                continue\n            password+=str(i)\n        brackethist=bracket\n        if bracket<2 and brackethist<2:\n            break\n    else:\n        if i==\'[\':\n            bracket+=1\n        elif i==\']\':\n            bracket-=1\n        if icoend:\n            if icocurrent!=\'\':\n                if int(icocurrent)==icofind:\n                    ico.append(icocurrent)\n                    rnii=True\n                    continue\n                icocurrent=\'\'\n                icoend=False\n        if bracket==2 and brackethist==2:\n            if i ==\',\':\n                icoend=True\n                userdef=True\n                continue\n            icocurrent+=i\n        brackethist=bracket\nif not wh:\n    user=open(sys.argv[2], \'x\')\nuser.close()\nx=open(\'DONE\',\'x\')\nx.close()')
passwordapp = str('import sys\ndecodename=str(sys.argv[1])\ndn=open(decodename,\'r\')\ndnr=dn.readlines()\ntry:\n    number=int(dnr[0])\n    number=str(dnr[0])\n    number=dnr[0][:6]\nexcept Exception:\n    number=None\nx=open(\'DONE\',\'w\')\nx.write(number)\nx.close()')
addapp= str('import sys\ndecodename=str(sys.argv[1])\nicofind=int(sys.argv[2])\nsubjectfind = sys.argv[3]\nmarkadd = sys.argv[4]\ndn=open(decodename,\'r\')\ndnr=dn.read()\nbracket,brackethist=0,0\nico=[]\nicocurrent=\'\'\nicoend=False\nrnii=False\nrniiend=False\nsubject=\'\'\nik=False\nuserdef=False\nwh=False\npassword=\'\'\npassend=False\nik2=False\nadd=False\nuser=open(\'data1\',\'w\', newline=\'\')\nfor i in dnr:\n    user.write(i)\n    if rnii:\n        wh=True\n        if i==\'[\':\n            bracket+=1\n        elif i==\']\':\n            bracket-=1\n        if add and subject==subjectfind:\n            subjectfind=None\n            user.write(str(markadd) + \',\')\n            add=False\n        if passend:\n            passend=False\n        if ik:\n            if ik2:\n                ik2=False\n                add=True\n            if bracket==3:\n                subject=\'\'\n                ik=False\n                rniiend=False\n        if rniiend:\n            ik=True\n            ik2=True\n            rniiend=False\n            brackethist=bracket\n            continue\n        if userdef:\n            userdef=False\n        if bracket==3 and brackethist==3 and i!=\"\'\":\n            if i ==\',\':\n                rniiend=True\n                continue\n            subject+=str(i)\n        elif bracket==5 and brackethist==5 and i!=\"\'\":\n            if i ==\',\':\n                passend=True\n                continue\n            password+=str(i)\n        brackethist=bracket\n    else:\n        if i==\'[\':\n            bracket+=1\n        elif i==\']\':\n            bracket-=1\n        if icoend:\n            if icocurrent!=\'\':\n                if int(icocurrent)==icofind:\n                    ico.append(icocurrent)\n                    rnii=True\n                    continue\n                icocurrent=\'\'\n                icoend=False\n        if bracket==2 and brackethist==2:\n            if i ==\',\':\n                icoend=True\n                userdef=True\n                continue\n            icocurrent+=i\n        brackethist=bracket\nif not wh:\n    user=open(sys.argv[2], \'x\')\nuser.close()\nx=open(\'DONE\',\'x\')\nx.close()')

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


cachename = 'data.xp2'

def inactive():
    leave = False
    for i in os.listdir():
        if i == 'INACTIVE':
            leave = True
            os.remove('INACTIVE')
            break
    if leave:
        sleep(0.05)
        return True
    else:
        return False

def main():
    historyname = str(datetime.now().strftime("%H-%M-%S"))
    history = open(historyname, 'w')
    logged = False
    exit = False
    if args.language == "SK":
        print('SK')
        print("Načítavam...")
    if args.language == "EN":
        print('EN')
        print("Loading...")
    try:
        with zipfile.ZipFile(cachename, mode='r') as zip:
            zip.extractall(pwd=bytes('grenmansk','utf-8'))
            zip.close()
        if args.language == "SK":
            subprocess.call([sys.executable, 'xp3.py', 'data.xp3', 'data1', '-e', 'neko_vol0_steam'])
        if args.language == "EN":
            subprocess.call([sys.executable, 'xp3.py', 'data.xp3', 'data1', '-e', 'neko_vol0_steam', '-lang', 'EN'])
        shutil.move('data1/data', 'data')
        shutil.rmtree('data1')
        os.remove(cachename)
        os.remove('data.xp3')
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
        print('Používate ZnámE ' + verzia.read())
    if args.language == "EN":
        print('You\'re using ZnámE ' + verzia.read())
    verzia.close()
    try:
        if sys.argv[1] == 'inactive':
            sleep(0.25)
            if args.language == "SK":
                print('Bol si neaktívny, bol si odhlásený a program sa reštartoval!!!')
            if args.language == "EN":
                print('You were inactive, you were logged out and the program restarted!!!')
    except Exception:
        pass
    tologin = False
    restart = False
    topassword = False
    topasswordhelp = False
    loggedhelp = False
    firstlogin = True
    help = ['help','pomoc','-h','-help','?','-?']
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
                    loggedhelp = False
                vstup = input('> ')
                help = ['help','pomoc','-h','-help','?','-?']
                for i in range(len(help)):
                    if vstup == help[i]:
                        loggedhelp = True
                if loggedhelp:
                    continue
                if vstup == "zz":
                    passwordfile = open(loginvstupuser, 'r')
                    countersubject = 0
                    counterfirst = True
                    for i in passwordfile.read():
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
                        mark = input('Znamka > ')
                    if args.language == "EN":
                        subject = input('Subject > ')
                        mark = input('Mark > ')
                    code(add(decode(True, False), loginvstupuser, subject, mark), 'justcode')
                    os.mkdir("temp")
                    shutil.move("data", 'temp/')
                    os.rename('data1crypted', 'data')
                    shutil.rmtree('temp')
                    os.remove('data1')
            if topassword:
                if args.language == "SK":
                    vstup = input('Heslo > ')
                if args.language == "EN":
                    vstup = input('Password > ')
                help = ['help','pomoc','-h','-help','?','-?']
                for i in range(len(help)):
                    if vstup == help[i]:
                        topasswordhelp = True
                if topasswordhelp:
                    if args.language == "SK":
                        print("6 číselne heslo\n 'back' pre menu\n 'quit' pre koniec")
                    if args.language == "EN":
                        print("6 numeric password\n 'back' for menu\n 'quit' for end")
                    topasswordhelp = False
                    continue
                if vstup == "back":
                    print('Idem späť.')
                    topassword = False
                    os.remove(loginvstupuser + 'crypted')
                    continue
                elif vstup == "quit" or vstup == "koniec":
                    print("Idem späť a ukončujem program.")
                    sleep(0.5)
                    os.remove(loginvstupuser + 'crypted')
                    exit = True
                    continue
                password = password(decode(loginvstupuser + 'crypted', True))
                if vstup == password:
                    if args.language == "SK":
                        print('Si prihlaseny')
                    if args.language == "EN":
                        print('You\'re logged')
                    os.rename(loginvstupuser + 'crypted', loginvstupuser)
                    passwordfile = open(loginvstupuser, 'r')
                    passwordfile1 = open(loginvstupuser + "1", 'w')
                    counter = 0
                    for i in passwordfile.readlines():
                        if counter == 0:
                            counter += 1
                            continue
                        else:
                            passwordfile1.write(i)
                    passwordfile.close()
                    passwordfile1.close()
                    os.remove(loginvstupuser)
                    os.rename(loginvstupuser + '1', loginvstupuser)
                    topassword = False
                    logged = True
                    continue
                elif vstup != password:
                    topassword = False
                    os.remove(loginvstupuser + 'crypted')
                    if args.language == "SK":
                        print("ZLÉ HESLO")
                    if args.language == "EN":
                        print("WRONG PASSWORD")
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
                if args.language == "SK":
                    print("Si odhlásený")
                if args.language == "EN":
                    print("You\'re logged out")
                continue
            elif logged and inactivelogout and restart:
                logged = False
                if args.language == "SK":
                    print("Si odhlásený")
                if args.language == "EN":
                    print("You\'re logged out")
                continue
            elif not logged and vstup == "logout" or inactivelogout:
                logged = False
                if args.language == "SK":
                    print('Nie si prihlásený!!!')
                if args.language == "EN":
                    print("You\'re not logged in!!!")
                continue
            elif vstup == 'quit' or vstup == 'koniec':
                exit = True
                continue
            history = open(historyname, 'a')
            if vstup != "" and not restart:
                for i in range(len(help)):
                    if vstup == help[i]:
                        if args.language == "SK":
                            print("'login' pre prihlásenie\n'logout' pre odhlásenie\n'quit' alebo 'koniec' pre koniec")
                        if args.language == "EN":
                            print("'login' for login\n'logout' for logout\n'quit' or 'end' for end")
                        continue
                if vstup == 'login' and not logged or tologin and not logged:
                    loginvstupuser = ''
                    tologin = False
                    def add(name, ico, subject, mark):
                        decodename = str(datetime.now().strftime("%H-%M-%S"))
                        crdecode = open(decodename + ".py", "w")
                        crdecode.write(addapp)
                        crdecode.close()
                        subprocess.check_output('start ' + decodename + '.py ' + str(name) + ' ' + str(ico) + ' ' + str(subject) + ' ' + str(mark), shell=True)
                        if args.language == "SK":
                            print('Pridávam ...', end='\r')
                        if args.language == "EN":
                            print('Adding ...', end='\r')
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
                            print('Pridávam Hotovo')
                        if args.language == "EN":
                            print('Adding Complete')
                        os.remove(decodename + '.py')
                        os.remove(name)
                        os.remove('DONE')
                        name = ('data1', None)
                        return name
                    def decode(name, password):
                        decodename = str(datetime.now().strftime("%H-%M-%S"))
                        decodename2 = 'False'
                        if password:
                            decodename2 = name
                        if name:
                            decodename1 = decodename
                        if isinstance(name, str):
                            decodename1 = name
                        crdecode = open(decodename + ".py", "w")
                        crdecode.write(decodeapp)
                        crdecode.close()
                        subprocess.check_output('start ' + decodename + '.py ' + str(decodename1) + ' ' + str(decodename2), shell=True)
                        if args.language == "SK":
                            print('Odkoduvávam ...', end='\r')
                        if args.language == "EN":
                            print('Encrypting ...', end='\r')
                        while True:
                            leave = False
                            for i in os.listdir():
                                if i == 'DONE':
                                    leave = True
                                    break
                            if leave:
                                sleep(0.01)
                                break
                        if args.language == "SK":
                            print('Odkoduvávam Hotovo')
                        if args.language == "EN":
                            print('Encrypting Complete')
                        os.remove(decodename + '.py')
                        os.remove('DONE')
                        return decodename1
                    def password(name):
                        passwordname = str(datetime.now().strftime("%H-%M-%S"))
                        crfind = open(passwordname + ".py", "w")
                        crfind.write(passwordapp)
                        crfind.close()
                        if args.language == "SK":
                            print('Kontrolujem ...', end='\r')
                        if args.language == "EN":
                            print('Controling ...', end='\r')
                        subprocess.check_output('start ' + passwordname + '.py ' + str(name), shell=True)
                        while True:
                            leave = False
                            for i in os.listdir():
                                if i == 'DONE':
                                    leave = True
                                    break
                            if leave:
                                sleep(0.01)
                                break
                        os.remove(passwordname + '.py')
                        password = ''
                        for i in open('DONE', 'r').read():
                            password+=str(i)
                        if args.language == "SK":
                            print('Kontrolujem Complete')
                        if args.language == "EN":
                            print('Controling Complete')
                        os.remove('DONE')
                        return password
                    def find(name):
                        findname = str(datetime.now().strftime("%H-%M-%S"))
                        crfind = open(findname + ".py", "w")
                        crfind.write(findapp)
                        crfind.close()
                        if args.language == "SK":
                            print('Hľadám ...', end='\r')
                        if args.language == "EN":
                            print('Finding ...', end='\r')
                        subprocess.check_output('start ' + findname + '.py ' + str(name) + ' ' + str(loginvstupuser), shell=True)
                        while True:
                            leave = False
                            for i in os.listdir():
                                if i == 'DONE':
                                    leave = True
                                    break
                            if leave:
                                sleep(0.01)
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
                                print('Hľadám CHYBA')
                            if args.language == "EN":
                                print('Finding ERROR')
                            end = True
                        if end:
                            return (loginvstupuser, end)
                        test.close()
                        if args.language == "SK":
                            print('Hľadám Hotovo')
                        if args.language == "EN":
                            print('Finding Complete')
                        return (loginvstupuser, end)
                    def code(name, new):
                        codename = str(datetime.now().strftime("%H-%M-%S"))
                        crcode = open(codename + ".py", "w")
                        crcode.write(codeapp)
                        crcode.close()
                        if args.language == "SK":
                            print('Zakoduvávam ...', end='\r')
                        if args.language == "EN":
                            print('Coding ...', end='\r')
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
                            print('Zakoduvávam Complete')
                        if args.language == "EN":
                            print('Coding Complete')
                        os.remove(codename + '.py')
                        if new == 'justcode':
                            pass
                        elif new:
                            os.remove(loginvstupuser + 'crypted')
                            shutil.move(loginvstupuser + 'cryptedcrypted', loginvstupuser + 'crypted')
                        else:
                            os.remove(loginvstupuser)
                        os.remove('DONE')
                        return name[1], new
                    if args.language == "SK":
                        loginvstupuser = input("Prihlasovacie číslo (PID) > ")
                    if args.language == "EN":
                        loginvstupuser = input("Login Number (PID) > ")
                    history.write(loginvstupuser)
                    history.close()
                    history = open(historyname, 'a')
                    tologinhelp = False
                    if loginvstupuser == "back":
                        if args.language == "SK":
                            print('Idem späť.')
                        if args.language == "EN":
                            print('Going back.')
                        continue
                    elif loginvstupuser == "quit" or loginvstupuser == "koniec":
                        if args.language == "SK":
                            print("Idem späť a ukončujem program.")
                        if args.language == "EN":
                            print("Going back and exiting the program.")
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
                        tologin = True
                        continue
                    elif not loginvstupuser.isnumeric():
                        if args.language == "SK":
                            print('PID neobsahuje písmená alebo znaky!!!')
                        if args.language == "EN":
                            print('The PID does not contain letters or characters!!!')
                        tologin = True
                        continue
                    history.write(loginvstupuser + '\n')
                    if len(str(loginvstupuser)) == 6:
                        exit = False
                        icofind = code(find(decode(True, False)), False)
                        if icofind[0]:
                            logged = False
                            os.remove(loginvstupuser + 'crypted')
                            if args.language == "SK":
                                print("ZLÉ PID!!!")
                            if args.language == "EN":
                                print("WRONG PID!!!")
                            tologin = True
                            continue
                        Thread(target=delcache, args=(loginvstupuser,historyname,), daemon=True).start()
                        topassword = True
                    else:
                        if args.language == "SK":
                            print('PID má byt 6 čísel dlhé!!!')
                        if args.language == "EN":
                            print('The PID should be 6 numbers long!!!')
                        tologin = True
                elif logged and vstup == 'login':
                    if args.language == "SK":
                        print('Už si prihlasení!!!')
                    if args.language == "EN":
                        print('You are already logged in!!!')
        elif vstup == 'quit' or vstup == 'koniec' or exit:
            try:
                open('END', 'x')
            except Exception:
                pass
            if logged:
                try:
                    sleep(0.25)
                    os.remove(loginvstupuser)
                except Exception:
                    pass
                if args.language == "SK":
                    print("Si odhlásený")
                if args.language == "EN":
                    print('You are already logged in!!!')
            history.close()
            if args.language == "SK":
                print("ODSTRAŇOVANIE NEPOTREBNÝCH SÚBOROV")
            if args.language == "EN":
                print("DELETING UNNECESSARY FILES")
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
                subprocess.call([sys.executable, 'xp3.py', 'datafolder', 'data.xp3', '-mode', 'repack', '-e', 'neko_vol0_steam'])
            if args.language == "EN":
                subprocess.call([sys.executable, 'xp3.py', 'datafolder', 'data.xp3', '-mode', 'repack', '-e', 'neko_vol0_steam', '-lang', 'EN'])
            shutil.rmtree('datafolder')
            with zipfile.ZipFile(cachename, mode='w') as zip:
                zip.write('tests.py')
                zip.write('xp3.py')
                zip.write('xp3reader.py')
                zip.write('xp3writer.py')
                zip.write('data.xp3')
                for path, directories, files in os.walk('structs'):
                    for file in files:
                        file_name = os.path.join(path, file)
                        zip.write(file_name)
                zip.close()
            print('..', end='\r')
            sleep(0.2)
            os.remove('xp3.py')
            os.remove('xp3reader.py')
            os.remove('xp3writer.py')
            os.remove('data.xp3')
            os.remove('tests.py')
            shutil.rmtree('structs')
            print('...')
            sleep(0.2)
            if args.language == "SK":
                print("HOTOVO")
            if args.language == "EN":
                print("COMPLETE")
            sleep(0.5)
            if restart:
                if args.language == "SK":
                    print('Program sa automaticky reštartuje.')
                if args.language == "EN":
                    print('The program will restart automatically.')
            elif not restart:
                if args.language == "SK":
                    print('Program sa automaticky vypne.')
                if args.language == "EN":
                    print('The program will automatically shut down.')
            sleep(0.5)
            os.remove('END')
            sleep(1)
            if restart:
                subprocess.check_call('start python edupage.py inactive', shell=True)
                quit()
            elif not restart:
                quit()


if '__main__' == __name__:
    main()
