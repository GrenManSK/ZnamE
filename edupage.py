try:  # type: ignore
    import cProfile
    import pstats
    from datetime import datetime
    from time import sleep
    import sys
    import os
    
    if os.path.isfile('INSTALL_RESTART'):
        sleep(1)
    try:
        import verbose
    except ModuleNotFoundError:
        print(f'Verbose not found\nUse this command to install it {sys.executable} -m pip install git+https://github.com/GrenManSK/verbose.git')
        input()
        sys.exit(1)
    try:
        from final import mathematical
    except ModuleNotFoundError:
        print(f'final not found\nUse this command to install it {sys.executable} -m pip install git+https://github.com/GrenManSK/final.git')
        input()
        sys.exit(1)
    logger = verbose.get_logger()
    datelog: str = datetime.now().strftime("%y-%m-%d-%H-%M-%S")
    with open('.env', 'w') as dotenv:
        dotenv.write(f'DATELOG={datelog}\n')
    from essentials.writing import printnlog, log, to_info, typewriter
    from essentials.file_operations import mkdir, remove

    modulenames: list = list(set(sys.modules) & set(globals()))
    modulenames1: list = list(set(sys.modules) & set(globals()))
    moduleminus: int = 0

    def print_module(addto: str = '') -> None:
        """
        The print_module function prints all the modules that are currently loaded in memory.
        It also adds a new module to the list of modules printed by this function.
        The print_module function is useful for debugging purposes.

        :param add: Add a module to the list of modules that will be printed
        :return: The names of all the modules currently loaded
        """
        global modulenames1
        modulenames1 = list(set(sys.modules) & set(globals()))
        for i in range(len(modulenames) - moduleminus):
            modulenames1.remove(modulenames[i])
        for i in range(len(modulenames1)):
            modulenames.append(modulenames1[i])
        if __name__ == '__main__':
            for i in modulenames1:
                logger.stay(printnlog(i, toprint=False))
            if addto != '':
                logger.stay(printnlog(addto, toprint=False))

    print_module('datetime')
    print_module('sleep from time')
    print_module('cProfile')
    print_module('pstats')
    print_module('sys')
    print_module()
    import subprocess
    print_module()
    import yaml
    print_module()
    import inspect
    print_module()
    import time
    print_module()
    from time import sleep
    print_module()
    import traceback
    print_module()
    if __name__ == '__main__':
        logger.stay(printnlog('DONE', toprint=False))

    "Defining custom exceptions"

    from essentials.exceptions import argGameError, argenvironmentError, argInactiveLimitError, argIntroError, argMusicError, argMusicListError, argNekoError, argWaifuError, configNoOption
    from essentials.exceptions import error_get
    from essentials.system_info import get_line_number
    allerror = []
    for name, obj in inspect.getmembers(sys.modules[__name__]):
        if inspect.isclass(obj):
            allerror.append(obj.__name__)

    if __name__ == '__main__':
        for i in range(0, len(allerror)-1):
            printnlog(allerror[i], end=', ')
        printnlog(allerror[len(allerror)-1])

    "Checking if config file is in correct state"

    if __name__ == '__main__':
        logger.stay(printnlog('Reading config file (ini)', toprint=False))
        config = yaml.safe_load(open('config.yml', 'r'))
        config['user history'] = {}
        line_number: int = get_line_number(-1)

    "Printing out important config setting"

    try:
        if __name__ == '__main__':
            from essentials.arguments import print_config
            print_config(logger, config)
    except AttributeError:
        printnlog("'config.ini' file is corrupt -> option missing")
        error_get(configNoOption(
            'Corruption of config file => option missing'), [line_number],)
        input("Press 'enter' to quit")
        sys.exit(1)

    logger.stay(printnlog('\nDone\n', toprint=False))

    from essentials.arguments import set_config

    if __name__ == '__main__':
        from essentials.arguments import arguments, check_correctness
        server: list[str] = ['nekos.best', 'waifu.pics', 'kyoko', 'nekos_api']
        parser, music, UNSPECIFIED = arguments(config)
        args = parser.parse_args()
        check_correctness(args, config, logger, music)
        """
        If the program has specified that we should update the rotation dictionary, remove the old update.py file.
        """
        if args.update is None:
            try:
                os.remove('update.py')
            except FileNotFoundError:
                args.update = UNSPECIFIED
                error_get(ExceptionGroup('', [FileNotFoundError(
                    'update.py isn\'t present'), TypeError('NOT FATAL ERROR')]), [get_line_number()])

        logger.stay(printnlog('DONE', toprint=False))

        if args.configoptions == None:
            from essentials.arguments import write_config_options
            write_config_options(server)

    if __name__ == '__main__':
        from essentials.app_alternations import python_update
        python_update(args, logger)

    from threading import Thread
    if __name__ == '__main__':
        print_module('Thread from threading')
    import pyautogui as pg
    if __name__ == '__main__':
        print_module('pyautogui')
        if args.restart is None:
            pg.keyDown('alt')
            pg.press('tab')
            pg.keyUp('alt')
            pg.keyDown('alt')
            pg.press('tab')
            pg.keyUp('alt')
        pg.keyDown('win')
        pg.press('up')
        pg.keyUp('win')
    if __name__ == '__main__':
        if not os.path.isfile("C:/Users/" + os.getlogin() + "/AppData/Local/ZnámE/info.txt"):
            logger.stay(printnlog('First time setup', toprint=False))
            from essentials.app_alternations import install_choco, install_packages
            if not os.path.isfile('INSTALL_RESTART'):
                install_choco(logger)
            if os.path.isfile('INSTALL'):
                install_packages(args, logger)
            sleep(1)
            os.remove('INSTALL_RESTART')
            typewriter('Trying ffmpeg ...')
            os.system('ffmpeg')

    from essentials.internet import internet_check, download
    if __name__ == '__main__':
        internet_check(args)
        logger.stay(printnlog('DONE', toprint=False))
        logger.stay(printnlog('Importing libraries', toprint=False))
        logger.next('')
    from tqdm import tqdm
    if __name__ == '__main__':
        print_module()
    from uninstall import uninstall
    if __name__ == '__main__':
        print_module()
    import shutil
    if __name__ == '__main__':
        print_module()
    import requests
    if __name__ == '__main__':
        print_module()
    import cv2
    if __name__ == '__main__':
        print_module()
    import webbrowser
    if __name__ == '__main__':
        print_module()
    import vlc
    if __name__ == '__main__':
        print_module()
    import pygetwindow
    if __name__ == '__main__':
        print_module()
    from PIL import Image
    if __name__ == '__main__':
        print_module('Image from PIL')
    from pygame import mixer
    if __name__ == '__main__':
        print_module('mixer from pygame')
    import logging
    if __name__ == '__main__':
        print_module()
    import moviepy.editor as mp
    if __name__ == '__main__':
        print_module('moviepy.editor')
        logger.prev(printnlog('DONE', toprint=False))
        os.system('color ' + str(config['basic info']['environmentA']) + str(config['basic info']['environmentA']))
        os.system('Title ' + 'ZnámE')
        from essentials.system_info import get_screensize
        screensize, screensizepercentage = get_screensize()
        if not os.path.isfile("C:/Users/" + os.getlogin() + "/AppData/Local/ZnámE/info.txt"):
            from essentials.system_info import system_info
            system_info(logger, screensize)
        if not os.path.exists("C:/Users/" + os.getlogin() + "/AppData/Local/ZnámE/backup/"):

            "Creating backup files of data.xp2"

            logger.stay(printnlog('Creating backup...\b', toprint=False))
            os.makedirs("C:/Users/" + os.getlogin() +
                        "/AppData/Local/ZnámE/backup/")
            shutil.copy('data.xp2', "C:/Users/" + os.getlogin() + "/AppData/Local/ZnámE/backup/backup-" +
                        str(datetime.now().strftime("%y-%m-%d-%H-%M-%S")) + '.xp2')
            with open("C:/Users/" + os.getlogin() + "/AppData/Local/ZnámE/backup/info.txt", 'w') as x:
                x.write( 'Rename \'xp2\' file to \'data.xp2\' and move it to your \'ZnámE\' directory')
            logger.stay(printnlog('Done'))

        logger.stay(printnlog("Defining functions", toprint=False))

    LOG_FILENAME = 'completer.log'
    logging.basicConfig(filename=LOG_FILENAME,
                        level=logging.DEBUG,
                        format="%(asctime)s,%(msecs)03d %(levelname)-8s [%(filename)s:%(lineno)d] - %(message)s",
                        datefmt='%Y-%m-%d:%H:%M:%S')
    
    updateapp: str = str(
        'import argparse, shutil, subprocess, yaml, sys\nfrom time import sleep\nUNSPECIFIED = object()\nglobal parser\nparser = argparse.ArgumentParser()\nparser.add_argument(\'-ef\', \'--endf\', help=\'Will not automatically end program\', default=UNSPECIFIED, nargs=\'?\')\nparser.add_argument(\'input\', help=\'Input folder\', nargs=\'?\')\nargs = parser.parse_args()\nconfig = yaml.safe_load(open(\'config.yml\', \'r\'))\nif args.input != \"\":\n    shutil.rmtree(\'old\')\n    if args.endf == None:\n        subprocess.call(sys.executable + \' edupage.py -endf -update\', shell=True)\n    else:\n        subprocess.call(sys.executable + \' edupage.py -update\', shell=True)\n    sys.exit(0)')

    if __name__ == '__main__':
        if args.test is not None:
            logger.stay(printnlog('Checking for newer version of ZnámE', toprint=False))
            from essentials.app_alternations import update_app
            update_app(args, logger)

    from essentials.system_operations import getWindow, getImg, move, show_cmd, wait_for_file

    if __name__ == '__main__':
        logger.stay(printnlog('Function: move', toprint=False))
        logger.stay(printnlog('Function: getImg', toprint=False))
        logger.stay(printnlog('Function: getWindow', toprint=False))
        logger.next(printnlog('\nDefining apps', toprint=False))

    codeapp: str = str('import sys\nPLOCHA = [[\"a\", \"b\", \"c\", \"d\", \"e\"], [\"f\", \"g\", \"h\", \"i\", \"j\"], [\n    \"k\", \"l\", \"m\", \"n\", \"o\", ], [\"p\", \"q\", \"r\", \"s\", \"t\"], [\n    \"u\", \"v\", \"w\", \"x\", \"y\"], [\"A\", \"B\", \"C\", \"D\", \"E\"], [\n    \"F\", \"G\", \"H\", \"I\", \"J\"], [\"K\", \"L\", \"M\", \"N\", \"O\", ], [\n    \"P\", \"Q\", \"R\", \"S\", \"T\"], [\"U\", \"V\", \"W\", \"X\", \"y\"], [\n    \"z\", \" \", \",\", \".\", \":\"], [\"!\", \"?\", \"\'\", \'\"\', \"`\"], [\n    \"1\", \"2\", \"3\", \"4\", \"5\"], [\"6\", \"7\", \"8\", \"9\", \"0\"], [\n    \"\\n\", \"<\", \">\", \";\", \"/\"], [\"\\\\", \"{\", \"}\", \"(\", \")\"],[\n    \"[\",\"]\",\"|\",\"-\",\"_\"],[\"=\",\"+\",\"@\",\"#\",\"$\"],[\"%\",\"^\",\"&\",\"*\",\"~\"]]\ndef read_file(file):\n    obsah = \"\"\n    obsah_list = []\n    for i in file:\n        obsah = \"\"\n        obsah += i\n        for i in obsah:\n            i.lower()\n            obsah_list.append(i)\n    return obsah_list\ndef encode(obsah):\n    sifra = []\n    for i in obsah:\n        riadok = 0\n        stlpec = 0\n        while True:\n            if riadok == 19 and stlpec == 0:\n                break\n            if i == PLOCHA[riadok][stlpec]:\n                sifra.append(str(riadok) + \" \" + str(stlpec))\n                break\n            if stlpec == 4:\n                riadok += 1\n                stlpec = 0\n            else:\n                stlpec += 1\n    return sifra\ndef output_file(file, name):\n    y = []\n    x = open(name + \"crypted\", \"w\")\n    for i in file:\n        y.append(i)\n    x.write(str(y))\n    x.close\n    return\ndef main():\n    name = sys.argv[1]\n    open_file = open(name, \"r\")\n    open_file.close\n    output_file(encode(read_file(open_file)), name)\nmain()\nx=open(\'DONE\',\'x\')\nx.close()')
    decodeapp: str = str('import os\nos.system(\'Title \' + \'code\')\nimport sys\nPLOCHA = [[\"a\", \"b\", \"c\", \"d\", \"e\"], [\"f\", \"g\", \"h\", \"i\", \"j\"], [\n    \"k\", \"l\", \"m\", \"n\", \"o\", ], [\"p\", \"q\", \"r\", \"s\", \"t\"], [\n    \"u\", \"v\", \"w\", \"x\", \"y\"], [\"A\", \"B\", \"C\", \"D\", \"E\"], [\n    \"F\", \"G\", \"H\", \"I\", \"J\"], [\"K\", \"L\", \"M\", \"N\", \"O\", ], [\n    \"P\", \"Q\", \"R\", \"S\", \"T\"], [\"U\", \"V\", \"W\", \"X\", \"y\"], [\n    \"z\", \" \", \",\", \".\", \":\"], [\"!\", \"?\", \"\'\", \'"\', \"`"], [\n    \"1\", \"2\", \"3\", \"4\", \"5\"], [\"6\", \"7\", \"8\", \"9\", \"0\"], [\n    \"\\n\", \"<\", \">\", \";\", \"/\"], [\"\\\\", \"{\", \"}\", \"(\", \")\"],[\n    \"[\",\"]\",\"|\",\"-\",\"_\"],[\"=\",\"+\",\"@\",\"#\",\"$\"],[\"%\",\"^\",\"&\",\"*\",\"~\"]]\ndef read_file(file):\n    obsah = \"\"\n    obsah_list = []\n    for i in file:\n        obsah += i\n        for i in obsah:\n            obsah_list.append(i)\n    return obsah_list\ndef decode(obsah):\n    done = \"\"\n    sifra = []\n    for i in obsah:\n        done += str(i)\n        if i == \"[\" or i == \"\'\" or i == \",\" or i == \"]\":\n            done = \"\"\n            continue\n        if i == \" \":\n            sifra.append(i)\n        else:\n            sifra.append(i)\n    return sifra\ndef real_decode(obsah):\n    cislo = 0\n    pokracovanie = False\n    done = \"\"\n    vysledok = []\n    for i in obsah:\n        done += str(i)\n        cislo = 0\n        for i in done:\n            cislo += 1\n        if i == \" \":\n            done = \"\"\n            continue\n        if pokracovanie and done.isnumeric() and cislo == 1:\n            stlpec = int(done)\n            vysledok.append(PLOCHA[riadok][stlpec])\n            pokracovanie = False\n            done = \"\"\n            continue\n        if not pokracovanie or cislo == 2:\n            pokracovanie = True\n            riadok = int(done)\n            continue\n    return vysledok\ndef to_text(obsah):\n    text = \"\"\n    for i in obsah:\n        if i == \".\":\n            text += i + \"\\n\"\n            continue\n        text += i\n    return text\ndef create_file(obsah, name):\n    x = open(sys.argv[1], \"w\")\n    x.write(obsah)\n    x.close\n    return\ndef main():\n    if sys.argv[2] == \'False\':\n        name = \'data\'\n    else:\n        name = sys.argv[2]\n    open_file = open(name, \"r\")\n    code = list(decode(read_file(open_file)))\n    create_file(to_text(real_decode(code)), name)\nmain()\nx=open(\'DONE\',\'x\')\nx.close()')
    findapp: str = str('import sys\ndecodename=str(sys.argv[1])\nicofind=int(sys.argv[2])\ndn=open(decodename,\'r\')\ndnr=dn.read()\nbracket,brackethist=0,0\nico=[]\nicocurrent=\'\'\nicoend=False\nrnii=False\nrniiend=False\nsubject=\'\'\nik=False\nuserdef=False\nwh=False\npassword=\'\'\npassend=False\nfor i in dnr:\n    if rnii:\n        wh=True\n        if i==\'[\':\n            bracket+=1\n        elif i==\']\':\n            bracket-=1\n        if passend:\n            user.write(password+\'\\n\')\n            passend=False\n        if ik:\n            if i!="," and bracket==4 and brackethist==4:\n                user.write(i)\n            if bracket==3:\n                subject=\'\'\n                ik=False\n                rniiend=False\n                user.write(\"\\n\")\n        if rniiend:\n            user.write(subject)\n            ik=True\n            rniiend=False\n            brackethist=bracket\n            continue\n        if userdef:\n            userdef=False\n            user=open(str(ico[0]),\'w\')\n        if bracket==3 and brackethist==3 and i!=\"\'\":\n            if i ==\',\':\n                rniiend=True\n                continue\n            subject+=str(i)\n        elif bracket==5 and brackethist==5 and i!=\"\'\":\n            if i ==\',\':\n                passend=True\n                continue\n            password+=str(i)\n        brackethist=bracket\n        if bracket<2 and brackethist<2:\n            break\n    else:\n        if i==\'[\':\n            bracket+=1\n        elif i==\']\':\n            bracket-=1\n        if icoend:\n            if icocurrent!=\'\':\n                if int(icocurrent)==icofind:\n                    ico.append(icocurrent)\n                    rnii=True\n                    continue\n                icocurrent=\'\'\n                icoend=False\n        if bracket==2 and brackethist==2:\n            if i ==\',\':\n                icoend=True\n                userdef=True\n                continue\n            icocurrent+=i\n        brackethist=bracket\nif not wh:\n    user=open(sys.argv[2], \'x\')\nuser.close()\nx=open(\'DONE\',\'x\')\nx.close()')
    passwordapp: str = str('import sys\ndecodename=str(sys.argv[1])\ndn=open(decodename,\'r\')\ndnr=dn.readlines()\ntry:\n    number=int(dnr[0])\n    number=str(dnr[0])\n    number=dnr[0][:6]\nexcept Exception:\n    number=None\nx=open(\'DONE\',\'w\')\nx.write(number)\nx.close()')
    addapp: str = str('import sys\ndecodename=str(sys.argv[1])\nicofind=int(sys.argv[2])\nsubjectfind = sys.argv[3]\nmarkadd = sys.argv[4]\ndn=open(decodename,\'r\')\ndnr=dn.read()\nbracket,brackethist=0,0\nico=[]\nicocurrent=\'\'\nicoend=False\nrnii=False\nrniiend=False\nsubject=\'\'\nik=False\nuserdef=False\nwh=False\npassword=\'\'\npassend=False\nik2=False\nadd=False\nuser=open(\'data1\',\'w\', newline=\'\')\nfor i in dnr:\n    user.write(i)\n    if rnii:\n        wh=True\n        if i==\'[\':\n            bracket+=1\n        elif i==\']\':\n            bracket-=1\n        if add and subject==subjectfind and bracket==4 and brackethist==4:\n            subjectfind=None\n            user.write(str(markadd) + \',\')\n            add=False\n        if passend:\n            passend=False\n        if ik:\n            if ik2:\n                ik2=False\n                add=True\n            if bracket==3:\n                subject=\'\'\n                ik=False\n                rniiend=False\n        if rniiend:\n            ik=True\n            ik2=True\n            rniiend=False\n            brackethist=bracket\n            continue\n        if userdef:\n            userdef=False\n        if bracket==3 and brackethist==3 and i!=\"\'\":\n            if i ==\',\':\n                rniiend=True\n                continue\n            subject+=str(i)\n        elif bracket==5 and brackethist==5 and i!=\"\'\":\n            if i ==\',\':\n                passend=True\n                continue\n            password+=str(i)\n        brackethist=bracket\n    else:\n        if i==\'[\':\n            bracket+=1\n        elif i==\']\':\n            bracket-=1\n        if icoend:\n            if icocurrent!=\'\':\n                if int(icocurrent)==icofind:\n                    ico.append(icocurrent)\n                    rnii=True\n                    continue\n                icocurrent=\'\'\n                icoend=False\n        if bracket==2 and brackethist==2:\n            if i ==\',\':\n                icoend=True\n                userdef=True\n                continue\n            icocurrent+=i\n        brackethist=bracket\nif not wh:\n    user=open(sys.argv[2], \'x\')\nuser.close()\nx=open(\'DONE\',\'x\')\nx.close()')
    restartapp: str = str('import argparse, time, pygetwindow\nimport pyautogui as pg\nUNSPECIFIED = object()\nparser = argparse.ArgumentParser()\nparser.add_argument(\'-al\',\'--autol\', choices=[], default=UNSPECIFIED, nargs=\'?\')\nargs = parser.parse_args()\nwindow = pygetwindow.getWindowsWithTitle(\'ZnámE\')[0]\nwindow.activate()\nif args.autol == None:\n    time.sleep(1)\n    pg.write("login\\n")\n    time.sleep(1)\n    pg.write("y\\n")')
    gameapp: str = str('from game_assets_offline import game\ngame()')

    if __name__ == '__main__':
        logger.stay('codeapp')
        logger.stay('decodeapp')
        logger.stay('findapp')
        logger.stay('passwordapp')
        logger.stay('addapp')
        logger.stay('restartapp')
        logger.stay('gameapp')
        logger.prev('')
        if args.log is None:
            from essentials.system_info import get_log_info
            get_log_info(codeapp, decodeapp, findapp, passwordapp, addapp, restartapp, updateapp)
        logger.stay(printnlog('DONE', toprint=False))
        logger.next(printnlog('Defining functions', toprint=False))

    def delcache(name: str, hist: str) -> None:
        """
        The delcache function deletes the cache file if it is empty.

        :param name: Name the file that is used to store the time
        :param hist: Check if the history file has changed
        :return: The value of the timer
        """
        global timer
        time_got: int = int(config['basic info']['inactivelimit'])
        timer = time_got
        filesize: int = os.path.getsize(hist)
        sizehist: int = filesize
        while True:
            try:
                for i in os.listdir():
                    if i == "END":
                        raise Exception
                if timer <= 0:
                    os.remove(name)
                    open("INACTIVE", 'x')
                    os.system('cls')
                    pg.write('\n')
                    playhtml(args, config, 'apphtml\\inactive')
                    break
                if filesize != sizehist:
                    timer = time_got
                    sizehist: int = filesize
                else:
                    sizehist: int = filesize
                    filesize: int = os.path.getsize(hist)
                    sleep(1)
                    timer -= 1
            except Exception:
                pass

    if __name__ == '__main__':
        logger.stay(printnlog('Function: delcache', toprint=False))

    global progress_bar_check
    progress_bar_check = 0

    cachename = 'data.xp2'

    def inactive() -> bool:
        """
        The inactive function is used to check if the INACTIVE file exists in the current directory. If it does, then it will remove the password file and return True. Otherwise, it returns False.

        :return: True if the inactive file is found in the current directory
        """
        global passwordp
        leave: bool = False
        for i in os.listdir():
            if i == 'INACTIVE':
                leave = True
                remove(passwordp[1])
                break
        if leave:
            sleep(0.05)
            return True
        else: return False

    if __name__ == '__main__':
        logger.stay(printnlog('Function: inactive', toprint=False))

    def progress_bar(name: str, number: int) -> None:
        """
        The progress_bar function is a function that takes in two parameters: name and number.
        The progress_bar function will print out the name of the task being executed, and then display a progress bar for how 
        far along it is to completion. The progress bar will be displayed as 100% if number = 1,000,000 or more.

        :param name: Give the progress bar a name
        :param number: Determine the number of iterations
        :return: The progress bar
        """
        global progress_bar_check
        progress_bar_check = 0
        progress_bar_check_old: int = 0
        end: bool = False
        for i in tqdm(range(0, number), desc=name + ' '):
            if end: break
            while True:
                if progress_bar_check >= 100:
                    end: bool = True
                    break
                if progress_bar_check == progress_bar_check_old: continue
                elif progress_bar_check != progress_bar_check_old:
                    progress_bar_check_old: int = progress_bar_check
                    break

    if __name__ == '__main__':
        logger.stay(printnlog('Function: progress_bar', toprint=False))

    def add(name1, ico: int, subject: str, mark: str) -> tuple[str, None]:
        """
        The add function adds a new subject to the database.
        It takes 4 arguments: name, ico, subject and mark.
        The name argument is the name of the school or college that you want to add as a string.
        The ico argument is an integer representing your school's ICO number (the first 6 digits of your student ID).
        The subject argument is a string containing what you want to be written in the &quot;predmet&quot; column in our database (e.g.: &quot;Matematika&quot;). The mark argument should be an integer between 1 and 5 inclusive.

        :param name: Name the file
        :param ico: Check if the student already exists in the database
        :param subject: Specify the subject of the student
        :param mark: Specify the mark of the student
        :return: The tuple (data, none)
        """
        global progress_bar_check
        decodename: str = str(datetime.now().strftime("%H-%M-%S"))
        decodename: str = 'add'
        crdecode = open(decodename + ".py", "w")
        crdecode.write(addapp)
        crdecode.close()
        subprocess.check_output('start ' + decodename + '.py ' + str(name1) +
                                ' ' + str(ico) + ' ' + str(subject) + ' ' + str(mark), shell=True)
        tqdm.write('Adding ...', end='\r')
        wait_for_file('DONE')
        tqdm.write('Adding Complete')
        os.remove(decodename + '.py')
        os.remove(name1)
        os.remove('DONE')
        progress_bar_check += 1
        name: tuple[str, None] = ('data1', None)
        return name

    if __name__ == '__main__':
        logger.stay(printnlog('Function: add', toprint=False))

    def decode(name: str, password, mode: int = 0) -> str:  # type: ignore
        """
        The decode function takes two arguments, name and password. If the name argument is not provided it will default to None.
        If the password argument is not provided it will default to None as well. The function then creates a file with the current time in its name and writes a python script into that file which decrypts all files in this directory (except for itself) using pyAesCrypt library with given password or generated one if none was given.

        :param name: Specify the name of the file to be decoded
        :param password: Encrypt the file with a password
        :param mode=0: Encode the file, mode=0 is used to decode the file
        :return: The value of the name variable, if it is not none
        """
        global progress_bar_check
        decodename: str = str(datetime.now().strftime("%H-%M-%S"))
        decodename: str = 'decode'
        decodename2: str = 'False'
        if password: decodename2: str = name
        if name: decodename1: str = decodename
        elif isinstance(name, str): decodename1: str = name
        else: decodename1: str = "None"
        crdecode = open(decodename + ".py", "w")
        crdecode.write(decodeapp)
        crdecode.close()
        if mode == 1: subprocess.check_output(
                'start ' + decodename + '.py ' + str(name) + ' ' + str(password), shell=True)
        elif mode == 0: subprocess.check_output(
                'start ' + decodename + '.py ' + str(decodename1) + ' ' + str(decodename2), shell=True)
        tqdm.write('Encrypting ...', end='\r')
        wait_for_file('DONE')
        tqdm.write('Encrypting Complete')
        os.remove(decodename + '.py')
        os.remove('DONE')
        if mode == 1:
            file = open('1', 'r')
            fileline: str = str(file.readlines())
            fileline: str = fileline[2:len(fileline)-2]
            file.close()
            os.remove('1')
            return fileline
        progress_bar_check += 1
        return decodename1

    if __name__ == '__main__':
        logger.stay(printnlog('Function: decode', toprint=False))

    def password(name: str) -> list[str]:
        """
        Create a password file for the current session.
        @param name - the name of the file to be created.
        """
        global progress_bar_check
        passwordname: str = str(datetime.now().strftime("%H-%M-%S"))
        passwordnameL: str = 'pasword'
        crfind = open(passwordname + ".py", "w")
        crfind.write(passwordapp)
        crfind.close()
        tqdm.write('Controling ...', end='\r')
        subprocess.check_output(
            'start ' + passwordname + '.py ' + str(name), shell=True)
        wait_for_file('DONE')
        os.remove(passwordname + '.py')
        password: str = ''
        for i in open('DONE', 'r').read():
            password += str(i)
        tqdm.write('Controling Complete')
        os.remove('DONE')
        progress_bar_check += 1
        return [password, name]

    if __name__ == '__main__':
        logger.stay(printnlog('Function: password', toprint=False))

    def find(name: str) -> list:  # type: ignore
        """
        The find function is used to find the password of a user. It takes in two arguments, 
        the first being the name of the file that contains all usernames and passwords, and 
        the second being a string containing what you are looking for. The function then creates 
        a new file with an extension .py which it runs through cmd to find your password.

        :param name: Find the name of the file that is being searched for
        :return: The name of the file that was found
        """
        global progress_bar_check
        findname: str = str(datetime.now().strftime("%H-%M-%S"))
        findname: str = 'find'
        crfind = open(findname + ".py", "w")
        crfind.write(findapp)
        crfind.close()
        tqdm.write('Finding ...', end='\r')
        subprocess.check_output(
            'start ' + findname + '.py ' + str(name) + ' ' + str(loginvstupuser), shell=True)
        wait_for_file('DONE')
        os.remove(findname + '.py')
        os.remove(name)
        os.remove('DONE')
        test = open(loginvstupuser, 'r')
        end: bool = False
        pocitadlo: int = 0
        for i in test.read(): pocitadlo += 1
        if 0 <= pocitadlo <= 5:
            test.close()
            tqdm.write('Finding ERROR')
            end: bool = True
        if end: return [loginvstupuser, end]
        test.close()
        tqdm.write('Finding Complete')
        progress_bar_check += 1
        return [loginvstupuser, end]

    if __name__ == '__main__':
        logger.stay(printnlog('Function: find', toprint=False))

    def code(name: str, new: str, mode: int = 0) -> list[str]:
        """
        The code function is used to encrypt files.
        It takes two arguments: name, new.
        name is the file that will be encrypted.
        new is the password for encryption.

        :param name: str: Get the name of the file to be encrypted
        :param new: str: Save the password for encryption
        :param mode: int: Determine the mode of operation
        :return: The name and new value of the file
        """
        global progress_bar_check
        codename = str(datetime.now().strftime("%H-%M-%S"))
        codename = 'code'
        crcode = open(codename + ".py", "w")
        crcode.write(codeapp)
        crcode.close()
        tqdm.write('Coding ...', end='\r')
        if mode == 1:
            file = open('1', 'w')
            file.write(str(name) + ' = ' + str(new))
            file.close()
            subprocess.check_output('start ' + codename + '.py 1', shell=True)
        if mode == 0: subprocess.check_output(
                'start ' + codename + '.py ' + str(name[0]), shell=True)
        wait_for_file('DONE')
        tqdm.write('Coding Complete')
        os.remove(codename + '.py')
        if mode == 0 and new == 'justcode': pass
        elif mode == 0 and new:
            os.remove(loginvstupuser + 'crypted')
            shutil.move(loginvstupuser + 'cryptedcrypted',
                        loginvstupuser + 'crypted')
        elif mode == 0: os.remove(loginvstupuser)
        progress_bar_check += 1
        os.remove('DONE')
        if mode == 1:
            file = open('1crypted', 'r')
            savelog: list[str] = file.readlines()
            file.close()
            os.remove('1')
            os.remove('1crypted')
            return savelog
        return [name[1], new]

    if __name__ == '__main__':
        logger.stay(printnlog('Function: code', toprint=False))

    def add_marks(linenumber, historyname, neko, waifu):
        subject: str = input(str(linenumber) + ' Subject > ')
        historyfile = open(historyname, 'a')
        historyfile.write('[' + str(linenumber) + ', ' + subject + ']\n')
        subject.lower()
        historyfile.close()
        historyfile = open(historyname, 'a')
        if subject == 'quit' or subject == 'back': return
        mark: str = input(str(linenumber) + ' Mark > ')
        historyfile.write(
            '[' + str(linenumber) + ', ' + (mark) + ']\n')
        mark.lower()
        historyfile.close()
        historyfile = open(historyname, 'a')
        if subject == 'quit' or mark == 'quit':
            exit: bool = True
            return
        if subject == 'back' or mark == 'back': return
        Thread(target=progress_bar, args=(
            'Checking', 3,), daemon=True).start()
        code(add(decode(True, False), loginvstupuser,
                    subject, mark), 'justcode')
        cv2.destroyAllWindows()
        getImg('assets/banner.png', 'banner', 0, 0,
                screensize[0], int((round((322/1736)*screensize[0], 0))))
        if neko or waifu:
            pg.keyDown('alt')
            pg.press('tab')
            pg.keyUp('alt')
            pg.keyDown('alt')
            pg.press('tab')
            pg.keyUp('alt')
        os.mkdir("temp")
        shutil.move("data", 'temp/')
        os.rename('data1crypted', 'data')
        shutil.rmtree('temp')
        os.remove('data1')

    if __name__ == '__main__':
        logger.stay(printnlog('Function: add_marks', toprint=False))

    def show_marks(passwordp):
        with open(passwordp[1], 'r') as passwordfile:
            countersubject: int = 0
            counter: int = 6
            counterfirst: bool = True
            for i in passwordfile.read():
                if counter != 0:
                    counter -= 1
                    continue
                try:
                    if i == '\n':
                        typewriter('\n', end="")
                        continue
                    int(i)
                    if counterfirst:
                        typewriter(i, end="")
                    else:
                        typewriter(','+i, end="")
                except Exception:
                    if countersubject > 2: countersubject: int = 0
                    counterfirst: bool = True
                    countersubject += 1
                    print(i, end="")
                    if countersubject > 2: typewriter(" | ", end="")

    if __name__ == '__main__':
        logger.stay(printnlog('Function: show_marks', toprint=False))

    from essentials.html import playhtml
    
    
    def spotMusicDow():
        """
        The spotMusicDow function is a function that downloads music from Spotify.
        It uses the spotdl module to download music from Spotify, and then adds it to the user's playlist.

        :return: A string
        """
        import downloadmusic  # type: ignore
        from essentials.app_alternations import installing_carousel
        typewriter('Starting web player', ttime=0.01)
        Thread(target=downloadmusic.spotdl_get).start()
        with open('SPOTDL_OUTPUT', 'w', encoding='utf-8') as file:
            subprocess.run(['python', '-m', 'spotdl', 'web'],
                           stdout=file, text=True)
        sleep(1)
        carousel = installing_carousel(
            '', comment='Waiting for synchronization')
        Thread(target=carousel.start()).start()
        while os.path.isfile('SPOTDL_QUEUE'): sleep(1)
        open('SPOTDL_QUIT', 'x')
        carousel.stop()
        music: list[str] = list(
            set(config['basic info']['musiclist'].split(',')[0:]))
        if music[0] == '':  music = []
        else:
            for i in music:
                if i == '':
                    music.remove('')
        musiclistnewstring: str = ''
        for i in range(len(music)): musiclistnewstring += str(music[i]) + ','
        try:
            for line, content in enumerate(open('MUSIC', 'r', encoding='utf-8').readlines()):
                musiclistnewstring += content + ','
        except Exception: pass
        remove('MUSIC')
        remove('SPOTDL_QUIT')
        remove('SPOTDL_OUTPUT')
        sleep(1)
        pg.write('music\n')
        return musiclistnewstring

    if __name__ == '__main__':
        logger.stay(printnlog('Function: spotMusicDow', toprint=False))

    def vlc_init():
        typewriter(printnlog('Initialization VLC\n', toprint=False))
        media_player = vlc.MediaPlayer()
        typewriter(printnlog('END\n', toprint=False))
        return media_player

    def intro():
        from essentials.system_operations import intro_video
        exit = False
        move('ZnámE', -10, -10, screensize[0], screensize[1])
        if args.test is not None:
                show_cmd()
        if args.restart is not None:
            media_player = vlc.MediaPlayer()
            media_player.set_fullscreen(True)
            media = vlc.Media("assets/transition.mp4")
            media_player.set_media(media)
            media_player.play()
        intro_video(args, media_player)
        return exit

    def was_updated():
        try:
            for root, dirs, files in os.walk('..\\'):
                for i in files:
                    if i == 'INACTIVE':
                        inactive1: bool = True
                        os.remove('INACTIVE')
                        sleep(0.25)
                        printnlog('You were inactive, you were logged out and the program restarted!!!\n')
            if args.update is None:
                sleep(0.25)
                printnlog('Program was updated!!!\n')
            return inactive1
        except Exception: pass

    def main() -> None:
        global config
        global loginvstupuser
        global historyfile
        global music
        try:
            """
            The main function. This is where the program starts. It is the first function called.
            """
            historyname: str = str(datetime.now().strftime("%H-%M-%S"))
            historyfile = open(historyname, 'w')
            if args.nointrof is None: historyfile.write('[*restarted]\n')
            global passwordp
            from essentials.file_operations import extract
            extract(args, datelog)
            media_player = vlc_init()
            from downloadmusic import DownloadMusic  # type: ignore
            print_module('DownloadMusic from downloadmusic')
            from media import PlayVideo, DownloadVideo, play_loop  # type: ignore
            from login import save_credentials  # type: ignore
            from essentials.writing import show_version
            from essentials.arguments import music2str
            
            musiclistnew: list = []
            for i in range(len(music)):
                music_name = music[i]
                music.remove(music_name)
                if not os.path.exists('assets/' + str(music_name) + '.mp3'):
                    musiclistnew.append(DownloadMusic(str(music_name)))
                else: musiclistnew.append(music_name)
            music = []
            config = music2str(musiclistnew)
            intro()
            inactive1: bool = False

            """
            If the INACTIVE file is present, delete it and print a message to the user indicating that they have been logged out.
            @param root - the root directory of the file system
            @param dirs - the directories in the root directory
            @param files - the files in the root directory
            @returns nothing
            """
            inactive1 = was_updated()
            logged: bool = False
            exit: bool = False
            tologin: bool = False
            restart: bool = False
            topassword: bool = False
            topasswordhelp: bool = False
            loggedhelp: bool = False
            firstlogin: bool = True
            vstup: str = ''
            loginvstupuser = ''
            logins: int = 0
            help: list[str] = ['help', 'pomoc', '-h', '-help', '?', '-?']
            advhelp: list[str] = ['advanced help',
                                  'ah', '-ah', '-advanced help']
            linenumber: int = 1  # type: ignore
            neko: bool = False
            waifu: bool = False
            waifuvid: bool = False
            musicplay: bool = False
            savefilemode: bool = False
            offline_game: bool = config['game settings']['offline_game']
            maxlogins: int = 1
            """
            If the user has not disabled the intro, play it. Otherwise, do nothing.
            @param None
            @return None
            """
            if not inactive1: playhtml(args, config, 'apphtml\\start', 1, 3,)
            exit: bool = getWindow(args)
            if args.nointro is None or config['basic info']['intro'] == False: pass
            else:
                window = pygetwindow.getWindowsWithTitle('frame2')[0]
                window.activate()
            getImg('assets/banner.png', 'banner', 0, 0,
                   screensize[0], int((round((322/1736)*screensize[0], 0))))
            move('ZnámE', 0, int((round((322/1736)*screensize[0], 0))-35), screensize[0], screensize[1]-int(
                (round((322/1736)*screensize[0], 0))))
            if args.test is not None:
                    show_cmd()
            pg.press('win')
            sleep(0.1)
            pg.press('win')
            os.system('cls')
            if args.music != 0:
                mixer.init()
                mixer.music.load(
                    'assets/' + musiclistnew[int(args.music)-1] + '.mp3')
                mixer.music.play()
            show_version(args)
            from completer import SimpleCompleter, completer  # type: ignore
            unlogged_completer = ['ffmpeg', 'animesearch', 'save', 'clear', 'cls', 'quit', 'quitneko', 'quitwaifu', 'quitmusic', 'login', 'delsavlog', 'waifu', 'neko', 'setup', 'settings', 'anotherwaifu', 'anotherneko',
                                  'music', 'game', 'offlinegame', 'motivational', 'history', 'help', 'pomoc', '-h', '-help', '?', '-?', 'advanced help', 'ah', '-ah', '-advanced help']
            logged_completer = ['ffmpeg', 'animesearch', 'save', 'clear', 'cls', 'quit', 'quitneko', 'quitwaifu', 'quitmusic', 'logout', 'delsavlog', 'waifu', 'neko', 'setup', 'settings', 'anotherwaifu', 'anotherneko',
                                'music', 'game', 'offlinegame', 'motivational', 'history', 'help', 'pomoc', '-h', '-help', '?', '-?', 'advanced help', 'ah', '-ah', '-advanced help']
            bq_completer = ['back', 'quit']
            if args.debug == None:
                unlogged_completer.extend(dir())
                logged_completer.extend(dir())
            while True:
                completer(unlogged_completer)
                internet_check(args)
                if not exit:
                    if logged:
                        completer(logged_completer)
                        if firstlogin:
                            logins += 1
                            firstlogin: bool = False
                            shutil.copy2('data', 'data_backup')
                            """
                            If the user wants to save their login credentials, save them to a file.
                            @param loginvstupuser - the username for the login credentials
                            @param password - the password for the login credentials
                            @param savefilemode - whether or not we are saving the file or not
                            """
                            linenumber = save_credentials(
                                args, loginvstupuser, passwordp, code, savefilemode, linenumber)
                        """
                        Prints the help menu for the program.
                        @param loggedhelp - whether or not the help menu has been printed already.
                        @param args - the arguments passed to the program.
                        """
                        if loggedhelp:
                            typewriter("'zz' to display marks\n'pz' to add marks")
                            loggedhelp: bool = False
                        vstup: str = input(str(linenumber) + ' > ')
                        if args.debug == None:
                            try: print(str(eval(vstup)))
                            except Exception: pass
                        linenumber += 1
                        historyfile.write(
                            '[' + str(linenumber) + ', ' + vstup + ']\n')
                        vstup.lower()
                        historyfile.close()
                        historyfile = open(historyname, 'a')
                        help: list[str] = ['help', 'pomoc',
                                           '-h', '-help', '?', '-?']
                        for i in range(len(help)):
                            if vstup == help[i]: loggedhelp: bool = True
                        if loggedhelp: continue
                        if vstup == 'delsavlog': uninstall()
                        if vstup == "zz": show_marks(passwordp=passwordp)
                        if vstup == "pz": add_marks(linenumber=linenumber, historyname=historyname, neko=neko, waifu=waifu)
                    if topassword:
                        completer(bq_completer)
                        if savefilemode:   # type: ignore
                            vstup: str = savefile[9:15]   # type: ignore
                            linenumber -= 1
                        else: vstup = input(str(linenumber) + ' Password > ')
                        linenumber += 1
                        historyfile.write(
                            '[' + str(linenumber) + ', ' + len(vstup)*'*' + ']\n')   # type: ignore
                        vstup.lower()
                        historyfile.close()
                        historyfile = open(historyname, 'a')
                        help: list[str] = ['help', 'pomoc',
                                           '-h', '-help', '?', '-?']
                        for i in range(len(help)):
                            if vstup == help[i]: topasswordhelp: bool = True
                        """
                        If the user has requested help, print the appropriate help message.
                        @param topasswordhelp - the boolean value for requesting help.
                        """
                        if topasswordhelp:
                            typewriter("6 numeric password\n 'back' for menu\n 'quit' for end")
                            topasswordhelp: bool = False
                            continue
                        """
                            this function is used to go back to the main menu if the user wants to change their password. 
                        """
                        if vstup == "back":
                            typewriter('Going back.')
                            topassword: bool = False
                            os.remove(loginvstupuser + 'crypted')
                            continue
                        """
                        If the user types quit , remove the encrypted file and exit the program.
                        @param vstup - the user input
                        @returns nothing
                        """
                        if vstup == "quit":
                            typewriter("Going back and ending program.")
                            sleep(0.5)
                            os.remove(loginvstupuser + 'crypted')
                            exit: bool = True
                        Thread(target=progress_bar, args=(
                                'Checking', 2,), daemon=True).start()
                        passwordp = password(
                            decode(loginvstupuser + 'crypted', True))
                        cv2.destroyAllWindows()
                        getWindow(args)
                        pg.press('win')
                        sleep(0.1)
                        pg.press('win')
                        getImg('assets/banner.png', 'banner', 0, 0,
                               screensize[0], int((round((322/1736)*screensize[0], 0))))
                        if neko or waifu:
                            pg.keyDown('alt')
                            pg.press('tab')
                            pg.keyUp('alt')
                            pg.keyDown('alt')
                            pg.press('tab')
                            pg.keyUp('alt')
                        sleep(0.1)
                        """
                        If the user is logged in, check if the password is correct. If it is, then the user is logged in.
                        @param vstup - the password input by the user           
                        """
                        if vstup == passwordp[0]:  # type: ignore
                            typewriter('You\'re logged\n')
                            os.rename(loginvstupuser +
                                      'crypted', loginvstupuser)
                            passwordfile = open(loginvstupuser, 'r')
                            passwordfile1 = open(loginvstupuser + "1", 'w')
                            counter: int = 0
                            for i in passwordfile.read():
                                passwordfile1.write(i)
                            passwordfile.close()
                            passwordfile1.close()
                            os.remove(loginvstupuser)
                            os.rename(loginvstupuser + '1', loginvstupuser)
                            topassword: bool = False
                            logged: bool = True
                            mixer.music.pause()
                            mixer.Channel(1).play(mixer.Sound(
                                'assets\\maxtac.mp3'), fade_ms=10)
                            sleep(2.5)
                            mixer.music.unpause()
                            if os.path.exists("restart.py"):
                                os.remove('restart.py')
                                cv2.destroyAllWindows()
                                getWindow(args)
                                pg.press('win')
                                sleep(0.1)
                                pg.press('win')
                                getImg('assets/banner.png', 'banner', 0, 0,
                                       screensize[0], int((round((322/1736)*screensize[0], 0))))
                                if neko or waifu:
                                    pg.keyDown('alt')
                                    pg.press('tab')
                                    pg.keyUp('alt')
                                    pg.keyDown('alt')
                                    pg.press('tab')
                                    pg.keyUp('alt')
                                typewriter("All is set!!!\nYou can use progam\n")
                            historyfile.write(
                                '[' + str(linenumber) + ', ' + '*logged]\n')
                            historyfile.close()
                            historyfile = open(historyname, 'a')
                            Thread(target=delcache, args=(
                                loginvstupuser, historyname,), daemon=True).start()
                            continue
                        """
                        If the password is incorrect, remove the encrypted password file and the password file itself.
                        @param vstup - the user input password
                        @param password - the password from the encrypted file
                        @param loginvstupuser - the user input username
                        @param topassword - the boolean value for if the password is correct
                        """
                        if vstup != passwordp[0]:  # type: ignore
                            topassword: bool = False
                            os.remove(loginvstupuser + 'crypted')
                            os.remove(passwordp[1])  # type: ignore
                            global progress_bar_check
                            sleep(0.1)
                            typewriter("WRONG PASSWORD")
                            os.remove('data')
                            shutil.copy('data_backup', 'data')
                    if args.neko is None:
                        sleep(1)
                        pg.write("nekon\n")
                    if args.waifu is None:
                        sleep(1)
                        pg.write("waifun\n")
                    if args.restart is None:
                        args.restart = UNSPECIFIED
                        if args.autologin == None:
                            pg.write('restarted\n')
                    if not tologin and not logged:
                        vstup: str = input(str(linenumber) + ' > ')
                        if args.debug == None:
                            try: print(str(eval(vstup)))
                            except Exception: pass
                        historyfile.write(
                            '[' + str(linenumber) + ', ' + vstup + ']\n')
                        vstup.lower()
                        historyfile.close()
                        historyfile = open(historyname, 'a')
                        linenumber += 1
                    inactivelogout: bool = inactive()
                    if vstup in ['settings', 'setup']:
                        import settings  # type: ignore
                        settings.main(logged=logged)
                        config = yaml.safe_load(open('config.yml', 'r'))
                    if vstup == 'restarted': subprocess.check_output('start restart.py --autol', shell=True)
                    if vstup == 'playvideo':
                        import playvideo  # type: ignore
                        playvideo.main()
                    if vstup == 'music':
                        mixer.init()
                        musicnone = False
                        if len(musiclistnew) == 0:
                            musicnone = True
                            typewriter('No audio is downloaded')
                            musicvstup: str = input(
                                '1) Download music\n2) Back\n> ')
                            if musicvstup == '1':
                                to_append = spotMusicDow().split(',')
                                for item in to_append:
                                    if item == '': continue
                                    musiclistnew.append(item)
                                remove('MUSIC')
                                continue
                            elif musicvstup == '2': continue
                        if not musicnone:
                            for i in range(0, len(musiclistnew)):
                                typewriter(str(i + 1) + ') ' + musiclistnew[i])
                            typewriter(str(i + 2) + ') Delete audio')
                            typewriter(str(i + 3) + ') Download music')
                            typewriter(str(i + 4) + ') Back')
                            while True:
                                try:
                                    musicvstup: int = int(input('> '))
                                    break
                                except ValueError: continue
                        if musicnone or musicvstup == i+3:
                            to_append = spotMusicDow().split(',')
                            for item in to_append: musiclistnew.append(item)
                            musiclistnewstring: str = ''
                            config = music2str(musiclistnew)
                            remove('MUSIC')
                        elif musicvstup == len(musiclistnew) + 1 and not musicnone:
                            typewriter('Vymaž audio')
                            for i in range(0, len(musiclistnew)):
                                typewriter(str(i + 1) + ') ' + musiclistnew[i])
                            while True:
                                try:
                                    musicvstup: int = int(input('> '))
                                    break
                                except ValueError: continue
                            mixer.music.stop()
                            mixer.music.unload()
                            os.remove(
                                'assets/' + musiclistnew[musicvstup-1] + '.mp3')
                            musiclistnew.remove(musiclistnew[musicvstup-1])
                            lenmusic = len(musiclistnew) + 1
                            intconfig = int(config['basic info']['musicnumber'])
                            while lenmusic < intconfig:
                                config = set_config('basic info', 'musicnumber',
                                           int(args.music)-1)
                                intconfig = int(config['basic info']['musicnumber'])
                                continue
                            musiclistnewstring: str = ''
                            config = music2str(musiclistnew)
                            pg.write('music\n')
                        if not musicnone:
                            if musicvstup == len(musiclistnew) + 3:  # back
                                continue
                            args.music = str(musicvstup)
                            try:
                                if musicvstup == len(music)+1: continue
                                mixer.music.load(
                                    'assets/' + musiclistnew[musicvstup-1] + '.mp3')
                            except IndexError: pass
                            try:
                                mixer.music.play()
                                musicplay: bool = True
                            except Exception: pass
                    if vstup == 'quitmusic':
                        try:
                            mixer.music.stop()
                            musicplay: bool = False
                        except Exception: pass
                    if vstup == 'save':
                        if waifu or neko or waifuvid:
                            imagetime: str = str(
                                datetime.now().strftime("%H-%M-%S"))
                            try:
                                os.mkdir('download/')
                                typewriter(
                                    'Making directory \'download\'', end='\r', ttime=0.01)
                            except Exception: pass
                            if neko:
                                typewriter(
                                    'Copying neko to download folder', end='\r', ttime=0.01)
                                shutil.copy(
                                    'assets/neko.png', 'download/neko-' + imagetime + '.png')
                            elif waifuvid:
                                typewriter(
                                    'Copying waifu video to download folder', end='\r', ttime=0.01)
                                shutil.copy(
                                    'assets/waifu.mp4', 'download/waifu-' + imagetime + '.mp4')
                            elif waifu:
                                typewriter(
                                    'Copying waifu to download folder', end='\r', ttime=0.01)
                                shutil.copy(
                                    'assets/waifu.png', 'download/waifu-' + imagetime + '.png')
                            typewriter(
                                'Done                                            ', ttime=0.01)
                        else: typewriter("You don't have image to save", ttime=0.01)
                    if vstup == 'offlinegame':
                        config = set_config('game settings', 'offline_game', True)
                        offline_game = True
                        shutil.copy('game_assets.py', 'game_assets_offline.py')
                        import game_assets  # type: ignore
                        game_assets.create_gamefiles()
                    if vstup == 'restart':
                        restart: bool = True
                        exit: bool = True
                        continue
                    if vstup == 'game':
                        if waifu or waifuvid or neko:
                            typewriter('First you need to quit neko or waifu')
                            continue
                        mixer.music.pause()
                        import game_assets  # type: ignore
                        print_module()
                        game_assets.game()
                        mixer.music.unpause()
                        os.system('title ZnámE')
                        os.system('cls')
                        show_version(args)
                    if vstup == 'motivational':
                        resp = requests.get(
                            "https://animechan.vercel.app/api/random")
                        data: dict[str, str] = resp.json()
                        anime: str = data["anime"]
                        character: str = data["character"]
                        quote: str = data["quote"]
                        sleep(1)
                        typewriter("Anime: " + anime + '\nCharacter: ' +
                                   character + "\nQuote: " + quote, ttime=0.01)
                    if vstup == 'anotherneko':
                        pg.write("quitneko\nneko\n")
                    if vstup[0:4] == 'neko':
                        if neko:
                            typewriter("Sorry you can't have two nekos", ttime=0.01)
                            continue
                        if waifu:
                            typewriter("Sorry you can't have neko if you have waifu", ttime=0.01)
                            continue
                        typewriter('WAIT', ttime=0.01)
                        if args.neko is not None:
                            if config['neko settings']['server'] == 'nekos.best':
                                typewriter('Getting image from nekos.best server', ttime=0.01)
                                resp = requests.get(
                                    "https://nekos.best/api/v2/neko")
                                data: dict[str, str] = resp.json()
                                res = requests.get(
                                    data["results"][0]["url"], stream=True)  # type: ignore
                            elif config['neko settings']['server'] == 'waifu.pics':
                                typewriter('Getting image from waifu.pics server', ttime=0.01)
                                resp = requests.get(
                                    "https://api.waifu.pics/sfw/neko")
                                data: dict[str, str] = resp.json()
                                res = requests.get(data["url"], stream=True)
                            elif config['neko settings']['server'] == 'kyoko':
                                typewriter('Getting image from kyoko server', ttime=0.01)
                                resp = requests.get(
                                    "https://kyoko.rei.my.id/api/sfw.php")
                                data: dict[str, str] = resp.json()
                                res = requests.get(
                                    data["apiResult"]["url"][0], stream=True)
                            elif config['neko settings']['server'] == 'nekos_api':
                                typewriter('Getting image from nekos_api server', ttime=0.01)
                                resp = requests.get(
                                    "https://nekos.nekidev.com/api/image/random?categories=catgirl")
                                data: dict[str, str] = resp.json()
                                res = requests.get(
                                    data["data"][0]["url"], stream=True)
                            else:
                                typewriter('No server provided', ttime=0.01)
                                continue
                            typewriter('Downloading image', ttime=0.01)
                            if res.status_code == 200:
                                if config['neko settings']['server'] == 'nekos.best':
                                    download(data["results"][0]
                                             ["url"], 'assets/neko.png')
                                elif config['neko settings']['server'] == 'waifu.pics':
                                    download(data['url'], 'assets/neko.png')
                                elif config['neko settings']['server'] == 'kyoko':
                                    download(data["apiResult"]
                                             ["url"][0], 'assets/neko.png')
                                elif config['neko settings']['server'] == 'nekos_api':
                                    download(data["data"][0]
                                             ["url"], 'assets/neko.png')
                        else: args.neko = object()
                        typewriter('Setting image          ',
                                   end='\r', ttime=0.01)
                        img = Image.open('assets/neko.png')
                        typewriter('Opening image          ',
                                   end='\r', ttime=0.01)
                        img.show()
                        sleep(0.1)
                        typewriter('DONE                          ', end='\r')
                        pg.keyDown('win')
                        typewriter('......', end='\r', ttime=0.01)
                        pg.press('right')
                        typewriter('.......', end='\r', ttime=0.01)
                        pg.keyUp('win')
                        sleep(0.1)
                        pg.press('esc')
                        sleep(0.1)
                        typewriter('Getting cli in foreground     ',
                                   end='\r', ttime=0.01)
                        if args.test is not None:
                            window = pygetwindow.getWindowsWithTitle('ZnámE')[
                                0]
                            window.activate()
                        mixer.Channel(0).play(mixer.Sound('assets/neko.mp3'))
                        typewriter('Playing sound                 ',
                                   end='\r', ttime=0.01)
                        sleep(0.5)
                        typewriter('DONE           ')
                        move("ZnámE", 0, int((round((322/1736)*screensize[0], 0))-35), int(screensize[0]/2), int(
                            (round((0.95-(0.31203703703703706))*screensize[1], 0))))  # 337/1080
                        neko = True
                    if vstup == 'quitneko':
                        if not neko:
                            typewriter(":( You can't have -1 neko", ttime=0.01)
                            continue
                        typewriter('Closing image', end='\r', ttime=0.01)
                        pg.keyDown('alt')
                        pg.press('tab')
                        pg.keyUp('alt')
                        pg.keyDown('alt')
                        pg.press('f4')
                        pg.keyUp('alt')
                        try: img.close()  # type: ignore
                        except UnboundLocalError: pass
                        typewriter('Done             ', end='\r', ttime=0.01)
                        sleep(0.1)
                        typewriter('Removeing image', end='\r', ttime=0.01)
                        os.remove('assets/neko.png')
                        typewriter('Resizing cli', end='\r', ttime=0.01)
                        move('ZnámE', 0, int((round((322/1736)*screensize[0], 0))-35), screensize[0], screensize[1]-int(
                            (round((322/1736)*screensize[0], 0))))
                        typewriter('Done             ', ttime=0.01)
                        neko = False
                    if vstup == 'anotherwaifu':
                        pg.write("quitwaifu\nwaifu\n")
                    if vstup[0:5] == 'waifu':
                        if waifu:
                            typewriter("Sorry you can't have two waifu", ttime=0.01)
                            continue
                        if neko:
                            typewriter("Sorry you can't have waifu and neko", ttime=0.01)
                            continue
                        typewriter('WAIT', ttime=0.01)
                        if args.waifu is not None:
                            typewriter('Getting image from waifu.pics server', ttime=0.01)
                            resp = requests.get(
                                "https://api.waifu.pics/" + config['waifu settings']['type'] + "/" + config['waifu settings']['category'])
                            data: dict[str, str] = resp.json()
                            img_data = requests.get(data["url"]).content
                            typewriter('Downloading image', ttime=0.01)
                            if data["url"].split('.')[-1] == 'gif':
                                res = requests.get(data["url"], stream=True)
                                if res.status_code == 200:
                                    download(data['url'], 'assets/waifu.gif')
                                clip = mp.VideoFileClip("assets/waifu.gif")
                                clip.write_videofile("assets/waifu.mp4")
                                sleep(0.5)
                                waifuvid: bool = True
                                media_player = play_loop()
                                sleep(1)
                            elif data["url"].split('.')[-1] != 'gif':
                                res = requests.get(data["url"], stream=True)
                                if res.status_code == 200:
                                    download(data['url'], 'assets/waifu.png')
                        elif args.waifuvid is None:
                            data: dict[str, str] = {
                                'url': 'https://api.waifu.pics/waifu.mp4'}
                            waifuvid: bool = True
                            media_player = play_loop()
                            args.waifu = UNSPECIFIED
                            sleep(1)
                        elif args.waifu is None:
                            args.waifu = UNSPECIFIED
                            data: dict[str, str] = {
                                'url': 'https://api.waifu.pics/waifu.png'}
                        typewriter('Setting image    ', end='\r', ttime=0.01)
                        if data["url"].split('.')[-1] != 'gif' and data["url"].split('.')[-1] != 'mp4':
                            img = Image.open('assets/waifu.png')
                            typewriter('Opening image   ',
                                       end='\r', ttime=0.01)
                            img.show()
                        elif data["url"].split('.')[-1] == 'gif' or data["url"].split('.')[-1] == 'mp4':
                            sleep(0.2)
                            typewriter('Getting video in foreground',
                                       end='\r', ttime=0.01)
                            window = pygetwindow.getWindowsWithTitle(
                                'VLC (Direct3D11 Output)')[0]
                            window.activate()
                            sleep(0.1)
                        sleep(0.1)
                        pg.keyDown('win')
                        typewriter('......                        ',
                                   end='\r', ttime=0.01)
                        pg.press('right')
                        typewriter('.......', end='\r', ttime=0.01)
                        pg.keyUp('win')
                        typewriter('........', end='\r', ttime=0.01)
                        pg.press('esc')
                        typewriter('Getting cli in foreground',
                                   end='\r', ttime=0.01)
                        if args.test is not None:
                            window = pygetwindow.getWindowsWithTitle('ZnámE')[
                                0]
                            window.activate()
                        sleep(0.5)
                        typewriter('..........                  ',
                                   end='\r', ttime=0.01)
                        sleep(0.25)
                        typewriter('.............', end='\r', ttime=0.01)
                        typewriter('DONE           ', ttime=0.01)
                        move("ZnámE", 0, int((round((322/1736)*screensize[0], 0))-35), int(screensize[0]/2), int(
                            (round((0.95-(0.31203703703703706))*screensize[1], 0))))  # 337/1080
                        waifu: bool = True
                    if vstup == 'quitwaifu':
                        if not waifu:
                            typewriter(":( You can't have -1 waifu", ttime=0.01)
                            continue
                        elif waifuvid:
                            typewriter('Stoping video', end='\r', ttime=0.01)
                            media_player.stop()  # type: ignore
                            waifuvid: bool = False
                            typewriter('Removing video   ',
                                       end='\r', ttime=0.01)
                            os.remove('assets/waifu.mp4')
                        else:
                            typewriter('Closing image', end='\r', ttime=0.01)
                            pg.keyDown('alt')
                            pg.press('tab')
                            pg.keyUp('alt')
                            pg.keyDown('alt')
                            pg.press('f4')
                            pg.keyUp('alt')
                            try: img.close()  # type: ignore
                            except UnboundLocalError: pass
                        typewriter('Resizing cli      ', end='\r', ttime=0.01)
                        move('ZnámE', 0, int((round((322/1736)*screensize[0], 0))-35), screensize[0], screensize[1]-int(
                            (round((322/1736)*screensize[0], 0))))
                        try:
                            typewriter('Removing image', end='\r', ttime=0.01)
                            os.remove('assets/waifu.png')
                        except Exception: pass
                        waifu: bool = False
                        typewriter('Done               ', ttime=0.01)
                    if vstup == 'animesearch':
                        import anime_search  # type: ignore
                        anime_search.main()
                    if vstup == 'delsavlog': uninstall()
                    """
                    Clear the screen.
                    @param vstup - the input from the user.
                    """
                    if vstup == 'clear' or vstup == 'cls':
                        os.system('cls')
                        show_version(args)
                    if inactivelogout:
                        restart: bool = True
                        exit: bool = True
                    """
                    If the user is logged in and the user types "logout" in the command line, log the user out.
                    @param logged - whether the user is logged in or not.
                    @param vstup - the user input.
                    @param restart - whether the user is restarting the program or not.
                    @param loginvstupuser - the file that contains the username of the logged in user.
                    @param password - the file that contains the password of the logged in user.
                    @param history - the file that contains the history of the user.
                    @param linenumber - the line number of the history file.
                    """
                    if logged and vstup == "logout" and not restart:
                        logged: bool = False
                        os.remove(loginvstupuser)
                        os.remove(passwordp[1])  # type: ignore
                        print("You\'re logged out")
                        historyfile.write(
                            '[' + str(linenumber) + ', ' + '*logout]\n')
                        historyfile.close()
                        historyfile = open(historyname, 'a')
                        mixer.music.pause()
                        mixer.Channel(1).play(mixer.Sound(
                            'assets\\horror.mp3'), fade_ms=10)
                        sleep(6)
                        mixer.music.unpause()
                        continue
                    """
                    If the user has logged in and is inactive for a long time, log them out.
                    @param logged - whether the user is logged in or not.
                    @param inactivelogout - whether the user is inactive or not.
                    @param restart - whether the user has restarted the program or not.
                    """
                    if logged and inactivelogout and restart:
                        logged: bool = False
                        print("You\'re logged out")
                        continue
                    """
                    If the user is not logged in, print an error message and continue.           
                    """
                    if not logged and vstup == "logout" or inactivelogout:
                        logged: bool = False
                        print("You\'re not logged in!!!")
                        continue
                    """
                    Check if the user wants to quit the program. If so, exit the program. Otherwise, continue.
                    @param vstup - the user input for quitting the program.
                    @returns True if the user wants to quit the program, False otherwise.
                    """
                    if vstup == 'quit' or vstup == 'koniec' or vstup == 'end':
                        exit: bool = True
                        continue
                    historyfile = open(historyname, 'a')
                    """
                    Print the help file for the advanced help menu.
                    @param vstup - the input from the user during the advanced help menu.
                    @param restart - whether the program is restarting.
                    """
                    if vstup != "" and not restart:
                        for i in range(len(advhelp)):
                            if vstup == advhelp[i]:
                                advhelpcont: bool = False
                                with open('Help.txt', 'r', encoding='UTF-8') as advhelpfile:
                                     print(advhelpfile.read())
                        for i in range(len(help)):
                            if vstup == help[i]:
                                print("'login' for login\n'logout' for logout\n'quit' or 'end' for end\n'delsavlog' to clear autologin\n\nFor more detailed help, type '-ah' or '-advanced help' or 'ah' or 'advanced help'\n'history' show your currently saved history\'waifu\' for waifu\n\'neko\' for neko\n\'motivational\' for motivational message\n\'game\' for game\n\'music\' for music\n\'quit* **\' to quit music use \'quitmusic\' if you want to quit waifu \'quitwaifu\' if you want to quit neko \'quitneko\'")
                                continue
                        """
                        Print the history of the user.
                        @param args - the command line arguments
                        """
                        if vstup == 'history':
                            historylist = config['user history']
                            for i in historylist:
                                print('Start time = ' + i[0] + ', End time = ' + i[1][0:26] + ', Input = ' + i[1][26:])
                            if len(historylist) == 0:
                                print('History is empty')
                        if vstup == 'login' and not logged or tologin and not logged:
                            completer(bq_completer)
                            loginvstupuserL: str = ''
                            tologin: bool = False
                            savefilemode: bool = False
                            """
                            If the user wants to login, check if the user wants to restart the program. If the user wants to restart the program,
                            set the restart flag to true. If the user does not want to restart the program, set the restart flag to false.
                            @param logins - the number of logins since the last restart.
                            @param args - the arguments from the command line.
                            @returns the restart flag and the exit flag.
                            """
                            if logins == maxlogins:
                                vstup = input("If you want to login you need to restart program (Y/n) > ")
                                vstup.lower()
                                if vstup == "n":
                                    continue
                                elif vstup == "y" or vstup == "":
                                    restart: bool = True
                                    exit: bool = True
                                    args.nointro = None
                                    continue
                            """
                            Check if the save file exists. If it does, ask the user if they want to auto-login.
                            @param savefile - the save file
                            @returns the save file mode
                            """
                            if os.path.isfile("C:/Users/" + os.getlogin() + "/AppData/Local/ZnámE/saved"):
                                loginvstupuser = ''
                                savefile = decode(
                                    '1', "C:/Users/" + os.getlogin() + "/AppData/Local/ZnámE/saved", mode=1)
                                loginvstupuser = input(
                                    str(linenumber) + " Do you want to auto-login? (Y/n) > ")
                                linenumber += 1
                                loginvstupuser.lower()
                                if loginvstupuser == "" or loginvstupuser == "y":
                                    savefilemode: bool = True
                            if savefilemode: loginvstupuser = savefile[0:6]   # type: ignore
                            else: loginvstupuser = input(
                                    str(linenumber) + " Login Number (PID) > ")
                            historyfile.write(
                                '[' + str(linenumber) + ', ' + loginvstupuser + "]\n")
                            historyfile.close()
                            historyfile = open(historyname, 'a')
                            linenumber += 1
                            tologinhelp: bool = False
                            if loginvstupuser == "back":
                                print('Going back.')
                                continue
                            """
                            If the user types quit or koniec, then go back to the main menu. Otherwise, continue.
                            @param loginvstupuser - the user's input for the login/signup menu
                            @returns the user's input for the login/signup menu
                            """
                            if loginvstupuser == "quit" or loginvstupuser == "koniec":
                                print("Going back and exiting the program.")
                                sleep(0.5)
                                exit: bool = True
                                continue
                            help: list[str] = ['help', 'pomoc',
                                               '-h', '-help', '?', '-?']
                            for i in range(len(help)):
                                if loginvstupuser == help[i]:
                                    tologinhelp: bool = True
                            if tologinhelp:
                                print("'back' for menu\n'quit' or 'end' for end")
                                tologin: bool = True
                                continue
                            elif not loginvstupuser.isnumeric():
                                print('The PID does not contain letters or characters!!!')
                                tologin: bool = True
                                continue
                            if len(str(loginvstupuser)) == 6:
                                exit: bool = False
                                Thread(target=progress_bar, args=(
                                    'Checking', 3,), daemon=True).start()
                                icofind = code(
                                    find(decode(True, False)), False)
                                cv2.destroyAllWindows()
                                getWindow(args)
                                pg.press('win')
                                sleep(0.1)
                                pg.press('win')
                                getImg('assets/banner.png', 'banner', 0, 0,
                                       screensize[0], int((round((322/1736)*screensize[0], 0))))
                                if neko or waifu:
                                    pg.keyDown('alt')
                                    pg.press('tab')
                                    pg.keyUp('alt')
                                    pg.keyDown('alt')
                                    pg.press('tab')
                                    pg.keyUp('alt')
                                if icofind[0]:
                                    logged: bool = False
                                    os.remove(loginvstupuser + 'crypted')
                                    progress_bar_check = 100
                                    sleep(0.1)
                                    print("WRONG PID!!!")
                                    tologin: bool = True
                                    continue
                                topassword: bool = True
                            else:
                                print('The PID should be 6 numbers long!!!')
                                tologin: bool = True
                        elif logged and vstup == 'login': print('You are already logged in!!!')
                elif vstup == 'quit' or vstup == 'koniec' or vstup == 'end' or exit:
                    from endscreen import not_restart, mixer_stop, not_offline_game  # type: ignore
                    from essentials.file_operations import file_to_datafolder, xp3_finalization, to_zip
                    if neko or waifu:
                        if not waifuvid:
                            pg.keyDown('alt')
                            pg.press('tab')
                            pg.keyUp('alt')
                            pg.keyDown('alt')
                            pg.press('f4')
                            pg.keyUp('alt')
                            try:
                                img.close()  # type: ignore
                            except UnboundLocalError:
                                pass
                        else:
                            media_player.stop()
                        move('ZnámE', 0, int((round((322/1736)*screensize[0], 0))-35), screensize[0], screensize[1]-int(
                            (round((322/1736)*screensize[0], 0))))
                    if not restart: 
                        shutil.copy('assets/end.mp4', 'end.mp4')
                        media_player = vlc.MediaPlayer()
                        media_player.set_fullscreen(True)
                        media = vlc.Media("end.mp4")
                        media_player.set_media(media)
                        media_player.play()
                        video_start = int(time.time())
                        try:
                            window = pygetwindow.getWindowsWithTitle(
                                'VLC (Direct3D11 output)')[0]
                            window.activate()
                            window.maximize()
                        except Exception:
                            pass
                    mixer_stop()
                    if not restart: not_restart()
                    if not offline_game: not_offline_game()
                    try:open('END', 'x')
                    except Exception:pass
                    if logged:
                        try:
                            sleep(0.25)
                            os.remove(loginvstupuser)
                            os.remove(passwordp[1])  # type: ignore
                        except Exception:pass
                        typewriter('\nYou are logged out\n')
                        historyfile.write(
                            '[' + str(linenumber) + ', ' + '*logout]\n')
                        historyfile.close()
                        historyfile = open(historyname, 'a')
                        loginvstupuser = ''
                        sleep(0.5)
                    historyfile.close()
                    logger.stay(
                        "DELETING UNNECESSARY FILES\nWriting history\n")
                    start = time.time()
                    sleep(0.25)
                    version = open('version', 'r')
                    versionlist: list[str] = version.readlines()[0].split('.')
                    version.close()
                    version = open('version', 'w')
                    version.write(versionlist[0] + '.' + versionlist[1] + '.' + versionlist[2] + '.' + str(
                                  datetime.today().strftime("%Y%m%d.%H%M%S")))
                    version.close()
                    historylist: list = []
                    try:
                        historyfile = open(historyname, 'r')
                        for i in historyfile.readlines(): historylist.append(i.strip('\n'))
                    except Exception:pass
                    musiclistnewstring: str = ''
                    config = music2str(musiclistnew)
                    config = set_config('user history', str(historyname), str(
                        datetime.today().strftime("%d-%m-%Y__time__%H-%M-%S")) + str(historylist))
                    logger.next(historyname + ' ' + str(
                        datetime.today().strftime("%d-%m-%Y__time__%H-%M-%S")) + str(historylist) + '\n')
                    historyfile.close()
                    remove(historyname)
                    logger.prev("Done\n")
                    playhtml(args, config, 'apphtml\\end', 1, 3)
                    remove('data_backup')
                    mkdir('datafolder')
                    try: shutil.move('data', 'datafolder/')
                    except Exception: sys.exit(0)
                    file_to_datafolder()
                    logger.stay("PACKING DATA\n")
                    xp3_finalization()
                    logger.stay("COMPLETE")
                    cv2.destroyAllWindows()
                    logger.stay("PACKING SECOND PART OF DATA")
                    to_zip(logger, cachename, start)
                    if restart: logger.stay('The program will restart automatically.')
                    elif not restart:
                        if args.endf is None: pass
                        else: logger.stay('The program will automatically shut down.')
                    count: int = 0
                    for root_dir, cur_dir, files in os.walk(r"C:/Users/" + os.getlogin() + r"/AppData/Local/ZnámE/backup/"):
                        count += len(files)
                    if not os.path.exists(r"C:/Users/" + os.getlogin() + r"/AppData/Local/ZnámE/backup/"):
                        os.makedirs(r"C:/Users/" + os.getlogin() +
                                    r"/AppData/Local/ZnámE/backup/")
                        shutil.copy('data.xp2', "C:/Users/" + os.getlogin() + r"/AppData/Local/ZnámE/backup/backup-" + str(
                            datetime.now().strftime("%y-%m-%d-%H-%M-%S")) + '.xp2')
                        x = open(r"C:/Users/" + os.getlogin() +
                                 r"/AppData/Local/ZnámE/backup/info.txt", 'w')
                        x.write(
                            'Rename \'xp2\' file to \'data.xp2\' and move it to your \'ZnámE\' directory')
                        x.close()
                    else:
                        if count >= 11:
                            for root_dir, cur_dir, files in os.walk(r"C:/Users/" + os.getlogin() + r"/AppData/Local/ZnámE/backup/"):
                                os.remove(r"C:/Users/" + os.getlogin() +
                                          r"/AppData/Local/ZnámE/backup/" + files[0])
                        shutil.copy('data.xp2', r"C:/Users/" + os.getlogin() + r"/AppData/Local/ZnámE/backup/backup-" + str(
                            datetime.now().strftime("%y-%m-%d-%H-%M-%S")) + '.xp2')
                    if args.endf is not None and not restart: sleep(2.5)
                    if not restart:
                        import keyboard
                        video_end = int(time.time())
                        while video_end - video_start < 27:
                            time.sleep(0.1)
                            video_end = int(time.time())
                            if keyboard.is_pressed('q'):
                                break
                        media_player.stop()
                        os.remove('end.mp4')
                    if restart:
                        crrestart = open("restart.py", "w", encoding='utf-8')
                        crrestart.write(restartapp)
                        crrestart.close()
                        os.remove('END')
                        remove('.env')
                        if not inactivelogout and os.path.isfile(r"C:/Users/" + os.getlogin() + r"/AppData/Local/ZnámE/saved"):
                            typewriter(
                                "!\n!!\n!!!\nWARNING\nWAIT UNTIL PROGRAM SAYS YOU CAN\n!!!\n!!\n!\n", ttime=0.01)
                            vstup = input("Do you understand (Y/n) > ")
                            vstup.lower()
                            if not vstup in ['', 'y']:
                                if os.path.isfile("restart.py"): os.remove("restart.py")
                                if neko or waifu or waifuvid:
                                    from essentials.file_operations import del_wn
                                    del_wn()
                                os.remove('crash_dump-' + datelog + '.txt')
                                return 0
                            elif vstup in ['', 'y']:
                                os.system('cls')
                                sys.stdout.flush()
                                if os.path.isfile("C:/Users/" + os.getlogin() + "/AppData/Local/ZnámE/saved"):
                                    sleep(0.5)
                                    if waifuvid: subprocess.check_output(
                                            'start edupage.py --restart --autologin --nointrof --waifu --waifuvid --music ' + str(args.music), shell=True)
                                    elif neko: subprocess.check_output(
                                            'start edupage.py --restart --autologin --nointrof --neko --music ' + str(args.music), shell=True)
                                    elif waifu: subprocess.check_output(
                                            'start edupage.py --restart --autologin --nointrof --waifu --music ' + str(args.music), shell=True)
                                    else: subprocess.check_output(
                                            'start edupage.py --restart --autologin --nointrof --music ' + str(args.music), shell=True)
                                    os.remove('crash_dump-' + datelog + '.txt')
                        else:
                            os.system('cls')
                            sys.stdout.flush()
                            if neko: subprocess.check_output(
                                    'start edupage.py --restart --nointrof --neko --music ' + str(args.music), shell=True)
                            elif waifu: subprocess.check_output(
                                    'start edupage.py --restart --nointrof --waifu --music ' + str(args.music), shell=True)
                            else: subprocess.check_output(
                                    'start edupage.py --restart --nointrof --music ' + str(args.music), shell=True)
                            os.remove('crash_dump-' + datelog + '.txt')
                            return 0
                    elif not restart:
                        remove('END')
                        remove('.env')
                        if args.endf is None:
                            input("'ENTER' TO END")
                        if os.path.exists('restart.py'): os.remove('restart.py')
                        os.remove('crash_dump-' + datelog + '.txt')
                        return 0
        except *Exception as e:
            printnlog('Writing an error to \'error.log\'!!!')
            for error in e.exceptions: printnlog(traceback.format_exc())
            line_numbers: list = []
            for error in range(0, len(e.exceptions)):
                if (line_number := sys.exc_info()[-2].exceptions[0 + error].__traceback__) is None:
                    line_number = sys.exc_info()[-2].__traceback__.tb_lineno
                    line_numbers.append(line_number)
                else:
                    line_number = line_number.tb_lineno
                    line_numbers.append(line_number)
            error_get(e, line_numbers)
            printnlog('End')
            input("Enter to quit")
            sys.exit(0)

    if __name__ == '__main__':
        logger.stay(printnlog('Function: main\n', toprint=False))
        logger.prev(printnlog('Done defining functions\n', toprint=False))
        if args.debug == None:
            with cProfile.Profile() as pr: main()
            stats = pstats.Stats(pr)
            stats.sort_stats(pstats.SortKey.TIME)
            stats.dump_stats(filename='PROFILING.prof')
        else: main()
    else:
        try: os.remove('crash_dump-' + datelog + '.txt')
        except FileNotFoundError: pass
except *Exception as e:
    import os
    import sys
    import traceback
    printnlog('Writing an error to \'error.log\'!!!')
    for error in e.exceptions: printnlog(traceback.format_exc())
    line_numbers: list = []
    for error in range(0, len(e.exceptions)):
        if (line_number := sys.exc_info()[-2].exceptions[0 + error].__traceback__) is None:
            line_number = sys.exc_info()[-2].__traceback__.tb_lineno
            line_numbers.append(line_number)
        else:
            line_number = line_number.tb_lineno
            line_numbers.append(line_number)
    error_get(e, line_numbers)
    printnlog('End')
    input("Enter to quit")
    sys.exit(0)
