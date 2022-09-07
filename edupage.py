import pkg_resources
import sys
import os
import subprocess
potrebne = {'psutil', 'keyboard'}
nainstalovane = {pkg.key for pkg in pkg_resources.working_set}
nenajdene = potrebne - nainstalovane
if nenajdene:
    python = sys.executable
    subprocess.check_call([sys.executable, '-m', 'pip', 'install', *nenajdene])
    subprocess.call(
        [sys.executable, os.path.realpath(__file__)] + sys.argv[1:])
os.system('cls')
os.system('Title ' + 'ZnámE')
from time import sleep
from threading import Thread
from datetime import datetime

codeapp = str('import sys\nPLOCHA = [[\"a\", \"b\", \"c\", \"d\", \"e\"], [\"f\", \"g\", \"h\", \"i\", \"j\"], [\n    \"k\", \"l\", \"m\", \"n\", \"o\", ], [\"p\", \"q\", \"r\", \"s\", \"t\"], [\n    \"u\", \"v\", \"w\", \"x\", \"y\"], [\"A\", \"B\", \"C\", \"D\", \"E\"], [\n    \"F\", \"G\", \"H\", \"I\", \"J\"], [\"K\", \"L\", \"M\", \"N\", \"O\", ], [\n    \"P\", \"Q\", \"R\", \"S\", \"T\"], [\"U\", \"V\", \"W\", \"X\", \"y\"], [\n    \"z\", \" \", \",\", \".\", \":\"], [\"!\", \"?\", \"\'\", \'\"\', \"`\"], [\n    \"1\", \"2\", \"3\", \"4\", \"5\"], [\"6\", \"7\", \"8\", \"9\", \"0\"], [\n    \"\\n\", \"<\", \">\", \";\", \"/\"], [\"\\\\", \"{\", \"}\", \"(\", \")\"],[\n    \"[\",\"]\",\"|\",\"-\",\"_\"],[\"=\",\"+\",\"@\",\"#\",\"$\"],[\"%\",\"^\",\"&\",\"*\",\"~\"]]\ndef read_file(file):\n    obsah = \"\"\n    obsah_list = []\n    for i in file:\n        obsah = \"\"\n        obsah += i\n        for i in obsah:\n            i.lower()\n            obsah_list.append(i)\n    return obsah_list\ndef encode(obsah):\n    sifra = []\n    for i in obsah:\n        riadok = 0\n        stlpec = 0\n        while True:\n            if riadok == 19 and stlpec == 0:\n                break\n            if i == PLOCHA[riadok][stlpec]:\n                sifra.append(str(riadok) + \" \" + str(stlpec))\n                break\n            if stlpec == 4:\n                riadok += 1\n                stlpec = 0\n            else:\n                stlpec += 1\n    return sifra\ndef output_file(file, name):\n    y = []\n    x = open(name + \"crypted\", \"w\")\n    for i in file:\n        y.append(i)\n    x.write(str(y))\n    x.close\n    return\ndef main():\n    name = sys.argv[1]\n    open_file = open(name, \"r\")\n    open_file.close\n    output_file(encode(read_file(open_file)), name)\nmain()\nx=open(\'DONE\',\'x\')\nx.close()')
decodeapp = str('import os\nos.system(\'Title \' + \'code\')\nimport sys\nPLOCHA = [[\"a\", \"b\", \"c\", \"d\", \"e\"], [\"f\", \"g\", \"h\", \"i\", \"j\"], [\n    \"k\", \"l\", \"m\", \"n\", \"o\", ], [\"p\", \"q\", \"r\", \"s\", \"t\"], [\n    \"u\", \"v\", \"w\", \"x\", \"y\"], [\"A\", \"B\", \"C\", \"D\", \"E\"], [\n    \"F\", \"G\", \"H\", \"I\", \"J\"], [\"K\", \"L\", \"M\", \"N\", \"O\", ], [\n    \"P\", \"Q\", \"R\", \"S\", \"T\"], [\"U\", \"V\", \"W\", \"X\", \"y\"], [\n    \"z\", \" \", \",\", \".\", \":\"], [\"!\", \"?\", \"\'\", \'"\', \"`"], [\n    \"1\", \"2\", \"3\", \"4\", \"5\"], [\"6\", \"7\", \"8\", \"9\", \"0\"], [\n    \"\\n\", \"<\", \">\", \";\", \"/\"], [\"\\\\", \"{\", \"}\", \"(\", \")\"],[\n    \"[\",\"]\",\"|\",\"-\",\"_\"],[\"=\",\"+\",\"@\",\"#\",\"$\"],[\"%\",\"^\",\"&\",\"*\",\"~\"]]\ndef read_file(file):\n    obsah = \"\"\n    obsah_list = []\n    for i in file:\n        obsah += i\n        for i in obsah:\n            obsah_list.append(i)\n    return obsah_list\ndef decode(obsah):\n    done = \"\"\n    sifra = []\n    for i in obsah:\n        done += str(i)\n        if i == \"[\" or i == \"\'\" or i == \",\" or i == \"]\":\n            done = \"\"\n            continue\n        if i == \" \":\n            sifra.append(i)\n        else:\n            sifra.append(i)\n    return sifra\ndef real_decode(obsah):\n    cislo = 0\n    pokracovanie = False\n    done = \"\"\n    vysledok = []\n    for i in obsah:\n        done += str(i)\n        cislo = 0\n        for i in done:\n            cislo += 1\n        if i == \" \":\n            done = \"\"\n            continue\n        if pokracovanie and done.isnumeric() and cislo == 1:\n            stlpec = int(done)\n            vysledok.append(PLOCHA[riadok][stlpec])\n            pokracovanie = False\n            done = \"\"\n            continue\n        if not pokracovanie or cislo == 2:\n            pokracovanie = True\n            riadok = int(done)\n            continue\n    return vysledok\ndef to_text(obsah):\n    text = \"\"\n    for i in obsah:\n        if i == \".\":\n            text += i + \"\\n\"\n            continue\n        text += i\n    return text\ndef create_file(obsah, name):\n    x = open(sys.argv[1], \"w\")\n    x.write(obsah)\n    x.close\n    return\ndef main():\n    name = \'data\'\n    open_file = open(name, \"r\")\n    code = list(decode(read_file(open_file)))\n    create_file(to_text(real_decode(code)), name)\nmain()\nx=open(\'DONE\',\'x\')\nx.close()')
findapp = str('import sys\ndecodename=str(sys.argv[1])\nicofind=int(sys.argv[2])\ndn=open(decodename,\'r\')\ndnr=dn.read()\nbracket,brackethist=0,0\nico=[]\nicocurrent=\'\'\nicoend=False\nrnii=False\nrniiend=False\nsubject=\'\'\nik=False\nuserdef=False\nwh=False\npassword=\'\'\npassend=False\nfor i in dnr:\n    if rnii:\n        wh=True\n        if i==\'[\':\n            bracket+=1\n        elif i==\']\':\n            bracket-=1\n        if passend:\n            user.write(password+\'\\n\')\n            passend=False\n        if ik:\n            if i!="," and bracket==4 and brackethist==4:\n                user.write(i)\n            if bracket==3:\n                subject=\'\'\n                ik=False\n                rniiend=False\n                user.write(\"\\n\")\n        if rniiend:\n            user.write(subject)\n            ik=True\n            rniiend=False\n            brackethist=bracket\n            continue\n        if userdef:\n            userdef=False\n            user=open(str(ico[0]),\'w\')\n        if bracket==3 and brackethist==3 and i!=\"\'\":\n            if i ==\',\':\n                rniiend=True\n                continue\n            subject+=str(i)\n        elif bracket==5 and brackethist==5 and i!=\"\'\":\n            if i ==\',\':\n                passend=True\n                continue\n            password+=str(i)\n        brackethist=bracket\n        if bracket<2 and brackethist<2:\n            break\n    else:\n        if i==\'[\':\n            bracket+=1\n        elif i==\']\':\n            bracket-=1\n        if icoend:\n            if icocurrent!=\'\':\n                if int(icocurrent)==icofind:\n                    ico.append(icocurrent)\n                    rnii=True\n                    continue\n                icocurrent=\'\'\n                icoend=False\n        if bracket==2 and brackethist==2:\n            if i ==\',\':\n                icoend=True\n                userdef=True\n                continue\n            icocurrent+=i\n        brackethist=bracket\nif not wh:\n    user=open(sys.argv[2], \'x\')\nuser.close()\nx=open(\'DONE\',\'x\')\nx.close()')


# def delcache(name):
#     timer = 10
#     size = os.path.getsize(name + 'crypted')
#     sizehist = size
#     while True:
#         if timer >= 0:
#             os.remove(name + 'crypted')
#             break
#         if size != sizehist:
#             timer = 10
#         else:
#             sizehist = size
#             size = os.path.getsize(name + 'crypted')
#             sleep(1)
#             timer -= 1



def main():
    verzia = open('version', 'r')
    print('Používate ZnámE ' + verzia.read())
    verzia.close()
    historyname = str(datetime.now().strftime("%H-%M-%S"))
    history = open(historyname, 'w')
    while True:
        vstup = input('> ')
        history.write(vstup + '\n')
        if vstup == '?' or vstup == 'help':
            print("login")
        elif vstup == 'login':
            global loginvstupuser
            loginvstupuser = ''
            def decode():
                decodename = str(datetime.now().strftime("%H-%M-%S"))
                crdecode = open(decodename + ".py", "w")
                crdecode.write(decodeapp)
                crdecode.close()
                subprocess.check_output('start ' + decodename + '.py ' + str(decodename), shell=True)
                while True:
                    leave = False
                    for i in os.listdir():
                        if i == 'DONE':
                            leave = True
                            break
                    if leave:
                        sleep(0.5)
                        break
                os.remove(decodename + '.py')
                os.remove('DONE')
                return decodename
            def find(name):
                findname = str(datetime.now().strftime("%H-%M-%S"))
                crfind = open(findname + ".py", "w")
                crfind.write(findapp)
                crfind.close()
                subprocess.check_output('start ' + findname + '.py ' + str(name) + ' ' + str(loginvstupuser), shell=True)
                while True:
                    leave = False
                    for i in os.listdir():
                        if i == 'DONE':
                            leave = True
                            break
                    if leave:
                        sleep(0.5)
                        break
                os.remove(findname + '.py')
                os.remove(name)
                os.remove('DONE')
                sleep(0.1)
                return loginvstupuser
            def code(name):
                codename = str(datetime.now().strftime("%H-%M-%S"))
                crcode = open(codename + ".py", "w")
                crcode.write(codeapp)
                crcode.close()
                subprocess.check_output('start ' + codename + '.py ' + str(name), shell=True)
                while True:
                    leave = False
                    for i in os.listdir():
                        if i == 'DONE':
                            leave = True
                            break
                    if leave:
                        sleep(0.5)
                        break
                os.remove(codename + '.py')
                os.remove(loginvstupuser)
                os.remove('DONE')
                sleep(0.1)
            loginvstupuser = input("Prihlasovacie číslo (IČO) > ")
            history.write(loginvstupuser + '\n')
            sleep(0.1)
            if len(str(loginvstupuser)) == 6:
                code(find(decode()))
                sleep(0.1)
                test = open(loginvstupuser + 'crypted', 'r')
                for i in test.readlines():
                    if len(i) < 7:
                        test.close()
                        os.remove(loginvstupuser + 'crypted')
                        print('Zlé IČO!!!')
                test.close()
                #Thread(target=delcache, args=(loginvstupuser,), daemon=True).start()
            else:
                print('IČO má byt 6 čísel dlhé!!!')
        elif vstup == "quit":
            history.close()
            os.remove(historyname)
            os.remove(loginvstupuser + 'crypted')
            


if '__main__' == __name__:
    main()
