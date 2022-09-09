import pkg_resources, sys, os, subprocess
potrebne = {'psutil', 'numpy'}
nainstalovane = {pkg.key for pkg in pkg_resources.working_set}
nenajdene = potrebne - nainstalovane
if nenajdene:
    from time import sleep
    print("Sťahujú sa aktualizácie")
    sleep(0.5)
    subprocess.check_call([sys.executable, '-m', 'pip', 'install', *nenajdene])
    print("Program sa reštartuje!!!")
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
decodeapp = str('import os\nos.system(\'Title \' + \'code\')\nimport sys\nPLOCHA = [[\"a\", \"b\", \"c\", \"d\", \"e\"], [\"f\", \"g\", \"h\", \"i\", \"j\"], [\n    \"k\", \"l\", \"m\", \"n\", \"o\", ], [\"p\", \"q\", \"r\", \"s\", \"t\"], [\n    \"u\", \"v\", \"w\", \"x\", \"y\"], [\"A\", \"B\", \"C\", \"D\", \"E\"], [\n    \"F\", \"G\", \"H\", \"I\", \"J\"], [\"K\", \"L\", \"M\", \"N\", \"O\", ], [\n    \"P\", \"Q\", \"R\", \"S\", \"T\"], [\"U\", \"V\", \"W\", \"X\", \"y\"], [\n    \"z\", \" \", \",\", \".\", \":\"], [\"!\", \"?\", \"\'\", \'"\', \"`"], [\n    \"1\", \"2\", \"3\", \"4\", \"5\"], [\"6\", \"7\", \"8\", \"9\", \"0\"], [\n    \"\\n\", \"<\", \">\", \";\", \"/\"], [\"\\\\", \"{\", \"}\", \"(\", \")\"],[\n    \"[\",\"]\",\"|\",\"-\",\"_\"],[\"=\",\"+\",\"@\",\"#\",\"$\"],[\"%\",\"^\",\"&\",\"*\",\"~\"]]\ndef read_file(file):\n    obsah = \"\"\n    obsah_list = []\n    for i in file:\n        obsah += i\n        for i in obsah:\n            obsah_list.append(i)\n    return obsah_list\ndef decode(obsah):\n    done = \"\"\n    sifra = []\n    for i in obsah:\n        done += str(i)\n        if i == \"[\" or i == \"\'\" or i == \",\" or i == \"]\":\n            done = \"\"\n            continue\n        if i == \" \":\n            sifra.append(i)\n        else:\n            sifra.append(i)\n    return sifra\ndef real_decode(obsah):\n    cislo = 0\n    pokracovanie = False\n    done = \"\"\n    vysledok = []\n    for i in obsah:\n        done += str(i)\n        cislo = 0\n        for i in done:\n            cislo += 1\n        if i == \" \":\n            done = \"\"\n            continue\n        if pokracovanie and done.isnumeric() and cislo == 1:\n            stlpec = int(done)\n            vysledok.append(PLOCHA[riadok][stlpec])\n            pokracovanie = False\n            done = \"\"\n            continue\n        if not pokracovanie or cislo == 2:\n            pokracovanie = True\n            riadok = int(done)\n            continue\n    return vysledok\ndef to_text(obsah):\n    text = \"\"\n    for i in obsah:\n        if i == \".\":\n            text += i + \"\\n\"\n            continue\n        text += i\n    return text\ndef create_file(obsah, name):\n    x = open(sys.argv[1], \"w\")\n    x.write(obsah)\n    x.close\n    return\ndef main():\n    name = \'data\'\n    open_file = open(name, \"r\")\n    code = list(decode(read_file(open_file)))\n    create_file(to_text(real_decode(code)), name)\nmain()\nx=open(\'DONE\',\'x\')\nx.close()')
findapp = str('import sys\ndecodename=str(sys.argv[1])\nicofind=int(sys.argv[2])\ndn=open(decodename,\'r\')\ndnr=dn.read()\nbracket,brackethist=0,0\nico=[]\nicocurrent=\'\'\nicoend=False\nrnii=False\nrniiend=False\nsubject=\'\'\nik=False\nuserdef=False\nwh=False\npassword=\'\'\npassend=False\nfor i in dnr:\n    if rnii:\n        wh=True\n        if i==\'[\':\n            bracket+=1\n        elif i==\']\':\n            bracket-=1\n        if passend:\n            user.write(password+\'\\n\')\n            passend=False\n        if ik:\n            if i!="," and bracket==4 and brackethist==4:\n                user.write(i)\n            if bracket==3:\n                subject=\'\'\n                ik=False\n                rniiend=False\n                user.write(\"\\n\")\n        if rniiend:\n            user.write(subject)\n            ik=True\n            rniiend=False\n            brackethist=bracket\n            continue\n        if userdef:\n            userdef=False\n            user=open(str(ico[0]),\'w\')\n        if bracket==3 and brackethist==3 and i!=\"\'\":\n            if i ==\',\':\n                rniiend=True\n                continue\n            subject+=str(i)\n        elif bracket==5 and brackethist==5 and i!=\"\'\":\n            if i ==\',\':\n                passend=True\n                continue\n            password+=str(i)\n        brackethist=bracket\n        if bracket<2 and brackethist<2:\n            break\n    else:\n        if i==\'[\':\n            bracket+=1\n        elif i==\']\':\n            bracket-=1\n        if icoend:\n            if icocurrent!=\'\':\n                if int(icocurrent)==icofind:\n                    ico.append(icocurrent)\n                    rnii=True\n                    continue\n                icocurrent=\'\'\n                icoend=False\n        if bracket==2 and brackethist==2:\n            if i ==\',\':\n                icoend=True\n                userdef=True\n                continue\n            icocurrent+=i\n        brackethist=bracket\nif not wh:\n    user=open(sys.argv[2], \'x\')\nuser.close()\nx=open(\'DONE\',\'x\')\nx.close()')
passwordapp = str('import sys\ndecodename=str(sys.argv[1])\ndn=open(decodename,\'r\')\ndnr=dn.read()\nbracket,brackethist=0,0\npassword=\'\'\nicoend=False\nrnii=False\nfor i in dnr:\n    if rnii:\n        break\n    if i==\'[\':\n        bracket+=1\n    elif i==\']\':\n        bracket-=1\n    if icoend:\n        if password!=\'\':\n            rnii=True\n            continue\n    if bracket==5 and brackethist==5:\n        if i ==\',\':\n            icoend=True\n            passwordfile=open(decodename[:6], \'w\')\n            passwordfile.write(str(password))\n            continue\n        password+=i\n    brackethist=bracket\npasswordfile.close()\nx=open(\'DONE\',\'w\')\nx.write(decodename)\nx.close()')

def delcache(name, hist):
    global timer
    timer = 300
    size = os.path.getsize(hist)
    sizehist = size
    while True:
        try:
            for i in os.listdir():
                if i == "END":
                    raise Exception
            if timer <= 0:
                os.remove(name+'crypted')
                x = open("INACTIVE", 'x')
                x.close()
                os.system('cls')
                print("Stlač 'enter'")
                break
            if size != sizehist:
                timer = 300
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
    print("Načítavam...")
    try:
        with zipfile.ZipFile(cachename, mode='r') as zip:
            zip.extractall(pwd=bytes('grenmansk','utf-8'))
            zip.close()
        subprocess.call([sys.executable, 'xp3.py', 'data.xp3', 'data1', '-e', 'neko_vol0_steam'])
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
    print('Používate ZnámE ' + verzia.read())
    verzia.close()
    tologin = False
    restart = False
    topassword = False
    topasswordhelp = False
    help = ['help','pomoc','-h','-help','?','-?']
    while True:
        if not exit:
            global loginvstupuser
            if topassword:
                vstup = input('Heslo > ')
                help = ['help','pomoc','-h','-help','?','-?']
                for i in range(len(help)):
                    if vstup == help[i]:
                        topasswordhelp = True
                if topasswordhelp:
                    print("6 číselne heslo\n 'back' pre menu\n 'quit' pre koniec")
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
                password = code(password(decode(loginvstupuser + 'crypted')), True)[0]
                if vstup == password:
                    print('Si prihlaseny')
                    topassword = False
                    logged = True
                elif vstup != password:
                    topassword = False
                    os.remove(loginvstupuser + 'crypted')
                    print("ZLÉ HESLO")
            if not tologin:
                vstup = input('> ')
                history.write(vstup + '\n')
                vstup.lower()
                history.close()
                history = open(historyname, 'a')
            inactivelogout = inactive()
            if inactivelogout:
                restart = True
                exit = True
            if logged and vstup == "logout" and not restart:
                logged = False
                os.remove(loginvstupuser + 'crypted')
                print("Si odhlásený")
                continue
            elif logged and inactivelogout and restart:
                logged = False
                print("Si odhlásený!!!")
                continue
            elif not logged and vstup == "logout" or inactivelogout:
                logged = False
                print('Nie si prihlásený!!!')
                continue
            elif vstup == 'quit' or vstup == 'koniec':
                exit = True
                continue
            history = open(historyname, 'a')
            if vstup != "" and not restart:
                for i in range(len(help)):
                    if vstup == help[i]:
                        print("'login' pre prihlásenie\n'logout' pre odhlásenie\n'quit' alebo 'koniec' pre koniec")
                        continue
                if vstup == 'login' and not logged or tologin and not logged:
                    loginvstupuser = ''
                    tologin = False
                    def decode(name):
                        decodename = str(datetime.now().strftime("%H-%M-%S"))
                        if name:
                            decodename1 = decodename
                        if isinstance(name, str):
                            decodename1 = name
                        crdecode = open(decodename + ".py", "w")
                        crdecode.write(decodeapp)
                        crdecode.close()
                        subprocess.check_output('start ' + decodename + '.py ' + str(decodename1), shell=True)
                        print('Odkoduvávam ...', end='\r')
                        while True:
                            leave = False
                            for i in os.listdir():
                                if i == 'DONE':
                                    leave = True
                                    break
                            if leave:
                                sleep(0.05)
                                break
                        print('Odkoduvávam Hotovo')
                        os.remove(decodename + '.py')
                        os.remove('DONE')
                        return decodename1
                    def password(name):
                        passwordname = str(datetime.now().strftime("%H-%M-%S"))
                        crfind = open(passwordname + ".py", "w")
                        crfind.write(passwordapp)
                        crfind.close()
                        print('Kontrolujem ...', end='\r')
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
                        for i in open(name[:6], 'r').read():
                            password+=str(i)
                        print('Kontrolujem Hotovo')
                        os.remove(loginvstupuser)
                        os.remove('DONE')
                        return loginvstupuser+'crypted',password
                    def find(name):
                        findname = str(datetime.now().strftime("%H-%M-%S"))
                        crfind = open(findname + ".py", "w")
                        crfind.write(findapp)
                        crfind.close()
                        print('Hľadám ...', end='\r')
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
                            print('Hľadám CHYBA')
                            end = True
                        if end:
                            return (loginvstupuser, end)
                        test.close()
                        print('Hľadám Hotovo')
                        return (loginvstupuser, end)
                    def code(name, new):
                        codename = str(datetime.now().strftime("%H-%M-%S"))
                        crcode = open(codename + ".py", "w")
                        crcode.write(codeapp)
                        crcode.close()
                        print('Zakoduvávam ...', end='\r')
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
                        print('Zakoduvávam Hotovo')
                        os.remove(codename + '.py')
                        if new:
                            os.remove(loginvstupuser + 'crypted')
                            shutil.move(loginvstupuser + 'cryptedcrypted', loginvstupuser + 'crypted')
                        else:
                            os.remove(loginvstupuser)
                        os.remove('DONE')
                        return name[1], new
                    loginvstupuser = input("Prihlasovacie číslo (PID) > ")
                    history.write(loginvstupuser)
                    history.close()
                    history = open(historyname, 'a')
                    tologinhelp = False
                    if loginvstupuser == "back":
                        print('Idem späť.')
                        continue
                    elif loginvstupuser == "quit" or loginvstupuser == "koniec":
                        print("Idem späť a ukončujem program.")
                        sleep(0.5)
                        exit = True
                        continue
                    help = ['help','pomoc','-h','-help','?','-?']
                    for i in range(len(help)):
                        if loginvstupuser == help[i]:
                            tologinhelp = True
                    if tologinhelp:
                        print("'back' pre menu\n'quit' alebo 'koniec' pre koniec")
                        tologin = True
                        continue
                    elif not loginvstupuser.isnumeric():
                        print('PID neobsahuje písmená alebo znaky!!!')
                        tologin = True
                        continue
                    history.write(loginvstupuser + '\n')
                    if len(str(loginvstupuser)) == 6:
                        exit = False
                        icofind = code(find(decode(True)), False)
                        if icofind[0]:
                            logged = False
                            os.remove(loginvstupuser + 'crypted')
                            print("ZLÉ PID!!!")
                            tologin = True
                            continue
                        Thread(target=delcache, args=(loginvstupuser,historyname,), daemon=True).start()
                        topassword = True
                    else:
                        print('PID má byt 6 čísel dlhé!!!')
                        tologin = True
                elif logged and vstup == 'login':
                    print('Už si prihlasení!!!')
        elif vstup == 'quit' or vstup == 'koniec' or exit:
            try:
                open('END', 'x')
            except Exception:
                pass
            if logged:
                try:
                    sleep(0.25)
                    os.remove(loginvstupuser + 'crypted')
                except Exception:
                    pass
                print("Si odhlásený")
            history.close()
            print("ODSTRAŇOVANIE NEPOTREBNÝCH SÚBOROV")
            try:
                os.remove(historyname)
            except Exception:
                pass
            print('.', end='\r')
            sleep(0.2)
            os.mkdir('datafolder')
            sleep(0.2)
            shutil.move('data', 'datafolder/')
            sleep(0.2)
            subprocess.call([sys.executable, 'xp3.py', 'datafolder', 'data.xp3', '-mode', 'repack', '-e', 'neko_vol0_steam'])
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
            print("HOTOVO")
            sleep(0.5)
            if restart:
                print('Program sa automaticky reštartuje.')
            elif not restart:
                print('Program sa automaticky vypne.')
            sleep(0.5)
            os.remove('END')
            sleep(1)
            if restart:
                subprocess.check_call('start python edupage.py', shell=True)
                quit()
            elif not restart:
                quit()


if '__main__' == __name__:
    main()
