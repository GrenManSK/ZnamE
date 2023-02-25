try:  # type: ignore
    import cProfile
    import pstats
    import verbose
    from datetime import datetime
    from time import sleep
    import sys
    import os
    if os.path.isfile('INSTALL_RESTART'):
        sleep(1)
    logger = verbose.verbose()
    datelog: str = datetime.now().strftime("%y-%m-%d-%H-%M-%S")

    def printnlog(msg: str, end: str = '\n', toprint: bool = True) -> str:
        """
        It takes a message and an end character, and prints the message to the console and to a file

        :param msg: The message to be printed and logged
        :param end: The character that will be printed at the end of the message, defaults to \n
        (optional)
        """
        with open(f"crash_dump-{datelog}.txt", 'a', encoding='utf-8') as crashfile:
            if toprint:
                print(str(msg), end=str(end))
            crashfile.write(str(msg) + str(end))
        return msg

    def to_info(msg: str, end: str = '\n', file: str = 'info.txt', mode: str = 'a', toprint: bool = True) -> str:
        """
        The to_info function takes a message and an end character, and prints the message to the console 
        and to a file. It is used for logging purposes.

        :param msg: Print the message to the console and log file
        :param end: Determine what character will be printed at the end of the message
        :param file: Specify the file to which the message will be printed
        :param mode: Determine whether the file is being read or written to
        :return: The message that was passed to it
        """
        with open(f"crash_dump-{datelog}.txt", 'a', encoding='utf-8') as crashfile:
            if toprint:
                print(str(msg), end=str(end))
            crashfile.write(str(msg) + str(end))
            crashfile.close()
            crashfile1 = open(
                f"C:/Users/{os.getlogin()}/AppData/Local/ZnámE/{file}", mode, encoding='utf-8')
            crashfile1.write(str(msg) + str(end))
        return msg

    def log(msg: str, end: str = '\n') -> str:
        """
        It opens a file, writes a message to it, and closes the file

        :param msg: The message to be logged
        :param end: The character that will be used to end the line, defaults to \n (optional)
        """
        with open(f"crash_dump-{datelog}.txt", 'a', encoding='utf-8') as crashfile:
            crashfile.write(str(msg) + str(end))
        return msg

    def typewriter(word: str, ttime: float = 0.001, end: str = '\n') -> None:
        """
        The typewriter function prints each character in a word with a delay.
        The default time between characters is 0.01 seconds, but the user can specify
        their own value for the time.

        :param word: Pass the word that needs to be printed
        :param time=0.01: Set the time between each character printed out
        :param end='\n': Print the output on a new line
        :return: A string
        """
        for char in word:
            sleep(ttime)
            sys.stdout.write(char)
            sys.stdout.flush()
        sys.stdout.write(end)

    if __name__ == '__main__':
        logger.stay(printnlog('Importing initial libraries', toprint=False))

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
    import argparse
    print_module()
    import pkg_resources
    print_module()
    import subprocess
    print_module()
    import configparser
    print_module()
    import inspect
    print_module()
    from time import sleep
    print_module()
    import traceback
    print_module()
    if __name__ == '__main__':
        logger.stay(printnlog('DONE', toprint=False))


    class configNoOption(Exception):
        pass

    class argLanguageError(Exception):
        pass

    class argIntroError(Exception):
        pass

    class argInactiveLimitError(Exception):
        pass

    class argMusicListError(Exception):
        pass
    
    class argMusicError(Exception):
        pass

    class argEnviromentError(Exception):
        pass

    class argWaifuError(Exception):
        pass

    class argNekoError(Exception):
        pass

    class argGameError(Exception):
        pass

    allerror = []
    for name, obj in inspect.getmembers(sys.modules[__name__]):
        if inspect.isclass(obj):
            allerror.append(obj.__name__)

    if __name__ == '__main__':
        for i in range(0, len(allerror)-1):
            printnlog(allerror[i], end=', ')
        printnlog(allerror[len(allerror)-1])

    def error_log(line: int) -> None:
        """
        It writes the error to a file and prints it to the console

        :param line: The line number of the error
        """
        with open('error.log', 'a', encoding='utf-8') as errorfile:
            exc_type, exc_obj, exc_tb = sys.exc_info()
            exc_type = exc_type.__qualname__
            fname: str = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
            errorfile.write(
                f'Type of error: {str(exc_type)} | Comment: {str(exc_obj)} | In file: {str(fname)} | On line: {str(line)}\n')
        printnlog(
            f'Type of error: {str(exc_type)} | Comment: {str(exc_obj)} | In file: {str(fname)} | On line: {str(line)}')

    def error_get(errors, line: int) -> None:
        """
        It takes an error, a line number, and a comment, and then raises the error with the comment, and
        then logs the error with the line number

        :param error: The error to raise
        :param line: The line of code that the error is on
        :param comment: The comment that will be displayed in the error log
        """
        for times ,error in enumerate(errors.exceptions):
            try:
                raise eval(error.with_traceback.__qualname__.split('.')[0])(error)
            except eval(error.with_traceback.__qualname__.split('.')[0]):
                if len(line) == 1 and times > 0:
                    error_log(line[0])
                else:
                    error_log(line[times])

    def get_line_number(goback: int = 0, relative_frame: int = 1) -> int:
        """
        It returns the line number of the code that called it

        :param relative_frame: The number of frames to go back, defaults to 1 (optional)
        :param msg: The message to print
        :return: The line number of the code that called the function.
        """
        return int(inspect.stack()[relative_frame][0].f_lineno)-int(goback)

    if __name__ == '__main__':
        logger.stay(printnlog('Reading config file (ini)', toprint=False))
    line_number: int = get_line_number(1)
    try:
        config = configparser.RawConfigParser()
        line_number: int = get_line_number(-1)
        config.read('config.ini')
    except configparser.DuplicateSectionError:
        printnlog("'config.ini' file is corrupt -> Duplicate section")
        error_get(configparser.DuplicateSectionError('Corruption of config file => Duplicate section'), [line_number])
        input("Press 'enter' to quit")
        quit()
    except configparser.DuplicateOptionError:
        printnlog("'config.ini' file is corrupt -> Duplicate option")
        error_get(configparser.DuplicateSectionError('Corruption of config file => Duplicate option'), [line_number])
        input("Press 'enter' to quit")
        quit()
    except configparser.NoSectionError:
        printnlog("'config.ini' file is corrupt -> No section")
        error_get(configparser.DuplicateSectionError('Corruption of config file => No section'), [line_number])
        input("Press 'enter' to quit")
        quit()
    try:
        if __name__ == '__main__':
            logger.next((printnlog('Language: ' +
                                 config.get('basic info', 'lang').split(' ')[0], toprint=False)))
            logger.stay((printnlog('Enviroment: ' + config.get('basic info',
                                                             'enviroment').split(' ')[0], toprint=False)))
            logger.stay((printnlog('Intro: ' + config.get('basic info',
                       'intro').split(' ')[0], toprint=False)), toprint=False)
            logger.stay((printnlog('Inactivelimit: ' + config.get('basic info',
                                                                'inactivelimit').split(' ')[0], toprint=False)))
            logger.stay((printnlog('Music: ' + config.get('basic info',
                       'music').split(' ')[0], toprint=False)), toprint=False)
            logger.stay((printnlog('Musiclist: ' + str(config.get('basic info',
                                                                'musiclist').split(',')[0:]), toprint=False)))
            logger.stay(printnlog('User history: ' + str(config.items('user history')), toprint=False))
            logger.prev('')
    except configparser.NoOptionError:
        printnlog("'config.ini' file is corrupt -> option missing")
        error_get(configNoOption('Corruption of config file => option missing'), [line_number],)
        input("Press 'enter' to quit")
        quit()
        printnlog('\nDone\n')
    

    def set_config(section: str, name: str, info: str) -> None:
        """
        The set_config function writes a new config.ini file with the specified section, name, and info.

        :param section: Define the section of the config
        :param name: Set the name of the configuration file
        :param info: Set the value of the name parameter in the section specified
        :return: None
        """
        os.remove('config.ini')
        with open('config.ini', 'a') as configfile:
            config.set(section, name, str(info))
            config.write(configfile)

    if __name__ == '__main__':
        global parser
        parser = argparse.ArgumentParser()
        UNSPECIFIED = object()
        language: list[str] = ['SK', 'EN', 'JP']
        music: list[str] = list(
            set(config.get('basic info', 'musiclist').split(',')[0:]))
        if music[0] == '':
            music = []
        else:
            for i in music:
                if i == '':
                    music.remove('')
        musicchoices: list[str] = ['0']
        for i in range(1, len(music) + 1):
            musicchoices.append(str(i))
        parser.add_argument('-lang', '--language', choices=language,
                            help='Language selection', nargs='?')
        parser.add_argument('-v', '--version', choices=[],
                            help='Show version of this program', default=UNSPECIFIED, nargs='?')
        parser.add_argument('-ef', '--endf', choices=[],
                            help='Will not automatically end program', default=UNSPECIFIED, nargs='?')
        parser.add_argument('-ni', '--nointro', choices=[],
                            help='Will not start intro', default=UNSPECIFIED, nargs='?')
        parser.add_argument('-nif', '--nointrof', choices=[],
                            help='Will not start intro', default=UNSPECIFIED, nargs='?')
        parser.add_argument('-neko', '--neko', choices=[],
                            help='Easter egg was activated', default=UNSPECIFIED, nargs='?')
        parser.add_argument('-waifu', '--waifu', choices=[],
                            help='Easter egg was activated', default=UNSPECIFIED, nargs='?')
        parser.add_argument('-waifuvid', '--waifuvid', choices=[],
                            help='Easter egg was activated', default=UNSPECIFIED, nargs='?')
        parser.add_argument('-co', '--configoptions', choices=[],
                            help='Make a file with all config options', default=UNSPECIFIED, nargs='?')
        parser.add_argument('-music', '--music', choices=musicchoices,
                            help='Starts music; you can select from: ' + str(i for i in music), default='0', nargs='?')
        parser.add_argument('-inactive', '--inactive', choices=[],
                            help='!!! Argument for program to use', default=UNSPECIFIED, nargs='?')
        parser.add_argument('-restart', '--restart', choices=[],
                            help='!!! Argument for program to use', default=UNSPECIFIED, nargs='?')
        parser.add_argument('-log', '--log', choices=[],
                            help='!!! Argument for program to use', default=UNSPECIFIED, nargs='?')
        parser.add_argument('-update', '--update', choices=[],
                            help='!!! Argument for program to use (this command won\'t update this program, it does it automatically)', default=UNSPECIFIED, nargs='?')
        parser.add_argument('-autol', '--autologin', choices=[],
                            help='!!! Argument for program to use', default=UNSPECIFIED, nargs='?')
        parser.add_argument('-test', '--test', choices=[],
                            help='!!! Argument for program to use', default=UNSPECIFIED, nargs='?')
        parser.add_argument('-debug', '--debug', choices=[],
                            help='Debugging enabled', default=UNSPECIFIED, nargs='?')
        args = parser.parse_args()
        hexnumber: list[str] = ['0', '1', '2', '3', '4', '5', '6',
                                '7', '8', '9', 'a', 'b', 'c', 'd', 'e', 'f']
        logger.stay(printnlog("Checking argument correctness", toprint=False))
        if not config.get('basic info', 'enviroment').split(' ')[0][0] in hexnumber:
            error_get(ExceptionGroup('',[argEnviromentError('Wrong choice \'basic info\' => enviroment first character'), ValueError(f'Not allowed character | Allowed: {hexnumber}')]), [get_line_number()])
            quit()
        elif not config.get('basic info', 'enviroment').split(' ')[0][1] in hexnumber:
            error_get(ExceptionGroup('',[argEnviromentError('Wrong choice \'basic info\' => enviroment second character'), ValueError(f'Not allowed character | Allowed: {hexnumber}')]), [get_line_number()])
            quit()
        else:
            printnlog('basic info => enviroment')
        try:
            int(config.get('basic info', 'inactivelimit').split(' ')[0])
            printnlog('basic info => inactivelimit')
        except ValueError:
            error_get(ExceptionGroup('',[argInactiveLimitError('Wrong choice in \'basic info\' => inactivelimit'), ValueError('take only numbers')]), [get_line_number()])
            quit()
        if not config.get('basic info', 'intro').split(' ')[0] in ['True', 'False']:
            error_get(ExceptionGroup('',[argIntroError('Wrong choice in \'basic info\' => intro'), ValueError('Only \'True\' or \'False\'')]), [get_line_number()])
            quit()
        else:
            printnlog('basic info => intro')
        if config.get('basic info', 'music').split(' ')[0] == 'enable':
            args.music = config.get('basic info', 'musicnumber').split(' ')[0]
            printnlog('basic info => music')
        elif config.get('basic info', 'music').split(' ')[0] == 'disable':
            printnlog('basic info => music')
            pass
        else:
            error_get(ExceptionGroup('',[argMusicError('Wrong choice in \'basic info\' => music'), ValueError('Only \'enable\' or \'disable\'')]), [get_line_number()])
            quit()
        if not config.get('waifu settings', 'type').split(' ')[0] in ['sfw', 'nsfw']:
            error_get(ExceptionGroup('',[argWaifuError('Wrong choice in \'waifu settings\' => type'), ValueError('Only \'sfw\' or \'nsfw\'')]), [get_line_number()])
            quit()
        else:
            printnlog('waifu settings => type')
        if config.get('waifu settings', 'type').split(' ')[0] == 'sfw':
            category: list[str] = ["waifu", "neko", "shinobu", "megumin", "bully", "cuddle", "cry", "hug", "awoo", "kiss", "lick", "pat", "smug", "bonk", "yeet",
                                   "blush", "smile", "wave", "highfive", "handhold", "nom", "bite", "glomp", "slap", "kill", "kick", "happy", "wink", "poke", "dance", "cringe"]
            if not config.get('waifu settings', 'category').split(' ')[0] in category:
                error_get(ExceptionGroup('',[argWaifuError('Wrong choice in \'waifu settings\' => category'), ValueError('Use \'waifu\' and see option in setup function')]), [get_line_number()])
                quit()
            else:
                printnlog('waifu settings => category')
        elif config.get('waifu settings', 'type').split(' ')[0] == 'nsfw':
            category: list[str] = ['waifu', 'neko', 'trap', 'blowjob']
            if not config.get('waifu settings', 'category').split(' ')[0] in category:
                error_get(ExceptionGroup('',[argWaifuError('Wrong choice in \'waifu settings\' => category'), ValueError('Use \'waifu\' and see option in setup function')]), [get_line_number()])
                quit()
            else:
                printnlog('waifu settings => category')
        server: list[str] = ['nekos.best', 'waifu.pics', 'kyoko', 'nekos_api']
        if not config.get('neko settings', 'server').split(' ')[0] in server:
            error_get(ExceptionGroup('',[argNekoError('Wrong choice in \'neko settings\' => server'), ValueError(f'Only take {str(server)}')]), [get_line_number()])
            quit()
        else:
            printnlog('neko settings => server')
        try:
            int(config.get('game settings', 'goal_score').split(' ')[0])
            printnlog('game settings => goal_score')
        except ValueError:
            error_get(ExceptionGroup('',[argGameError('Wrong choice in \'game settings\' => goal_score'), ValueError('take only numbers')]), [get_line_number()])
            quit()
        try:
            if 10 <= int(config.get('game settings', 'goal_score').split(' ')[0]):
                printnlog('game settings => goal_score')
            else:
                raise ValueError
        except ValueError:
            error_get(ExceptionGroup('',[argGameError('Wrong choice in \'game settings\' => goal_score'), ValueError('minimum is 10')]), [get_line_number()])
            quit()
        try:
            float(config.get('game settings', 'computer_power').split(' ')[0])
            printnlog('game settings => computer_power')
        except ValueError:
            error_get(ExceptionGroup('',[argGameError('Wrong choice in \'game settings\' => computer_power'), ValueError('take only numbers')]), [get_line_number()])
            quit()
        if config.get('basic info', 'music').split(' ')[0] == 'enable':
            musiclimittext: bool = False
            while len(music) < int(config.get('basic info', 'musicnumber')):
                if not musiclimittext:
                    typewriter(printnlog('basic info => musicnumber; you have exceeded the limit by ' + str(
                        int(config.get('basic info', 'musicnumber')) - len(music)), toprint=False))
                    musiclimittext: bool = True
                set_config('basic info', 'musicnumber', str(int(args.music)-1))
                args.music = str(int(args.music)-1)

        """
        If the language is not specified, use the default language from the config file.
        @param args.language - the language specified by the user, or the default language from the config file.
        """
        if args.language is None:
            if config.get('basic info', 'lang').split(' ')[0] in language:
                args.language = config.get('basic info', 'lang').split(' ')[0]
            else:
                error_get(ExceptionGroup('',[argLanguageError('Wrong choice in \'basic info\' => lang'), ValueError('Language doesn\'t exist')]), [get_line_number()])
                quit()

        """
        If the user has specified that we should update the rotation dictionary, remove the old update.py file.
        """
        if args.update is None:
            try:
                os.remove('update.py')
            except FileNotFoundError:
                args.update = UNSPECIFIED
                error_get(ExceptionGroup('',[FileNotFoundError('update.py isn\'t present'), TypeError('NOT FATAL ERROR')]), [get_line_number()])

        logger.stay(printnlog('DONE', toprint=False))

        if args.configoptions == None:
            with open('CONFIG_OPTIONS.txt', 'w') as file:
                file.write('[BASIC INFO]\n')
                file.write(f'lang = {language}\n')
                file.write(f'enviroment = [0-f][0-f]\n')
                file.write(f'intro = [True/False]\n')
                file.write(f'inactivelimit = [Any number]\n')
                file.write(f'music = [disable/enable]\n')
                file.write(f'musiclist = [Any Youtube video title, divided by comma]\n')
                file.write(f'musicnumber = [Any number; Max is number of items in musiclist]\n')
                file.write('[WAIFU SETTINGS]\n')
                file.write(f'type = [sfw/nsfw]\n')
                category: list[str] = ["waifu", "neko", "shinobu", "megumin", "bully", "cuddle", "cry", "hug", "awoo", "kiss", "lick", "pat", "smug", "bonk", "yeet",
                                   "blush", "smile", "wave", "highfive", "handhold", "nom", "bite", "glomp", "slap", "kill", "kick", "happy", "wink", "poke", "dance", "cringe"]
                file.write(f'category (sfw) = {category}\n')
                category: list[str] = ['waifu', 'neko', 'trap', 'blowjob']
                file.write(f'category (nsfw) = {category}\n')
                file.write('[NEKO SETTINGS]\n')
                file.write(f'server = {server}\n')
                file.write('[GAME SETTINGS]\n')
                file.write('goal_score = [Any number]\n')
                file.write('computer_power = [Any number; Lower the powerfull]\n')
            os.remove(f'crash_dump-{datelog}.txt')
            quit()


    if __name__ == '__main__':
        potrebne: set[str] = {'psutil', 'tqdm', 'spotdl', 'pyunpack', 'semantic-version', 'patool', 'gputil', 'py-cpuinfo', 'tabulate', 'opencv-python', 'glob2', 'wmi', 'translate', 'show-in-file-manager',
                              'keyboard', 'cpufreq', 'pywin32', 'pypiwin32', 'pyautogui', 'moviepy', 'playsound', 'python-vlc', 'pygetwindow', 'pygame', 'pytube', 'bs4', 'uuid'}
        printnlog('Libraries needed: ', end='')
        potrebne1: list[str] = list(potrebne)
        for i in range(0, len(potrebne1)):
            printnlog(potrebne1[i], end=' ')
        printnlog("\n\nChecking for updates\n")
        nainstalovane: set[str] = {
            pkg.key for pkg in pkg_resources.working_set}
        nenajdene: set[str] = potrebne - nainstalovane
        if args.version is None:
            verzia = open('version', 'r')
            logger.stay(printnlog(verzia.read(), toprint=False))
            verzia.close()
            if nenajdene:
                if args.language == "SK":
                    print('Aktualizácia je k dispozícií: ', *nenajdene)
                elif args.language == "EN":
                    print('Update is available: ', *nenajdene)
                elif args.language == "JP":
                    print('アップデートが利用可能です： ', *nenajdene)
            os.remove('crash_dump-' + datelog + '.txt')
            quit()
        if __name__ == '__main__':
            if nenajdene:
                printnlog('\nUpdate is available: ' + str(nenajdene))
                vstup: str = input(
                    f'Do you want to install following modules? {nenajdene} (Y/n)> ').lower()
                if vstup in ['', 'y']:
                    printnlog("\nDownloading updates")
                    subprocess.check_call(
                        ['python', '-m', 'pip', 'install', *nenajdene])
                    printnlog("The program is restarting!!!")
                    sleep(1)
                    os.system('cls')
                    os.remove('crash_dump-' + datelog + '.txt')
                    subprocess.call(
                        [sys.executable, os.path.realpath(__file__)] + sys.argv[1:])
                    quit()
                else:
                    quit()
            printnlog('DONE\n')
            printnlog('Checking internet connection\n')

    def internet():
        number = 0
        while True:
            sleep(1)
            if os.path.isfile('INTERNET_CHECK_CORRECT'):
                os.remove('INTERNET_CHECK_CORRECT')
                break
            number += 1
            if 10 >= number >= 5:
                if args.language == "SK":
                    printnlog("Zdá sa, že máme problém s internetovým pripojením")
                elif args.language == "EN":
                    printnlog("Seems like we're having trouble with internet connection")
                elif args.language == "JP":
                    printnlog(
                        "インターネット接続に問題があるようです\nIf you don't see any of characters watch 'help.txt'")
                break
            if number >= 10:
                break 


    def internet_check() -> None:
        try:
            global requests
            import requests
            timeout: int = 10
            Thread(target=internet).start()
            requests.head("http://www.google.com/", timeout=timeout)
            try:
                open('INTERNET_CHECK_CORRECT', 'x')
            except FileExistsError:
                pass
        except requests.ConnectionError:  # type: ignore
            line_number: int = get_line_number()
            if __name__ == '__main__':
                if args.language == "SK":
                    printnlog("Vaše internetové pripojenie nefunguje")
                elif args.language == "EN":
                    printnlog("The internet connection is down")
                elif args.language == "JP":
                    printnlog(
                        "インターネット接続がダウンしています\nIf you don't see any of characters watch 'help.txt'")
                sleep(2)
                quit()

    def installing_carousel(package: str, comment: str = 'Installing', bar=False):
        """
        The installing_carousel function is a function that will print out the string 'Installing' and then
        the package name, in an animated fashion. It will do this until it reaches the INSTALL_DONE file, which
        is created by another function. This is to prevent multiple instances of installing_carousel from running at once.
        
        :param package: str: Specify the package that is being installed
        :param comment: str: Tell the user what is happening during the installation process
        :return: :
        """
        error = False
        alinst = False
        while True:
            if os.path.isfile('INSTALL_DONE'):
                break
            if os.path.isfile('INSTALL_ERROR'):
                error = True
                break
            if os.path.isfile('INSTALL_ALINST'):
                alinst = True
                break
            if os.path.isfile('INSTALL_PAUSE'):
                if not bar:
                    print('                                            ', end='\r')
                if bar:
                    tqdm.write('                                            ', end='\r')
                sleep(0.4)
                os.remove('INSTALL_PAUSE')
            if not bar:
                print(f'{comment} {package} /               ', end='\r')
            if bar:
                tqdm.write(f'{comment} {package} /               ', end='\r')
            sleep(0.25)
            if os.path.isfile('INSTALL_DONE'):
                break
            if os.path.isfile('INSTALL_ERROR'):
                error = True
                break
            if os.path.isfile('INSTALL_ALINST'):
                alinst = True
                break
            if os.path.isfile('INSTALL_PAUSE'):
                if not bar:
                    print('                                            ', end='\r')
                if bar:
                    tqdm.write('                                            ', end='\r')
                sleep(0.4)
                os.remove('INSTALL_PAUSE')
            if not bar:    
                print(f'{comment} {package} -               ', end='\r')
            if bar:
                tqdm.write(f'{comment} {package} -               ', end='\r')
            sleep(0.25)
            if os.path.isfile('INSTALL_DONE'):
                break
            if os.path.isfile('INSTALL_ERROR'):
                error = True
                break
            if os.path.isfile('INSTALL_ALINST'):
                alinst = True
                break
            if os.path.isfile('INSTALL_PAUSE'):
                if not bar:
                    print('                                            ', end='\r')
                if bar:
                    tqdm.write('                                            ', end='\r')
                sleep(0.4)
                os.remove('INSTALL_PAUSE')
            if not bar:
                print(f'{comment} {package} \\              ', end='\r')
            if bar:
                tqdm.write(f'{comment} {package} \\              ', end='\r')
            sleep(0.25)
            if os.path.isfile('INSTALL_DONE'):
                break
            if os.path.isfile('INSTALL_ERROR'):
                error = True
                break
            if os.path.isfile('INSTALL_ALINST'):
                alinst = True
                break
            if os.path.isfile('INSTALL_PAUSE'):
                if not bar:
                    print('                                            ', end='\r')
                if bar:
                    tqdm.write('                                            ', end='\r')
                sleep(0.4)
                os.remove('INSTALL_PAUSE')
            if not bar:
                print(f'{comment} {package} |               ', end='\r')
            if bar:
                tqdm.write(f'{comment} {package} |               ', end='\r')
            sleep(0.25)
        if error:
            if not bar:
                print(f'{comment} {package} ERROR             ')
            if bar:
                tqdm.write(f'{comment} {package} ERROR             ')
        elif alinst:
            if not bar:
                print(f'{comment} {package} ALREADY INSTALLED             ')
            if bar:
                tqdm.write(f'{comment} {package} ALREADY INSTALLED             ')
        else:
            if not bar:
                print(f'{comment} {package} DONE             ')
            if bar:
                tqdm.write(f'{comment} {package} DONE             ')
        try:
            os.remove('INSTALL_DONE')
        except Exception:
            pass
        try:
            os.remove('INSTALL_ERROR')
        except Exception:
            pass
        try:
            os.remove('INSTALL_ALINST')
        except Exception:
            pass

    def choco_install(*packages: str) -> None:
        """
        The choco_install function installs a list of packages using Chocolatey.
        It returns the number of packages successfully installed and the number that were already installed.
        
        :param *packages: str: Pass a variable number of arguments to the function
        :return: A tuple of two integers
        """
        
        alinst_number = 0
        inst_number = 0
        for package in packages:
            version = ''
            if len(pack := package.split(' --version ')) > 1:
                version = pack[1]
                package = pack[0]
            with open('choco_output', 'w') as file:
                Thread(target=installing_carousel, args=(package,)).start()
                Thread(target=choco_check, args=(package,)).start()
                subprocess.run(['choco', 'install', package, version, '-y'], stdout=file, text=True)
            with open('choco_output', 'r') as file:
                alinst = False
                for line, content in enumerate(file.readlines()):
                    if 'already installed.' in content and package in content:
                        open('INSTALL_ALINST', 'x')
                        alinst = True
                        alinst_number += 1
                        break
            try:
                open('choco_end', 'x')
            except Exception:
                pass
            if not alinst:
                open('INSTALL_DONE', 'x')
                inst_number += 1
            sleep(2)
        return (inst_number, alinst_number)
    
    def choco_check(module: str) -> None:
        """
        The choco_check function checks if chocolatey is installed and prompts the user to continue.
        It also checks if the user is an admin, and confirms that they want to run as non-admin.
        
        :param module: str: Determine which module is being checked for
        :return: True when chocolatey is installed, and false when it is not
        """
        admin: bool = True
        adminline = -1
        cont = False
        contline = -1
        ffmpeg_conf = False
        ffmpegline = -1
        ffmpeg_confline = -1
        sleep(2)
        while os.path.isfile('choco_output'):
            sleep(0.1)
            for line, content in enumerate(open('choco_output', 'r').readlines()):
                if 'WARNING: \'choco\' was found at' in content and module == 'chocolatey':
                    return True
                if 'Ensuring chocolatey.nupkg is in the lib folder' in content and module == 'chocolatey':
                    return False
                if 'Chocolatey detected you are not running' in content and admin:
                    if adminline == line:
                        pass
                    else:
                        admin = False
                        adminline = line
                if 'Do you want to continue' in content and not admin:
                    if contline == line:
                        pass
                    else:
                        cont = True
                        contline = line
                if 'ffmpeg package files install completed. Performing other installation steps.' in content and module == 'ffmpeg':
                    if ffmpegline == line:
                        pass
                    else:
                        ffmpeg_conf = True
                        ffmpegline = line
                if 'Do you want to run the script' in content and module == 'ffmpeg':
                    if ffmpeg_confline == line:
                        pass
                    else:
                        cont = True
                        ffmpeg_confline = line
            if not admin or ffmpeg_conf or cont:
                open('INSTALL_PAUSE', 'x')
                sleep(0.25)
            if not admin:
                pg.press('y')
                admin = True
            if ffmpeg_conf:
                pg.press('a')
                ffmpeg_conf = False
            if cont or ffmpeg_conf:
                pg.press('enter')
                cont = False
                ffmpeg_conf = False
            if os.path.isfile('choco_end'):
                os.remove('choco_end')
                break

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
        if not os.path.isfile("C:/Users/" + os.getlogin() + "/AppData/Local/ZnámE/info.txt") or args.update is None:
            logger.stay(printnlog('First time setup', toprint=False))
            if not os.path.isfile('INSTALL_RESTART'):
                with open('choco.ps1', 'w') as file:
                    file.write('$InstallDir=\'C:\ProgramData\chocoportable\'\n$env:ChocolateyInstall="$InstallDir"\nSet-ExecutionPolicy Bypass -Scope Process -Force;\niex ((New-Object System.Net.WebClient).DownloadString(\'https://community.chocolatey.org/install.ps1\'))')
                logger.next("Checking if chocolatey is installed if not downloading\n")
                Thread(target=installing_carousel, args=('chocolatey',)).start()
                Thread(target=choco_check, args=('chocolatey',)).start()
                with open('choco_output', 'w') as file:
                    choco = subprocess.run(['powershell.exe', '-file', 'choco.ps1', '--quiet', '--no-verbose'], stdout=file, text=True)
                with open('choco_output', 'r') as file:
                    for line in file.readlines():
                        if 'cannot be loaded because running scripts is disabled on this system' in line:
                            open('INSTALL_ERROR', 'x')
                            logger.stay('Run Powershell as administrator and type \'Set-ExecutionPolicy RemoteSigned\' type Y and press \'enter\'')
                            with open('set_permissions.txt', 'w') as file:
                                file.write('Run Powershell as administrator and type following code press \'enter\' type Y and press \'enter\'\n\nSet-ExecutionPolicy RemoteSigned')
                            osCommandString = "notepad.exe set_permissions.txt"
                            os.system(osCommandString)
                            input('Enter to continue ...')
                            os.remove('set_permissions.txt')
                            with open('choco_output', 'w') as file:
                                choco = subprocess.run(['powershell.exe', '-file', 'choco.ps1', '--quiet', '--no-verbose'], stdout=file, text=True)
                open('choco_end', 'x')
                open('INSTALL_DONE', 'x')
                logger.prev('')
                sleep(1)

                def isUserAdmin():
                    """
                    The isUserAdmin function checks to see if the user running this script is an admin.
                    This is for Windows only.
                    :return: A boolean value
                    """
                    if os.name == 'nt':
                        import ctypes
                        # WARNING: requires Windows XP SP2 or higher!
                        try:
                            return ctypes.windll.shell32.IsUserAnAdmin()
                        except:
                            traceback.print_exc()
                            print("Admin check failed, assuming not an admin.")
                            return False
                    elif os.name == 'posix':
                        # Check for root on Posix
                        return os.getuid() == 0
                    else:
                        raise RuntimeError("Unsupported operating system for this module: %s" % (os.name,))

                def runAsAdmin(cmdLine=None, wait=True):
                    """
                    The runAsAdmin function is a simple function that will run your python script as the Administrator.
                    This function will attempt to do the following:
                    :param cmdLine: Pass arguments to the executable
                    :param wait: Determine whether the function should wait for the process to finish or not
                    :return: The process handle of the elevated process
                    """
                    if os.name != 'nt':
                        raise RuntimeError("This function is only implemented on Windows.")

                    import win32api, win32con, win32event, win32process
                    from win32com.shell.shell import ShellExecuteEx # type: ignore
                    from win32com.shell import shellcon # type: ignore

                    python_exe = sys.executable

                    if cmdLine is None:
                        cmdLine = [python_exe] + sys.argv
                    elif type(cmdLine) not in (ctypes.TupleType,ctypes.ListType):
                        raise ValueError("cmdLine is not a sequence.")
                    cmd = '"%s"' % (cmdLine[0],)
                    params = " ".join(['"%s"' % (x,) for x in cmdLine[1:]])
                    cmdDir = ''
                    showCmd = win32con.SW_SHOWNORMAL
                    lpVerb = 'runas'
                    procInfo = ShellExecuteEx(nShow=showCmd,
                                            fMask=shellcon.SEE_MASK_NOCLOSEPROCESS,
                                            lpVerb=lpVerb,
                                            lpFile=cmd,
                                            lpParameters=params)
                    if wait:
                        procHandle = procInfo['hProcess']    
                        obj = win32event.WaitForSingleObject(procHandle, win32event.INFINITE)
                        rc = win32process.GetExitCodeProcess(procHandle)
                    else:
                        rc = None
                    return rc

                def checkAdmin():
                    """
                    The checkAdmin function checks if the user is an admin. If not, it will run the program as an admin.
                    :return: 0 if the user is an admin, and returns 1 if the user is not an admin
                    :doc-author: Trelent
                    """
                    rc = 0
                    if not isUserAdmin():
                        print("You're not an admin.", os.getpid(), "params: ", sys.argv)
                        rc = runAsAdmin()
                    else:
                        print("You are an admin!", os.getpid(), "params: ", sys.argv)
                        rc = 0
                    return rc

                os.remove(f"crash_dump-{datelog}.txt")
                open('INSTALL', 'x')
                open('INSTALL_RESTART', 'x')
                os.remove('choco.ps1')
                os.remove('choco_output')
                sleep(1)
                checkAdmin()
                quit()
            if os.path.isfile('INSTALL'):
                os.remove('INSTALL')
                inst_number, alinst_number = choco_install('ffmpeg --version 5.1.2', 'vlc --version 3.0.18', 'vcredist2015 --version 14.0.24215.20170201 -y')
                if inst_number == 0:
                    pass
                else:
                    logger.stay("Restarting program ...")
                    sleep(1)
                    subprocess.check_output('start edupage.py --language ' + args.language, shell=True)
                    os.remove(f"crash_dump-{datelog}.txt")
                os.remove('choco_output')
                try:
                    os.remove('choco_end')
                except Exception:
                    pass
                if inst_number != 0:
                    quit()
            sleep(1)
            os.remove('INSTALL_RESTART')
            typewriter('Trying ffmpeg ...')
            os.system('ffmpeg')

    if __name__ == '__main__':
        internet_check()
        logger.stay(printnlog('DONE', toprint=False))
        logger.stay(printnlog('Importing libraries', toprint=False))
        logger.next('')
    from tqdm import tqdm
    if __name__ == '__main__':
        print_module()
    from urllib.parse import unquote
    if __name__ == '__main__':
        print_module('unquote from urllib.parse')
    from pathlib import Path
    if __name__ == '__main__':
        print_module('Path from pathlib')
    import pathlib
    if __name__ == '__main__':
        print_module()
    from uninstall import uninstall
    if __name__ == '__main__':
        print_module()
    import shutil
    if __name__ == '__main__':
        print_module()
    import zipfile
    if __name__ == '__main__':
        print_module()
    import hashlib
    if __name__ == '__main__':
        print_module()
    import GPUtil
    if __name__ == '__main__':
        print_module()
    import semantic_version
    if __name__ == '__main__':
        print_module()
    import win32gui
    if __name__ == '__main__':
        print_module()
    import ctypes
    if __name__ == '__main__':
        print_module()
    import cpuinfo
    if __name__ == '__main__':
        print_module()
    import cv2
    if __name__ == '__main__':
        print_module()
    import glob
    if __name__ == '__main__':
        print_module()
    import webbrowser
    if __name__ == '__main__':
        print_module()
    import win32api
    if __name__ == '__main__':
        print_module()
    import cpufreq
    if __name__ == '__main__':
        print_module()
    import time
    if __name__ == '__main__':
        print_module()
    import psutil
    if __name__ == '__main__':
        print_module()
    import vlc
    if __name__ == '__main__':
        print_module()
    import pygetwindow
    if __name__ == '__main__':
        print_module()
    import wmi
    if __name__ == '__main__':
        print_module()
    from showinfm import show_in_file_manager
    if __name__ == '__main__':
        print_module('show_in_file_manager from showinfm')
    import platform
    if __name__ == '__main__':
        print_module()
    import socket
    if __name__ == '__main__':
        print_module()
    import re
    if __name__ == '__main__':
        print_module()
    import uuid
    if __name__ == '__main__':
        print_module()
    from tabulate import tabulate
    if __name__ == '__main__':
        print_module()
    from PIL import Image
    if __name__ == '__main__':
        print_module('Image from PIL')
    from pygame import mixer
    if __name__ == '__main__':
        print_module('mixer from pygame')
    import readline
    if __name__ == '__main__':
        print_module('readline')
    import logging
    if __name__ == '__main__':
        print_module()
    import moviepy.editor as mp
    if __name__ == '__main__':
        print_module('moviepy.editor')

    LOG_FILENAME = 'completer.log'
    logging.basicConfig(filename=LOG_FILENAME,
                        level=logging.DEBUG,
                        format="%(asctime)s,%(msecs)03d %(levelname)-8s [%(filename)s:%(lineno)d] - %(message)s",
                        datefmt='%Y-%m-%d:%H:%M:%S')



    def download(url: str, fname: str, chunk_size: int = 1024) -> bool:
        """
        "Download a file from a URL to a local file."

        The first line is the function's signature. It's a single line of code that tells you everything
        you need to know about the function

        :param url: The URL of the file to download
        :type url: str
        :param fname: The name of the file to be downloaded
        :type fname: str
        :param chunk_size: The size of the chunks to download, defaults to 1024 (optional)
        """
        try:
            resp = requests.get(url, stream=True)
            total: int = int(resp.headers.get('content-length', 0))
            with open(fname, 'wb') as file, tqdm(
                desc=fname,
                total=total,
                unit='iB',
                unit_scale=True,
                unit_divisor=1024,
            ) as bar:
                for data in resp.iter_content(chunk_size=chunk_size):
                    size = file.write(data)
                    bar.update(size)
        except ConnectionError:
            logging.warning("Connection error")
            return False
        return True

    if __name__ == '__main__':
        print_module('mixer from pygame')
        logger.prev(printnlog('DONE', toprint=False))
        verzia = open('version', 'r')
        os.system('color ' + config.get('basic info',
                  'enviroment').split(' ')[0])
        os.system('Title ' + 'ZnámE')
        user32 = ctypes.windll.user32
        screensize: tuple[int, int] = user32.GetSystemMetrics(
            0), user32.GetSystemMetrics(1)
        screensizepercentage: tuple[float, float] = float(
            (1/1920)*screensize[0]), float((1/1080)*screensize[1])


        if not os.path.isfile("C:/Users/" + os.getlogin() + "/AppData/Local/ZnámE/info.txt") or args.update is None:
            sleep(1)
            try:
                os.makedirs("C:/Users/" + os.getlogin() +
                            "/AppData/Local/ZnámE/")
            except FileExistsError:
                pass
            open("C:/Users/" + os.getlogin() +
                 "/AppData/Local/ZnámE/info.txt", "x")
            logger.stay(to_info(verzia.read(), end='', file='version', mode='w', toprint=False))
            logger.stay(printnlog('Getting system information', toprint=False))
            logger.next(to_info('Resolution: ' +
                    str(screensize[0]) + 'x' + str(screensize[1]) + '\n', toprint=False))
            computer1 = wmi.WMI()
            computer_info: list[str] = computer1.Win32_ComputerSystem()[0]
            os_info: list[str] = computer1.Win32_OperatingSystem()[0]
            proc_info: list[str] = computer1.Win32_Processor()[0]
            gpu_info: list[str] = computer1.Win32_VideoController()[0]

            def get_size1(bytes: int | float, suffix: str = "B"):
                """
                It takes a number of bytes and returns a string with the number of bytes and the appropriate
                unit

                :param bytes: The number of bytes to convert
                :param suffix: The suffix to be appended to the size, defaults to B (optional)
                """
                """
                Scale bytes to its proper format
                e.g:
                    1253656 => '1.20MB'
                    1253656678 => '1.17GB'
                """
                factor: int = 1024
                for unit in ["", "K", "M", "G", "T", "P"]:
                    if bytes < factor:
                        return f"{bytes:.2f}{unit}{suffix}"
                    bytes /= factor

            my_system = platform.uname()
            my_cpuinfo = cpuinfo.get_cpu_info()
            pc = wmi.WMI()
            svmem = psutil.virtual_memory()
            swap = psutil.swap_memory()
            gpus = GPUtil.getGPUs()
            partitions = psutil.disk_partitions()
            disk_io = psutil.disk_io_counters()
            if_addrs = psutil.net_if_addrs()
            net_io = psutil.net_io_counters()
            os_info = pc.Win32_operatingSystem()[0]
            os_name = os_info.Name.encode('utf-8').split(b'|')[0]
            cpufreq = psutil.cpu_freq()
            os_version: str = ' '.join([os_info.Version, os_info.BuildNumber])
            logger.stay(to_info(os_info, toprint=False))
            system_ram = float(os_info.TotalVisibleMemorySize) / \
                1048576  # KB to GB
            logger.stay(to_info('OS Name: {0}'.format(os_name), toprint=False))
            logger.stay(to_info(f"Device Name: {my_system.node}", toprint=False))
            logger.stay(to_info(f"Architecture: {my_system.machine}", toprint=False))
            logger.stay(to_info(f"Processor: {my_system.processor}", toprint=False))
            logger.stay(to_info('CPU: {0}'.format(proc_info.Name), toprint=False))
            logger.stay(to_info("="*40 + "CPU Info" + "="*40, toprint=False))
            logger.stay(to_info(f"CPU architecture: {my_cpuinfo['arch']}", toprint=False))
            logger.stay(to_info("Physical cores:" + str(psutil.cpu_count(logical=False)), toprint=False))
            logger.stay(to_info("Total cores:" + str(psutil.cpu_count(logical=True)), toprint=False))
            logger.stay(to_info(f"Max Frequency: {cpufreq.max:.2f}Mhz", toprint=False))
            logger.stay(to_info(f"Min Frequency: {cpufreq.min:.2f}Mhz", toprint=False))
            logger.stay(to_info(f"Current Frequency: {cpufreq.current:.2f}Mhz", toprint=False))
            logger.stay(to_info("CPU Usage Per Core:", toprint=False))
            logger.next('')
            for i, percentage in enumerate(psutil.cpu_percent(percpu=True, interval=1)):
                to_info(f"Core {i}: {percentage}%")
            logger.prev(to_info(pc.Win32_Processor()[0], toprint=False))
            logger.stay(to_info(f"Total CPU Usage: {psutil.cpu_percent()}%", toprint=False))
            logger.stay(to_info('RAM: {0} GB'.format(system_ram), toprint=False))
            logger.stay(to_info("="*40 + "Memory Information" + "="*40, toprint=False))
            logger.stay(to_info(f"Total: {get_size1(svmem.total)}", toprint=False))
            logger.stay(to_info(f"Available: {get_size1(svmem.available)}", toprint=False))
            logger.stay(to_info(f"Used: {get_size1(svmem.used)}", toprint=False))
            logger.stay(to_info(f"Percentage: {svmem.percent}%", toprint=False))
            logger.stay(to_info("="*20 + "SWAP" + "="*20, toprint=False))
            logger.stay(to_info(f"Total: {get_size1(swap.total)}", toprint=False))
            logger.stay(to_info(f"Free: {get_size1(swap.free)}", toprint=False))
            logger.stay(to_info(f"Used: {get_size1(swap.used)}", toprint=False))
            logger.stay(to_info(f"Percentage: {swap.percent}%", toprint=False))
            logger.stay(to_info('Graphics Card: {0}'.format(gpu_info.Name), toprint=False))
            logger.stay(to_info("="*40 + "GPU Details" + "="*40, toprint=False))
            list_gpus: list = []
            for gpu in gpus:
                gpu_id = gpu.id
                gpu_name = gpu.name
                gpu_load = f"{gpu.load*100}%"
                gpu_free_memory = f"{gpu.memoryFree}MB"
                gpu_used_memory = f"{gpu.memoryUsed}MB"
                gpu_total_memory = f"{gpu.memoryTotal}MB"
                gpu_temperature = f"{gpu.temperature} °C"
                gpu_uuid = gpu.uuid
                list_gpus.append((
                    gpu_id, gpu_name, gpu_load, gpu_free_memory, gpu_used_memory,
                    gpu_total_memory, gpu_temperature, gpu_uuid
                ))

            logger.stay(to_info(tabulate(list_gpus, headers=("id", "name", "load", "free memory", "used memory", "total memory",
                                                 "temperature", "uuid")), toprint=False))
            logger.stay(to_info(f'IP Adress: {socket.gethostbyname(socket.gethostname())}', toprint=False))
            logger.stay(to_info(
                f"MAC Adress: {':'.join(re.findall('..', '%012x' % uuid.getnode()))}, toprint=False"))
            logger.stay(to_info("="*40 + "Disk Information" + "="*40, toprint=False))
            logger.stay(to_info("Partitions and Usage:", toprint=False))
            logger.next('')
            for partition in partitions:
                logger.stay(to_info(f"=== Device: {partition.device} ===", toprint=False))
                logger.stay(to_info(f"  Mountpoint: {partition.mountpoint}", toprint=False))
                logger.stay(to_info(f"  File system type: {partition.fstype}", toprint=False))
                try:
                    partition_usage = psutil.disk_usage(partition.mountpoint)
                except PermissionError:
                    continue
                logger.stay(to_info(f"  Total Size: {get_size1(partition_usage.total)}", toprint=False))
                logger.stay(to_info(f"  Used: {get_size1(partition_usage.used)}", toprint=False))
                logger.stay(to_info(f"  Free: {get_size1(partition_usage.free)}", toprint=False))
                logger.stay(to_info(f"  Percentage: {partition_usage.percent}%", toprint=False))
            logger.prev(to_info(f"Total read: {get_size1(disk_io.read_bytes)}", toprint=False))
            logger.stay(to_info(f"Total write: {get_size1(disk_io.write_bytes)}", toprint=False))
            logger.stay(to_info("="*40 + "Network Information" + "="*40, toprint=False))
            for interface_name, interface_addresses in if_addrs.items():
                for address in interface_addresses:
                    logger.next(to_info(f"=== Interface: {interface_name} ===", toprint=False))
                    if str(address.family) == 'AddressFamily.AF_INET':
                        logger.next(to_info(f"  IP Address: {address.address}", toprint=False))
                        logger.stay(to_info(f"  Netmask: {address.netmask}", toprint=False))
                        logger.stay(to_info(f"  Broadcast IP: {address.broadcast}", toprint=False))
                    elif str(address.family) == 'AddressFamily.AF_PACKET':
                        logger.next(to_info(f"  MAC Address: {address.address}", toprint=False))
                        logger.stay(to_info(f"  Netmask: {address.netmask}", toprint=False))
                        logger.stay(to_info(f"  Broadcast MAC: {address.broadcast}", toprint=False))
                    logger.prev('', by=1)
            logger.prev('')
            logger.stay(to_info(f"Total Bytes Sent: {get_size1(net_io.bytes_sent)}", toprint=False))
            logger.stay(to_info(f"Total Bytes Received: {get_size1(net_io.bytes_recv)}", toprint=False))
            logger.stay(to_info(pc.Win32_VideoController()[0], toprint=False))
            logger.stay(to_info("User Current Version:-" + str(sys.version), toprint=False))
            logger.stay(printnlog('\nDONE\n', toprint=False))

        if not os.path.exists("C:/Users/" + os.getlogin() + "/AppData/Local/ZnámE/backup/"):
            logger.stay(printnlog('Creating backup...\b', toprint=False))
            os.makedirs("C:/Users/" + os.getlogin() +
                        "/AppData/Local/ZnámE/backup/")
            shutil.copy('data.xp2', "C:/Users/" + os.getlogin() + "/AppData/Local/ZnámE/backup/backup-" +
                        str(datetime.now().strftime("%y-%m-%d-%H-%M-%S")) + '.xp2')
            x = open("C:/Users/" + os.getlogin() +
                     "/AppData/Local/ZnámE/backup/info.txt", 'w')
            x.write(
                'Rename \'xp2\' file to \'data.xp2\' and move it to your \'ZnámE\' directory')
            x.close()
            logger.stay(printnlog('Done'))

        logger.stay(printnlog("Defining functions", toprint=False))


    updateapp: str = str(
        'import argparse, shutil, os, subprocess, configparser, sys\nfrom time import sleep\nUNSPECIFIED = object()\nglobal parser\nparser = argparse.ArgumentParser()\nparser.add_argument(\'-ef\', \'--endf\', help=\'Will not automatically end program\', default=UNSPECIFIED, nargs=\'?\')\nparser.add_argument(\'-lang\', \'--language\', choices=[\'SK\',\'EN\',\'JP\'], help=\'Language selection\', nargs=\'?\')\nparser.add_argument(\'input\', help=\'Input folder\', nargs=\'?\')\nargs = parser.parse_args()\nconfig = configparser.RawConfigParser()\nconfig.read(\'config.ini\')\nargs.language = config.get(\'basic info\', \'lang\').split(\' \')[0]\nif args.input != "":\n    sleep(0.5)\n    shutil.move(\'edupage.py\', \'old/edupage.py\')\n    shutil.move(args.input + \'/edupage.py\', \'edupage.py\')\n    sleep(0.2)\n    shutil.rmtree(args.input)\n    shutil.rmtree(\'old\')\n    if args.endf == None:\n        subprocess.call(sys.executable + \' edupage.py -lang \' + args.language + \' -endf -update\', shell=True)\n    else:\n        subprocess.call(sys.executable + \' edupage.py -lang \' + args.language + \' -update\', shell=True)\n    quit()')

    if __name__ == '__main__':
        if args.log is None:
            x = open('log_update.py', 'w')
            x.write(updateapp)
            x.close()

    """
    Update the program to the newest version.
    @param directory - the directory of the new version
    @param args.language - the language of the program
    """

    if __name__ == '__main__':
        if args.test is not None:
            logger.stay(printnlog('Checking for newer version of ZnámE', toprint=False))
            try:
                url = 'https://raw.githubusercontent.com/GrenManSK/ZnamE/main/version'
                page = requests.get(url)
                verzia = open('version', 'r')
                if semantic_version.Version(page.text[1:]) <= semantic_version.Version(verzia.read()[1:]):
                    logger.next(printnlog('You have the latest version', toprint=False))
                    logger.prev('')
                else:
                    if args.language == "SK":
                        printnlog(
                            "Bola nájdená nová aktualizacia: " + page.text)
                    elif args.language == "EN":
                        printnlog("Newer version was found: " + page.text)
                    elif args.language == "JP":
                        printnlog("新しいバージョンが見つかりました: " + page.text)
                    verzia.close()
                    sleep(0.5)
                    url = 'https://api.github.com/repos/GrenManSK/ZnamE/zipball/main'
                    r = requests.get(url)
                    filename = "new.zip"
                    with open(filename, 'wb') as output_file:
                        download(url, 'new.zip')
                    with zipfile.ZipFile("new.zip", mode='r') as zip:
                        if args.language == "SK":
                            for member in tqdm(iterable=zip.namelist(), total=len(zip.namelist()), desc='Rozbaľujem '):
                                try:
                                    zip.extract(member)
                                    tqdm.write(
                                        f"{os.path.basename(member)}(" + str(os.path.getsize(member)) + "KB)")
                                except zipfile.error as e:
                                    pass
                        elif args.language == "EN":
                            for member in tqdm(iterable=zip.namelist(), total=len(zip.namelist()), desc='Extracting '):
                                try:
                                    zip.extract(member)
                                    tqdm.write(
                                        f"{os.path.basename(member)}(" + str(os.path.getsize(member)) + "KB)")
                                except zipfile.error as e:
                                    pass
                        elif args.language == "JP":
                            for member in tqdm(iterable=zip.namelist(), total=len(zip.namelist()), desc='抽出中 '):
                                try:
                                    zip.extract(member)
                                    tqdm.write(
                                        f"{os.path.basename(member)}(" + str(os.path.getsize(member)) + "KB)")
                                except zipfile.error as e:
                                    pass
                        zip.close()
                    os.remove("new.zip")
                    directory = None
                    for path, currentDirectory, files in os.walk(Path.cwd()):
                        for directory1 in currentDirectory:
                            if directory1.startswith("GrenManSK-ZnamE-"):
                                printnlog(directory1)
                                directory = directory1
                    if directory is None:
                        if args.language == "SK":
                            printnlog(
                                "CHYBA STAHOVANIA\nStiahnete manuálne novšiu verziu z\n'https://github.com/GrenManSK/ZnamE'")
                        elif args.language == "EN":
                            printnlog(
                                "DOWNLOADING ERROR\nManually download newer version from\n'https://github.com/GrenManSK/ZnamE'")
                        elif args.language == "JP":
                            printnlog(
                                "ダウンロード エラー\n'https://github.com/GrenManSK/ZnamE' から新しいバージョンを手動でダウンロードしてください")
                        sleep(2)
                        input()
                        quit()
                    os.mkdir('old')
                    shutil.move('data.xp2', 'old/data.xp2')
                    shutil.move('help.txt', 'old/help.txt')
                    shutil.move('LICENSE', 'old/LICENSE')
                    shutil.move('README.md', 'old/README.md')
                    shutil.move('version', 'old/version')
                    shutil.copyfile('config.ini', 'config_old.ini')
                    sleep(0.5)
                    shutil.move(directory + "/data.xp2", 'data.xp2')
                    shutil.move(directory + "/help.txt", 'help.txt')
                    shutil.move(directory + "/LICENSE", 'LICENSE')
                    shutil.move(directory + "/README.md", 'README.md')
                    shutil.move(directory + "/version", 'version')
                    shutil.move(directory + "/config.ini", 'config.ini')
                    crupdate = open("update.py", "w")
                    crupdate.write(updateapp)
                    crupdate.close()
                    if args.endf is None:
                        subprocess.call(sys.executable + ' update.py ' + directory +
                                        ' -lang ' + args.language + ' -endf', shell=True)
                    else:
                        subprocess.call(sys.executable + ' update.py ' +
                                        directory + ' -lang ' + args.language, shell=True)
                    sleep(0.1)
                    os.remove('crash_dump-' + datelog + '.txt')
                    try:
                        os.remove('choco_end')
                    except Exception:
                        pass
                    try:
                        os.remove('INSTALL')
                    except Exception:
                        pass
                    try:
                        os.remove('INSTALL_RESTART')
                    except Exception:
                        pass
                    quit()
            except requests.ConnectionError:  # type: ignore
                line_number: int = get_line_number()
                pass

        verzia.close()

    def getWindow() -> bool:
        """
        The getWindow function is used to find the window of Známý (the game) and activate it.
        It also checks if the file 'banner.png' exists in the assets folder.

        :return: If error occured
        """

        global exit
        stop_thread1: bool = True
        a = None
        cv2.namedWindow('frame2', cv2.WND_PROP_FULLSCREEN)
        cv2.setWindowProperty(
            'frame2', cv2.WND_PROP_FULLSCREEN, cv2.WINDOW_FULLSCREEN)
        test: str = "assets/banner.png"
        for file in glob.glob(test):
            a = cv2.imread(file)
        try:
            cv2.imshow("Image", a)
        except cv2.error:
            error_get(cv2.error('File is corrupt (probably \'banner.png\')'), [get_line_number()])
            return True
        cv2.waitKey(1)
        sleep(0.1)
        cv2.destroyWindow("Image")
        if args.test is not None:
            try:
                window = pygetwindow.getWindowsWithTitle('ZnámE')[0]
                window.activate()
                return False
            except IndexError:
                error_get(IndexError('Possible solution; run in cmd or python aplication not ide or put arguments \'--test\''), [get_line_number()])
                return True
        return False

    if __name__ == '__main__':
        logger.next(printnlog('Function: getWindow', toprint=False))

    def getImg(imgSrc: str, name: str, x=None, y=None, width=None, length=None) -> None:
        """
        The getImg function displays an image from the source. If x, y, width, and length are specified, then the image will be displayed at those coordinates with the specified width and length. Otherwise, the image will be displayed at the default coordinates and default width and length.

        :param imgSrc: str: Specify the source of the image
        :param name: str: Name the window
        :param x: Set the x coordinate of the window
        :param y: Specify the y coordinate of the window
        :param width: Set the width of the window
        :param length: Set the length of the window
        :return: The image that is displayed
        """
        path: str = imgSrc
        for file in glob.glob(path):
            global a
            a = cv2.imread(file)
            cv2.imshow(name, a)
            if x is not None and y is not None and width is not None and length is not None:
                appname: str = name
                xpos: int = x
                ypos: int = y
                if width is None:
                    width = int((screensize[0]/10)*9)
                if length is None:
                    length = int((screensize[1]/10)*9)

                def enumHandler(hwnd, lParam):
                    if win32gui.IsWindowVisible(hwnd):  # type: ignore
                        # type: ignore
                        if appname in win32gui.GetWindowText(hwnd):
                            win32gui.MoveWindow(
                                hwnd, xpos, ypos, width, length, True)  # type: ignore
                win32gui.EnumWindows(enumHandler, None)  # type: ignore
            k = cv2.waitKey(33)
            cv2.setWindowProperty(
                name, cv2.WND_PROP_FULLSCREEN, cv2.WINDOW_FULLSCREEN)
            if k == 27:
                break
            elif k == -1:
                continue
            else:
                print(k)
                cv2.destroyAllWindows()

    if __name__ == '__main__':
        logger.stay(printnlog('Function: getImg', toprint=False))

    def move(window: str, x: int, y: int, width, length) -> None:  # type: ignore
        """
        The move function moves the specified window to a specified location.
        The move function takes four arguments:
            1) The name of the window as a string. This is case sensitive and should be enclosed in quotation marks if it contains spaces or special characters (e.g., &quot;Microsoft Word&quot;). 
            2) The x-coordinate of the desired location on your screen, measured in pixels from the left edge of your screen to where you want your window located (e.g., 100). 
            3) The y-coordinate of the desired location on your screen, measured in pixels from the top edge of your screen

        :param window: str: Specify the name of the window
        :param x: int: Set the x position of the window, y is used to set the y position
        :param y: int: Set the y position of the window, measured in pixels from the top edge of your screen
        :param width: Set the width of the window
        :param length: Set the height of the window
        :return: None
        """
        appname: str = window
        xpos: int = x
        ypos: int = y
        if width is None:
            width: int = int((screensize[0]/10)*9)
        if length is None:
            length: int = int((screensize[1]/10)*9)

        def enumHandler(hwnd, lParam):  # type: ignore
            if win32gui.IsWindowVisible(hwnd):  # type: ignore
                if appname in win32gui.GetWindowText(hwnd):  # type: ignore
                    win32gui.MoveWindow(
                        hwnd, xpos, ypos, width, length, True)  # type: ignore
        win32gui.EnumWindows(enumHandler, None)  # type: ignore

    if __name__ == '__main__':
        logger.stay(printnlog('Function: move', toprint=False))

        logger.next(printnlog('\nDefining apps', toprint=False))

    codeapp: str = str(
        'import sys\nPLOCHA = [[\"a\", \"b\", \"c\", \"d\", \"e\"], [\"f\", \"g\", \"h\", \"i\", \"j\"], [\n    \"k\", \"l\", \"m\", \"n\", \"o\", ], [\"p\", \"q\", \"r\", \"s\", \"t\"], [\n    \"u\", \"v\", \"w\", \"x\", \"y\"], [\"A\", \"B\", \"C\", \"D\", \"E\"], [\n    \"F\", \"G\", \"H\", \"I\", \"J\"], [\"K\", \"L\", \"M\", \"N\", \"O\", ], [\n    \"P\", \"Q\", \"R\", \"S\", \"T\"], [\"U\", \"V\", \"W\", \"X\", \"y\"], [\n    \"z\", \" \", \",\", \".\", \":\"], [\"!\", \"?\", \"\'\", \'\"\', \"`\"], [\n    \"1\", \"2\", \"3\", \"4\", \"5\"], [\"6\", \"7\", \"8\", \"9\", \"0\"], [\n    \"\\n\", \"<\", \">\", \";\", \"/\"], [\"\\\\", \"{\", \"}\", \"(\", \")\"],[\n    \"[\",\"]\",\"|\",\"-\",\"_\"],[\"=\",\"+\",\"@\",\"#\",\"$\"],[\"%\",\"^\",\"&\",\"*\",\"~\"]]\ndef read_file(file):\n    obsah = \"\"\n    obsah_list = []\n    for i in file:\n        obsah = \"\"\n        obsah += i\n        for i in obsah:\n            i.lower()\n            obsah_list.append(i)\n    return obsah_list\ndef encode(obsah):\n    sifra = []\n    for i in obsah:\n        riadok = 0\n        stlpec = 0\n        while True:\n            if riadok == 19 and stlpec == 0:\n                break\n            if i == PLOCHA[riadok][stlpec]:\n                sifra.append(str(riadok) + \" \" + str(stlpec))\n                break\n            if stlpec == 4:\n                riadok += 1\n                stlpec = 0\n            else:\n                stlpec += 1\n    return sifra\ndef output_file(file, name):\n    y = []\n    x = open(name + \"crypted\", \"w\")\n    for i in file:\n        y.append(i)\n    x.write(str(y))\n    x.close\n    return\ndef main():\n    name = sys.argv[1]\n    open_file = open(name, \"r\")\n    open_file.close\n    output_file(encode(read_file(open_file)), name)\nmain()\nx=open(\'DONE\',\'x\')\nx.close()')
    decodeapp: str = str(
        'import os\nos.system(\'Title \' + \'code\')\nimport sys\nPLOCHA = [[\"a\", \"b\", \"c\", \"d\", \"e\"], [\"f\", \"g\", \"h\", \"i\", \"j\"], [\n    \"k\", \"l\", \"m\", \"n\", \"o\", ], [\"p\", \"q\", \"r\", \"s\", \"t\"], [\n    \"u\", \"v\", \"w\", \"x\", \"y\"], [\"A\", \"B\", \"C\", \"D\", \"E\"], [\n    \"F\", \"G\", \"H\", \"I\", \"J\"], [\"K\", \"L\", \"M\", \"N\", \"O\", ], [\n    \"P\", \"Q\", \"R\", \"S\", \"T\"], [\"U\", \"V\", \"W\", \"X\", \"y\"], [\n    \"z\", \" \", \",\", \".\", \":\"], [\"!\", \"?\", \"\'\", \'"\', \"`"], [\n    \"1\", \"2\", \"3\", \"4\", \"5\"], [\"6\", \"7\", \"8\", \"9\", \"0\"], [\n    \"\\n\", \"<\", \">\", \";\", \"/\"], [\"\\\\", \"{\", \"}\", \"(\", \")\"],[\n    \"[\",\"]\",\"|\",\"-\",\"_\"],[\"=\",\"+\",\"@\",\"#\",\"$\"],[\"%\",\"^\",\"&\",\"*\",\"~\"]]\ndef read_file(file):\n    obsah = \"\"\n    obsah_list = []\n    for i in file:\n        obsah += i\n        for i in obsah:\n            obsah_list.append(i)\n    return obsah_list\ndef decode(obsah):\n    done = \"\"\n    sifra = []\n    for i in obsah:\n        done += str(i)\n        if i == \"[\" or i == \"\'\" or i == \",\" or i == \"]\":\n            done = \"\"\n            continue\n        if i == \" \":\n            sifra.append(i)\n        else:\n            sifra.append(i)\n    return sifra\ndef real_decode(obsah):\n    cislo = 0\n    pokracovanie = False\n    done = \"\"\n    vysledok = []\n    for i in obsah:\n        done += str(i)\n        cislo = 0\n        for i in done:\n            cislo += 1\n        if i == \" \":\n            done = \"\"\n            continue\n        if pokracovanie and done.isnumeric() and cislo == 1:\n            stlpec = int(done)\n            vysledok.append(PLOCHA[riadok][stlpec])\n            pokracovanie = False\n            done = \"\"\n            continue\n        if not pokracovanie or cislo == 2:\n            pokracovanie = True\n            riadok = int(done)\n            continue\n    return vysledok\ndef to_text(obsah):\n    text = \"\"\n    for i in obsah:\n        if i == \".\":\n            text += i + \"\\n\"\n            continue\n        text += i\n    return text\ndef create_file(obsah, name):\n    x = open(sys.argv[1], \"w\")\n    x.write(obsah)\n    x.close\n    return\ndef main():\n    if sys.argv[2] == \'False\':\n        name = \'data\'\n    else:\n        name = sys.argv[2]\n    open_file = open(name, \"r\")\n    code = list(decode(read_file(open_file)))\n    create_file(to_text(real_decode(code)), name)\nmain()\nx=open(\'DONE\',\'x\')\nx.close()')
    findapp: str = str('import sys\ndecodename=str(sys.argv[1])\nicofind=int(sys.argv[2])\ndn=open(decodename,\'r\')\ndnr=dn.read()\nbracket,brackethist=0,0\nico=[]\nicocurrent=\'\'\nicoend=False\nrnii=False\nrniiend=False\nsubject=\'\'\nik=False\nuserdef=False\nwh=False\npassword=\'\'\npassend=False\nfor i in dnr:\n    if rnii:\n        wh=True\n        if i==\'[\':\n            bracket+=1\n        elif i==\']\':\n            bracket-=1\n        if passend:\n            user.write(password+\'\\n\')\n            passend=False\n        if ik:\n            if i!="," and bracket==4 and brackethist==4:\n                user.write(i)\n            if bracket==3:\n                subject=\'\'\n                ik=False\n                rniiend=False\n                user.write(\"\\n\")\n        if rniiend:\n            user.write(subject)\n            ik=True\n            rniiend=False\n            brackethist=bracket\n            continue\n        if userdef:\n            userdef=False\n            user=open(str(ico[0]),\'w\')\n        if bracket==3 and brackethist==3 and i!=\"\'\":\n            if i ==\',\':\n                rniiend=True\n                continue\n            subject+=str(i)\n        elif bracket==5 and brackethist==5 and i!=\"\'\":\n            if i ==\',\':\n                passend=True\n                continue\n            password+=str(i)\n        brackethist=bracket\n        if bracket<2 and brackethist<2:\n            break\n    else:\n        if i==\'[\':\n            bracket+=1\n        elif i==\']\':\n            bracket-=1\n        if icoend:\n            if icocurrent!=\'\':\n                if int(icocurrent)==icofind:\n                    ico.append(icocurrent)\n                    rnii=True\n                    continue\n                icocurrent=\'\'\n                icoend=False\n        if bracket==2 and brackethist==2:\n            if i ==\',\':\n                icoend=True\n                userdef=True\n                continue\n            icocurrent+=i\n        brackethist=bracket\nif not wh:\n    user=open(sys.argv[2], \'x\')\nuser.close()\nx=open(\'DONE\',\'x\')\nx.close()')
    passwordapp: str = str(
        'import sys\ndecodename=str(sys.argv[1])\ndn=open(decodename,\'r\')\ndnr=dn.readlines()\ntry:\n    number=int(dnr[0])\n    number=str(dnr[0])\n    number=dnr[0][:6]\nexcept Exception:\n    number=None\nx=open(\'DONE\',\'w\')\nx.write(number)\nx.close()')
    addapp: str = str('import sys\ndecodename=str(sys.argv[1])\nicofind=int(sys.argv[2])\nsubjectfind = sys.argv[3]\nmarkadd = sys.argv[4]\ndn=open(decodename,\'r\')\ndnr=dn.read()\nbracket,brackethist=0,0\nico=[]\nicocurrent=\'\'\nicoend=False\nrnii=False\nrniiend=False\nsubject=\'\'\nik=False\nuserdef=False\nwh=False\npassword=\'\'\npassend=False\nik2=False\nadd=False\nuser=open(\'data1\',\'w\', newline=\'\')\nfor i in dnr:\n    user.write(i)\n    if rnii:\n        wh=True\n        if i==\'[\':\n            bracket+=1\n        elif i==\']\':\n            bracket-=1\n        if add and subject==subjectfind and bracket==4 and brackethist==4:\n            subjectfind=None\n            user.write(str(markadd) + \',\')\n            add=False\n        if passend:\n            passend=False\n        if ik:\n            if ik2:\n                ik2=False\n                add=True\n            if bracket==3:\n                subject=\'\'\n                ik=False\n                rniiend=False\n        if rniiend:\n            ik=True\n            ik2=True\n            rniiend=False\n            brackethist=bracket\n            continue\n        if userdef:\n            userdef=False\n        if bracket==3 and brackethist==3 and i!=\"\'\":\n            if i ==\',\':\n                rniiend=True\n                continue\n            subject+=str(i)\n        elif bracket==5 and brackethist==5 and i!=\"\'\":\n            if i ==\',\':\n                passend=True\n                continue\n            password+=str(i)\n        brackethist=bracket\n    else:\n        if i==\'[\':\n            bracket+=1\n        elif i==\']\':\n            bracket-=1\n        if icoend:\n            if icocurrent!=\'\':\n                if int(icocurrent)==icofind:\n                    ico.append(icocurrent)\n                    rnii=True\n                    continue\n                icocurrent=\'\'\n                icoend=False\n        if bracket==2 and brackethist==2:\n            if i ==\',\':\n                icoend=True\n                userdef=True\n                continue\n            icocurrent+=i\n        brackethist=bracket\nif not wh:\n    user=open(sys.argv[2], \'x\')\nuser.close()\nx=open(\'DONE\',\'x\')\nx.close()')
    restartapp: str = str('import argparse, time, pygetwindow\nimport pyautogui as pg\nUNSPECIFIED = object()\nparser = argparse.ArgumentParser()\nparser.add_argument(\'-al\',\'--autol\', choices=[], default=UNSPECIFIED, nargs=\'?\')\nargs = parser.parse_args()\nwindow = pygetwindow.getWindowsWithTitle(\'ZnámE\')[0]\nwindow.activate()\nif args.autol == None:\n    time.sleep(1)\n    pg.write("login\\n")\n    time.sleep(1)\n    pg.write("y\\n")')
    gameapp: str = str('from edupage import game\ngame()')

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
            x = open('log_codeapp.py', 'w')
            x.write(codeapp)
            x.close()
            x = open('log_decodeapp.py', 'w')
            x.write(decodeapp)
            x.close()
            x = open('log_findapp.py', 'w')
            x.write(findapp)
            x.close()
            x = open('log_passwordapp.py', 'w')
            x.write(passwordapp)
            x.close()
            x = open('log_addapp.py', 'w')
            x.write(addapp)
            x.close()
            x = open('log_restartapp.py', 'w')
            x.write(restartapp)
            x.close()

    if __name__ == '__main__':
        logger.stay(printnlog('DONE', toprint=False))

    def get_size(bytes):
        """
        The get_size function accepts a number of bytes and returns a human-readable string representation of the size.
        For example, calling get_size(1024) will return '0.98KiB'.


        :param bytes: Store the value of bytes
        :return: The size of the bytes in human readable format
        """

        for unit in ['', 'K', 'M', 'G', 'T', 'P']:
            if bytes < 1024:
                return f"{bytes:.2f}{unit}B"
            bytes /= 1024

    if __name__ == '__main__':
        logger.stay(printnlog('Function: get_size', toprint=False))

    def delcache(name: str, hist: str) -> None:
        """
        The delcache function deletes the cache file if it is empty.


        :param name: Name the file that is used to store the time
        :param hist: Check if the history file has changed
        :return: The value of the timer
        """

        global timer
        time_got: int = int(config.get(
            'basic info', 'inactivelimit').split(' ')[0])
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
                    x = open("INACTIVE", 'x')
                    x.close()
                    os.system('cls')
                    pg.write('\n')
                    playhtml('apphtml\\inactive')
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

    loginvstupuser = ''
    global progress_bar_check
    progress_bar_check = 0
    global progress_bar_end
    progress_bar_end = False

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
                try:
                    os.remove(passwordp[1])  # type: ignore
                except Exception:
                    pass
                break
        if leave:
            sleep(0.05)
            return True
        else:
            return False

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
            if end:
                break
            while True:
                if progress_bar_check >= 100:
                    end: bool = True
                    break
                if progress_bar_check == progress_bar_check_old:
                    continue
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
        if args.language == "SK":
            tqdm.write('Pridávam ...', end='\r')
        elif args.language == "EN":
            tqdm.write('Adding ...', end='\r')
        elif args.language == "JP":
            tqdm.write('追加する ...', end='\r')
        while True:
            leave: bool = False
            for i in os.listdir():
                if i == 'DONE':
                    leave: bool = True
                    break
            if leave:
                sleep(0.05)
                break
        if args.language == "SK":
            tqdm.write('Pridávam Hotovo')
        elif args.language == "EN":
            tqdm.write('Adding Complete')
        elif args.language == "JP":
            tqdm.write('追加完了')
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
        if password:
            decodename2: str = name
        if name:
            decodename1: str = decodename
        elif isinstance(name, str):
            decodename1: str = name
        else:
            decodename1: str = "None"
        crdecode = open(decodename + ".py", "w")
        crdecode.write(decodeapp)
        crdecode.close()
        if mode == 1:
            subprocess.check_output(
                'start ' + decodename + '.py ' + str(name) + ' ' + str(password), shell=True)
        elif mode == 0:
            subprocess.check_output(
                'start ' + decodename + '.py ' + str(decodename1) + ' ' + str(decodename2), shell=True)
        if args.language == "SK":
            tqdm.write('Odkoduvávam ...', end='\r')
        elif args.language == "EN":
            tqdm.write('Encrypting ...', end='\r')
        elif args.language == "JP":
            tqdm.write('暗号化 ...', end='\r')
        while True:
            leave: bool = False
            for i in os.listdir():
                if i == 'DONE':
                    leave: bool = True
                    break
            if leave:
                sleep(0.05)
                break
        if args.language == "SK":
            tqdm.write('Odkoduvávam Hotovo')
        elif args.language == "EN":
            tqdm.write('Encrypting Complete')
        elif args.language == "JP":
            tqdm.write('暗号化完了')
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
        if args.language == "SK":
            tqdm.write('Kontrolujem ...', end='\r')
        elif args.language == "EN":
            tqdm.write('Controling ...', end='\r')
        elif args.language == "JP":
            tqdm.write('制御する ...', end='\r')
        subprocess.check_output(
            'start ' + passwordname + '.py ' + str(name), shell=True)
        while True:
            leave: bool = False
            for i in os.listdir():
                if i == 'DONE':
                    leave: bool = True
                    break
            if leave:
                sleep(0.05)
                break
        os.remove(passwordname + '.py')
        password: str = ''
        for i in open('DONE', 'r').read():
            password += str(i)
        if args.language == "SK":
            tqdm.write('Kontrolujem Hotovo')
        elif args.language == "EN":
            tqdm.write('Controling Complete')
        elif args.language == "JP":
            tqdm.write('制御完了')
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
        if args.language == "SK":
            tqdm.write('Hľadám ...', end='\r')
        elif args.language == "EN":
            tqdm.write('Finding ...', end='\r')
        elif args.language == "JP":
            tqdm.write('発見 ...', end='\r')
        subprocess.check_output(
            'start ' + findname + '.py ' + str(name) + ' ' + str(loginvstupuser), shell=True)
        while True:
            leave: bool = False
            for i in os.listdir():
                if i == 'DONE':
                    leave: bool = True
                    break
            if leave:
                sleep(0.05)
                break
        os.remove(findname + '.py')
        os.remove(name)
        os.remove('DONE')
        test = open(loginvstupuser, 'r')
        end: bool = False
        pocitadlo: int = 0
        for i in test.read():
            pocitadlo += 1
        if 0 <= pocitadlo <= 5:
            test.close()
            if args.language == "SK":
                tqdm.write('Hľadám CHYBA')
            if args.language == "EN":
                tqdm.write('Finding ERROR')
            elif args.language == "JP":
                tqdm.write('発見 エラー')
            end: bool = True
        if end:
            return [loginvstupuser, end]
        test.close()
        if args.language == "SK":
            tqdm.write('Hľadám Hotovo')
        elif args.language == "EN":
            tqdm.write('Finding Complete')
        elif args.language == "JP":
            tqdm.write('発見完了')
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
        if args.language == "SK":
            tqdm.write('Zakoduvávam ...', end='\r')
        elif args.language == "EN":
            tqdm.write('Coding ...', end='\r')
        elif args.language == "JP":
            tqdm.write('コーディング ...', end='\r')
        if mode == 1:
            file = open('1', 'w')
            file.write(str(name) + ' = ' + str(new))
            file.close()
            subprocess.check_output('start ' + codename + '.py 1', shell=True)
        if mode == 0:
            subprocess.check_output(
                'start ' + codename + '.py ' + str(name[0]), shell=True)
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
        elif args.language == "EN":
            tqdm.write('Coding Complete')
        elif args.language == "JP":
            tqdm.write('コーディング 完了')
        os.remove(codename + '.py')
        if mode == 0 and new == 'justcode':
            pass
        elif mode == 0 and new:
            os.remove(loginvstupuser + 'crypted')
            shutil.move(loginvstupuser + 'cryptedcrypted',
                        loginvstupuser + 'crypted')
        elif mode == 0:
            os.remove(loginvstupuser)
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
        if args.language == "SK":
            subject: str = input(
                str(linenumber) + ' Predmet > ')
            historyfile.write(
                '[' + str(linenumber) + ', ' + subject + ']\n')
            subject.lower()
            historyfile.close()
            historyfile = open(historyname, 'a')
            if subject == 'quit':
                exit: bool = True
                return
            if subject == 'back':
                return
            mark: str = input(str(linenumber) + ' Známka > ')
            historyfile.write(
                '[' + str(linenumber) + ', ' + mark + ']\n')
            mark.lower()
            historyfile.close()
            historyfile = open(historyname, 'a')
        elif args.language == "EN":
            subject: str = input(
                str(linenumber) + ' Subject > ')
            historyfile.write(
                '[' + str(linenumber) + ', ' + subject + ']\n')
            vstup.lower()
            historyfile.close()
            historyfile = open(historyname, 'a')
            if subject == 'quit':
                exit: bool = True
                return
            if subject == 'back':
                return
            mark: str = input(str(linenumber) + ' Mark > ')
            historyfile.write(
                '[' + str(linenumber) + ', ' + (mark) + ']\n')
            vstup.lower()
            historyfile.close()
            historyfile = open(historyname, 'a')
        elif args.language == "JP":
            subject: str = input(str(linenumber) + ' 主題 > ')
            historyfile.write(
                '[' + str(linenumber) + ', ' + subject + ']\n')
            vstup.lower()
            historyfile.close()
            historyfile = open(historyname, 'a')
            if subject == 'quit':
                exit: bool = True
                return
            if subject == 'back':
                return
            mark: str = input(str(linenumber) + ' マーク > ')
            historyfile.write(
                '[' + str(linenumber) + ', ' + mark + ']\n')
            vstup.lower()
            historyfile.close()
            historyfile = open(historyname, 'a')
        else:
            subject: str = input(
                str(linenumber) + ' Subject > ')
            historyfile.write(
                '[' + str(linenumber) + ', ' + subject + ']\n')
            vstup.lower()
            historyfile.close()
            historyfile = open(historyname, 'a')
            if subject == 'quit':
                exit: bool = True
                return
            if subject == 'back':
                return
            mark: str = input(str(linenumber) + ' Mark > ')
            historyfile.write(
                '[' + str(linenumber) + ', ' + mark + ']\n')
            vstup.lower()
            historyfile.close()
            historyfile = open(historyname, 'a')
            if subject == 'quit' or mark == 'quit':
                exit: bool = True
                return
            if subject == 'back' or mark == 'back':
                return
            if args.language == "SK":
                Thread(target=progress_bar, args=(
                    'Preverujem', 3,), daemon=True).start()
            elif args.language == "EN":
                Thread(target=progress_bar, args=(
                    'Checking', 3,), daemon=True).start()
            elif args.language == "JP":
                Thread(target=progress_bar, args=(
                    'チェック中', 3,), daemon=True).start()
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
                    if countersubject > 2:
                        countersubject: int = 0
                    counterfirst: bool = True
                    countersubject += 1
                    print(i, end="")
                    if countersubject > 2:
                        typewriter(" | ", end="")

    if __name__ == '__main__':
        logger.stay(printnlog('Function: show_marks', toprint=False))

    def mouseclick(time: int = 0) -> None:
        """
        The mouseclick function is used to click the F11 key on the keyboard.
        This function is useful for maximizing a window.

        :param time: int=0: Make the mouseclick function run for a specified amount of time
        :return: The time it takes to click the mouse
        """

        while True:
            state_left = win32api.GetKeyState(0x01)   # type: ignore
            a = win32api.GetKeyState(0x01)   # type: ignore
            if state_left == -127 or state_left == -128 or time != 0:
                sleep(2 + time)
                pg.press('f11')
                pg.keyDown('ctrl')
                pg.press('w')
                pg.keyUp('ctrl')
                break
            else:
                pass

    if __name__ == '__main__':
        logger.stay(printnlog('Function: mouseclick', toprint=False))

    def playhtml(htmlFile: str, mode: int = 0, time: int = 0):
        """
        The playhtml function is used to open the html file containing the game's intro.
        It can be called in two ways:
            1) playhtml(htmlFile, mode=0, time=0):  # mode = 0 means that it will click through all of the intro automatically. 
                                                    # time = 0 means that it will not wait for a specific amount of time before clicking
                                                    # through each part of the intro.

        :param htmlFile: str: Specify which html file to open
        :param mode: int: Determine whether the function is used to start a new game or load an existing one
        :param time: int: Specify how long the mouseclick function should wait before clicking
        :return: Nothing
        """
        if args.nointro is None or args.nointrof is None:
            args.nointrof = object()
            if args.test is None and config.get('basic info', 'intro').split(' ')[0] == 'True':
                if args.language == 'SK':
                    webbrowser.open(htmlFile + '_sk.html', 1)
                elif args.language == 'EN':
                    webbrowser.open(htmlFile + '.html', 1)
                elif args.language == 'JP':
                    webbrowser.open(htmlFile + '_jp.html', 1)
                sleep(1)
                pg.press('f11')
                if mode == 0:
                    mouseclick()
                elif mode == 1:
                    mouseclick(time=time)
            else:
                pass
        else:
            if config.get('basic info', 'intro').split(' ')[0] == 'True':
                if args.language == 'SK':
                    webbrowser.open(htmlFile + '_sk.html', 1)
                elif args.language == 'EN':
                    webbrowser.open(htmlFile + '.html', 1)
                elif args.language == 'JP':
                    webbrowser.open(htmlFile + '_jp.html', 1)
                sleep(1.5)
                pg.press('f11')
                if mode == 0:
                    mouseclick()
                elif mode == 1:
                    mouseclick(time=time)
                if args.test is not None:
                    window = pygetwindow.getWindowsWithTitle('ZnámE')[0]
                    window.activate()
            else:
                pass

    if __name__ == '__main__':
        logger.stay(printnlog('Function: playhtml', toprint=False))

    if __name__ == '__main__':
        logger.stay(printnlog('Function: game', toprint=False))

    def unpack(cachename: str) -> None:
        """
        The unpack function unpacks the downloaded zip file and extracts the data from it.
        It then moves all of the files to their appropriate locations, deletes any unneeded folders,
        and removes the zip file. It also prints out a progress bar for each step.

        :param cachename: Determine the name of the file to extract from
        :return: :
        """
        with zipfile.ZipFile(cachename, mode='r') as zip:
            if args.language == "SK":
                for member in tqdm(iterable=zip.namelist(), total=len(zip.namelist()), desc='Rozbaľujem '):
                    try:
                        zip.extract(member)
                        tqdm.write(
                            f"{os.path.basename(member)}(" + str(os.path.getsize(member)) + "B)")
                        log(f"{os.path.basename(member)}(" +
                            str(os.path.getsize(member)) + "B)")
                    except zipfile.error as e:
                        pass
            elif args.language == "EN":
                for member in tqdm(iterable=zip.namelist(), total=len(zip.namelist()), desc='Extracting '):
                    try:
                        zip.extract(member)
                        tqdm.write(
                            f"{os.path.basename(member)}(" + str(os.path.getsize(member)) + "B)")
                        log(f"{os.path.basename(member)}(" +
                            str(os.path.getsize(member)) + "B)")
                    except zipfile.error as e:
                        pass
            elif args.language == "JP":
                for member in tqdm(iterable=zip.namelist(), total=len(zip.namelist()), desc='抽出中 '):
                    try:
                        zip.extract(member)
                        tqdm.write(
                            f"{os.path.basename(member)}(" + str(os.path.getsize(member)) + "B)")
                        log(f"{os.path.basename(member)}(" +
                            str(os.path.getsize(member)) + "B)")
                    except zipfile.error as e:
                        pass
            zip.close()
        if args.language == "SK":
            typewriter(printnlog('Hotovo\n', toprint=False))
            typewriter(printnlog("Rozbaľujem druhu časť...\n", toprint=False))
        elif args.language == "EN":
            typewriter(printnlog('Done\n', toprint=False))
            typewriter(printnlog("Unpacking second part...\n", toprint=False))
        elif args.language == "JP":
            typewriter(printnlog('終わり\n', toprint=False))
            typewriter(printnlog("2 番目の部分を解凍しています...\n", toprint=False))
        """
        Extract the data from the xp3 file.
        @param xp3_file - the xp3 file to extract from
        @param output_folder - the folder to extract to
        @param extract_name - the name of the file to extract
        @param language - the language to extract
        """
        if args.language == "SK":
            subprocess.call(
                [sys.executable, 'xp3.py', 'data.xp3', 'data1', '-e', 'neko_vol0_steam'])
        elif args.language == "EN":
            subprocess.call([sys.executable, 'xp3.py', 'data.xp3',
                            'data1', '-e', 'neko_vol0_steam', '-lang', 'EN'])
        elif args.language == "JP":
            subprocess.call([sys.executable, 'xp3.py', 'data.xp3',
                            'data1', '-e', 'neko_vol0_steam', '-lang', 'JP'])
        try:
            shutil.move('data1/data', 'data')
        except Exception:
            pass
        try:
            os.mkdir('apphtml')
        except Exception:
            pass
        try:
            os.mkdir('assets')
        except Exception:
            pass
        if cachename == 'data.xp2':
            for r, d, f in os.walk('data1/apphtml/'):
                for file in f:
                    printnlog(os.path.join('./', file))
                    shutil.move(os.path.join('data1/apphtml/',
                                file), os.path.join('apphtml/', file))
            for r, d, f in os.walk('data1/assets/'):
                for file in f:
                    printnlog(os.path.join('./', file))
                    shutil.move(os.path.join('data1/assets/', file),
                                os.path.join('assets/', file))
            shutil.rmtree('data1/apphtml')
            shutil.rmtree('data1/assets')
            for i in os.listdir('data1'):
                printnlog(i)
                shutil.move(f'data1/{i}', i)
            shutil.rmtree('data1')
        os.remove(cachename)
        os.remove('data.xp3')

    if __name__ == '__main__':
        logger.stay(printnlog('Function: unpack', toprint=False))

    def get_download_path():
        """Returns the default downloads path for linux or windows"""
        if os.name == 'nt':
            import winreg
            sub_key = r'SOFTWARE\Microsoft\Windows\CurrentVersion\Explorer\Shell Folders'
            downloads_guid = '{374DE290-123F-4565-9164-39C4925E467B}'
            with winreg.OpenKey(winreg.HKEY_CURRENT_USER, sub_key) as key:
                location = winreg.QueryValueEx(key, downloads_guid)[0]
            return location
        else:
            return os.path.join(os.path.expanduser('~'), 'downloads')

    if __name__ == '__main__':
        logger.stay(printnlog('Function: get_download_path', toprint=False))

    def spotdl_get():
        lines = []
        sleep(1)
        while not os.path.isfile('SPOTDL_QUIT'):
            for line, content in enumerate(open('SPOTDL_OUTPUT').readlines()):
                if '"GET /api/download/file?file=' in content:
                    if not line in lines:
                        open('SPOTDL_QUEUE', 'x')
                        lines.append(line)
                        content = unquote(content.split('"GET /api/download/file?file=')[1].split('&client_id=')[0])
                        download_path = get_download_path()
                        old_kb = 0
                        new_kb = 0
                        sleep(0.5)
                        while True:
                            new_kb = os.path.getsize(download_path + '/' + content)
                            print(new_kb)
                            if new_kb == old_kb:
                                print('breaked')
                                break
                            sleep(0.25)
                            old_kb = new_kb
                        sleep(2.5)
                        try:
                            shutil.move(download_path + '/' + content, 'assets/' + content.replace(',', ''))
                        except FileNotFoundError:
                            os.remove('SPOTDL_QUEUE')
                            return
                        content = content.replace(',','')
                        content = content.replace('\n','')
                        new_content = ''
                        for i in content.split('.'):
                            if i == content.split('.')[-1]:
                                continue
                            else:
                                new_content += i
                        with open('MUSIC', 'a') as file:
                            file.write(str(new_content) + ',')
                        os.remove('SPOTDL_QUEUE')
        if os.path.isfile('MUSIC'):
            with open('MUSIC', 'r') as file:
                fileread = file.readlines()[0]
            with open('MUSIC', 'w') as file:
                file.write(fileread[:-1])

    if __name__ == '__main__':
        logger.stay(printnlog('Function: spotdl_get', toprint=False))
                    
    def spotMusicDow():
        typewriter('Starting web player', ttime=0.01)
        spotdl = Thread(target=spotdl_get)
        spotdl.start()
        with open('SPOTDL_OUTPUT', 'w') as file:
            subprocess.run(['python' ,'-m' ,'spotdl','web'], stdout=file, text=True)
        sleep(1)
        Thread(target=installing_carousel, args=('',), kwargs={'comment': 'Waiting for synchronization'}).start()
        while os.path.isfile('SPOTDL_QUEUE'):
            sleep(1)
        open('SPOTDL_QUIT', 'x')
        open("INSTALL_DONE", 'x')
        music: list[str] = list(
            set(config.get('basic info', 'musiclist').split(',')[0:]))
        if music[0] == '':
            music = []
        else:
            for i in music:
                if i == '':
                    music.remove('')
        musiclistnewstring: str = ''
        for i in range(len(music)):
            musiclistnewstring += str(music[i]) + ','
        try:
            for line, content in enumerate(open('MUSIC', 'r').readlines()):
                musiclistnewstring += content + ','
        except Exception:
            pass
        try:
            os.remove('MUSIC')
        except Exception:
            pass
        try:
            os.remove('SPOTDL_QUIT')
        except Exception:
            pass
        try:
            os.remove('SPOTDL_OUTPUT')
        except Exception:
            pass
        sleep(1)
        return musiclistnewstring

    if __name__ == '__main__':
        logger.stay(printnlog('Function: spotMusicDow', toprint=False))

    def main() -> None:
        try:
            """
            The main function. This is where the program starts. It is the first function called.
            """
            historyname: str = str(datetime.now().strftime("%H-%M-%S"))
            historyfile = open(historyname, 'w')
            if args.nointrof is None:
                historyfile.write('[*restarted]\n')
            global passwordp
            if args.language == "SK":
                typewriter(printnlog('\nZačínam rozbaľovať\n', toprint=False))
            elif args.language == "EN":
                typewriter(printnlog('\nStarting to extract\n', toprint=False))
            elif args.language == "JP":
                typewriter(printnlog("\n抽出開始\n", toprint=False))
            try:
                datafiles: list = []
                for file in os.listdir("./"):
                    if file.startswith("data"):
                        if file.endswith('.xp2'):
                            datafiles.append(file)
                for i in range(1, len(datafiles)+1):
                    unpack(datafiles[-i])
                shutil.copy('data', 'data_backup')
                if args.language == "SK":
                    printnlog('\nHotovo\n')
                elif args.language == "EN":
                    printnlog('\nDone\n')
                elif args.language == "JP":
                    printnlog('\n完了\n')
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
            if args.language == 'SK':
                typewriter(printnlog('Inicializácia VLC\n', toprint=False))
            elif args.language == 'EN':
                typewriter(printnlog('Initialization VLC\n', toprint=False))
            elif args.language == 'JP':
                typewriter(printnlog('初期化 VLC\n', toprint=False))
            media_player = vlc.MediaPlayer()
            if args.language == 'SK':
                typewriter(printnlog('KONIEC\n', toprint=False))
            elif args.language == 'EN':
                typewriter(printnlog('END\n', toprint=False))
            elif args.language == 'JP':
                typewriter(printnlog('終わり\n', toprint=False))
            from downloadmusic import DownloadMusic  # type: ignore
            print_module('DownloadMusic from downloadmusic')
            from media import PlayVideo, DownloadVideo  # type: ignore
            musiclistnew: list = []
            for i in range(len(music)):
                music_name = music[i]
                print(str(music_name[1]))
                if not os.path.exists('assets/' + str(music_name) + '.mp3'):
                    musiclistnew.append(DownloadMusic(str(music_name)))
                else:
                    musiclistnew.append(music_name)
            move('ZnámE', -10, -10, screensize[0], screensize[1])
            if args.test is not None:
                try:
                    window = pygetwindow.getWindowsWithTitle('ZnámE')[0]
                    window.maximize()
                except IndexError:
                    exit: bool = True
                    error_get(IndexError('Possible solution; run in cmd or python aplication not ide or put arguments \'--test\''), [get_line_number()])
            if args.restart is not None:
                player = vlc.Instance('--fullscreen')
                media_list = player.media_list_new()  # type: ignore
                media_player = player.media_list_player_new()  # type: ignore
                media = player.media_new(
                    "assets/transition.mp4")  # type: ignore
                media_list.add_media(media)
                media_player.set_media_list(media_list)
                media_player.play()
            inactive1: bool = False
            """
            If the INACTIVE file is present, delete it and print a message to the user indicating that they have been logged out.
            @param root - the root directory of the file system
            @param dirs - the directories in the root directory
            @param files - the files in the root directory
            @returns nothing
            """
            try:
                for root, dirs, files in os.walk('..\\'):
                    for i in files:
                        if i == 'INACTIVE':
                            inactive1: bool = True
                            os.remove('INACTIVE')
                            sleep(0.25)
                            if args.language == "SK":
                                printnlog(
                                    'Bol si neaktívny, bol si odhlásený a program sa reštartoval!!!\n')
                            elif args.language == "EN":
                                printnlog(
                                    'You were inactive, you were logged out and the program restarted!!!\n')
                            elif args.language == "JP":
                                printnlog(
                                    '非アクティブでした。ログアウトし、プログラムを再起動しました!!!\n')
                if args.update is None:
                    sleep(0.25)
                    if args.language == "SK":
                        printnlog('Program bol aktualizovaný!!!\n')
                    elif args.language == "EN":
                        printnlog('Program was updated!!!\n')
                    elif args.language == "JP":
                        printnlog('プログラムが更新されました!!!\n')
            except Exception:
                pass
            """
            If the language is Japanese, print a message that tells the user to watch the help file.
            @param args - the command line arguments
            """
            if args.language == 'JP':
                printnlog(
                    "If you don't see any of characters watch 'help.txt'\nインターネット接続がダウンしています\n")
            logged: bool = False
            exit: bool = False
            tologin: bool = False
            restart: bool = False
            topassword: bool = False
            topasswordhelp: bool = False
            loggedhelp: bool = False
            firstlogin: bool = True
            vstup: str = ''
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
            offline_game: bool = False
            maxlogins: int = 1
            """
            If the user has not disabled the intro, play it. Otherwise, do nothing.
            @param None
            @return None
            """
            if args.restart is not None:
                try:
                    sleep(0.1)
                    window = pygetwindow.getWindowsWithTitle(
                        'VLC (Direct3D11 output)')[0]
                    window.activate()
                    window.maximize()
                except Exception:
                    pass
                sleep(2.5)
                mixer.init()
                mixer.music.load('assets/greeting.mp3')
                mixer.music.play()
                sleep(2.5)
                media_player.stop()

            if not inactive1:
                playhtml('apphtml\\start', 1, 3,)
            exit: bool = getWindow()
            if args.nointro is None or config.get('basic info', 'intro').split(' ')[0] == 'False':
                pass
            else:
                window = pygetwindow.getWindowsWithTitle('frame2')[0]
                window.activate()
            getImg('assets/banner.png', 'banner', 0, 0,
                   screensize[0], int((round((322/1736)*screensize[0], 0))))
            move('ZnámE', 0, int((round((322/1736)*screensize[0], 0))-35), screensize[0], screensize[1]-int(
                (round((322/1736)*screensize[0], 0))))
            if args.test is not None:
                try:
                    window = pygetwindow.getWindowsWithTitle('ZnámE')[0]
                    window.activate()
                except IndexError:
                    exit = True
                    error_get(IndexError('Possible solution; run in cmd or python aplication not ide or put arguments \'--test\''), [get_line_number()])
            pg.press('win')
            sleep(0.1)
            pg.press('win')
            os.system('cls')
            if args.music != '0':
                mixer.init()
                mixer.music.load(
                    'assets/' + musiclistnew[int(args.music)-1] + '.mp3')
                mixer.music.play()
            """
                this function prints the version of the program 
            """
            verzia = open('version', 'r')
            if args.language == "SK":
                typewriter('Používate ZnámE ' + verzia.read() + "\n")
            elif args.language == "EN":
                typewriter('You\'re using ZnámE ' + verzia.read() + "\n")
            elif args.language == "JP":
                typewriter('ZnámE を使用しています ' + verzia.read() + "\n")
            verzia.close()
            from completer import SimpleCompleter # type: ignore
            unlogged_completer = ['ffmpeg','animesearch','save','clear','cls','quit', 'quitneko', 'quitwaifu','quitmusic','login', 'delsavlog', 'waifu', 'neko', 'music', 'game', 'offlinegame', 'motivational', 'history', 'help', 'pomoc', '-h', '-help', '?', '-?', 'advanced help', 'ah', '-ah', '-advanced help']
            logged_completer = ['ffmpeg','animesearch','save','clear','cls','quit', 'quitneko', 'quitwaifu','quitmusic','logout', 'delsavlog', 'waifu', 'neko', 'music', 'game', 'offlinegame', 'motivational', 'history', 'help', 'pomoc', '-h', '-help', '?', '-?', 'advanced help', 'ah', '-ah', '-advanced help']
            bq_completer = ['back', 'quit']
            if args.debug == None:
                unlogged_completer.extend(dir())
                logged_completer.extend(dir())
            while True:
                readline.set_completer(SimpleCompleter(unlogged_completer).complete)
                readline.parse_and_bind('tab: complete')
                internet_check()
                if not exit:
                    global loginvstupuser
                    if logged:
                        readline.set_completer(SimpleCompleter(logged_completer).complete)
                        readline.parse_and_bind('tab: complete')
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
                            if savefilemode:   # type: ignore
                                flvstup: str = ''
                                linenumber -= 1
                            elif args.language == "SK":
                                flvstup: str = input(
                                    str(linenumber) + ") Chcete si uložiť svoje prihlasovacie údaje? (y/N) > ")
                            elif args.language == "EN":
                                flvstup: str = input(
                                    str(linenumber) + ") Do you want to save your login credentials? (y/N) > ")
                            elif args.language == "JP":
                                flvstup: str = input(
                                    str(linenumber) + ") ログイン資格情報を保存しますか? (y/N) > ")
                            else:
                                flvstup: str = input(
                                    "Do you want to save your login credentials? (y/N) > ")
                            flvstup.lower()
                            if flvstup == "y":
                                if not os.path.exists("C:/Users/" + os.getlogin() + "/AppData/Local/ZnámE/"):
                                    os.makedirs(
                                        "C:/Users/" + os.getlogin() + "/AppData/Local/ZnámE/")
                                savelog = open(
                                    "C:/Users/" + os.getlogin() + "/AppData/Local/ZnámE/saved", "w")
                                tolog: str = str(code(str(loginvstupuser), str(
                                    passwordp[0]), mode=1))  # type: ignore
                                tolog: str = tolog[2:len(tolog)-2]
                                savelog.write(tolog)
                                savelog.close()
                        """
                        Prints the help menu for the program.
                        @param loggedhelp - whether or not the help menu has been printed already.
                        @param args - the arguments passed to the program.
                        """
                        if loggedhelp:
                            if args.language == "SK":
                                typewriter(
                                    "'zz' pre zobrazenie známok\n'pz' pre pridanie známok")
                            elif args.language == "EN":
                                typewriter(
                                    "'zz' to display marks\n'pz' to add marks")
                            elif args.language == "JP":
                                typewriter('「zz」でマークを表示\n「pz」でマークを追加')
                            loggedhelp: bool = False
                        vstup: str = input(str(linenumber) + ' > ')
                        if args.debug == None:
                            try:
                                print(str(eval(vstup)))
                            except Exception:
                                pass
                        linenumber += 1
                        historyfile.write(
                            '[' + str(linenumber) + ', ' + vstup + ']\n')
                        vstup.lower()
                        historyfile.close()
                        historyfile = open(historyname, 'a')
                        help: list[str] = ['help', 'pomoc',
                                           '-h', '-help', '?', '-?']
                        for i in range(len(help)):
                            if vstup == help[i]:
                                loggedhelp: bool = True
                        if loggedhelp:
                            continue
                        if vstup == 'delsavlog':
                            uninstall()
                        if vstup == "zz":
                            show_marks(passwordp=passwordp)
                        if vstup == "pz":
                            add_marks(
                                linenumber=linenumber, historyname=historyname, neko=neko, waifu=waifu)
                    if topassword:
                        readline.set_completer(SimpleCompleter(bq_completer).complete)
                        readline.parse_and_bind('tab: complete')
                        if savefilemode:   # type: ignore
                            vstup: str = savefile[9:15]   # type: ignore
                            linenumber -= 1
                        elif args.language == "SK":
                            vstup = input(str(linenumber) + ' Heslo > ')
                        elif args.language == "EN":
                            vstup = input(str(linenumber) + ' Password > ')
                        elif args.language == "JP":
                            vstup = input(str(linenumber) + ' パスワード > ')
                        else:
                            vstup = input(str(linenumber) + ' Password > ')
                        linenumber += 1
                        historyfile.write(
                            '[' + str(linenumber) + ', ' + len(vstup)*'*' + ']\n')   # type: ignore
                        vstup.lower()
                        historyfile.close()
                        historyfile = open(historyname, 'a')
                        help: list[str] = ['help', 'pomoc',
                                           '-h', '-help', '?', '-?']
                        for i in range(len(help)):
                            if vstup == help[i]:
                                topasswordhelp: bool = True
                        """
                        If the user has requested help, print the appropriate help message.
                        @param topasswordhelp - the boolean value for requesting help.
                        """
                        if topasswordhelp:
                            if args.language == "SK":
                                typewriter(
                                    "6 číselne heslo\n 'back' pre menu\n 'quit' pre koniec")
                            elif args.language == "EN":
                                typewriter(
                                    "6 numeric password\n 'back' for menu\n 'quit' for end")
                            elif args.language == "JP":
                                typewriter('6桁のパスワード\n メニューの「戻る」\n 終了の「終了」')
                            topasswordhelp: bool = False
                            continue
                        """
                            this function is used to go back to the main menu if the user wants to change their password. 
                        """
                        if vstup == "back":
                            if args.language == "SK":
                                typewriter('Idem späť.')
                            elif args.language == "EN":
                                typewriter('Going back.')
                            elif args.language == "JP":
                                typewriter('戻る。')
                            topassword: bool = False
                            os.remove(loginvstupuser + 'crypted')
                            continue
                        """
                        If the user types quit or koniec, remove the encrypted file and exit the program.
                        @param vstup - the user input
                        @returns nothing
                        """
                        if vstup == "quit" or vstup == "koniec":
                            if args.language == "SK":
                                typewriter("Idem späť a ukončujem program.")
                            elif args.language == "EN":
                                typewriter("Going back and ending program.")
                            elif args.language == "JP":
                                typewriter('戻ってプログラムを終了します。')
                            sleep(0.5)
                            os.remove(loginvstupuser + 'crypted')
                            exit: bool = True
                        if args.language == "SK":
                            Thread(target=progress_bar, args=(
                                'Preverujem', 2,), daemon=True).start()
                        elif args.language == "EN":
                            Thread(target=progress_bar, args=(
                                'Checking', 2,), daemon=True).start()
                        elif args.language == "JP":
                            Thread(target=progress_bar, args=(
                                'チェック中', 2,), daemon=True).start()
                        passwordp = password(
                            decode(loginvstupuser + 'crypted', True))
                        cv2.destroyAllWindows()
                        getWindow()
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
                            if args.language == "SK":
                                typewriter('Si prihlaseny\n')
                            elif args.language == "EN":
                                typewriter('You\'re logged\n')
                            elif args.language == "JP":
                                typewriter('あなたはログインしています\n')
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
                                getWindow()
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
                                if args.language == 'SK':
                                    typewriter(
                                        "Všetko je nastavené!!!\nMôžete použiť program\n")
                                elif args.language == 'EN':
                                    typewriter(
                                        "All is set!!!\nYou can use progam\n")
                                elif args.language == 'JP':
                                    typewriter(
                                        "すべてが設定されました!!!\nプログラムを使用できます\n")
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
                            progress_bar_check = 100
                            sleep(0.1)
                            if args.language == "SK":
                                typewriter("ZLÉ HESLO")
                            elif args.language == "EN":
                                typewriter("WRONG PASSWORD")
                            elif args.language == "JP":
                                typewriter('間違ったパスワード')
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
                            try:
                                print(str(eval(vstup)))
                            except Exception:
                                pass
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
                        config.read('config.ini')
                    if vstup == 'restarted':
                        subprocess.check_output(
                            'start restart.py --autol', shell=True)
                    if vstup == 'playvideo':
                        import playvideo  # type: ignore
                        playvideo.main()
                    if vstup == 'music':
                        mixer.init()
                        musicnone = False
                        if len(musiclistnew) == 0:
                            musicnone = True
                            if args.language == 'EN':
                                typewriter('No audio is downloaded')
                            if args.language == 'SK':
                                typewriter('Nie je stiahnutý žiadny zvuk')
                            if args.language == 'JP':
                                typewriter('オーディオはダウンロードされません')
                            musicvstup: str = input('1) Download music\n2) Back\n> ')
                            if musicvstup == '1':
                                to_append = spotMusicDow().split(',')
                                for item in to_append:
                                    if item == '':
                                        continue
                                    musiclistnew.append(item)
                                try:
                                    os.remove('MUSIC')
                                except Exception:
                                    pass
                                continue
                            elif musicvstup == '2':
                                continue
                        if not musicnone:
                            for i in range(0, len(musiclistnew)):
                                typewriter(str(i + 1) + ') ' + musiclistnew[i])
                            if args.language == 'EN':
                                typewriter(str(i + 2) + ') Delete audio')
                            if args.language == 'SK':
                                typewriter(str(i + 2) + ') Vymaž audio')
                            if args.language == 'JP':
                                typewriter(str(i + 2) + ') 音声を削除')
                            typewriter(str(i + 3) + ') Download music')
                            typewriter(str(i + 4) + ') Back')
                            while True:
                                try:
                                    musicvstup: int = int(input('> '))
                                    break
                                except ValueError:
                                    continue
                        if musicnone or musicvstup == i+3:
                            to_append = spotMusicDow().split(',')
                            for item in to_append:
                                musiclistnew.append(item)
                            try:
                                os.remove('MUSIC')
                            except Exception:
                                pass
                        elif musicvstup == len(musiclistnew) + 1 and not musicnone:  # remove audio
                            if args.language == 'EN':
                                typewriter('Delete audio')
                            if args.language == 'SK':
                                typewriter('Vymaž audio')
                            if args.language == 'JP':
                                typewriter('音声を削除')
                            for i in range(0, len(musiclistnew)):
                                typewriter(str(i + 1) + ') ' + musiclistnew[i])
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
                            while len(musiclistnew) < int(config.get('basic info', 'musicnumber')):
                                set_config('basic info', 'musicnumber',
                                           str(int(args.music)-1))
                                continue
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
                                musicplay: bool = True
                            except Exception:
                                pass
                    if vstup == 'quitmusic':
                        try:
                            mixer.music.stop()
                            musicplay: bool = False
                        except Exception:
                            pass
                    if vstup == 'save':
                        if waifu or neko or waifuvid:
                            imagetime: str = str(
                                datetime.now().strftime("%H-%M-%S"))
                            try:
                                os.mkdir('download/')
                                typewriter(
                                    'Making directory \'download\'', end='\r', ttime=0.01)
                            except Exception:
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
                            if args.language == 'SK':
                                typewriter('Nemáte obrázok na uloženie', ttime=0.01)
                            elif args.language == 'EN':
                                typewriter("You don't have image to save", ttime=0.01)
                            elif args.language == 'JP':
                                typewriter('保存する画像がありません', ttime=0.01)
                    if vstup == 'offlinegame':
                        offline_game: bool = True
                        import game_assets  # type: ignore
                        game_assets.create_gamefiles()
                    if vstup == 'restart':
                        restart: bool = True
                        exit: bool = True
                        continue
                    if vstup == 'game':
                        if waifu or waifuvid or neko:
                            if args.language == 'SK':
                                typewriter(
                                    'Najprv musíte ukončiť neko alebo waifu')
                            if args.language == 'EN':
                                typewriter(
                                    'First you need to quit neko or waifu')
                            if args.language == 'JP':
                                typewriter('まず、nekoまたはwaifuを終了する必要があります')
                            continue
                        mixer.music.pause()
                        import game_assets  # type: ignore
                        print_module()
                        game_assets.game()
                        mixer.music.unpause()
                        os.system('title ZnámE')
                        os.system('cls')
                        verzia = open('version', 'r')
                        if args.language == "SK":
                            typewriter('Používate ZnámE ' +
                                       verzia.read() + "\n")
                        elif args.language == "EN":
                            typewriter('You\'re using ZnámE ' +
                                       verzia.read() + "\n")
                        elif args.language == "JP":
                            typewriter('ZnámE を使用しています ' +
                                       verzia.read() + "\n")
                        verzia.close()
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
                            if args.language == 'SK':
                                typewriter('Prepáč, že nemôžeš mať dve neko', ttime=0.01)
                            elif args.language == 'EN':
                                typewriter("Sorry you can't have two nekos", ttime=0.01)
                            elif args.language == 'JP':
                                typewriter('ごめんね、ネコを2匹飼えないよ', ttime=0.01)
                            continue
                        if waifu:
                            if args.language == 'SK':
                                typewriter(
                                    'Prepáčte, že nemôžete mať neko, ak máte waifu', ttime=0.01)
                            elif args.language == 'EN':
                                typewriter(
                                    "Sorry you can't have neko if you have waifu", ttime=0.01)
                            elif args.language == 'JP':
                                typewriter('すみません、ワイフを持っているならネコを持ってはいけない', ttime=0.01)
                            continue
                        if args.language == 'SK':
                            typewriter('ČAKAJ', ttime=0.01)
                        elif args.language == 'EN':
                            typewriter('WAIT', ttime=0.01)
                        elif args.language == 'JP':
                            typewriter('待つ', ttime=0.01)
                        if args.neko is not None:
                            if config.get('neko settings', 'server').split(' ')[0] == 'nekos.best':
                                if args.language == 'SK':
                                    typewriter(
                                        'Získavanie obrazu zo servera nekos.best', ttime=0.01)
                                elif args.language == 'EN':
                                    typewriter(
                                        'Getting image from nekos.best server', ttime=0.01)
                                elif args.language == 'JP':
                                    typewriter('nekos.best サーバーから画像を取得する', ttime=0.01)
                                resp = requests.get(
                                    "https://nekos.best/api/v2/neko")
                                data: dict[str, str] = resp.json()
                                res = requests.get(
                                    data["results"][0]["url"], stream=True)  # type: ignore
                            elif config.get('neko settings', 'server').split(' ')[0] == 'waifu.pics':
                                if args.language == 'SK':
                                    typewriter(
                                        'Získavanie obrazu zo servera waifu.pics', ttime=0.01)
                                elif args.language == 'EN':
                                    typewriter(
                                        'Getting image from waifu.pics server', ttime=0.01)
                                elif args.language == 'JP':
                                    typewriter('waifu.pics サーバーから画像を取得する', ttime=0.01)
                                resp = requests.get(
                                    "https://api.waifu.pics/sfw/neko")
                                data: dict[str, str] = resp.json()
                                res = requests.get(data["url"], stream=True)
                            elif config.get('neko settings', 'server').split(' ')[0] == 'kyoko':
                                if args.language == 'SK':
                                    typewriter(
                                        'Získavanie obrazu zo servera kyoko', ttime=0.01)
                                elif args.language == 'EN':
                                    typewriter(
                                        'Getting image from kyoko server', ttime=0.01)
                                elif args.language == 'JP':
                                    typewriter('kyoko サーバーから画像を取得する', ttime=0.01)
                                resp = requests.get(
                                    "https://kyoko.rei.my.id/api/sfw.php")
                                data: dict[str, str] = resp.json()
                                res = requests.get(data["apiResult"]["url"][0], stream=True)
                            elif config.get('neko settings', 'server').split(' ')[0] == 'nekos_api':
                                if args.language == 'SK':
                                    typewriter(
                                        'Získavanie obrazu zo servera nekos_api', ttime=0.01)
                                elif args.language == 'EN':
                                    typewriter(
                                        'Getting image from nekos_api server', ttime=0.01)
                                elif args.language == 'JP':
                                    typewriter('nekos_api サーバーから画像を取得する', ttime=0.01)
                                resp = requests.get(
                                    "https://nekos.nekidev.com/api/image/random?categories=catgirl")
                                data: dict[str, str] = resp.json()
                                res = requests.get(data["data"][0]["url"], stream=True)
                            else:
                                if args.language == 'SK':
                                    typewriter(
                                        'Nie je poskytnutý žiadny server', ttime=0.01)
                                elif args.language == 'EN':
                                    typewriter('No server provided', ttime=0.01)
                                elif args.language == 'JP':
                                    typewriter('サーバーが提供されていません', ttime=0.01)
                                continue
                            typewriter('Downloading image', ttime=0.01)
                            if res.status_code == 200:
                                if config.get('neko settings', 'server').split(' ')[0] == 'nekos.best':
                                    download(data["results"][0]
                                             ["url"], 'assets/neko.png')
                                elif config.get('neko settings', 'server').split(' ')[0] == 'waifu.pics':
                                    download(data['url'], 'assets/neko.png')
                                elif config.get('neko settings', 'server').split(' ')[0] == 'kyoko':
                                    download(data["apiResult"]["url"][0], 'assets/neko.png')
                                elif config.get('neko settings', 'server').split(' ')[0] == 'nekos_api':
                                    download(data["data"][0]["url"], 'assets/neko.png')
                        else:
                            args.neko = object()
                        typewriter('Setting image          ', end='\r', ttime=0.01)
                        img = Image.open('assets/neko.png')
                        typewriter('Opening image          ', end='\r', ttime=0.01)
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
                        typewriter('Getting cli in foreground     ', end='\r', ttime=0.01)
                        if args.test is not None:
                            window = pygetwindow.getWindowsWithTitle('ZnámE')[
                                0]
                            window.activate()
                        mixer.Channel(0).play(mixer.Sound('assets/neko.mp3'))
                        typewriter('Playing sound                 ', end='\r', ttime=0.01)
                        sleep(0.5)
                        if args.language == 'SK':
                            typewriter('HOTOVO         ')
                        elif args.language == 'EN':
                            typewriter('DONE           ')
                        elif args.language == 'JP':
                            typewriter('終わり          ')
                        move("ZnámE", 0, int((round((322/1736)*screensize[0], 0))-35), int(screensize[0]/2), int(
                            (round((0.95-(0.31203703703703706))*screensize[1], 0))))  # 337/1080
                        neko = True
                    if vstup == 'quitneko':
                        if not neko:
                            if args.language == 'SK':
                                typewriter(':( Nemôžeš mať -1 neko', ttime=0.01)
                            elif args.language == 'EN':
                                typewriter(":( You can't have -1 neko", ttime=0.01)
                            elif args.language == 'JP':
                                typewriter(':( 猫を-1にすることはできません', ttime=0.01)
                            continue
                        typewriter('Closing image', end='\r', ttime=0.01)
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
                            if args.language == 'SK':
                                typewriter('Prepáčte, nemôžete mať dve waifu', ttime=0.01)
                            elif args.language == 'EN':
                                typewriter("Sorry you can't have two waifu", ttime=0.01)
                            elif args.language == 'JP':
                                typewriter('申し訳ありませんが、ワイフを 2 つ持つことはできません', ttime=0.01)
                            continue
                        if neko:
                            if args.language == 'SK':
                                typewriter(
                                    'Prepáčte, ale nemôžete mať waifu a neko', ttime=0.01)
                            elif args.language == 'EN':
                                typewriter(
                                    "Sorry you can't have waifu and neko", ttime=0.01)
                            elif args.language == 'JP':
                                typewriter('ごめんなさい、ワイフとネコは使えません', ttime=0.01)
                            continue
                        if args.language == 'SK':
                            typewriter('ČAKAJ', ttime=0.01)
                        elif args.language == 'EN':
                            typewriter('WAIT', ttime=0.01)
                        elif args.language == 'JP':
                            typewriter('待つ', ttime=0.01)
                        if args.waifu is not None:
                            if args.language == 'SK':
                                typewriter(
                                    'Získavanie obrazu zo servera waifu.pics', ttime=0.01)
                            elif args.language == 'EN':
                                typewriter(
                                    'Getting image from waifu.pics server', ttime=0.01)
                            elif args.language == 'JP':
                                typewriter('waifu.pics サーバーから画像を取得する', ttime=0.01)
                            resp = requests.get("https://api.waifu.pics/" + config.get('waifu settings', 'type').split(
                                ' ')[0] + "/" + config.get('waifu settings', 'category').split(' ')[0])
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
                                player = vlc.Instance('--input-repeat=999999')
                                media_list = player.media_list_new()  # type: ignore
                                media_player = player.media_list_player_new()  # type: ignore
                                media = player.media_new(
                                    "assets/waifu.mp4")  # type: ignore
                                media_list.add_media(media)
                                media_player.set_media_list(media_list)
                                player.vlm_set_loop(
                                    "waifu", True)  # type: ignore
                                media_player.play()
                                waifuvid: bool = True
                                sleep(1)
                            elif data["url"].split('.')[-1] != 'gif':
                                res = requests.get(data["url"], stream=True)
                                if res.status_code == 200:
                                    download(data['url'], 'assets/waifu.png')
                        elif args.waifuvid is None:
                            data: dict[str, str] = {
                                'url': 'https://api.waifu.pics/waifu.mp4'}
                            waifuvid: bool = True
                            player = vlc.Instance('--input-repeat=999999')
                            media_list = player.media_list_new()  # type: ignore
                            media_player = player.media_list_player_new()  # type: ignore
                            media = player.media_new(
                                "assets/waifu.mp4")  # type: ignore
                            media_list.add_media(media)
                            media_player.set_media_list(media_list)
                            player.vlm_set_loop("waifu", True)  # type: ignore
                            media_player.play()
                            args.waifu = UNSPECIFIED
                            sleep(1)
                        elif args.waifu is None:
                            args.waifu = UNSPECIFIED
                            data: dict[str, str] = {
                                'url': 'https://api.waifu.pics/waifu.png'}
                        typewriter('Setting image    ', end='\r', ttime=0.01)
                        if data["url"].split('.')[-1] != 'gif' and data["url"].split('.')[-1] != 'mp4':
                            img = Image.open('assets/waifu.png')
                            typewriter('Opening image   ', end='\r', ttime=0.01)
                            img.show()
                        elif data["url"].split('.')[-1] == 'gif' or data["url"].split('.')[-1] == 'mp4':
                            sleep(0.2)
                            typewriter('Getting video in foreground', end='\r', ttime=0.01)
                            window = pygetwindow.getWindowsWithTitle(
                                'VLC (Direct3D11 Output)')[0]
                            window.activate()
                            sleep(0.1)
                        sleep(0.1)
                        pg.keyDown('win')
                        typewriter('......                        ', end='\r', ttime=0.01)
                        pg.press('right')
                        typewriter('.......', end='\r', ttime=0.01)
                        pg.keyUp('win')
                        typewriter('........', end='\r', ttime=0.01)
                        pg.press('esc')
                        typewriter('Getting cli in foreground', end='\r', ttime=0.01)
                        if args.test is not None:
                            window = pygetwindow.getWindowsWithTitle('ZnámE')[0]
                            window.activate()
                        sleep(0.5)
                        typewriter('..........                  ', end='\r', ttime=0.01)
                        sleep(0.25)
                        typewriter('.............', end='\r', ttime=0.01)
                        if args.language == 'SK':
                            typewriter('HOTOVO         ', ttime=0.01)
                        elif args.language == 'EN':
                            typewriter('DONE           ', ttime=0.01)
                        elif args.language == 'JP':
                            typewriter('終わり          ', ttime=0.01)
                        move("ZnámE", 0, int((round((322/1736)*screensize[0], 0))-35), int(screensize[0]/2), int(
                            (round((0.95-(0.31203703703703706))*screensize[1], 0))))  # 337/1080
                        waifu: bool = True
                    if vstup == 'quitwaifu':
                        if not waifu:
                            if args.language == 'SK':
                                typewriter(':( Nemôžeš mať -1 waifu', ttime=0.01)
                            elif args.language == 'EN':
                                typewriter(":( You can't have -1 waifu", ttime=0.01)
                            elif args.language == 'JP':
                                typewriter(':( -1ワイフを持つことはできません', ttime=0.01)
                            continue
                        elif waifuvid:
                            typewriter('Stoping video', end='\r', ttime=0.01)
                            media_player.stop()  # type: ignore
                            waifuvid: bool = False
                            typewriter('Removing video   ', end='\r', ttime=0.01)
                            os.remove('assets/waifu.mp4')
                        else:
                            typewriter('Closing image', end='\r', ttime=0.01)
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
                        typewriter('Resizing cli      ', end='\r', ttime=0.01)
                        move('ZnámE', 0, int((round((322/1736)*screensize[0], 0))-35), screensize[0], screensize[1]-int(
                            (round((322/1736)*screensize[0], 0))))
                        try:
                            typewriter('Removing image', end='\r', ttime=0.01)
                            os.remove('assets/waifu.png')
                        except Exception:
                            pass
                        waifu: bool = False
                        typewriter('Done               ', ttime=0.01)
                    if vstup == 'animesearch':
                        import anime_search  # type: ignore
                        anime_search.main()
                    if vstup == 'delsavlog':
                        uninstall()
                    """
                    Clear the screen.
                    @param vstup - the input from the user.
                    """
                    if vstup == 'clear' or vstup == 'cls':
                        os.system('cls')
                        verzia = open('version', 'r')
                        if args.language == "SK":
                            print('Používate ZnámE ' + verzia.read() + "\n")
                        elif args.language == "EN":
                            print('You\'re using ZnámE ' +
                                  verzia.read() + "\n")
                        elif args.language == "JP":
                            print('ZnámE を使用しています ' + verzia.read() + "\n")
                        verzia.close()
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
                    @param args.language - the language of the program.
                    @param history - the file that contains the history of the user.
                    @param linenumber - the line number of the history file.
                    """
                    if logged and vstup == "logout" and not restart:
                        logged: bool = False
                        os.remove(loginvstupuser)
                        os.remove(passwordp[1])  # type: ignore
                        if args.language == "SK":
                            print("Si odhlásený")
                        elif args.language == "EN":
                            print("You\'re logged out")
                        elif args.language == "JP":
                            print('ログアウトしました')
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
                        if args.language == "SK":
                            print("Si odhlásený")
                        elif args.language == "EN":
                            print("You\'re logged out")
                        elif args.language == "JP":
                            print('ログアウトしました')
                        continue
                    """
                    If the user is not logged in, print an error message and continue.           
                    """
                    if not logged and vstup == "logout" or inactivelogout:
                        logged: bool = False
                        if args.language == "SK":
                            print('Nie si prihlásený!!!')
                        elif args.language == "EN":
                            print("You\'re not logged in!!!")
                        elif args.language == "JP":
                            print('ログインしていません!!!')
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
                                advhelpfile = open(
                                    'Help.txt', 'r', encoding='UTF-8')
                                for i in advhelpfile.readlines():
                                    if advhelpcont:
                                        for j in language:
                                            if i == j + '\n':
                                                if j == args.language:
                                                    break
                                                else:
                                                    advhelpcont = False
                                                    break
                                        if not advhelpcont:
                                            break
                                        if i == "":
                                            continue
                                        print(i, end="")
                                        continue
                                    if i == args.language + '\n':
                                        advhelpcont: bool = True
                                        print(i, end="")
                                        continue
                                advhelpfile.close()
                        for i in range(len(help)):
                            if vstup == help[i]:
                                if args.language == "SK":
                                    print("'login' pre prihlásenie\n'logout' pre odhlásenie\n'quit' alebo 'koniec' pre koniec\n'delsavlog' pre vymazanie autoprihlasenia\n\nKeď chceš zmeniť jazyk programu v terminalu do commandu pridaj '-lang EN' or '-lang SK'\n\nPre podrobnejšiu pomoc napíš '-ah' alebo '-advanced help' alebo 'ah' alebo 'advanced help'\n'history' zobrazuje vašu aktuálne uloženú históriu\n\'waifu\' pre waifu\n\'neko\' pre neko\n\'motivational\' pre motivačnú hlášku\n\'game\' pre hru\n\'music\' pre hudbu\n\'quit***\' if you want to quit music use \'quitmusic\' if you want to quit waifu \'quitwaifu\' if you want to quit neko \'quitneko\'")
                                elif args.language == "EN":
                                    print("'login' for login\n'logout' for logout\n'quit' or 'end' for end\n'delsavlog' to clear autologin\n\nWhen you want to change the language of the program in the terminal, add '-lang EN' or '-lang SK' to the command\n\nFor more detailed help, type '-ah' or '-advanced help' or 'ah' or 'advanced help'\n'history' show your currently saved history\'waifu\' for waifu\n\'neko\' for neko\n\'motivational\' for motivational message\n\'game\' for game\n\'music\' for music\n\'quit* **\' to quit music use \'quitmusic\' if you want to quit waifu \'quitwaifu\' if you want to quit neko \'quitneko\'")
                                elif args.language == "JP":
                                    print("ログインの場合は「login」\nログアウトの場合は「logout」\n終了の場合は「quit」または「end」\n自動ログインをクリアする「delsavlog」\n\nターミナルでプログラムの言語を変更する場合は、「-lang EN」または「-lang」を追加します コマンドに SK'\n\n詳細なヘルプを表示するには、'-ah' または '-advanced help' または 'ah' または 'advanced help' と入力してください'\n「history」は、現在保存されている履歴を表示します\'waifu\' for waifu\n\'neko\' for neko\n\'motivational\' for motivational message\n\'game\' for game\n\'music\' for music\n\'quit* **\' to quit music use \'quitmusic\' if you want to quit waifu \'quitwaifu\' if you want to quit neko \'quitneko\'")
                                continue
                        """
                        Print the history of the user.
                        @param args - the command line arguments
                        """
                        if vstup == 'history':
                            historylist = config.items('user history')
                            for i in historylist:
                                if args.language == 'SK':
                                    print(
                                        'Čas začiatku = ' + i[0] + ', Čas ukončenia = ' + i[1][0:26] + ', Vstup = ' + i[1][26:])
                                elif args.language == 'EN':
                                    print(
                                        'Start time = ' + i[0] + ', End time = ' + i[1][0:26] + ', Input = ' + i[1][26:])
                                elif args.language == 'JP':
                                    print(
                                        '開始時間 = ' + i[0] + '、終了時間 = ' + i[1][0:26] + '、入力 = ' + i[1][26:])
                            if len(historylist) == 0:
                                if args.language == 'SK':
                                    print('História je prázdna')
                                elif args.language == 'EN':
                                    print('History is empty')
                                elif args.language == 'JP':
                                    print('履歴が空です')
                        if vstup == 'login' and not logged or tologin and not logged:
                            readline.set_completer(SimpleCompleter(bq_completer).complete)
                            readline.parse_and_bind('tab: complete')
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
                                if args.language == "SK":
                                    vstup = input(
                                        "Ak sa chcete prihlásiť, musíte reštartovať program (Y/n) >")
                                elif args.language == "EN":
                                    vstup = input(
                                        "If you want to login you need to restart program (Y/n) > ")
                                elif args.language == "JP":
                                    vstup = input(
                                        "ログインするには、プログラムを再起動する必要があります (Y/n) >")
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
                                if args.language == "SK":
                                    loginvstupuser = input(
                                        str(linenumber) + " Chcete sa automaticky prihlásiť? (Y/n) > ")
                                    linenumber += 1
                                elif args.language == "EN":
                                    loginvstupuser = input(
                                        str(linenumber) + " Do you want to auto-login? (Y/n) > ")
                                    linenumber += 1
                                elif args.language == "JP":
                                    loginvstupuser = input(
                                        str(linenumber) + " 自動ログインしますか？ (Y/n) > ")
                                    linenumber += 1
                                loginvstupuser.lower()
                                if loginvstupuser == "" or loginvstupuser == "y":
                                    savefilemode: bool = True
                            if savefilemode:
                                loginvstupuser = savefile[0:6]   # type: ignore
                            elif args.language == "SK":
                                loginvstupuser = input(
                                    str(linenumber) + " Prihlasovacie číslo (PID) > ")
                            elif args.language == "EN":
                                loginvstupuser = input(
                                    str(linenumber) + " Login Number (PID) > ")
                            elif args.language == "JP":
                                loginvstupuser = input(
                                    str(linenumber) + " ログイン番号 (PID) > ")
                            historyfile.write(
                                '[' + str(linenumber) + ', ' + loginvstupuser + "]\n")
                            historyfile.close()
                            historyfile = open(historyname, 'a')
                            linenumber += 1
                            tologinhelp: bool = False
                            if loginvstupuser == "back":
                                if args.language == "SK":
                                    print('Idem späť.')
                                elif args.language == "EN":
                                    print('Going back.')
                                elif args.language == "JP":
                                    print('戻る。')
                                continue
                            """
                            If the user types quit or koniec, then go back to the main menu. Otherwise, continue.
                            @param loginvstupuser - the user's input for the login/signup menu
                            @returns the user's input for the login/signup menu
                            """
                            if loginvstupuser == "quit" or loginvstupuser == "koniec":
                                if args.language == "SK":
                                    print("Idem späť a ukončujem program.")
                                elif args.language == "EN":
                                    print("Going back and exiting the program.")
                                elif args.language == "JP":
                                    print('戻ってプログラムを終了します。')
                                sleep(0.5)
                                exit: bool = True
                                continue
                            help: list[str] = ['help', 'pomoc',
                                               '-h', '-help', '?', '-?']
                            for i in range(len(help)):
                                if loginvstupuser == help[i]:
                                    tologinhelp: bool = True
                            if tologinhelp:
                                if args.language == "SK":
                                    print(
                                        "'back' pre menu\n'quit' alebo 'koniec' pre koniec")
                                elif args.language == "EN":
                                    print(
                                        "'back' for menu\n'quit' or 'end' for end")
                                elif args.language == "JP":
                                    print("メニューの「戻る」\n 'quit' または 'end' で終了")
                                tologin: bool = True
                                continue
                            elif not loginvstupuser.isnumeric():
                                if args.language == "SK":
                                    print('PID neobsahuje písmená alebo znaky!!!')
                                elif args.language == "EN":
                                    print(
                                        'The PID does not contain letters or characters!!!')
                                elif args.language == "JP":
                                    print('PID に文字が含まれていません!!!')
                                tologin: bool = True
                                continue
                            if len(str(loginvstupuser)) == 6:
                                exit: bool = False
                                if args.language == "SK":
                                    Thread(target=progress_bar, args=(
                                        'Preverujem', 3,), daemon=True).start()
                                elif args.language == "EN":
                                    Thread(target=progress_bar, args=(
                                        'Checking', 3,), daemon=True).start()
                                elif args.language == "JP":
                                    Thread(target=progress_bar, args=(
                                        'チェック中', 3,), daemon=True).start()
                                icofind = code(
                                    find(decode(True, False)), False)
                                cv2.destroyAllWindows()
                                getWindow()
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
                                    if args.language == "SK":
                                        print("ZLÉ PID!!!")
                                    elif args.language == "EN":
                                        print("WRONG PID!!!")
                                    elif args.language == "JP":
                                        print('間違った PID !!!')
                                    tologin: bool = True
                                    continue
                                topassword: bool = True
                            else:
                                if args.language == "SK":
                                    print('PID má byt 6 čísel dlhé!!!')
                                elif args.language == "EN":
                                    print('The PID should be 6 numbers long!!!')
                                elif args.language == "JP":
                                    print('PID は 6 桁の長さでなければなりません!!!')
                                tologin: bool = True
                        elif logged and vstup == 'login':
                            if args.language == "SK":
                                print('Už si prihlasení!!!')
                            elif args.language == "EN":
                                print('You are already logged in!!!')
                            elif args.language == "JP":
                                print('すでにログインしています！！！')
                elif vstup == 'quit' or vstup == 'koniec' or vstup == 'end' or exit:
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
                        move('ZnámE', 0, int((round((322/1736)*screensize[0], 0))-35), screensize[0], screensize[1]-int(
                            (round((322/1736)*screensize[0], 0))))
                    try:
                        media_player.stop()  # type: ignore
                    except Exception:
                        pass
                    try:
                        mixer.music.unload()
                        mixer.music.stop()
                    except Exception:
                        pass
                    if not restart:
                        try:
                            os.remove('assets/neko.png')
                        except Exception:
                            pass
                        try:
                            os.remove('assets/waifu.png')
                        except Exception:
                            pass
                        try:
                            os.remove('assets/waifu.gif')
                        except Exception:
                            pass
                        try:
                            os.remove('assets/waifu.mp4')
                        except Exception:
                            pass
                        try:
                            os.remove('assets/video.mp4')
                        except Exception:
                            pass
                        try:
                            os.remove('MUSIC')
                        except Exception:
                            pass
                        try:
                            shutil.rmtree('anime_search')
                        except Exception:
                            pass
                    if not offline_game:
                        try:
                            shutil.rmtree('game')
                        except Exception:
                            pass
                        try:
                            os.remove('game.py')
                        except Exception:
                            pass
                    try:
                        open('END', 'x')
                    except Exception:
                        pass
                    if logged:
                        try:
                            sleep(0.25)
                            os.remove(loginvstupuser)
                            os.remove(passwordp[1])  # type: ignore
                        except Exception:
                            pass
                        if args.language == "SK":
                            typewriter("\nSi odhlásený\n")
                        elif args.language == "EN":
                            typewriter('\nYou are logged out\n')
                        elif args.language == "JP":
                            typewriter('\nログアウトしました\n')
                        historyfile.write(
                            '[' + str(linenumber) + ', ' + '*logout]\n')
                        historyfile.close()
                        historyfile = open(historyname, 'a')
                        loginvstupuser = ''
                        sleep(0.5)
                    historyfile.close()
                    if args.language == "SK":
                        logger.stay(
                            "ODSTRAŇOVANIE NEPOTREBNÝCH SÚBOROV\nPísanie histórie\n")
                    elif args.language == "EN":
                        logger.stay(
                            "DELETING UNNECESSARY FILES\nWriting history\n")
                    elif args.language == "JP":
                        logger.stay('不要なファイルを削除しています\n執筆履歴\n')
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
                        for i in historyfile.readlines():
                            historylist.append(i.strip('\n'))
                    except Exception:
                        pass
                    musiclistnewstring: str = ''
                    for i in range(len(musiclistnew)):
                        musiclistnewstring += str(musiclistnew[i]) + ','
                    set_config('user history', historyname, str(
                        datetime.today().strftime("%d-%m-%Y__time__%H-%M-%S")) + str(historylist))
                    set_config('basic info', 'musiclist',
                               str(musiclistnewstring[0:-1]))
                    logger.next(historyname + ' ' + str(
                        datetime.today().strftime("%d-%m-%Y__time__%H-%M-%S")) + str(historylist) + '\n')
                    historyfile.close()
                    try:
                        os.remove(historyname)
                    except Exception:
                        pass
                    if args.language == "SK":
                        logger.prev("Hotovo\n")
                    elif args.language == "EN":
                        logger.prev("Done\n")
                    elif args.language == "JP":
                        logger.prev('終わり\n')
                    pg.screenshot().save('bg.png')
                    shutil.move('assets/green.mp4', 'green.mp4')
                    os.system("ffmpeg -i bg.png -i green.mp4 -map 1:a -c:a copy -filter_complex [1:v]colorkey=0x000000:0.01:0.7[ckout];[0:v][ckout]overlay[out] -map [out] output.mp4")
                    os.remove('bg.png')
                    shutil.move('green.mp4', 'assets/green.mp4')
                    player = vlc.Instance('--fullscreen')
                    media_list = player.media_list_new()  # type: ignore
                    media_player = player.media_list_player_new()  # type: ignore
                    media = player.media_new("output.mp4")  # type: ignore
                    media_list.add_media(media)
                    media_player.set_media_list(media_list)
                    media_player.play()
                    sleep(0.5)
                    if args.test != None:
                        window = pygetwindow.getWindowsWithTitle('ZnámE')[0]
                        window.activate()
                        window.maximize()
                    sleep(5)
                    media_player.stop()
                    os.remove('output.mp4')
                    playhtml('apphtml\\end', 1, 3)
                    try:
                        os.remove('data_backup')
                    except Exception:
                        pass
                    try:
                        os.mkdir('datafolder')
                    except FileExistsError:
                        pass
                    try:
                        shutil.move('data', 'datafolder/')
                    except Exception:
                        quit()
                    source_dir: str = 'assets/'
                    os.mkdir('datafolder/' + source_dir)
                    for file_name in os.listdir(source_dir):
                        shutil.move(os.path.join(source_dir, file_name),
                                    'datafolder/' + source_dir)
                    source_dir: str = 'apphtml/'
                    os.mkdir('datafolder/' + source_dir)
                    for file_name in os.listdir(source_dir):
                        shutil.move(os.path.join(source_dir, file_name),
                                    'datafolder/' + source_dir)
                    files: list = ['downloadmusic.py', 'anime_search.py',
                                   'playvideo.py', 'settings.py', 'media.py', 'game_assets.py', 'completer.py']
                    for i in files:
                        shutil.move(i, f'datafolder/{i}')
                    if args.language == "SK":
                        logger.stay("ZABAĽUJEM DATA\n")
                        subprocess.call([sys.executable, 'xp3.py', 'datafolder',
                                        'data.xp3', '-mode', 'repack', '-e', 'neko_vol0_steam'])
                    elif args.language == "EN":
                        logger.stay("PACKING DATA\n")
                        subprocess.call([sys.executable, 'xp3.py', 'datafolder', 'data.xp3',
                                        '-mode', 'repack', '-e', 'neko_vol0_steam', '-lang', 'EN'])
                    elif args.language == "JP":
                        logger.stay("梱包データ\n")
                        subprocess.call([sys.executable, 'xp3.py', 'datafolder', 'data.xp3',
                                        '-mode', 'repack', '-e', 'neko_vol0_steam', '-lang', 'JP'])
                    shutil.rmtree('datafolder')
                    shutil.rmtree('apphtml')
                    shutil.rmtree('assets')
                    if args.language == "SK":
                        logger.stay("HOTOVO")
                        cv2.destroyAllWindows()
                        logger.stay("ZABAĽUJEM DRUHÚ ČASŤ DATA")
                    elif args.language == "EN":
                        logger.stay("COMPLETE")
                        cv2.destroyAllWindows()
                        logger.stay("PACKING SECOND PART OF DATA")
                    elif args.language == "JP":
                        logger.stay("完了")
                        cv2.destroyAllWindows()
                        logger.stay("データの 2 番目の部分のパッキング")
                    zipfiles: list[str] = ['tests.py', 'xp3.py',
                                           'xp3reader.py', 'xp3writer.py', 'data.xp3']
                    zipfileswopath: list[str] = ['tests.py', 'xp3.py',
                                                 'xp3reader.py', 'xp3writer.py', 'data.xp3']
                    folders: list[str] = ['structs']
                    for i in range(0, len(folders)):
                        for path, directories, files in os.walk(folders[i]):
                            for file in files:
                                file_name: str = os.path.join(path, file)
                                zipfiles.append(file_name)
                                zipfileswopath.append(file)
                    logger.next('')
                    with zipfile.ZipFile(cachename, mode='w', compresslevel=5) as zip:
                        zip_kb_old: int = 0
                        zipfilesnumber: int = len(zipfiles)
                        if args.language == "SK":
                            bar = tqdm(range(0, len(zipfiles)),
                                       desc="Zabaľujem ")
                            for i in bar:
                                zip.write(zipfiles[i])
                                filesizesk: int = sum(
                                    [zinfo.file_size for zinfo in zip.filelist])
                                tqdm.write(logger.stay(zipfileswopath[i] + "(" + str(os.path.getsize(
                                    zipfiles[i])) + " KB) -> " + str(round(filesizesk - zip_kb_old, 2)) + " KB", end='', toprint=False))
                                zip_kb_old: int = filesizesk
                                os.remove(zipfiles[i])
                                if i == len(zipfiles)-1:
                                    tqdm.write("\n")
                            filesizeskend: int = sum(
                                [zinfo.file_size for zinfo in zip.filelist])
                            logger.prev("\nZabalené data majú > " +
                                       str(filesizeskend) + " KB")
                        elif args.language == "EN":
                            bar = tqdm(range(0, len(zipfiles)),
                                       desc="Packing ")
                            for i in bar:
                                zip.write(zipfiles[i])
                                filesizeen: int = sum(
                                    [zinfo.file_size for zinfo in zip.filelist])
                                tqdm.write(logger.stay(zipfileswopath[i] + "(" + str(os.path.getsize(
                                    zipfiles[i])) + " KB) -> " + str(round(filesizeen - zip_kb_old, 2)) + " KB", end='', toprint=False))
                                zip_kb_old: int = filesizeen
                                os.remove(zipfiles[i])
                                if i == len(zipfiles)-1:
                                    tqdm.write("\n")
                            filesizeenend: int = sum(
                                [zinfo.file_size for zinfo in zip.filelist])
                            logger.prev("\nPacked data have > " +
                                       str(filesizeenend) + " KB")
                        elif args.language == "JP":
                            bar = tqdm(range(0, len(zipfiles)), desc="梱包 ")
                            for i in bar:
                                zip.write(zipfiles[i])
                                filesizejp: int = sum(
                                    [zinfo.file_size for zinfo in zip.filelist])
                                tqdm.write(logger.stay(zipfileswopath[i] + "(" + str(os.path.getsize(
                                    zipfiles[i])) + " KB) -> " + str(round(filesizejp - zip_kb_old, 2)) + " KB", end='', toprint=False))
                                zip_kb_old: int = filesizejp
                                os.remove(zipfiles[i])
                                if i == len(zipfiles)-1:
                                    tqdm.write("\n")
                            filesizejpend: int = sum(
                                [zinfo.file_size for zinfo in zip.filelist])
                            logger.prev("\nパックされたデータは > " +
                                       str(filesizejpend) + " KB")
                        zip.close()
                    for i in range(0, len(folders)):
                        shutil.rmtree(folders[i])
                    end = time.time()
                    if args.language == "SK":
                        logger.stay('Uplynutý čas balenia: ' +
                                   str(end-start) + '\n')
                    elif args.language == "EN":
                        logger.stay('Elapsed time of packing: ' +
                                   str(end-start) + '\n')
                    elif args.language == "JP":
                        logger.stay('梱包経過時間: ' + str(end-start) + '\n')
                    if restart:
                        if args.language == "SK":
                            logger.stay('Program sa automaticky reštartuje.')
                        elif args.language == "EN":
                            logger.stay(
                                'The program will restart automatically.')
                        elif args.language == "JP":
                            logger.stay('プログラムが自動的に再起動します。')
                    elif not restart:
                        if args.endf is None:
                            pass
                        else:
                            if args.language == "SK":
                                logger.stay('Program sa automaticky vypne.')
                            elif args.language == "EN":
                                logger.stay(
                                    'The program will automatically shut down.')
                            elif args.language == "JP":
                                logger.stay('プログラムは自動的にシャットダウンします。')
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
                    if args.endf is not None and not restart:
                        sleep(2.5)
                    if restart:
                        crrestart = open("restart.py", "w", encoding='utf-8')
                        crrestart.write(restartapp)
                        crrestart.close()
                        os.remove('END')
                        if not inactivelogout and os.path.isfile(r"C:/Users/" + os.getlogin() + r"/AppData/Local/ZnámE/saved"):
                            if args.language == "SK":
                                typewriter(
                                    "!\n!!\n!!!\nUPOZORNENIE\nČAKAJTE, KÝM VÁM PROGRAM POVIE ŽE MÔŽETE\n!!!\n!!\n!\n", ttime=0.01)
                            elif args.language == "EN":
                                typewriter(
                                    "!\n!!\n!!!\nWARNING\nWAIT UNTIL PROGRAM SAYS YOU CAN\n!!!\n!!\n!\n", ttime=0.01)
                            elif args.language == "JP":
                                typewriter(
                                    "!\n!!\n!!!\n警告\nプログラムができると言うまで待ってください\n!!!\n!!\n!\n", ttime=0.01)
                            if args.language == "SK":
                                vstup = input("Rozumiete (Y/n) > ")
                            elif args.language == "EN":
                                vstup = input("Do you understand (Y/n) > ")
                            elif args.language == "JP":
                                vstup = input("わかりますか (Y/n) >")
                            vstup.lower()
                            if not vstup in ['', 'y']:
                                if os.path.isfile("restart.py"):
                                    os.remove("restart.py")
                                if neko:
                                    try:
                                        os.remove('assets/neko.png')
                                    except Exception:
                                        pass
                                    try:
                                        os.remove('assets/waifu.png')
                                    except Exception:
                                        pass
                                    try:
                                        os.remove('assets/waifu.gif')
                                    except Exception:
                                        pass
                                    try:
                                        os.remove('assets/waifu.mp4')
                                    except Exception:
                                        pass
                                    try:
                                        os.remove('assets/video.mp4')
                                    except Exception:
                                        pass
                                os.remove('crash_dump-' + datelog + '.txt')
                                return 0
                            elif vstup in ['', 'y']:
                                os.system('cls')
                                sys.stdout.flush()
                                if os.path.isfile("C:/Users/" + os.getlogin() + "/AppData/Local/ZnámE/saved"):
                                    if waifuvid:
                                        sleep(0.5)
                                        subprocess.check_output(
                                            'start edupage.py --restart --autologin --nointrof --waifu --waifuvid -lang ' + args.language + ' --music ' + args.music, shell=True)
                                    elif neko:
                                        sleep(0.5)
                                        subprocess.check_output(
                                            'start edupage.py --restart --autologin --nointrof --neko -lang ' + args.language + ' --music ' + args.music, shell=True)
                                    elif waifu:
                                        sleep(0.5)
                                        subprocess.check_output(
                                            'start edupage.py --restart --autologin --nointrof --waifu -lang ' + args.language + ' --music ' + args.music, shell=True)
                                    else:
                                        sleep(0.5)
                                        subprocess.check_output(
                                            'start edupage.py --restart --autologin --nointrof -lang ' + args.language + ' --music ' + args.music, shell=True)
                                    os.remove('crash_dump-' + datelog + '.txt')
                        else:
                            os.system('cls')
                            sys.stdout.flush()
                            if neko:
                                subprocess.check_output(
                                    'start edupage.py --restart --nointrof --neko -lang ' + args.language + ' --music ' + args.music, shell=True)
                            elif waifu:
                                subprocess.check_output(
                                    'start edupage.py --restart --nointrof --waifu -lang ' + args.language + ' --music ' + args.music, shell=True)
                            else:
                                subprocess.check_output(
                                    'start edupage.py --restart --nointrof -lang ' + args.language + ' --music ' + args.music, shell=True)
                            os.remove('crash_dump-' + datelog + '.txt')
                            return 0
                    elif not restart:
                        os.remove('END')
                        if args.endf is None:
                            if args.language == "SK":
                                input("'ENTER' NA KONIEC")
                            elif args.language == "EN":
                                input("'ENTER' TO END")
                            elif args.language == "JP":
                                input("「ENTER」で終了")
                            if os.path.exists('restart.py'):
                                os.remove('restart.py')
                            os.remove('crash_dump-' + datelog + '.txt')
                            return 0
                        else:
                            if os.path.exists('restart.py'):
                                os.remove('restart.py')
                            os.remove('crash_dump-' + datelog + '.txt')
                            return 0
        except *Exception as e:
            printnlog('Writing an error to \'error.log\'!!!')
            for error in e.exceptions:
                printnlog(traceback.format_exc())
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
            quit()
            
    if __name__ == '__main__':
        logger.stay(printnlog('Function: main\n', toprint=False))
        logger.prev(printnlog('Done defining functions\n', toprint=False))
        if args.debug == None:
            with cProfile.Profile() as pr:
                main()
            stats = pstats.Stats(pr)
            stats.sort_stats(pstats.SortKey.TIME)
            stats.dump_stats(filename='PROFILING.prof')
        else:
            main()
    else:
        try:
            os.remove('crash_dump-' + datelog + '.txt')
        except FileNotFoundError:
            pass
except *Exception as e:
    import os
    import sys
    import traceback
    printnlog('Writing an error to \'error.log\'!!!')
    for error in e.exceptions:
        printnlog(traceback.format_exc())
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
    quit()
