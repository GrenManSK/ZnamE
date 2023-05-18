"""_summary_
Main program execution
"""
try:  # type: ignore
    import cProfile
    import pstats
    from datetime import datetime
    from time import sleep
    import sys
    import os
    import traceback

    quiet = True if '--quiet'in sys.argv[1:] or '-quiet' in sys.argv[1:] else False
    
    if os.path.isfile('INSTALL_RESTART'):
        sleep(1)
    try:
        import verbose
    except ModuleNotFoundError:
        print(
            f'Verbose not found\nUse this command to install it {sys.executable} -m' +
            ' pip install git+https://github.com/GrenManSK/verbose.git')
        input()
        sys.exit(1)
    try:
        from final import mathematical
        del mathematical
    except ModuleNotFoundError:
        print(
            f'final not found\nUse this command to install it {sys.executable} -m' +
            ' pip install git+https://github.com/GrenManSK/final.git')
        input()
        sys.exit(1)
    if not quiet:
        logger = verbose.get_logger()
    if quiet:
        logger = verbose.get_logger(quiet=True)
    datelog: str = datetime.now().strftime("%y-%m-%d-%H-%M-%S")
    with open('.env', 'w', encoding='utf-8') as dotenv:
        dotenv.write(f'DATELOG={datelog}\n')
        dotenv.write(f'QUIET={quiet}\n')
    from essentials.functions.writing import printnlog, typewriter, change_quiet
    from essentials.system.file_operations import mkdir, remove

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
        for module_number in range(len(modulenames) - moduleminus):
            modulenames1.remove(modulenames[module_number])
        for module in modulenames1:
            modulenames.append(module)
        if __name__ == '__main__':
            for module_number1 in modulenames1:
                logger.stay(printnlog(module_number1, toprint=False))
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
    if __name__ == '__main__':
        logger.stay(printnlog('DONE', toprint=False))
    from essentials.system.exceptions import configNoOption, error_get
    from essentials.system.system_info import get_line_number
    
    if __name__ == '__main__':
        logger.stay(printnlog('Reading config file (yml)', toprint=False))
        config = yaml.safe_load(open('config.yml', 'r', encoding='utf-8'))
        config['user history'] = {}
        line_number: int = get_line_number(-1)

    try:
        if __name__ == '__main__':
            from essentials.arguments import print_config
            print_config(logger, config)
    except AttributeError:
        printnlog("'config.ini' file is corrupt -> option missing")
        error_get(configNoOption(
            'Corruption of config file => option missing'), [line_number], fname='edupage.py')
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
        
        from essentials.system.system_info import get_screensize, system_info
        screensize, screensizepercentage = get_screensize()
        if config['basic info']['quiet']:
            change_quiet(True)
            logger = verbose.get_logger(quiet=True)
            quiet = True
        
        if args.update is None:
            try:
                os.remove('update.py')
            except FileNotFoundError:
                args.update = UNSPECIFIED
                error_get(ExceptionGroup('', [FileNotFoundError(
                    'update.py isn\'t present'), TypeError('NOT FATAL' +
                                                           ' ERROR')]), [get_line_number()], fname='edupage.py')

        logger.stay(printnlog('DONE', toprint=False))

        if args.configoptions is None:
            from essentials.arguments import write_config_options
            write_config_options(server)

    if __name__ == '__main__':
        from essentials.app_alternations import python_update, install_choco,\
                                                install_packages, update_app
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
    import vlc
    if __name__ == '__main__':
        print_module()
    import pygetwindow
    if __name__ == '__main__':
        print_module()
    import keyboard
    if __name__ == '__main__':
        print_module()
    from PIL import Image
    if __name__ == '__main__':
        print_module('Image from PIL')
    from pygame import mixer
    if __name__ == '__main__':
        print_module('mixer from pygame')
    import pygame
    if __name__ == '__main__':
        print_module()
    import logging
    if __name__ == '__main__':
        print_module()
    import moviepy.editor as mp
    if __name__ == '__main__':
        print_module('moviepy.editor')
        logger.prev(printnlog('DONE', toprint=False))
        os.system('color ' + str(config['basic info']['environmentA']
                                 ) + str(config['basic info']['environmentA']))
        os.system('Title ' + 'ZnámE')
        if not os.path.isfile("C:/Users/" + os.getlogin() + "/AppData/Local/ZnámE/info.txt"):
            system_info(logger, screensize)
        if not os.path.exists("C:/Users/" + os.getlogin() + "/AppData/Local/ZnámE/backup/"):
            logger.stay(printnlog('Creating backup...\b', toprint=False))
            os.makedirs("C:/Users/" + os.getlogin() +
                        "/AppData/Local/ZnámE/backup/")
            shutil.copy('data.xp2', "C:/Users/" + os.getlogin() +
                        "/AppData/Local/ZnámE/backup/backup-" +
                        str(datetime.now().strftime("%y-%m-%d-%H-%M-%S"))
                        + '.xp2')
            with open("C:/Users/" + os.getlogin() + "/AppData/Local/ZnámE/" +
                      "backup/info.txt", 'w', encoding='utf-8') as x:
                x.write(
                    'Rename \'xp2\' file to \'data.xp2\' and move' +
                    ' it to your \'ZnámE\' directory')
            logger.stay(printnlog('Done'))

        logger.stay(printnlog("Defining functions", toprint=False))

    LOG_FILENAME = 'completer.log'
    logging.basicConfig(filename=LOG_FILENAME,
                        level=logging.DEBUG,
                        format="%(asctime)s,%(msecs)03d %(levelname)-8s " +
                        "[%(filename)s:%(lineno)d] - %(message)s",
                        datefmt='%Y-%m-%d:%H:%M:%S')

    if __name__ == '__main__':
        if args.test is not None:
            logger.stay(
                printnlog('Checking for newer version of ZnámE', toprint=False))
            update_app(args, logger)

    from essentials.system.system_operations import getWindow, getImg, move, show_cmd, wait_for_file
    from essentials.data.app import updateapp, codeapp, decodeapp, findapp, passwordapp, addapp,\
                               gameapp, restartapp

    if __name__ == '__main__':
        logger.stay(printnlog('Function: move', toprint=False))
        logger.stay(printnlog('Function: getImg', toprint=False))
        logger.stay(printnlog('Function: getWindow', toprint=False))
        logger.next(printnlog('\nDefining apps', toprint=False))

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
            from essentials.system.system_info import get_log_info
            get_log_info()
        logger.stay(printnlog('DONE', toprint=False))
        logger.next(printnlog('Defining functions', toprint=False))

    def delcache(cache_name: str, hist: str) -> None:
        """
        The delcache function deletes the cache file if it is empty.

        :param cache_name: cache_Name the file that is used to store the time
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
                for end_file in os.listdir():
                    if end_file == "END":
                        raise SystemError
                if timer <= 0:
                    os.remove(cache_name)
                    open("INACTIVE", 'x', encoding='utf-8')
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
            except SystemError:
                break

    if __name__ == '__main__':
        logger.stay(printnlog('Function: delcache', toprint=False))

    PROGRESS_BAR_CHECK = 0

    CACHENAME = 'data.xp2'

    def inactive() -> bool:
        """
        The inactive function is used to check if the INACTIVE file exists in the
        current directory. If it does, then it will remove the password file and
        return True. Otherwise, it returns False.

        :return: True if the inactive file is found in the current directory
        """
        global passwordp
        leave: bool = False
        for in_file in os.listdir():
            if in_file == 'INACTIVE':
                leave = True
                remove(passwordp[1])
                break
        if leave:
            sleep(0.05)
            return True
        return False

    if __name__ == '__main__':
        logger.stay(printnlog('Function: inactive', toprint=False))

    def progress_bar(bar_name: str, number: int) -> None:
        """
        The progress_bar function is a function that takes in two parameters: bar_name and number.
        The progress_bar function will print out the bar_name of the task being executed,
        and then display a progress bar for how 
        far along it is to completion. The progress bar will be displayed as 100%
        if number = 1,000,000 or more.

        :param bar_name: Give the progress bar a bar_name
        :param number: Determine the number of iterations
        :return: The progress bar
        """
        global PROGRESS_BAR_CHECK
        PROGRESS_BAR_CHECK = 0
        progress_bar_check_old: int = 0
        end: bool = False
        for bar_temp in tqdm(range(0, number), desc=bar_name + ' '):
            if end:
                break
            while True:
                if PROGRESS_BAR_CHECK >= 100:
                    end: bool = True
                    break
                if PROGRESS_BAR_CHECK == progress_bar_check_old:
                    continue
                if PROGRESS_BAR_CHECK != progress_bar_check_old:
                    progress_bar_check_old: int = PROGRESS_BAR_CHECK
                    break

    if __name__ == '__main__':
        logger.stay(printnlog('Function: progress_bar', toprint=False))

    def add(name1, ico: int, subject: str, mark: str) -> tuple[str, None]:
        """
        The add function adds a new subject to the database.
        It takes 4 arguments: name, ico, subject and mark.
        The name argument is the name of the school or college that you want to add as a string.
        The ico argument is an integer representing your school's ICO number).
        The subject argument is a string containing what you want to be written in the
        &quot;predmet&quot; column in our database (e.g.: &quot;Matematika&quot;).
        The mark argument should be an integer between 1 and 5 inclusive.

        :param name1: Name the file
        :param ico: Check if the student already exists in the database
        :param subject: Specify the subject of the student
        :param mark: Specify the mark of the student
        :return: The tuple (data, none)
        """
        global PROGRESS_BAR_CHECK
        decodename: str = str(datetime.now().strftime("%H-%M-%S"))
        decodename: str = 'add'
        with open(decodename + ".py", "w", encoding='utf-8') as crdecode:
            crdecode.write(addapp)
        subprocess.check_output('start ' + decodename + '.py ' + str(name1) +
                                ' ' + str(ico) + ' ' + str(subject) + ' ' + str(mark), shell=True)
        tqdm.write('Adding ...', end='\r')
        wait_for_file('DONE')
        tqdm.write('Adding Complete')
        os.remove(decodename + '.py')
        os.remove(name1)
        os.remove('DONE')
        PROGRESS_BAR_CHECK += 1
        result: tuple[str, None] = ('data1', None)
        return result

    if __name__ == '__main__':
        logger.stay(printnlog('Function: add', toprint=False))

    def decode(_file: str, _password, mode: int = 0) -> str:  # type: ignore
        """
        The decode function takes two arguments, _file and _password. If the _file
        argument is not provided it will default to None.
        If the _password argument is not provided it will default to None as well.
        The function then creates a file with the current time in its _file and
        writes a python script into that file which decrypts all files in this 
        directory (except for itself) using pyAesCrypt library with given _password
        or generated one if none was given.

        :param _file: Specify the _file of the file to be decoded
        :param _password: Encrypt the file with a _password
        :param mode=0: Encode the file, mode=0 is used to decode the file
        :return: The value of the _file variable, if it is not none
        """
        global PROGRESS_BAR_CHECK
        decodename: str = str(datetime.now().strftime("%H-%M-%S"))
        decodename: str = 'decode'
        decodename2: str = 'False'
        if _password:
            decodename2: str = _file
        if _file:
            decodename1: str = decodename
        elif isinstance(_file, str):
            decodename1: str = _file
        else:
            decodename1: str = "None"
        with open(decodename + ".py", "w", encoding='utf-8') as crdecode:
            crdecode.write(decodeapp)
        if mode == 1:
            subprocess.check_output(
                'start ' + decodename + '.py ' + str(_file) + ' ' + str(_password), shell=True)
        elif mode == 0:
            subprocess.check_output(
                'start ' + decodename + '.py ' + str(decodename1)
                + ' ' + str(decodename2), shell=True)
        tqdm.write('Encrypting ...', end='\r')
        wait_for_file('DONE')
        tqdm.write('Encrypting Complete')
        os.remove(decodename + '.py')
        os.remove('DONE')
        if mode == 1:
            with open('1', 'r', encoding='utf-8') as file:
                fileline: str = str(file.readlines())
                fileline: str = fileline[2:len(fileline)-2]
            os.remove('1')
            return fileline
        PROGRESS_BAR_CHECK += 1
        return decodename1

    if __name__ == '__main__':
        logger.stay(printnlog('Function: decode', toprint=False))

    def password(file_name: str) -> list[str]:
        """
        Create a password file for the current session.
        @param file_name - the file_name of the file to be created.
        """
        global PROGRESS_BAR_CHECK
        passwordname: str = str(datetime.now().strftime("%H-%M-%S"))
        with open(passwordname + ".py", "w", encoding='utf-8') as crfind:
            crfind.write(passwordapp)
        tqdm.write('Controling ...', end='\r')
        subprocess.check_output(
            'start ' + passwordname + '.py ' + str(file_name), shell=True)
        wait_for_file('DONE')
        os.remove(passwordname + '.py')
        password_chars: str = ''
        for pass_chars in open('DONE', 'r', encoding='utf-8').read():
            password_chars += str(pass_chars)
        tqdm.write('Controling Complete')
        os.remove('DONE')
        PROGRESS_BAR_CHECK += 1
        return [password_chars, file_name]

    if __name__ == '__main__':
        logger.stay(printnlog('Function: password', toprint=False))

    def find(find_file: str) -> list:  # type: ignore
        """
        The find function is used to find the password of a user. It takes in two arguments, 
        the first being the find_file of the file that contains all usernames and passwords, and 
        the second being a string containing what you are looking for. The function then creates 
        a new file with an extension .py which it runs through cmd to find your password.

        :param find_file: Find the find_file of the file that is being searched for
        :return: The find_file of the file that was found
        """
        global PROGRESS_BAR_CHECK
        findname: str = str(datetime.now().strftime("%H-%M-%S"))
        findname: str = 'find'
        with open(findname + ".py", "w", encoding='utf-8') as crfind:
            crfind.write(findapp)
        tqdm.write('Finding ...', end='\r')
        subprocess.check_output(
            'start ' + findname + '.py ' + str(find_file) + ' ' + str(loginvstupuser), shell=True)
        wait_for_file('DONE')
        os.remove(findname + '.py')
        os.remove(find_file)
        os.remove('DONE')
        with open(loginvstupuser, 'r', encoding='utf-8') as test:
            end: bool = False
            pocitadlo: int = len(test.read())
            if 0 <= pocitadlo <= 5:
                tqdm.write('Finding ERROR')
                end: bool = True
        if end:
            return [loginvstupuser, end]
        tqdm.write('Finding Complete')
        PROGRESS_BAR_CHECK += 1
        return [loginvstupuser, end]

    if __name__ == '__main__':
        logger.stay(printnlog('Function: find', toprint=False))

    def code(code_name: str, new: str, mode: int = 0) -> list[str]:
        """
        The code function is used to encrypt files.
        It takes two arguments: code_name, new.
        code_name is the file that will be encrypted.
        new is the password for encryption.

        :param code_name: str: Get the code_name of the file to be encrypted
        :param new: str: Save the password for encryption
        :param mode: int: Determine the mode of operation
        :return: The code_name and new value of the file
        """
        global PROGRESS_BAR_CHECK
        codename = str(datetime.now().strftime("%H-%M-%S"))
        codename = 'code'
        with open(codename + ".py", "w", encoding='utf-8') as crcode:
            crcode.write(codeapp)
        tqdm.write('Coding ...', end='\r')
        if mode == 1:
            with open('1', 'w', encoding='utf-8') as file:
                file.write(str(code_name) + ' = ' + str(new))
            subprocess.check_output('start ' + codename + '.py 1', shell=True)
        if mode == 0:
            subprocess.check_output(
                'start ' + codename + '.py ' + str(code_name[0]), shell=True)
        wait_for_file('DONE')
        tqdm.write('Coding Complete')
        os.remove(codename + '.py')
        if mode == 0 and new == 'justcode':
            pass
        elif mode == 0 and new:
            os.remove(loginvstupuser + 'crypted')
            shutil.move(loginvstupuser + 'cryptedcrypted',
                        loginvstupuser + 'crypted')
        elif mode == 0:
            os.remove(loginvstupuser)
        PROGRESS_BAR_CHECK += 1
        os.remove('DONE')
        if mode == 1:
            with open('1crypted', 'r', encoding='utf-8') as file:
                savelog: list[str] = file.readlines()
            os.remove('1')
            os.remove('1crypted')
            return savelog
        return [code_name[1], new]

    if __name__ == '__main__':
        logger.stay(printnlog('Function: code', toprint=False))

    def add_marks(linenumber, historyname, neko, waifu):
        """
        The add_marks function is used to add marks to the user's account.
        It takes in three arguments: linenumber, historyname and neko.
        The linenumber argument is used for the line number of the mark being added.
        The historyname argument is used for the name of a file that stores all commands
        entered by a user during their session with this program (for debugging purposes).
        The neko argument determines whether or not Neko Mode should be enabled.
        
        :param linenumber: Keep track of the line number in the history file
        :param historyname: Store the history of the user's input
        :param neko: Determine whether the user wants to use a neko or not
        :param waifu: Determine if the user is using a waifu or not
        :return: Nothing
        """
        subject: str = input(str(linenumber) + ' Subject > ')
        with open(historyname, 'a', encoding='utf-8') as _historyfile:
            _historyfile.write('[' + str(linenumber) + ', ' + subject + ']\n')
        subject.lower()
        if subject in ['quit', 'back']:
            return
        mark: str = input(str(linenumber) + ' Mark > ')
        with open(historyname, 'a', encoding='utf-8') as _historyfile:
            _historyfile.write(
                '[' + str(linenumber) + ', ' + (mark) + ']\n')
        mark.lower()
        if subject == 'back' or mark == 'back':
            return
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

    def show_marks(pass_list):
        """
        The show_marks function is used to display the marks of a student.
            It takes in a list as an argument, which contains the name of the file and its path.
            The function then opens that file and reads it line by line, printing
            out each mark on a newline.
        
        :param pass_list: Get the password file
        :return: The marks of the student
        """
        with open(pass_list[1], 'r', encoding='utf-8') as passwordfile:
            countersubject: int = 0
            counter: int = 6
            counterfirst: bool = True
            for pass_char in passwordfile.read():
                if counter != 0:
                    counter -= 1
                    continue
                try:
                    if pass_char == '\n':
                        typewriter('\n', end="")
                        continue
                    int(pass_char)
                    if counterfirst:
                        typewriter(pass_char, end="")
                    else:
                        typewriter(','+pass_char, end="")
                except ValueError:
                    if countersubject > 2:
                        countersubject: int = 0
                    counterfirst: bool = True
                    countersubject += 1
                    print(pass_char, end="")
                    if countersubject > 2:
                        typewriter(" | ", end="")

    if __name__ == '__main__':
        logger.stay(printnlog('Function: show_marks', toprint=False))

    from essentials.functions.html import playhtml

    def spot_music_dow():
        """
        The spot_music_dow function is a function that downloads music from Spotify.
        It uses the spotdl module to download music from Spotify, and then adds
        it to the user's playlist.

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
        while os.path.isfile('SPOTDL_QUEUE'):
            sleep(1)
        open('SPOTDL_QUIT', 'x')
        carousel.stop()
        _music: list[str] = list(
            set(config['basic info']['musiclist'].split(',')[0:]))
        if _music[0] == '':
            _music = []
        else:
            for music_name in _music:
                if music_name == '':
                    _music.remove('')
        musiclistnewstring: str = ''
        for music_n in _music:
            musiclistnewstring += str(music_n) + ','
        try:
            for content in open('MUSIC', 'r', encoding='utf-8').readlines():
                musiclistnewstring += content + ','
        except Exception:
            pass
        remove('MUSIC')
        remove('SPOTDL_QUIT')
        remove('SPOTDL_OUTPUT')
        sleep(1)
        pg.write('music\n')
        return musiclistnewstring

    if __name__ == '__main__':
        logger.stay(printnlog('Function: spot_music_dow', toprint=False))

    def vlc_init():
        """
        The vlc_init function initializes the VLC media player.
            It returns a MediaPlayer object that can be used to play audio files.
    
        :return: A vlc
        """
        typewriter(printnlog('Initialization VLC\n', toprint=False))
        media_player = vlc.MediaPlayer()
        typewriter(printnlog('END\n', toprint=False))
        return media_player

    def intro():
        """
        The intro function is the first function that runs when the program starts.
        It displays a video and then returns to main()
        
        :return: The variable exit
        """
        from essentials.system.system_operations import intro_video
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

    def was_updated():
        """
        The was_updated function checks if the program was updated or not.
            If it was, then it will print a message to the log file and console.
            It also checks if you were inactive for too long, in which case it will 
            restart the program.
        
        :return: True if the program was updated
        """
        try:
            for root, dirs, files in os.walk('..\\'):
                for file in files:
                    if file == 'INACTIVE':
                        inactive1: bool = True
                        os.remove('INACTIVE')
                        sleep(0.25)
                        printnlog(
                            'You were inactive, you were logged out and the ' +
                            'program restarted!!!\n')
            if args.update is None:
                sleep(0.25)
                printnlog('Program was updated!!!\n')
            return inactive1
        except Exception:
            return False

    def main() -> None:
        global config
        global loginvstupuser
        global historyfile
        global music
        try:
            historyname: str = str(datetime.now().strftime("%H-%M-%S"))
            with open(historyname, 'w', encoding='utf-8') as historyfile:
                if args.nointrof is None:
                    historyfile.write('[*restarted]\n')
            global passwordp
            from essentials.system.file_operations import extract
            extract(args, datelog)
            media_player = vlc_init()
            from downloadmusic import DownloadMusic  # type: ignore
            print_module('DownloadMusic from downloadmusic')
            from media import play_loop  # type: ignore
            from login import save_credentials  # type: ignore
            from essentials.functions.writing import show_version
            from essentials.arguments import music2str
            from essentials.system.conda import env_menu
            from essentials.functions.textractor import run_textractor
            from essentials.data.translate import t_languages
            from essentials.functions.function import run_app

            musiclistnew: list = []
            for music_name in music:
                music.remove(music_name)
                if not os.path.exists('assets/' + str(music_name) + '.mp3'):
                    musiclistnew.append(DownloadMusic(str(music_name)))
                else:
                    musiclistnew.append(music_name)
            music = []
            config = music2str(musiclistnew)
            intro()
            inactive1 = was_updated()
            logged: bool = False
            _exit: bool = False
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
            translator: bool = False
            translator_language: None|str = None
            offline_game: bool = config['game settings']['offline_game']
            maxlogins: int = 1
            if not inactive1:
                playhtml(args, config, 'apphtml\\start', 1, 3,)
            _exit: bool = getWindow(args)
            if args.nointro is None or not config['basic info']['intro']:
                pass
            else:
                window = pygetwindow.getWindowsWithTitle('frame2')[0]
                window.activate()
            getImg('assets/banner.png', 'banner', 0, 0,
                   screensize[0], int((round((322/1736)*screensize[0], 0))))
            move('ZnámE', 0, int((round((322/1736)*screensize[0], 0))-35),
                 screensize[0], screensize[1]-int(
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
            from completer import completer  # type: ignore
            unlogged_completer = ['animesearch', 'save', 'clear', 'cls', 'quit','manga_translator',
                                  'quitneko', 'quitwaifu', 'quitmusic', 'login', 'delsavlog','playvideo',
                                  'waifu', 'neko', 'setup', 'settings', 'anotherwaifu','kayopy',
                                  'anotherneko', 'music', 'game', 'offlinegame', 'motivational',
                                  'history', 'help', 'pomoc', '-h', '-help', '?', '-?','cbzprintable',
                                  'advanced help', 'ah', '-ah', '-advanced help', 'voicevox', 'translate']
            logged_completer = ['animesearch', 'save', 'clear', 'cls', 'quit', 'quitneko','playvideo',
                                'quitwaifu', 'quitmusic', 'logout', 'delsavlog', 'waifu', 'neko',
                                'setup', 'settings', 'anotherwaifu', 'anotherneko', 'voicevox',
                                'music', 'game', 'offlinegame', 'motivational', 'history', 'help',
                                'pomoc', '-h', '-help', '?', '-?', 'advanced help', 'ah', '-ah',
                                '-advanced help','cbzprintable', 'kayopy', 'manga_translator', 'translate']
            bq_completer = ['back', 'quit']
            if args.debug is None:
                unlogged_completer.extend(dir())
                logged_completer.extend(dir())
            if args.translate is not UNSPECIFIED and config['basic info']['translate'] == '':
                run_textractor(args, args.translate, config['basic info']['translator'])
                translator = True
                translator_language = args.translate
                if args.waifu is not None or args.neko is not None:
                    os.system('cls')
                    show_version(args)
            elif config['basic info']['translate'] != '':
                run_textractor(args, config['basic info']['translate'], config['basic info']['translator'])
                translator = True
                translator_language = config['basic info']['translate']
                os.system('cls')
                show_version(args)
            while True:
                completer(unlogged_completer)
                internet_check(args)
                if not _exit:
                    if logged:
                        completer(logged_completer)
                        if firstlogin:
                            logins += 1
                            firstlogin: bool = False
                            shutil.copy2('data', 'data_backup')
                            linenumber = save_credentials(
                                args, loginvstupuser, passwordp, code, savefilemode, linenumber)
                        if loggedhelp:
                            typewriter(
                                "'zz' to display marks\n'pz' to add marks")
                            loggedhelp: bool = False
                        vstup: str = input(str(linenumber) + ' > ')
                        if args.debug is None:
                            try:
                                print(str(eval(vstup)))
                            except Exception:
                                pass
                        linenumber += 1
                        with open(historyname, 'a', encoding='utf-8') as historyfile:
                            historyfile.write(
                                '[' + str(linenumber) + ', ' + vstup + ']\n')
                        vstup.lower()
                        help: list[str] = ['help', 'pomoc',
                                           '-h', '-help', '?', '-?']
                        for help_name in help:
                            if vstup == help_name:
                                loggedhelp: bool = True
                        if loggedhelp:
                            continue
                        if vstup == 'delsavlog':
                            uninstall()
                        if vstup == "zz":
                            show_marks(passwordp)
                        if vstup == "pz":
                            add_marks(
                                linenumber=linenumber,
                                historyname=historyname,
                                neko=neko,
                                waifu=waifu)
                    if topassword:
                        completer(bq_completer)
                        if savefilemode:   # type: ignore
                            vstup: str = savefile[9:15]   # type: ignore
                            linenumber -= 1
                        else:
                            vstup = input(str(linenumber) + ' Password > ')
                        linenumber += 1
                        with open(historyname, 'a', encoding='utf-8') as historyfile:
                            historyfile.write(
                                '[' + str(linenumber) + ', ' + len(vstup)*'*'
                                + ']\n')   # type: ignore
                        vstup.lower()
                        help: list[str] = ['help', 'pomoc',
                                           '-h', '-help', '?', '-?']
                        for help_name in help:
                            if vstup == help_name:
                                topasswordhelp: bool = True
                        if topasswordhelp:
                            typewriter(
                                "6 numeric password\n 'back' for menu\n 'quit' for end")
                            topasswordhelp: bool = False
                            continue
                        if vstup == "back":
                            typewriter('Going back.')
                            topassword: bool = False
                            os.remove(loginvstupuser + 'crypted')
                            continue
                        if vstup == "quit":
                            typewriter("Going back and ending program.")
                            sleep(0.5)
                            os.remove(loginvstupuser + 'crypted')
                            _exit: bool = True
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
                        if vstup == passwordp[0]:  # type: ignore
                            typewriter('You\'re logged\n')
                            os.rename(loginvstupuser +
                                      'crypted', loginvstupuser)
                            with open(loginvstupuser, 'r', encoding='utf-8') as passwordfile:
                                with open(loginvstupuser + "1", 'w', encoding='utf-8') as file:
                                    for pass_char in passwordfile.read():
                                        file.write(pass_char)
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
                                typewriter(
                                    "All is set!!!\nYou can use progam\n")
                            with open(historyname, 'a', encoding='utf-8') as historyfile:
                                historyfile.write(
                                    '[' + str(linenumber) + ', *logged]\n')
                            Thread(target=delcache, args=(
                                loginvstupuser, historyname,), daemon=True).start()
                            continue
                        if vstup != passwordp[0]:  # type: ignore
                            topassword: bool = False
                            os.remove(loginvstupuser + 'crypted')
                            os.remove(passwordp[1])  # type: ignore
                            global PROGRESS_BAR_CHECK
                            sleep(0.1)
                            typewriter("WRONG PASSWORD")
                            os.remove('data')
                            shutil.copy('data_backup', 'data')
                    if args.neko is None and not neko:
                        sleep(1)
                        pg.write("nekon\n")
                        if args.translate is not UNSPECIFIED:
                            pg.write('cls\n')
                    if args.waifu is None and not waifu:
                        sleep(1)
                        pg.write("waifun\n")
                        if args.translate is not UNSPECIFIED:
                            pg.write('cls\n')
                    if args.restart is None:
                        args.restart = UNSPECIFIED
                        if args.autologin is None:
                            pg.write('restarted\ncls\n')
                    if not tologin and not logged:
                        vstup: str = input(str(linenumber) + ' > ')
                        if args.debug is None:
                            try:
                                print(str(eval(vstup)))
                            except Exception:
                                pass
                        with open(historyname, 'a', encoding='utf-8') as historyfile:
                            historyfile.write(
                                '[' + str(linenumber) + ', ' + vstup + ']\n')
                        vstup.lower()
                        linenumber += 1
                    inactivelogout: bool = inactive()
                    if vstup in ['settings', 'setup']:
                        import settings  # type: ignore
                        settings.main(logged=logged)
                        config = yaml.safe_load(open('config.yml', 'r', encoding='utf-8'))
                    if vstup == 'restarted':
                        subprocess.check_output(
                            'start restart.py --autol', shell=True)
                        continue
                    if vstup == 'manga_translator':
                        run_app('manga_image_translator')
                        continue
                    if vstup == 'cbzprintable':
                        run_app('cbz')
                        continue
                    if vstup == 'kayopy':
                        run_app('kayopy')
                        continue
                    if vstup == 'voicevox':
                        run_app('voicevox')    
                        continue
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
                                to_append = spot_music_dow().split(',')
                                for item in to_append:
                                    if item == '':
                                        continue
                                    musiclistnew.append(item)
                                remove('MUSIC')
                                continue
                            if musicvstup == '2':
                                continue
                        if not musicnone:
                            for times, music_name in range(0, len(musiclistnew)):
                                typewriter(str(times + 1) + ') ' + music_name)
                            typewriter(str(times + 2) + ') Delete audio')
                            typewriter(str(times + 3) + ') Download music')
                            typewriter(str(times + 4) + ') Back')
                            while True:
                                try:
                                    musicvstup: int = int(input('> '))
                                    break
                                except ValueError:
                                    continue
                        if musicnone or musicvstup == times+3:
                            to_append = spot_music_dow().split(',')
                            for item in to_append:
                                musiclistnew.append(item)
                            musiclistnewstring: str = ''
                            config = music2str(musiclistnew)
                            remove('MUSIC')
                        elif musicvstup == len(musiclistnew) + 1 and not musicnone:
                            typewriter('Vymaž audio')
                            for times, music_name in range(0, len(musiclistnew)):
                                typewriter(str(times + 1) + ') ' + music_name)
                            while True:
                                try:
                                    musicvstup: int = int(input('> '))
                                    break
                                except ValueError:
                                    continue
                            mixer.music.stop()
                            mixer.music.unload()
                            os.remove(
                                'assets/' + musiclistnew[musicvstup-1] + '.mp3')
                            musiclistnew.remove(musiclistnew[musicvstup-1])
                            lenmusic = len(musiclistnew) + 1
                            intconfig = int(
                                config['basic info']['musicnumber'])
                            while lenmusic < intconfig:
                                config = set_config('basic info', 'musicnumber',
                                                    int(args.music)-1)
                                intconfig = int(
                                    config['basic info']['musicnumber'])
                                continue
                            musiclistnewstring: str = ''
                            config = music2str(musiclistnew)
                            pg.write('music\n')
                        if not musicnone:
                            if musicvstup == len(musiclistnew) + 3:  # back
                                continue
                            args.music = str(musicvstup)
                            try:
                                if musicvstup == len(music)+1:
                                    continue
                                mixer.music.load(
                                    'assets/' + musiclistnew[musicvstup-1] + '.mp3')
                            except IndexError:
                                pass
                            try:
                                mixer.music.play()
                            except pygame.error:
                                pass
                            musicplay: bool = True
                    if vstup == 'quitmusic':
                        try:
                            mixer.music.stop()
                            musicplay: bool = False
                        except Exception:
                            pass
                    if vstup == 'translate':
                        if translator:
                            continue
                        completer(['quit'] + t_languages)
                        translator_vstup = input('Select language *must be in google translate (e.g. slovak)> ')
                        if translator_vstup == 'quit':
                            continue
                        run_textractor(args, translator_vstup, config['basic info']['translator'])
                        translator = True
                        translator_language = translator_vstup
                        if waifu or neko or waifuvid:
                            window = pygetwindow.getWindowsWithTitle('tmp')[0]
                            window.activate()
                            window = pygetwindow.getWindowsWithTitle('ZnámE')[0]
                            window.activate()
                        if logged:
                            completer(unlogged_completer)
                        else:
                            completer(logged_completer)
                    if vstup == 'save':
                        if waifu or neko or waifuvid:
                            imagetime: str = str(
                                datetime.now().strftime("%H-%M-%S"))
                            try:
                                os.mkdir('download/')
                                typewriter(
                                    'Making directory \'download\'', end='\r', ttime=0.01)
                            except FileExistsError:
                                pass
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
                        else:
                            typewriter(
                                "You don't have image to save", ttime=0.01)
                    if vstup == 'offlinegame':
                        config = set_config(
                            'game settings', 'offline_game', True)
                        offline_game = True
                        shutil.copy('game_assets.py', 'game_assets_offline.py')
                        import game_assets  # type: ignore
                        game_assets.create_gamefiles()
                    if vstup == 'restart':
                        restart: bool = True
                        _exit: bool = True
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
                            "https://animechan.vercel.app/api/random", timeout=5)
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
                            typewriter(
                                "Sorry you can't have two nekos", ttime=0.01)
                            continue
                        if waifu:
                            typewriter(
                                "Sorry you can't have neko if you have waifu", ttime=0.01)
                            continue
                        typewriter('WAIT', ttime=0.01)
                        if args.neko is not None:
                            if config['neko settings']['server'] == 'nekos.best':
                                typewriter(
                                    'Getting image from nekos.best server', ttime=0.01)
                                resp = requests.get(
                                    "https://nekos.best/api/v2/neko", timeout=5)
                                data: dict[str, str] = resp.json()
                                res = requests.get(
                                    data["results"][0]["url"], stream=True,\
                                        timeout=5)  # type: ignore
                            elif config['neko settings']['server'] == 'waifu.pics':
                                typewriter(
                                    'Getting image from waifu.pics server', ttime=0.01)
                                resp = requests.get(
                                    "https://api.waifu.pics/sfw/neko", timeout=5)
                                data: dict[str, str] = resp.json()
                                res = requests.get(data["url"], stream=True, timeout=5)
                            elif config['neko settings']['server'] == 'kyoko':
                                typewriter(
                                    'Getting image from kyoko server', ttime=0.01)
                                resp = requests.get(
                                    "https://kyoko.rei.my.id/api/sfw.php", timeout=5)
                                data: dict[str, str] = resp.json()
                                res = requests.get(
                                    data["apiResult"]["url"][0], stream=True, timeout=5)
                            elif config['neko settings']['server'] == 'nekos_api':
                                typewriter(
                                    'Getting image from nekos_api server', ttime=0.01)
                                resp = requests.get(
                                    "https://nekos.nekidev.com/api/image/random?categories=catgirl", 
                                    timeout=5)
                                data: dict[str, str] = resp.json()
                                res = requests.get(
                                    data["data"][0]["url"], stream=True, timeout=5)
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
                        else:
                            args.neko = object()
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
                        move("ZnámE", 0, int((round((322/1736)*screensize[0], 0))-35),
                             int(screensize[0]/2), int(
                            (round((0.95-(0.31203703703703706))*screensize[1], 0))))  # 337/1080
                        neko = True
                    if vstup == 'quitneko':
                        if not neko:
                            typewriter(":( You can't have -1 neko", ttime=0.01)
                            continue
                        typewriter('Closing image', end='\r', ttime=0.01)
                        window = pygetwindow.getWindowsWithTitle('tmp')[0]
                        window.activate()
                        pg.keyDown('alt')
                        pg.press('f4')
                        pg.keyUp('alt')
                        try:
                            img.close()  # type: ignore
                        except UnboundLocalError:
                            pass
                        typewriter('Done             ', end='\r', ttime=0.01)
                        sleep(0.1)
                        typewriter('Removeing image', end='\r', ttime=0.01)
                        os.remove('assets/neko.png')
                        typewriter('Resizing cli', end='\r', ttime=0.01)
                        move('ZnámE', 0, int((round((322/1736)*screensize[0], 0))-35),
                             screensize[0], screensize[1]-int(
                            (round((322/1736)*screensize[0], 0))))
                        typewriter('Done             ', ttime=0.01)
                        neko = False
                    if vstup == 'anotherwaifu':
                        pg.write("quitwaifu\nwaifu\n")
                    if vstup[0:5] == 'waifu':
                        if waifu:
                            typewriter(
                                "Sorry you can't have two waifu", ttime=0.01)
                            continue
                        if neko:
                            typewriter(
                                "Sorry you can't have waifu and neko", ttime=0.01)
                            continue
                        typewriter('WAIT', ttime=0.01)
                        if args.waifu is not None:
                            typewriter(
                                'Getting image from waifu.pics server', ttime=0.01)
                            resp = requests.get(
                                "https://api.waifu.pics/" +
                                config['waifu settings']['type']
                                + "/" + config['waifu settings']['category'], timeout=5)
                            data: dict[str, str] = resp.json()
                            typewriter('Downloading image', ttime=0.01)
                            if data["url"].split('.')[-1] == 'gif':
                                res = requests.get(data["url"], stream=True, timeout=5)
                                if res.status_code == 200:
                                    download(data['url'], 'assets/waifu.gif')
                                clip = mp.VideoFileClip("assets/waifu.gif")
                                clip.write_videofile("assets/waifu.mp4")
                                clip.close()
                                sleep(0.5)
                                waifuvid: bool = True
                                media_player = play_loop()
                                sleep(1)
                            elif data["url"].split('.')[-1] != 'gif':
                                res = requests.get(data["url"], stream=True, timeout=5)
                                if res.status_code == 200:
                                    download(data['url'], 'assets/waifu.png')
                        elif args.waifuvid is None:
                            data: dict[str, str] = {
                                'url': 'https://api.waifu.pics/waifu.mp4'}
                            waifuvid: bool = True
                            media_player = play_loop()
                            args.waifu = UNSPECIFIED
                            args.waifuvid = UNSPECIFIED
                            sleep(1)
                        elif args.waifu is None:
                            args.waifu = UNSPECIFIED
                            data: dict[str, str] = {
                                'url': 'https://api.waifu.pics/waifu.png'}
                        typewriter('Setting image    ', end='\r', ttime=0.01)
                        if data["url"].split('.')[-1] != 'gif' \
                                and data["url"].split('.')[-1] != 'mp4':
                            img = Image.open('assets/waifu.png')
                            typewriter('Opening image   ',
                                       end='\r', ttime=0.01)
                            img.show()
                        elif data["url"].split('.')[-1] == 'gif' \
                                or data["url"].split('.')[-1] == 'mp4':
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
                        move("ZnámE", 0, int((round((322/1736)*screensize[0], 0))-35),
                             int(screensize[0]/2), int(
                            (round((0.95-(0.31203703703703706))*screensize[1], 0))))  # 337/1080
                        waifu: bool = True
                    if vstup == 'quitwaifu':
                        if not waifu:
                            typewriter(
                                ":( You can't have -1 waifu", ttime=0.01)
                            continue
                        if waifuvid:
                            typewriter('Stoping video', end='\r', ttime=0.01)
                            media_player.stop()  # type: ignore
                            waifuvid: bool = False
                            typewriter('Removing video   ',
                                       end='\r', ttime=0.01)
                            os.remove('assets/waifu.mp4')
                        else:
                            if translator:
                                window = pygetwindow.getWindowsWithTitle('tmp')[0]
                                window.activate()
                            typewriter('Closing image', end='\r', ttime=0.01)
                            window = pygetwindow.getWindowsWithTitle('tmp')[0]
                            window.activate()
                            pg.keyDown('alt')
                            pg.press('f4')
                            pg.keyUp('alt')
                            try:
                                img.close()  # type: ignore
                            except UnboundLocalError:
                                pass
                        typewriter('Resizing cli      ', end='\r', ttime=0.01)
                        move('ZnámE', 0, int((round((322/1736)*screensize[0], 0))-35),
                             screensize[0], screensize[1]-int(
                            (round((322/1736)*screensize[0], 0))))
                        typewriter('Removing image', end='\r', ttime=0.01)
                        remove('assets/waifu.png')
                        waifu: bool = False
                        typewriter('Done               ', ttime=0.01)
                    if vstup == 'animesearch':
                        import anime_search  # type: ignore
                        anime_search.main()
                    if vstup == 'delsavlog':
                        uninstall()
                    if vstup in ['clear', 'cls']:
                        os.system('cls')
                        show_version(args)
                    if inactivelogout:
                        restart: bool = True
                        _exit: bool = True
                    if logged and vstup == "logout" and not restart:
                        logged: bool = False
                        os.remove(loginvstupuser)
                        os.remove(passwordp[1])  # type: ignore
                        print("You\'re logged out")
                        with open(historyname, 'a', encoding='utf-8') as historyfile:
                            historyfile.write(
                                '[' + str(linenumber) + ', *logout]\n')
                        mixer.music.pause()
                        mixer.Channel(1).play(mixer.Sound(
                            'assets\\horror.mp3'), fade_ms=10)
                        sleep(6)
                        mixer.music.unpause()
                        continue
                    if logged and inactivelogout and restart:
                        logged: bool = False
                        print("You\'re logged out")
                        continue
                    if not logged and vstup == "logout" or inactivelogout:
                        logged: bool = False
                        print("You\'re not logged in!!!")
                        continue
                    if vstup in ['quit', 'koniec', 'end']:
                        _exit: bool = True
                        continue
                    if vstup != "" and not restart:
                        for advhelp_name in advhelp:
                            if vstup == advhelp_name:
                                with open('Help.txt', 'r', encoding='UTF-8') as advhelpfile:
                                    print(advhelpfile.read())
                        for help_name in help:
                            if vstup == help_name:
                                print("'login' for login\n'logout' for logout\n'quit'" +
                                      " or 'end' for end\n'delsavlog' to clear autologin" +
                                      "\n\nFor more detailed help, type '-ah' or '-advanced" +
                                      " help' or 'ah' or 'advanced help'\n'history' show" +
                                      " your currently saved history\'waifu\' for waifu\n" +
                                      "\'neko\' for neko\n\'motivational\' for motivational" +
                                      " message\n\'game\' for game\n\'music\' for music\n\'" +
                                      "quit* **\' to quit music use \'quitmusic\' if you want" +
                                      " to quit waifu \'quitwaifu\' if you want to quit neko" +
                                      " \'quitneko\'")
                                continue
                        if vstup == 'history':
                            historylist = config['user history']
                            for history_temp in historylist:
                                print(
                                    'Start time = ' + history_temp[0] + ', End time = '
                                    + history_temp[1][0:26] + ', Input = ' + history_temp[1][26:])
                            if len(historylist) == 0:
                                print('History is empty')
                        if vstup == 'login' and not logged or tologin and not logged:
                            completer(bq_completer)
                            tologin: bool = False
                            savefilemode: bool = False
                            if logins == maxlogins:
                                vstup = input(
                                    "If you want to login you need to restart" +
                                    " program (Y/n) > ")
                                vstup.lower()
                                if vstup == "n":
                                    continue
                                if vstup in ["y", ""]:
                                    restart: bool = True
                                    _exit: bool = True
                                    args.nointro = None
                                    continue
                            if os.path.isfile("C:/Users/" + os.getlogin() +
                                              "/AppData/Local/ZnámE/saved"):
                                loginvstupuser = ''
                                savefile = decode(
                                    '1', "C:/Users/" + os.getlogin() +
                                    "/AppData/Local/ZnámE/saved", mode=1)
                                loginvstupuser = input(
                                    str(linenumber) + " Do you want to auto-login? (Y/n) > ")
                                linenumber += 1
                                loginvstupuser.lower()
                                if loginvstupuser in ["", "y"]:
                                    savefilemode: bool = True
                            if savefilemode:
                                loginvstupuser = savefile[0:6]   # type: ignore
                            else:
                                loginvstupuser = input(
                                    str(linenumber) + " Login Number (PID) > ")
                            with open(historyname, 'a', encoding='utf-8') as historyfile:
                                historyfile.write(
                                    '[' + str(linenumber) + ', ' + loginvstupuser + "]\n")
                            linenumber += 1
                            tologinhelp: bool = False
                            if loginvstupuser == "back":
                                print('Going back.')
                                continue
                            if loginvstupuser in ["quit","koniec"]:
                                print("Going back and exiting the program.")
                                sleep(0.5)
                                _exit: bool = True
                                continue
                            help: list[str] = ['help', 'pomoc',
                                               '-h', '-help', '?', '-?']
                            for help_name in help:
                                if loginvstupuser == help_name:
                                    tologinhelp: bool = True
                            if tologinhelp:
                                print("'back' for menu\n'quit' or 'end' for end")
                                tologin: bool = True
                                continue
                            if not loginvstupuser.isnumeric():
                                print(
                                    'The PID does not contain letters or characters!!!')
                                tologin: bool = True
                                continue
                            if len(str(loginvstupuser)) == 6:
                                _exit: bool = False
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
                                    PROGRESS_BAR_CHECK = 100
                                    sleep(0.1)
                                    print("WRONG PID!!!")
                                    tologin: bool = True
                                    continue
                                topassword: bool = True
                            else:
                                print('The PID should be 6 numbers long!!!')
                                tologin: bool = True
                        elif logged and vstup == 'login':
                            print('You are already logged in!!!')
                elif vstup == 'quit' or vstup == 'koniec' or vstup == 'end' or _exit:
                    from endscreen import not_restart, mixer_stop, not_offline_game  # type: ignore
                    from essentials.system.file_operations import file_to_datafolder, xp3_finalization,\
                                                                                        to_zip
                    if translator:
                        window = pygetwindow.getWindowsWithTitle('Textractor')[1]
                        window.activate()
                        pg.keyDown('alt')
                        pg.press('f4')
                        pg.keyUp('alt')
                    if neko or waifu:
                        if not waifuvid:
                            if translator:
                                window = pygetwindow.getWindowsWithTitle('tmp')[0]
                                window.activate()
                                window = pygetwindow.getWindowsWithTitle('ZnámE')[0]
                                window.activate()
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
                        move('ZnámE', 0, int((round((322/1736)*screensize[0], 0))-35),
                             screensize[0], screensize[1]-int(
                            (round((322/1736)*screensize[0], 0))))
                    if not restart:
                        def play_end():
                            shutil.copy('assets/green1.mp4', 'green1.mp4')
                            media_player1 = vlc.MediaPlayer()
                            media_player1.set_fullscreen(True)
                            media = vlc.Media("green1.mp4")
                            media_player1.set_media(media)
                            media_player1.play()
                            sleep(4.5)
                            if args.test is not None:
                                window = pygetwindow.getWindowsWithTitle('ZnámE')[0]
                                window.activate()
                                window.minimize()
                            while not os.path.exists('VIDEO_END'):
                                sleep(0.1)
                            os.remove('VIDEO_END')
                            media_player1.stop()
                            os.remove('green1.mp4')
                            
                        Thread(target=play_end, daemon=True).start()
                    mixer_stop()
                    if not restart:
                        not_restart()
                    if not offline_game:
                        not_offline_game()
                    try:
                        open('END', 'x', encoding='utf-8')
                    except FileExistsError:
                        pass
                    if logged:
                        try:
                            sleep(0.25)
                            os.remove(loginvstupuser)
                            os.remove(passwordp[1])  # type: ignore
                        except FileNotFoundError:
                            pass
                        typewriter('\nYou are logged out\n')
                        with open(historyname, 'a', encoding='utf-8') as historyfile:
                            historyfile.write(
                                '[' + str(linenumber) + ', ' + '*logout]\n')
                        loginvstupuser = ''
                        sleep(0.5)
                    logger.stay(
                        "DELETING UNNECESSARY FILES\nWriting history\n")
                    start = time.time()
                    sleep(0.25)
                    with open('version', 'r', encoding='utf-8') as version:
                        versionlist: list[str] = version.readlines()[
                            0].split('.')
                    with open('version', 'w', encoding='utf-8') as version:
                        version.write(versionlist[0] + '.' + versionlist[1]
                                      + '.' + versionlist[2] + '.' + str(
                            datetime.today().strftime("%Y%m%d.%H%M%S")))
                    historylist: list = []
                    try:
                        with open(historyname, 'r', encoding='utf-8') as historyfile:
                            for history_char in historyfile.readlines():
                                historylist.append(history_char.strip('\n'))
                    except Exception:
                        historyfile.close()
                    musiclistnewstring: str = ''
                    config = music2str(musiclistnew)
                    config = set_config('user history', str(historyname), str(
                        datetime.today().strftime("%d-%m-%Y__time__%H-%M-%S"))
                        + str(historylist))
                    logger.next(historyname + ' ' + str(
                        datetime.today().strftime("%d-%m-%Y__time__%H-%M-%S"))
                        + str(historylist) + '\n')
                    remove(historyname)
                    remove('decode')
                    logger.prev("Done\n")
                    playhtml(args, config, 'apphtml\\end', 1, 3)
                    remove('data_backup')
                    mkdir('datafolder')
                    try:
                        shutil.move('data', 'datafolder/')
                    except FileNotFoundError:
                        sys.exit(0)
                    file_to_datafolder()
                    logger.stay("PACKING DATA\n")
                    xp3_finalization()
                    logger.stay("COMPLETE")
                    cv2.destroyAllWindows()
                    logger.stay("PACKING SECOND PART OF DATA")
                    to_zip(logger, CACHENAME, start)
                    if not restart:
                        open('VIDEO_END', 'x')
                    if restart:
                        logger.stay('The program will restart automatically.')
                    elif not restart:
                        if args.endf is None:
                            pass
                        else:
                            logger.stay(
                                'The program will automatically shut down.')
                    count: int = 0
                    for root_dir, cur_dir, files in os.walk(r"C:/Users/" + os.getlogin()
                                                            + r"/AppData/Local/ZnámE/backup/"):
                        count += len(files)
                    if not os.path.exists(r"C:/Users/" + os.getlogin() +
                                          r"/AppData/Local/ZnámE/backup/"):
                        os.makedirs(r"C:/Users/" + os.getlogin() +
                                    r"/AppData/Local/ZnámE/backup/")
                        shutil.copy('data.xp2', "C:/Users/" + os.getlogin() +
                                    r"/AppData/Local/ZnámE/backup/backup-" + str(
                            datetime.now().strftime("%y-%m-%d-%H-%M-%S")) + '.xp2')
                        with open(r"C:/Users/" + os.getlogin() +
                                  r"/AppData/Local/ZnámE/backup/info.txt", 'w',
                                  encoding='utf-8') as info_file:
                            info_file.write(
                                'Rename \'xp2\' file to \'data.xp2\' and ' +
                                'move it to your \'ZnámE\' directory')
                    else:
                        if count >= 11:
                            for rdir, cdir, files in os.walk(r"C:/Users/" + os.getlogin()
                                                             + r"/AppData/Local/ZnámE/backup/"):
                                os.remove(r"C:/Users/" + os.getlogin() +
                                          r"/AppData/Local/ZnámE/backup/" + files[0])
                        shutil.copy('data.xp2', r"C:/Users/" + os.getlogin()
                                    + r"/AppData/Local/ZnámE/backup/backup-" + str(
                            datetime.now().strftime("%y-%m-%d-%H-%M-%S")) + '.xp2')
                    if args.endf is not None and not restart:
                        sleep(2.5)
                    if restart:
                        with open("restart.py", "w", encoding='utf-8') as crrestart:
                            crrestart.write(restartapp)
                        os.remove('END')
                        remove('.env')
                        if not inactivelogout and os.path.isfile(r"C:/Users/" + os.getlogin()
                                                                 + r"/AppData/Local/ZnámE/saved"):
                            typewriter(
                                "!\n!!\n!!!\nWARNING\nWAIT UNTIL PROGRAM SAYS " +
                                "YOU CAN\n!!!\n!!\n!\n", ttime=0.01)
                            vstup = input("Do you understand (Y/n) > ")
                            vstup.lower()
                            if not vstup in ['', 'y']:
                                if os.path.isfile("restart.py"):
                                    os.remove("restart.py")
                                if neko or waifu or waifuvid:
                                    from essentials.system.file_operations import del_wn
                                    del_wn()
                                remove('crash_dump-' + datelog + '.txt')
                                return 0
                            if vstup in ['', 'y']:
                                translator_restart = ''
                                if translator:
                                    translator_restart = f' --translate {translator_language} ' 
                                os.system('cls')
                                sys.stdout.flush()
                                if os.path.isfile("C:/Users/" + os.getlogin()
                                                  + "/AppData/Local/ZnámE/saved"):
                                    sleep(0.5)
                                    if waifuvid:
                                        subprocess.check_output(
                                            'start edupage.py --restart --autologin --nointrof'+ translator_restart +
                                            ' --waifu --waifuvid --music '
                                            + str(args.music), shell=True)
                                    elif neko:
                                        subprocess.check_output(
                                            'start edupage.py --restart --autologin --nointrof' + translator_restart +
                                            ' --neko --music '
                                            + str(args.music), shell=True)
                                    elif waifu:
                                        subprocess.check_output(
                                            'start edupage.py --restart --autologin --nointrof ' + translator_restart +
                                            '--waifu --music '
                                            + str(args.music), shell=True)
                                    else:
                                        subprocess.check_output(
                                            'start edupage.py --restart --autologin --nointrof' + translator_restart +
                                            ' --music ' + str(args.music), shell=True)
                                    remove('crash_dump-' + datelog + '.txt')
                                return 0
                        else:
                            os.system('cls')
                            sys.stdout.flush()
                            if neko:
                                subprocess.check_output(
                                    'start edupage.py --restart --nointrof --neko --music '
                                    + str(args.music), shell=True)
                            elif waifu:
                                subprocess.check_output(
                                    'start edupage.py --restart --nointrof --waifu --music '
                                    + str(args.music), shell=True)
                            else:
                                subprocess.check_output(
                                    'start edupage.py --restart --nointrof --music '
                                    + str(args.music), shell=True)
                            remove('crash_dump-' + datelog + '.txt')
                            return 0
                    elif not restart:
                        remove('END')
                        remove('.env')
                        if args.endf is None:
                            input("'ENTER' TO END")
                        if os.path.exists('restart.py'):
                            os.remove('restart.py')
                        remove('crash_dump-' + datelog + '.txt')
                        return 0
        except *Exception as returned_error:
            printnlog('Writing an error to \'error.log\'!!!')
            printnlog(traceback.format_exc())
            error_line_numbers: list = []
            for error in range(0, len(returned_error.exceptions)):
                if (error_line_number := sys.exc_info()[-2].exceptions[0 + error].__traceback__)\
                                                                                    is None:
                    error_line_number = sys.exc_info()[-2].__traceback__.tb_lineno
                    error_line_numbers.append(error_line_number)
                else:
                    error_line_number = error_line_number.tb_lineno
                    error_line_numbers.append(error_line_number)
            error_get(returned_error, error_line_numbers)
            printnlog('End')
            input("Enter to quit")
            sys.exit(0)

    if __name__ == '__main__':
        logger.stay(printnlog('Function: main\n', toprint=False))
        logger.prev(printnlog('Done defining functions\n', toprint=False))
        if args.debug is None:
            with cProfile.Profile() as pr:
                main()
            stats = pstats.Stats(pr)
            stats.sort_stats(pstats.SortKey.TIME)
            stats.dump_stats(filename='PROFILING.prof')
        else:
            main()
    else:
        try:
            remove('crash_dump-' + datelog + '.txt')
        except FileNotFoundError:
            pass
except *Exception as e:
    printnlog('Writing an error to \'error.log\'!!!')
    printnlog(traceback.format_exc())
    line_numbers: list = []
    for error in range(0, len(e.exceptions)):
        if (error_line_number := sys.exc_info()[-2].exceptions[0 + error].__traceback__) is None:
            error_line_number = sys.exc_info()[-2].__traceback__.tb_lineno
            line_numbers.append(error_line_number)
        else:
            error_line_number = error_line_number.tb_lineno
            line_numbers.append(line_number)
    error_get(e, line_numbers)
    printnlog('End')
    input("Enter to quit")
    sys.exit(0)
