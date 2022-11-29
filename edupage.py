try: #  type: ignore
    from datetime import datetime
    from time import sleep
    import sys
    
    datelog = datetime.now().strftime("%y-%m-%d-%H-%M-%S")
    
    def printnlog(msg, end='\n', toprint=True):
        """
        It takes a message and an end character, and prints the message to the console and to a file

        :param msg: The message to be printed and logged
        :param end: The character that will be printed at the end of the message, defaults to \n
        (optional)
        """
        x = open('crash_dump-' + datelog + ".txt", 'a', encoding='utf-8')
        if toprint:
            print(str(msg), end=str(end))
        x.write(str(msg) + str(end))
        x.close()
        return msg

    def to_info(msg, end='\n', file='info.txt', format='a'):
        """
        It takes a message and an end character, and prints the message to the console and to a file

        :param msg: The message to be printed and logged
        :param end: The character that will be printed at the end of the message, defaults to \n
        (optional)
        """
        x = open('crash_dump-' + datelog + ".txt", 'a', encoding='utf-8')
        print(str(msg), end=str(end))
        x.write(str(msg) + str(end))
        x.close()
        x1 = open("C:/Users/" + os.getlogin() +
                  "/AppData/Local/ZnámE/" + file, format, encoding='utf-8')
        x1.write(str(msg) + str(end))
        x1.close()
        return msg

    def log(msg, end='\n'):
        """
        It opens a file, writes a message to it, and closes the file

        :param msg: The message to be logged
        :param end: The character that will be used to end the line, defaults to \n (optional)
        """
        x = open('crash_dump-' + datelog + ".txt", 'a', encoding='utf-8')
        x.write(str(msg) + str(end))
        x.close()
        return msg
    
    def typewriter(word, time=0.01, end='\n'):
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
            sleep(time)
            sys.stdout.write(char)
        sys.stdout.write(end)

    printnlog('Importing initial libraries\n')

    modulenames = list(set(sys.modules) & set(globals()))
    moduleminus = 0

    def print_module(add=None):
        global modulenames1
        global modulenames
        global moduleminus
        modulenames1 = list(set(sys.modules) & set(globals()))
        for i in range(len(modulenames) - moduleminus):
            modulenames1.remove(modulenames[i])
        for i in range(len(modulenames1)):
            modulenames.append(modulenames1[i])
        for i in modulenames1:
            typewriter(printnlog(i, toprint=False))
        if add != None:
            typewriter(printnlog(add, toprint=False))
    print_module('datetime')
    print_module('sleep from time')
    print_module('sys')
    print_module()
    import argparse
    print_module()
    import pkg_resources
    print_module()
    import os
    print_module()
    import subprocess
    print_module()
    import configparser
    print_module()
    import inspect
    print_module()
    from time import sleep
    print_module()
    printnlog('\nDONE\n')

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

    for i in range(0, len(allerror)-1):
        printnlog(allerror[i], end=', ')
    printnlog(allerror[len(allerror)-1])

    def error_log(line):
        """
        It writes the error to a file and prints it to the console

        :param line: The line number of the error
        """
        x = open('error_log.txt', 'a')
        exc_type, exc_obj, exc_tb = sys.exc_info()
        fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[# type: ignore
            1]  
        if str(exc_type.__name__) in allerror:  # type: ignore
            exc_type = exc_type.__name__  # type: ignore
        x.write('Type of error: ' + str(exc_type) + ' | Comment: ' + str(exc_obj) +
                ' | In file: ' + str(fname) + ' | On line: ' + str(line) + '\n')
        x.close()
        printnlog('Type of error: ' + str(exc_type) + ' | Comment: ' +
                  str(exc_obj) + ' | In file: ' + str(fname) + ' | On line: ' + str(line))

    def error_get(error, line, comment=None):
        """
        It takes an error, a line number, and a comment, and then raises the error with the comment, and
        then logs the error with the line number

        :param error: The error to raise
        :param line: The line of code that the error is on
        :param comment: The comment that will be displayed in the error log
        """
        try:
            raise error(comment)
        except error:
            error_log(line)

    def get_line_number(goback=0, relative_frame=1, msg=""):
        """
        It returns the line number of the code that called it

        :param relative_frame: The number of frames to go back, defaults to 1 (optional)
        :param msg: The message to print
        :return: The line number of the code that called the function.
        """
        return int(inspect.stack()[relative_frame][0].f_lineno)-int(goback)

    printnlog('\nReading config file (ini)\n')
    sleep(0.25)
    try:
        config = configparser.RawConfigParser()
        line_number = get_line_number(-1)
        config.read('config.ini')
    except configparser.DuplicateSectionError:
        printnlog("'config.ini' file is corrupt -> Duplicate section")
        error_get(configparser.DuplicateSectionError, line_number,  # type: ignore
                  'Corruption of config file => Duplicate section')
        input("Press 'enter' to quit")
        quit()
    except configparser.DuplicateOptionError:
        printnlog("'config.ini' file is corrupt -> Duplicate option")
        error_get(configparser.DuplicateSectionError, line_number,  # type: ignore
                  'Corruption of config file => Duplicate option')
        input("Press 'enter' to quit")
        quit()
    except configparser.NoSectionError:
        printnlog("'config.ini' file is corrupt -> No section")
        error_get(configparser.DuplicateSectionError, line_number,  # type: ignore
                  'Corruption of config file => No section')
        input("Press 'enter' to quit")
        quit()
    try:
        printnlog('Language: ' +
                  config.get('basic info', 'lang').split(' ')[0])
        printnlog('Enviroment: ' + config.get('basic info',
                  'enviroment').split(' ')[0])
        printnlog('Intro: ' + config.get('basic info', 'intro').split(' ')[0])
        printnlog('Inactivelimit: ' + config.get('basic info',
                  'inactivelimit').split(' ')[0])
        printnlog('Music: ' + config.get('basic info', 'music').split(' ')[0])
        printnlog('Musiclist: ' + config.get('basic info',
                  'musiclist').split(' ')[0])
        printnlog('User history: ' + str(config.items('user history')))
    except configparser.NoOptionError:
        printnlog("'config.ini' file is corrupt -> option missing")
        error_get(configNoOption, line_number,
                  'Corruption of config file => option missing')  # type: ignore
        input("Press 'enter' to quit")
        quit()
    printnlog('\nDone\n')

    """
    This function is the main function of the program. It will be called when the program is run.
    It will parse the arguments and call the appropriate functions.
    @param args - the arguments passed to the program.
    """

    global parser
    parser = argparse.ArgumentParser()
    UNSPECIFIED = object()
    sleep(0.5)
    language = ['SK', 'EN', 'JP']
    music = ['lowness', 'zurawie', 'Dan Dan Don Don']
    musicchoices = ['0']
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
    parser.add_argument('-music', '--music', choices=musicchoices, help='Starts music; you can select from: ' + str(i for i in music), default='0', nargs='?')
    parser.add_argument('-inactive', '--inactive', choices=[],
                        help='!!! Argument for program to use', default=UNSPECIFIED, nargs='?')
    parser.add_argument('-restart', '--restart', choices=[],
                        help='!!! Argument for program to use', default=UNSPECIFIED, nargs='?')
    parser.add_argument('-log', '--log', choices=[],
                        help='!!! Argument for program to use', default=UNSPECIFIED, nargs='?')
    parser.add_argument('-update', '--update', choices=[],
                        help='!!! Argument for program to use (this command won\'t update this program, it does it automatically)', default=UNSPECIFIED, nargs='?')
    parser.add_argument('-test', '--test', choices=[],
                        help='!!! Argument for program to use', default=UNSPECIFIED, nargs='?')
    args = parser.parse_args()
    hexnumber = ['0', '1', '2', '3', '4', '5', '6',
                 '7', '8', '9', 'a', 'b', 'c', 'd', 'e', 'f']
    

    printnlog("Checking argument correctness\n")

    if not config.get('basic info', 'enviroment').split(' ')[0][0] in hexnumber:
        error_get(argEnviromentError, get_line_number(),
                  'Wrong choice in \'basic info\' => enviroment')
        input()
        quit()
    elif not config.get('basic info', 'enviroment').split(' ')[0][1] in hexnumber:
        error_get(argEnviromentError, get_line_number(),
                  'Wrong choice in \'basic info\' => enviroment')
        input()
        quit()
    else:
        printnlog('basic info => enviroment')
    try:
        int(config.get('basic info', 'inactivelimit').split(' ')[0])
        printnlog('basic info => inactivelimit')
    except ValueError:
        error_get(argInactiveLimitError, get_line_number(
        ), 'Wrong choice in \'basic info\' => inactivelimit; take only numbers')
        input()
        quit()
    if not config.get('basic info', 'intro').split(' ')[0] in ['True', 'False']:
        error_get(argIntroError, get_line_number(),
                  'Wrong choice in \'basic info\' => intro')
        input()
        quit()
    else:
        printnlog('basic info => intro')
    if config.get('basic info', 'music').split(' ')[0] == 'enable':
        args.music = config.get('basic info', 'musiclist').split(' ')[0]
        printnlog('basic info => music')
    elif config.get('basic info', 'music').split(' ')[0] == 'disable':
        printnlog('basic info => music')
        pass
    else:
        error_get(configparser.ParsingError, get_line_number(),
                  'Wrong choice in \'basic info\' => music')
        input()
        quit()
    try:
        int(config.get('basic info', 'musiclist').split(' ')[0])
        printnlog('basic info => musiclist')
    except ValueError:
        error_get(argMusicListError, get_line_number(
        ), 'Wrong choice in \'basic info\' => musiclist; take only numbers')
        input()
        quit()
    if int(config.get('basic info', 'musiclist').split(' ')[0]) > len(music) or int(config.get('basic info', 'musiclist').split(' ')[0]) < 0:
        error_get(argMusicListError, get_line_number(
        ), 'Wrong choice in \'basic info\' => musiclist; Index out of range')
        input()
        quit()
    if not config.get('waifu settings', 'type').split(' ')[0] in ['sfw', 'nsfw']:
        error_get(argWaifuError, get_line_number(),
                  'Wrong choice in \'waifu settings\' => type')
        input()
        quit()
    else:
        printnlog('waifu settings => type')
    if config.get('waifu settings', 'type').split(' ')[0] == 'sfw':
        category = ["waifu", "neko", "shinobu", "megumin", "bully", "cuddle", "cry", "hug", "awoo", "kiss", "lick", "pat", "smug", "bonk", "yeet",
                    "blush", "smile", "wave", "highfive", "handhold", "nom", "bite", "glomp", "slap", "kill", "kick", "happy", "wink", "poke", "dance", "cringe"]
        if not config.get('waifu settings', 'category').split(' ')[0] in category:
            error_get(argWaifuError, get_line_number(),
                      'Wrong choice in \'waifu settings\' => category')
            input()
            quit()
        else:
            printnlog('waifu settings => category')
    elif config.get('waifu settings', 'type').split(' ')[0] == 'nsfw':
        category = ['waifu', 'neko', 'trap', 'blowjob']
        if not config.get('waifu settings', 'category').split(' ')[0] in category:
            error_get(argWaifuError, get_line_number(),
                      'Wrong choice in \'waifu settings\' => category')
            input()
            quit()
        else:
            printnlog('waifu settings => category')
    server = ['nekos.best', 'waifu.pics']
    if not config.get('neko settings', 'server').split(' ')[0] in server:
        error_get(argNekoError, get_line_number(),
                  'Wrong choice in \'neko settings\' => server')
        input()
        quit()
    else:
        printnlog('neko settings => server')
    try:
        int(config.get('game settings', 'goal_score').split(' ')[0])
        printnlog('game settings => goal_score')
    except ValueError:
        error_get(argGameError, get_line_number(
        ), 'Wrong choice in \'game settings\' => goal_score; take only numbers')
        input()
        quit()
    try:
        if 10 <= int(config.get('game settings', 'goal_score').split(' ')[0]):
            printnlog('game settings => goal_score')
        else:
            raise ValueError
    except ValueError:
        error_get(argGameError, get_line_number(
        ), 'Wrong choice in \'game settings\' => goal_score; minimum is 10')
        input()
        quit()
    try:
        float(config.get('game settings', 'computer_power').split(' ')[0])
        printnlog('game settings => computer_power')
    except ValueError:
        error_get(argMusicListError, get_line_number(
        ), 'Wrong choice in \'game settings\' => computer_power; take only numbers')
        input()
        quit()

    """
    If the language is not specified, use the default language from the config file.
    @param args.language - the language specified by the user, or the default language from the config file.
    """

    if args.language == None:
        if config.get('basic info', 'lang').split(' ')[0] in language:
            args.language = config.get('basic info', 'lang').split(' ')[0]
        else:
            error_get(argLanguageError, get_line_number(),
                      'Language doesn\'t exist')
            input()
            quit()

    """
    If the user has specified that we should update the rotation dictionary, remove the old update.py file.
    """
    if args.update == None:
        try:
            os.remove('update.py')
        except FileNotFoundError:
            args.update = UNSPECIFIED
            error_get(FileNotFoundError, get_line_number(),
                      'update.py isn\'t present, NOT FATAL ERROR')

    printnlog('\nDONE\n')

    """
    Check if the internet is working. If it is not, print an error message and quit.
    """

    """
    Check if the program is up to date. If not, update the program.
    @param potrebne - the packages needed for the program to run properly           
    @param nainstalovane - the packages installed on the system           
    @param nenajdene - the packages that are not installed on the system
    """
    potrebne = {'psutil', 'tqdm', 'semantic-version', 'gputil', 'py-cpuinfo', 'tabulate', 'opencv-python', 'glob2', 'wmi',
                'keyboard', 'cpufreq', 'pywin32', 'pypiwin32', 'pywinauto', 'moviepy', 'playsound', 'python-vlc', 'pygetwindow', 'pygame', 'keyboard'}
    printnlog('Libraries needed: ', end='')
    potrebne1 = list(potrebne)
    for i in range(0, len(potrebne1)):
        printnlog(potrebne1[i], end=' ')
    printnlog("\n\nChecking for updates\n")
    nainstalovane = {pkg.key for pkg in pkg_resources.working_set}
    nenajdene = potrebne - nainstalovane
    if args.version == None:
        verzia = open('version', 'r')
        printnlog(verzia.read())
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
            sleep(0.5)
            printnlog("\nDownloading updates")
            subprocess.check_call([sys.executable, '-m', 'pip', 'install', *nenajdene])
            printnlog("The program is restarting!!!")
            sleep(1)
            os.system('cls')
            os.remove('crash_dump-' + datelog + '.txt')
            subprocess.call(
                [sys.executable, os.path.realpath(__file__)] + sys.argv[1:])
            quit()

    printnlog('DONE\n')

    printnlog('Checking internet connection\n')

    def internet_check():
        try:
            import requests
            timeout = 5
            requests.head("http://www.google.com/", timeout=timeout)
        except requests.ConnectionError:  # type: ignore
            line_number = get_line_number()
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
            pass

    internet_check()

    printnlog('DONE\n')
    printnlog('\nImporting libraries\n')
    import pyautogui as pg
    print_module('pyautogui')
    pg.keyDown('win')
    pg.press('up')
    pg.keyUp('win')
    if args.restart == None:
        pg.keyDown('alt')
        pg.press('tab')
        pg.keyUp('alt')
        pg.keyDown('alt')
        pg.press('tab')
        pg.keyUp('alt')
    from threading import Thread
    print_module('Thread from threading')
    from tqdm import tqdm
    print_module()
    from pathlib import Path
    print_module('Path from pathlib')
    from uninstall import uninstall
    print_module()
    import shutil
    print_module()
    import zipfile
    print_module()
    import GPUtil
    print_module()
    import semantic_version
    print_module()
    import win32gui
    print_module()
    import ctypes
    print_module()
    import cpuinfo
    print_module()
    import cv2
    print_module()
    import glob
    print_module()
    import webbrowser
    print_module()
    import win32api
    print_module()
    import cpufreq
    print_module()
    import time
    print_module()
    import pywinauto
    print_module()
    import psutil
    print_module()
    import vlc
    print_module()
    import keyboard
    print_module()
    import pygetwindow
    print_module()
    import random
    print_module()
    import wmi
    print_module()
    import platform
    print_module()
    import socket
    print_module()
    import re
    print_module()
    import uuid
    print_module()
    import json
    print_module()
    import logging
    print_module()
    from tabulate import tabulate
    print_module()
    from PIL import Image
    print_module('Image from PIL')
    import moviepy.editor as mp
    print_module('moviepy.editor')
    from pygame import mixer
    print_module('mixer from pygame')
    printnlog('\nDONE\n')
    verzia = open('version', 'r')
    os.system('color ' + config.get('basic info', 'enviroment').split(' ')[0])
    os.system('Title ' + 'ZnámE')
    user32 = ctypes.windll.user32
    screensize = user32.GetSystemMetrics(0), user32.GetSystemMetrics(1)
    screensizepercentage = float(
        (1/1920)*screensize[0]), float((1/1080)*screensize[1])

    if not os.path.isfile("C:/Users/" + os.getlogin() + "/AppData/Local/ZnámE/info.txt") or args.update == None:
        printnlog('First time setup')
        sleep(1)
        try:
            os.mkdir("C:/Users/" + os.getlogin() + "/AppData/Local/ZnámE/")
        except FileExistsError:
            pass
        open("C:/Users/" + os.getlogin() + "/AppData/Local/ZnámE/info.txt", "x")
        to_info(verzia.read(), end='', file='version', format='w')
        printnlog('\n\nGetting system information\n')
        to_info('Resolution: ' +
                str(screensize[0]) + 'x' + str(screensize[1]) + '\n')
        computer = wmi.WMI()
        computer_info = computer.Win32_ComputerSystem()[0]
        os_info = computer.Win32_OperatingSystem()[0]
        proc_info = computer.Win32_Processor()[0]
        gpu_info = computer.Win32_VideoController()[0]

        def get_size1(bytes, suffix="B"):
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
            factor = 1024
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
        os_version = ' '.join([os_info.Version, os_info.BuildNumber])
        to_info(os_info)
        system_ram = float(os_info.TotalVisibleMemorySize) / \
            1048576  # KB to GB
        to_info('OS Name: {0}'.format(os_name))
        to_info(f"Device Name: {my_system.node}")
        to_info(f"Architecture: {my_system.machine}")
        to_info(f"Processor: {my_system.processor}")
        to_info('CPU: {0}'.format(proc_info.Name))
        to_info("="*40 + "CPU Info" + "="*40)
        to_info(f"CPU architecture: {my_cpuinfo['arch']}")
        to_info("Physical cores:" + str(psutil.cpu_count(logical=False)))
        to_info("Total cores:" + str(psutil.cpu_count(logical=True)))
        to_info(f"Max Frequency: {cpufreq.max:.2f}Mhz")
        to_info(f"Min Frequency: {cpufreq.min:.2f}Mhz")
        to_info(f"Current Frequency: {cpufreq.current:.2f}Mhz")
        to_info("CPU Usage Per Core:")
        for i, percentage in enumerate(psutil.cpu_percent(percpu=True, interval=1)): # type: ignore
            to_info(f"Core {i}: {percentage}%")
        to_info(pc.Win32_Processor()[0])
        to_info(f"Total CPU Usage: {psutil.cpu_percent()}%")
        to_info('RAM: {0} GB'.format(system_ram))
        to_info("="*40 + "Memory Information" + "="*40)
        to_info(f"Total: {get_size1(svmem.total)}")
        to_info(f"Available: {get_size1(svmem.available)}")
        to_info(f"Used: {get_size1(svmem.used)}")
        to_info(f"Percentage: {svmem.percent}%")
        to_info("="*20 + "SWAP" + "="*20)
        to_info(f"Total: {get_size1(swap.total)}")
        to_info(f"Free: {get_size1(swap.free)}")
        to_info(f"Used: {get_size1(swap.used)}")
        to_info(f"Percentage: {swap.percent}%")
        to_info('Graphics Card: {0}'.format(gpu_info.Name))
        to_info("="*40 + "GPU Details" + "="*40)
        list_gpus = []
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

        to_info(tabulate(list_gpus, headers=("id", "name", "load", "free memory", "used memory", "total memory",
                                             "temperature", "uuid")))
        to_info(f'IP Adress: {socket.gethostbyname(socket.gethostname())}')
        to_info(
            f"MAC Adress: {':'.join(re.findall('..', '%012x' % uuid.getnode()))}")
        to_info("="*40 + "Disk Information" + "="*40)
        to_info("Partitions and Usage:")
        for partition in partitions:
            to_info(f"=== Device: {partition.device} ===")
            to_info(f"  Mountpoint: {partition.mountpoint}")
            to_info(f"  File system type: {partition.fstype}")
            try:
                partition_usage = psutil.disk_usage(partition.mountpoint)
            except PermissionError:
                continue
            to_info(f"  Total Size: {get_size1(partition_usage.total)}")
            to_info(f"  Used: {get_size1(partition_usage.used)}")
            to_info(f"  Free: {get_size1(partition_usage.free)}")
            to_info(f"  Percentage: {partition_usage.percent}%")
        to_info(f"Total read: {get_size1(disk_io.read_bytes)}")  # type: ignore
        to_info(f"Total write: {get_size1(disk_io.write_bytes)}")# type: ignore
        to_info("="*40 + "Network Information" + "="*40)
        for interface_name, interface_addresses in if_addrs.items():
            for address in interface_addresses:
                to_info(f"=== Interface: {interface_name} ===")
                if str(address.family) == 'AddressFamily.AF_INET':
                    to_info(f"  IP Address: {address.address}")
                    to_info(f"  Netmask: {address.netmask}")
                    to_info(f"  Broadcast IP: {address.broadcast}")
                elif str(address.family) == 'AddressFamily.AF_PACKET':
                    to_info(f"  MAC Address: {address.address}")
                    to_info(f"  Netmask: {address.netmask}")
                    to_info(f"  Broadcast MAC: {address.broadcast}")
        to_info(f"Total Bytes Sent: {get_size1(net_io.bytes_sent)}")
        to_info(f"Total Bytes Received: {get_size1(net_io.bytes_recv)}")
        to_info(pc.Win32_VideoController()[0])
        to_info("User Current Version:-" + str(sys.version))
        printnlog('\nDONE\n')

    if not os.path.exists("C:/Users/" + os.getlogin() + "/AppData/Local/ZnámE/backup/"):
        typewriter(printnlog('Creating backup...\b'))
        os.mkdir("C:/Users/" + os.getlogin() + "/AppData/Local/ZnámE/backup/")
        shutil.copy('data.xp2', "C:/Users/" + os.getlogin() + "/AppData/Local/ZnámE/backup/backup-" +
                    str(datetime.now().strftime("%y-%m-%d-%H-%M-%S")) + '.xp2')
        x = open("C:/Users/" + os.getlogin() +
                 "/AppData/Local/ZnámE/backup/info.txt", 'w')
        x.write(
            'Rename \'xp2\' file to \'data.xp2\' and move it to your \'ZnámE\' directory')
        x.close()
        typewriter(printnlog('Done\n'))

    typewriter(printnlog("\nDefining functions\n", toprint=False))
    
    def download(url: str, fname: str, chunk_size=1024):
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
            total = int(resp.headers.get('content-length', 0))
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
            return False

    typewriter(printnlog('Function: download', toprint=False))

    updateapp = str(
        'import argparse, shutil, os, subprocess, configparser, sys\nfrom time import sleep\nUNSPECIFIED = object()\nglobal parser\nparser = argparse.ArgumentParser()\nparser.add_argument(\'-ef\', \'--endf\', help=\'Will not automatically end program\', default=UNSPECIFIED, nargs=\'?\')\nparser.add_argument(\'-lang\', \'--language\', choices=[\'SK\',\'EN\',\'JP\'], help=\'Language selection\', nargs=\'?\')\nparser.add_argument(\'input\', help=\'Input folder\', nargs=\'?\')\nargs = parser.parse_args()\nconfig = configparser.RawConfigParser()\nconfig.read(\'config.ini\')\nargs.language = config.get(\'basic info\', \'lang\').split(\' \')[0]\nif args.input != "":\n    sleep(0.5)\n    shutil.move(\'edupage.py\', \'old/edupage.py\')\n    shutil.move(args.input + \'/edupage.py\', \'edupage.py\')\n    sleep(0.2)\n    shutil.rmtree(args.input)\n    shutil.rmtree(\'old\')\n    if args.endf == None:\n        subprocess.call(sys.executable + \' edupage.py -lang \' + args.language + \' -endf -update\', shell=True)\n    else:\n        subprocess.call(sys.executable + \' edupage.py -lang \' + args.language + \' -update\', shell=True)\n    quit()')

    if args.log == None:
        x = open('log_update.py', 'w')
        x.write(updateapp)
        x.close()

    """
    Update the program to the newest version.
    @param directory - the directory of the new version
    @param args.language - the language of the program
    """

    if args.test != None:
        printnlog('\nChecking for newer version of ZnámE\n')
        try:
            import requests
            url = 'https://raw.githubusercontent.com/GrenManSK/ZnamE/main/version'
            page = requests.get(url)
            verzia = open('version', 'r')
            if semantic_version.Version(page.text[1:]) <= semantic_version.Version(verzia.read()[1:]):
                printnlog('You have the latest version\n')
            else:
                if args.language == "SK":
                    printnlog("Bola nájdená nová aktualizacia: " + page.text)
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
                                sleep(0.05)
                            except zipfile.error as e:
                                pass
                    elif args.language == "EN":
                        for member in tqdm(iterable=zip.namelist(), total=len(zip.namelist()), desc='Extracting '):
                            try:
                                zip.extract(member)
                                tqdm.write(
                                    f"{os.path.basename(member)}(" + str(os.path.getsize(member)) + "KB)")
                                sleep(0.05)
                            except zipfile.error as e:
                                pass
                    elif args.language == "JP":
                        for member in tqdm(iterable=zip.namelist(), total=len(zip.namelist()), desc='抽出中 '):
                            try:
                                zip.extract(member)
                                tqdm.write(
                                    f"{os.path.basename(member)}(" + str(os.path.getsize(member)) + "KB)")
                                sleep(0.05)
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
                if directory == None:
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
                if args.endf == None:
                    subprocess.call(sys.executable + ' update.py ' + directory +
                                    ' -lang ' + args.language + ' -endf', shell=True)
                else:
                    subprocess.call(sys.executable + ' update.py ' +
                                    directory + ' -lang ' + args.language, shell=True)
                sleep(0.1)
                os.remove('crash_dump-' + datelog + '.txt')
                quit()
        except requests.ConnectionError:  # type: ignore
            line_number = get_line_number()
            pass

    verzia.close()

    def getWindow():
        """
        The getWindow function is used to find the window of Známý (the game) and activate it.
        It also checks if the file 'banner.png' exists in the assets folder.

        :return: If error occured
        """

        global exit
        stop_thread1 = True
        a = None
        cv2.namedWindow('frame2', cv2.WND_PROP_FULLSCREEN)
        cv2.setWindowProperty(
            'frame2', cv2.WND_PROP_FULLSCREEN, cv2.WINDOW_FULLSCREEN)
        test = "assets/banner.png"
        for file in glob.glob(test):
            a = cv2.imread(file)
        try:
            cv2.imshow("Image", a)
        except cv2.error:
            error_get(cv2.error, get_line_number(),
                      'File is corrupt (probably \'banner.png\')')
            return True
        cv2.waitKey(1)
        sleep(0.1)
        cv2.destroyWindow("Image")
        if args.test != None:
            try:
                window = pygetwindow.getWindowsWithTitle('ZnámE')[0]
                window.activate()
                return False
            except IndexError:
                error_get(IndexError, get_line_number(
                ), 'Possible solution; run in cmd or python aplication not ide or put arguments \'--test\'')
                return True

    typewriter(printnlog('Function: getWindow', toprint=False))

    def PlayVideo(video_path):
        """
        The PlayVideo function plays a video from the specified path.
           The function will play the video in full screen mode and will not return until the user presses 'Q' to quit.
        
        
        :param video_path: Specify the path to the video file that should be played
        :return: Nothing
        """
        player = vlc.Instance('--fullscreen')
        media_list = player.media_list_new()  # type: ignore
        media_player = player.media_list_player_new()  # type: ignore
        media = player.media_new(video_path)  # type: ignore
        media_list.add_media(media)
        media_player.set_media_list(media_list)
        sleep(1)
        print("Press 'Q' to stop video")
        input('Press enter to continue')
        media_player.play()
        try:
            sleep(0.25)
            window = pygetwindow.getWindowsWithTitle(
                'VLC (Direct3D11 output)')[0]
            window.activate()
            window.maximize()
        except Exception:
            pass
        while True:
            if keyboard.is_pressed('q'):
                media_player.stop()
                ctypes.windll.user32.keybd_event(0x8, 0, 0, 0)
                sleep(0.01)
                ctypes.windll.user32.keybd_event(0x8, 0, 2, 0)
                sleep(0.01)
                break
            
    typewriter(printnlog('Function: PlayVideo', toprint=False))
    
    def getImg(imgSrc, name, x=None, y=None, width=None, length=None):
        """
        The getImg function displays an image from the source. If x, y, width, and length are specified, then the image will be displayed at those coordinates with the specified width and length. Otherwise, the image will be displayed at the default coordinates and default width and length.

        :param imgSrc: Specify the source of the image
        :param name: Name the window
        :param x=None: Specify the x coordinate of the window
        :param y=None: Specify the y coordinate of the window
        :param width=None: Specify the width of the window
        :param length=None: Set the length of the window to its default value
        :return: The image that is displayed
        """

        path = imgSrc
        for file in glob.glob(path):
            global a
            a = cv2.imread(file)
            cv2.imshow(name, a)
            if x != None and y != None and width != None and length != None:
                appname = name
                xpos = x
                ypos = y
                if width == None:
                    width = int((screensize[0]/10)*9)
                if length == None:
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

    typewriter(printnlog('Function: getImg', toprint=False))

    def move(window, x, y, width, length):
        """
        The move function moves the specified window to a specified location.
        The move function takes four arguments:
            1) The name of the window as a string. This is case sensitive and should be enclosed in quotation marks if it contains spaces or special characters (e.g., &quot;Microsoft Word&quot;). 
            2) The x-coordinate of the desired location on your screen, measured in pixels from the left edge of your screen to where you want your window located (e.g., 100). 
            3) The y-coordinate of the desired location on your screen, measured in pixels from the top edge of your screen

        :param window: Specify the window name
        :param x: Set the x position of the window, y is used to set the y position
        :param y: Move the window to the top of your screen
        :param width: Set the width of the window
        :param length: Set the height of the window
        :return: The window handle of the specified application
        """

        appname = window
        xpos = x
        ypos = y
        if width == None:
            width = int((screensize[0]/10)*9)
        if length == None:
            length = int((screensize[1]/10)*9)

        def enumHandler(hwnd, lParam):  # type: ignore
            if win32gui.IsWindowVisible(hwnd):  # type: ignore
                if appname in win32gui.GetWindowText(hwnd):  # type: ignore
                    win32gui.MoveWindow(
                        hwnd, xpos, ypos, width, length, True)  # type: ignore
        win32gui.EnumWindows(enumHandler, None)  # type: ignore

    typewriter(printnlog('Function: move', toprint=False))

    typewriter(printnlog('\nDefining apps', toprint=False))

    codeapp = str(
        'import sys\nPLOCHA = [[\"a\", \"b\", \"c\", \"d\", \"e\"], [\"f\", \"g\", \"h\", \"i\", \"j\"], [\n    \"k\", \"l\", \"m\", \"n\", \"o\", ], [\"p\", \"q\", \"r\", \"s\", \"t\"], [\n    \"u\", \"v\", \"w\", \"x\", \"y\"], [\"A\", \"B\", \"C\", \"D\", \"E\"], [\n    \"F\", \"G\", \"H\", \"I\", \"J\"], [\"K\", \"L\", \"M\", \"N\", \"O\", ], [\n    \"P\", \"Q\", \"R\", \"S\", \"T\"], [\"U\", \"V\", \"W\", \"X\", \"y\"], [\n    \"z\", \" \", \",\", \".\", \":\"], [\"!\", \"?\", \"\'\", \'\"\', \"`\"], [\n    \"1\", \"2\", \"3\", \"4\", \"5\"], [\"6\", \"7\", \"8\", \"9\", \"0\"], [\n    \"\\n\", \"<\", \">\", \";\", \"/\"], [\"\\\\", \"{\", \"}\", \"(\", \")\"],[\n    \"[\",\"]\",\"|\",\"-\",\"_\"],[\"=\",\"+\",\"@\",\"#\",\"$\"],[\"%\",\"^\",\"&\",\"*\",\"~\"]]\ndef read_file(file):\n    obsah = \"\"\n    obsah_list = []\n    for i in file:\n        obsah = \"\"\n        obsah += i\n        for i in obsah:\n            i.lower()\n            obsah_list.append(i)\n    return obsah_list\ndef encode(obsah):\n    sifra = []\n    for i in obsah:\n        riadok = 0\n        stlpec = 0\n        while True:\n            if riadok == 19 and stlpec == 0:\n                break\n            if i == PLOCHA[riadok][stlpec]:\n                sifra.append(str(riadok) + \" \" + str(stlpec))\n                break\n            if stlpec == 4:\n                riadok += 1\n                stlpec = 0\n            else:\n                stlpec += 1\n    return sifra\ndef output_file(file, name):\n    y = []\n    x = open(name + \"crypted\", \"w\")\n    for i in file:\n        y.append(i)\n    x.write(str(y))\n    x.close\n    return\ndef main():\n    name = sys.argv[1]\n    open_file = open(name, \"r\")\n    open_file.close\n    output_file(encode(read_file(open_file)), name)\nmain()\nx=open(\'DONE\',\'x\')\nx.close()')
    decodeapp = str(
        'import os\nos.system(\'Title \' + \'code\')\nimport sys\nPLOCHA = [[\"a\", \"b\", \"c\", \"d\", \"e\"], [\"f\", \"g\", \"h\", \"i\", \"j\"], [\n    \"k\", \"l\", \"m\", \"n\", \"o\", ], [\"p\", \"q\", \"r\", \"s\", \"t\"], [\n    \"u\", \"v\", \"w\", \"x\", \"y\"], [\"A\", \"B\", \"C\", \"D\", \"E\"], [\n    \"F\", \"G\", \"H\", \"I\", \"J\"], [\"K\", \"L\", \"M\", \"N\", \"O\", ], [\n    \"P\", \"Q\", \"R\", \"S\", \"T\"], [\"U\", \"V\", \"W\", \"X\", \"y\"], [\n    \"z\", \" \", \",\", \".\", \":\"], [\"!\", \"?\", \"\'\", \'"\', \"`"], [\n    \"1\", \"2\", \"3\", \"4\", \"5\"], [\"6\", \"7\", \"8\", \"9\", \"0\"], [\n    \"\\n\", \"<\", \">\", \";\", \"/\"], [\"\\\\", \"{\", \"}\", \"(\", \")\"],[\n    \"[\",\"]\",\"|\",\"-\",\"_\"],[\"=\",\"+\",\"@\",\"#\",\"$\"],[\"%\",\"^\",\"&\",\"*\",\"~\"]]\ndef read_file(file):\n    obsah = \"\"\n    obsah_list = []\n    for i in file:\n        obsah += i\n        for i in obsah:\n            obsah_list.append(i)\n    return obsah_list\ndef decode(obsah):\n    done = \"\"\n    sifra = []\n    for i in obsah:\n        done += str(i)\n        if i == \"[\" or i == \"\'\" or i == \",\" or i == \"]\":\n            done = \"\"\n            continue\n        if i == \" \":\n            sifra.append(i)\n        else:\n            sifra.append(i)\n    return sifra\ndef real_decode(obsah):\n    cislo = 0\n    pokracovanie = False\n    done = \"\"\n    vysledok = []\n    for i in obsah:\n        done += str(i)\n        cislo = 0\n        for i in done:\n            cislo += 1\n        if i == \" \":\n            done = \"\"\n            continue\n        if pokracovanie and done.isnumeric() and cislo == 1:\n            stlpec = int(done)\n            vysledok.append(PLOCHA[riadok][stlpec])\n            pokracovanie = False\n            done = \"\"\n            continue\n        if not pokracovanie or cislo == 2:\n            pokracovanie = True\n            riadok = int(done)\n            continue\n    return vysledok\ndef to_text(obsah):\n    text = \"\"\n    for i in obsah:\n        if i == \".\":\n            text += i + \"\\n\"\n            continue\n        text += i\n    return text\ndef create_file(obsah, name):\n    x = open(sys.argv[1], \"w\")\n    x.write(obsah)\n    x.close\n    return\ndef main():\n    if sys.argv[2] == \'False\':\n        name = \'data\'\n    else:\n        name = sys.argv[2]\n    open_file = open(name, \"r\")\n    code = list(decode(read_file(open_file)))\n    create_file(to_text(real_decode(code)), name)\nmain()\nx=open(\'DONE\',\'x\')\nx.close()')
    findapp = str('import sys\ndecodename=str(sys.argv[1])\nicofind=int(sys.argv[2])\ndn=open(decodename,\'r\')\ndnr=dn.read()\nbracket,brackethist=0,0\nico=[]\nicocurrent=\'\'\nicoend=False\nrnii=False\nrniiend=False\nsubject=\'\'\nik=False\nuserdef=False\nwh=False\npassword=\'\'\npassend=False\nfor i in dnr:\n    if rnii:\n        wh=True\n        if i==\'[\':\n            bracket+=1\n        elif i==\']\':\n            bracket-=1\n        if passend:\n            user.write(password+\'\\n\')\n            passend=False\n        if ik:\n            if i!="," and bracket==4 and brackethist==4:\n                user.write(i)\n            if bracket==3:\n                subject=\'\'\n                ik=False\n                rniiend=False\n                user.write(\"\\n\")\n        if rniiend:\n            user.write(subject)\n            ik=True\n            rniiend=False\n            brackethist=bracket\n            continue\n        if userdef:\n            userdef=False\n            user=open(str(ico[0]),\'w\')\n        if bracket==3 and brackethist==3 and i!=\"\'\":\n            if i ==\',\':\n                rniiend=True\n                continue\n            subject+=str(i)\n        elif bracket==5 and brackethist==5 and i!=\"\'\":\n            if i ==\',\':\n                passend=True\n                continue\n            password+=str(i)\n        brackethist=bracket\n        if bracket<2 and brackethist<2:\n            break\n    else:\n        if i==\'[\':\n            bracket+=1\n        elif i==\']\':\n            bracket-=1\n        if icoend:\n            if icocurrent!=\'\':\n                if int(icocurrent)==icofind:\n                    ico.append(icocurrent)\n                    rnii=True\n                    continue\n                icocurrent=\'\'\n                icoend=False\n        if bracket==2 and brackethist==2:\n            if i ==\',\':\n                icoend=True\n                userdef=True\n                continue\n            icocurrent+=i\n        brackethist=bracket\nif not wh:\n    user=open(sys.argv[2], \'x\')\nuser.close()\nx=open(\'DONE\',\'x\')\nx.close()')
    passwordapp = str(
        'import sys\ndecodename=str(sys.argv[1])\ndn=open(decodename,\'r\')\ndnr=dn.readlines()\ntry:\n    number=int(dnr[0])\n    number=str(dnr[0])\n    number=dnr[0][:6]\nexcept Exception:\n    number=None\nx=open(\'DONE\',\'w\')\nx.write(number)\nx.close()')
    addapp = str('import sys\ndecodename=str(sys.argv[1])\nicofind=int(sys.argv[2])\nsubjectfind = sys.argv[3]\nmarkadd = sys.argv[4]\ndn=open(decodename,\'r\')\ndnr=dn.read()\nbracket,brackethist=0,0\nico=[]\nicocurrent=\'\'\nicoend=False\nrnii=False\nrniiend=False\nsubject=\'\'\nik=False\nuserdef=False\nwh=False\npassword=\'\'\npassend=False\nik2=False\nadd=False\nuser=open(\'data1\',\'w\', newline=\'\')\nfor i in dnr:\n    user.write(i)\n    if rnii:\n        wh=True\n        if i==\'[\':\n            bracket+=1\n        elif i==\']\':\n            bracket-=1\n        if add and subject==subjectfind and bracket==4 and brackethist==4:\n            subjectfind=None\n            user.write(str(markadd) + \',\')\n            add=False\n        if passend:\n            passend=False\n        if ik:\n            if ik2:\n                ik2=False\n                add=True\n            if bracket==3:\n                subject=\'\'\n                ik=False\n                rniiend=False\n        if rniiend:\n            ik=True\n            ik2=True\n            rniiend=False\n            brackethist=bracket\n            continue\n        if userdef:\n            userdef=False\n        if bracket==3 and brackethist==3 and i!=\"\'\":\n            if i ==\',\':\n                rniiend=True\n                continue\n            subject+=str(i)\n        elif bracket==5 and brackethist==5 and i!=\"\'\":\n            if i ==\',\':\n                passend=True\n                continue\n            password+=str(i)\n        brackethist=bracket\n    else:\n        if i==\'[\':\n            bracket+=1\n        elif i==\']\':\n            bracket-=1\n        if icoend:\n            if icocurrent!=\'\':\n                if int(icocurrent)==icofind:\n                    ico.append(icocurrent)\n                    rnii=True\n                    continue\n                icocurrent=\'\'\n                icoend=False\n        if bracket==2 and brackethist==2:\n            if i ==\',\':\n                icoend=True\n                userdef=True\n                continue\n            icocurrent+=i\n        brackethist=bracket\nif not wh:\n    user=open(sys.argv[2], \'x\')\nuser.close()\nx=open(\'DONE\',\'x\')\nx.close()')
    restartapp = str('import argparse, time, os\nimport pyautogui as pg\nUNSPECIFIED = object()\nparser = argparse.ArgumentParser()\nparser.add_argument(\'-waifu\',\'--waifu\', choices=[], default=UNSPECIFIED, nargs=\'?\')\nparser.add_argument(\'-al\',\'--autol\', choices=[], default=UNSPECIFIED, nargs=\'?\')\nparser.add_argument(\'-neko\',\'--neko\', choices=[], default=UNSPECIFIED, nargs=\'?\')\nargs = parser.parse_args()\nwhile True:\n    leave = False\n    for i in os.listdir():\n        if i == \'CONTINUE\':\n            leave = True\n            break\n    if leave:\n        time.sleep(0.05)\n        os.remove(\'CONTINUE\')\n        break\nif args.neko == None and args.autol == None or args.waifu == None and args.autol == None:\n    time.sleep(10)\n    pg.write("login\\n")\n    time.sleep(1)\n    pg.write("y\\n")\nelif args.autol == None:\n    time.sleep(1)\n    pg.write("login\\n")\n    time.sleep(1)\n    pg.write("y\\n")')
    gameapp = str('from edupage import game\ngame()')

    if args.log == None:
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

    typewriter(printnlog('\nDONE\n', toprint=False))

    def set_config(section, name, info):
        """
        The set_config function writes a new config.ini file with the specified section, name, and info.

        :param section: Define the section of the config
        :param name: Set the name of the configuration file
        :param info: Set the value of the name parameter in the section specified
        :return: None
        """
        os.remove('config.ini')
        configfile = open('config.ini', 'a')
        config.set(section, name, info)
        config.write(configfile)
        configfile.close()

    typewriter(printnlog('Function: set_config', toprint=False))

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

    typewriter(printnlog('Function: get_size', toprint=False))

    def delcache(name, hist):
        """
        The delcache function deletes the cache file if it is empty.


        :param name: Name the file that is used to store the time
        :param hist: Check if the history file has changed
        :return: The value of the timer
        """

        global timer
        time_got = int(config.get('basic info', 'inactivelimit').split(' ')[0])
        timer = time_got
        filesize = os.path.getsize(hist)
        sizehist = filesize
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
                    elif args.language == "EN":
                        print("Press 'enter'")
                    elif args.language == "JP":
                        print("「入力」を押してください")
                    pg.write('\n')
                    playhtml('apphtml\\inactive')
                    break
                if filesize != sizehist:
                    timer = time_got
                    sizehist = filesize
                else:
                    sizehist = filesize
                    filesize = os.path.getsize(hist)
                    sleep(1)
                    timer -= 1
            except Exception:
                pass

    typewriter(printnlog('Function: delcache', toprint=False))

    loginvstupuser = ''
    global progress_bar_check
    progress_bar_check = 0
    global progress_bar_end
    progress_bar_end = False

    cachename = 'data.xp2'

    def inactive():
        """
        The inactive function is used to check if the INACTIVE file exists in the current directory. If it does, then it will remove the password file and return True. Otherwise, it returns False.

        :return: True if the file inactive is found in the directory
        """

        global password
        leave = False
        for i in os.listdir():
            if i == 'INACTIVE':
                leave = True
                try:
                    os.remove(password[1])  # type: ignore
                except Exception:
                    pass
                break
        if leave:
            sleep(0.05)
            return True
        else:
            return False

    typewriter(printnlog('Function: inactive', toprint=False))

    def progress_bar(name, number):
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
        progress_bar_check_old = 0
        end = False
        for i in tqdm(range(0, number), desc=name + ' '):
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

    typewriter(printnlog('Function: progress_bar', toprint=False))

    def add(name, ico, subject, mark):
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
        decodename = str(datetime.now().strftime("%H-%M-%S"))
        decodename = 'add'
        crdecode = open(decodename + ".py", "w")
        crdecode.write(addapp)
        crdecode.close()
        subprocess.check_output('start ' + decodename + '.py ' + str(name) +
                                ' ' + str(ico) + ' ' + str(subject) + ' ' + str(mark), shell=True)
        if args.language == "SK":
            tqdm.write('Pridávam ...', end='\r')
        elif args.language == "EN":
            tqdm.write('Adding ...', end='\r')
        elif args.language == "JP":
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
        elif args.language == "EN":
            tqdm.write('Adding Complete')
        elif args.language == "JP":
            tqdm.write('追加完了')
        os.remove(decodename + '.py')
        os.remove(name)
        os.remove('DONE')
        progress_bar_check += 1
        name = ('data1', None)
        return name

    typewriter(printnlog('Function: add', toprint=False))

    def decode(name, password, mode=0):
        """
        The decode function takes two arguments, name and password. If the name argument is not provided it will default to None.
        If the password argument is not provided it will default to None as well. The function then creates a file with the current time in its name and writes a python script into that file which decrypts all files in this directory (except for itself) using pyAesCrypt library with given password or generated one if none was given.

        :param name: Specify the name of the file to be decoded
        :param password: Encrypt the file with a password
        :param mode=0: Encode the file, mode=0 is used to decode the file
        :return: The value of the name variable, if it is not none
        """

        global progress_bar_check
        decodename = str(datetime.now().strftime("%H-%M-%S"))
        decodename = 'decode'
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
        elif args.language == "EN":
            tqdm.write('Encrypting Complete')
        elif args.language == "JP":
            tqdm.write('暗号化完了')
        os.remove(decodename + '.py')
        os.remove('DONE')
        if mode == 1:
            file = open('1', 'r')
            fileline = str(file.readlines())
            fileline = fileline[2:len(fileline)-2]
            file.close()
            os.remove('1')
            return fileline
        progress_bar_check += 1
        return decodename1

    typewriter(printnlog('Function: decode'))

    def password(name):
        """
        Create a password file for the current session.
        @param name - the name of the file to be created.
        """
        global progress_bar_check
        passwordname = str(datetime.now().strftime("%H-%M-%S"))
        passwordname = 'pasword'
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

    typewriter(printnlog('Function: password', toprint=False))

    def find(name):
        # Creating a file, writing to it, and then running it.

        global progress_bar_check
        findname = str(datetime.now().strftime("%H-%M-%S"))
        findname = 'find'
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
            elif args.language == "JP":
                tqdm.write('発見 エラー')
            end = True
        if end:
            return (loginvstupuser, end)
        test.close()
        if args.language == "SK":
            tqdm.write('Hľadám Hotovo')
        elif args.language == "EN":
            tqdm.write('Finding Complete')
        elif args.language == "JP":
            tqdm.write('発見完了')
        progress_bar_check += 1
        return [loginvstupuser, end]

    typewriter(printnlog('Function: find', toprint=False))

    def code(name, new, mode=0):
        """
        The code function is used to encrypt files.
        It takes two arguments: name, new.
        name is the file that will be encrypted.
        new is the password for encryption.

        :param name: Get the name of the file to be encrypted
        :param new: Save the new password
        :param mode=0: Encrypt the file
        :return: The name of the file and the new value
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
            savelog = file.readlines()
            file.close()
            os.remove('1')
            os.remove('1crypted')
            return savelog
        return name[1], new

    typewriter(printnlog('Function: code', toprint=False))

    def mouseclick(time=0):
        """
        The mouseclick function is used to click the F11 key on the keyboard.
        This function is useful for maximizing a window.

        :param time=0: Make the mouseclick function run for a specified amount of time
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

    typewriter(printnlog('Function: mouseclick', toprint=False))

    def playhtml(htmlFile, mode=0, time=0):
        """
        The playhtml function is used to open the html file containing the game's intro.
        It can be called in two ways:
            1) playhtml(htmlFile, mode=0, time=0):  # mode = 0 means that it will click through all of the intro automatically. 
                                                    # time = 0 means that it will not wait for a specific amount of time before clicking
                                                    # through each part of the intro.

        :param htmlFile: Specify which html file to open
        :param mode=0: Determine whether the function is used to start a new game or load an existing one
        :param time=0: Make the mouseclick function wait a certain amount of time
        :return: Nothing
        :doc-author: Trelent
        """

        if args.nointro == None or args.nointrof == None:
            args.nointrof = object()
            if args.test == None and config.get('basic info', 'intro').split(' ')[0] == 'True':
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
                if args.test != None:
                    window = pygetwindow.getWindowsWithTitle('ZnámE')[0]
                    window.activate()
            else:
                pass

    typewriter(printnlog('Function: playhtml', toprint=False))

    gamefiles = ['losing1_add.mp3', 'losing1_add2.mp3', 'losing1_end.mp3', 'losing1_loop.mp3', 'winning1_add.mp3', 'winning1_add2.mp3', 'winning1_end.mp3', 'winning1_loop.mp3',
                 'losing2_add.mp3', 'losing2_add2.mp3', 'losing2_end.mp3', 'losing2_loop.mp3', 'winning2_add.mp3', 'winning2_add2.mp3', 'winning2_end.mp3', 'winning2_loop.mp3', 'word.txt']

    def create_gamefiles():
        """
        The create_gamefiles function creates the game files needed to run a game.
        It copies over the assets folder and all of its contents into a new folder called 'game'.
        The create_gamefiles function does not take any arguments. It returns nothing.

        :return: A list of the files that were created
        """
        try:
            os.mkdir('game')
        except Exception:
            pass
        try:
            x = open('game.py', 'w')
            x.write(gameapp)
            x.close()
        except Exception:
            pass
        source_folder = "assets\\"
        destination_folder = "game\\"
        for file_name in os.listdir(source_folder):
            source = source_folder + file_name
            destination = destination_folder + file_name
            if os.path.isfile(source) and file_name in gamefiles:
                shutil.copy(source, destination)
                typewriter(destination)

    typewriter(printnlog('Function: create_gamefiles', toprint=False))

    score = 0
    scorec = 0
    goal_score = int(config.get('game settings', 'goal_score'))

    def game():
        os.system('title GAME')
        global score
        global scorec
        global goal_score
        os.system('cls')
        internet_check()
        if __name__ == '__main__':
            create_gamefiles()
        else:
            for i in gamefiles:
                if os.path.exists('game\\' + i):
                    pass
                else:
                    print(
                        'First you need to create a gamefiles, which you can do in \'edupage.py\' with command \'offlinegame\'')
                    input()
                    return
        print('You will be playing against computer')
        word = open('game/word.txt', 'r')
        words = word.readlines()
        music = False
        music_tense = 0
        after_game = False

        def computer():
            global score
            global scorec
            global goal_score
            word = open('game/word.txt', 'r')
            words = word.readlines()
            while scorec < goal_score and score < goal_score:
                number = random.randint(0, 10000-1)
                timeis = float(config.get('game settings', 'computer_power')
                               )*len(words[number][:-1])  # type: ignore
                sleep(timeis)
                scorec += 100/(timeis + 1)  # type: ignore
        while True:
            os.system('cls')
            if after_game:
                if score > scorec:
                    print('Victory')
                elif score < scorec:
                    print('Defeat')
                elif score == scorec:
                    print('Draw')
                print(score)
                print(scorec)
            maxmusicset = 1
            musicset = [random.randint(
                1, maxmusicset), random.randint(1, maxmusicset)]
            score = 0
            scorec = 0
            quitgame = False
            goal_score = int(config.get('game settings', 'goal_score'))
            gameinput = input('> ')
            if gameinput == 'start':
                mixer.Channel(0).fadeout(1000)
                mixer.Channel(1).fadeout(1000)
                nopoints = False
                Thread(target=computer, daemon=True).start()
                while score < goal_score and scorec < goal_score:
                    os.system('cls')
                    print(score)
                    print(scorec)
                    if not music and score >= goal_score/2 and score > scorec:
                        mixer.Channel(0).play(mixer.Sound(
                            'game\\winning' + str(musicset[0]) + '_loop.mp3'), fade_ms=1000, loops=-1)
                        music_tense = 1
                        music = True
                    elif music_tense == 1 and music and score >= (goal_score/3)*2 and score > scorec:
                        mixer.Channel(0).fadeout(1000)
                        mixer.Channel(1).play(mixer.Sound(
                            'game\\winning' + str(musicset[0]) + '_add.mp3'), fade_ms=1000, loops=-1)
                        music_tense = 2
                        music = True
                    elif music_tense == 2 and music and score >= (goal_score/6)*5 and score > scorec:
                        mixer.Channel(1).fadeout(1000)
                        mixer.Channel(0).play(mixer.Sound(
                            'game\\winning' + str(musicset[0]) + '_add2.mp3'), fade_ms=1000, loops=-1)
                        music_tense = 3
                        music = True
                    elif not music and scorec >= goal_score/2 and score < scorec:
                        mixer.Channel(0).play(mixer.Sound(
                            'game\\losing' + str(musicset[1]) + '_loop.mp3'), fade_ms=1000, loops=-1)
                        music_tense = 1
                        music = True
                    elif music_tense == 1 and music and scorec >= (goal_score/3)*2 and score < scorec:
                        mixer.Channel(0).fadeout(1000)
                        mixer.Channel(1).play(mixer.Sound(
                            'game\\losing' + str(musicset[1]) + '_add.mp3'), fade_ms=1000, loops=-1)
                        music_tense = 2
                        music = True
                    elif music_tense == 2 and music and scorec >= (goal_score/6)*5 and score < scorec:
                        mixer.Channel(1).fadeout(1000)
                        mixer.Channel(0).play(mixer.Sound(
                            'game\\losing' + str(musicset[1]) + '_add2.mp3'), fade_ms=1000, loops=-1)
                        music_tense = 3
                        music = True
                    number = random.randint(0, 10000-1)
                    print(words[number][:-1])
                    start = time.time()
                    while True:
                        gameinput = input('> ')
                        if gameinput == '-n':
                            nopoints = True
                            break
                        if gameinput == '-q':
                            quitgame = True
                            break
                        if gameinput == words[number][:-1]:
                            break
                    if quitgame:
                        score = int(config.get('game settings', 'goal_score'))
                        sleep(0.5)
                        score = 0
                        scorec = 0
                        break
                    end = time.time()
                    timeis = end - start
                    if timeis < 10 and not nopoints:
                        score += 100/(timeis + 1)
                    else:
                        nopoints = False
                print(score)
                print(scorec)
                after_game = True
                if score > scorec:
                    mixer.Channel(0).fadeout(1000)
                    mixer.Channel(1).play(mixer.Sound(
                        'game\\winning' + str(musicset[0]) + '_end.mp3'), fade_ms=1000)
                elif score < scorec:
                    mixer.Channel(0).fadeout(1000)
                    mixer.Channel(1).play(mixer.Sound(
                        'game\\losing' + str(musicset[1]) + '_end.mp3'), fade_ms=1000)
            elif gameinput == 'quit':
                break
        word.close()

    typewriter(printnlog('Function: game', toprint=False))

    def main():  # type: ignore
        try:
            """
            The main function. This is where the program starts. It is the first function called.
            """

            historyname = str(datetime.now().strftime("%H-%M-%S"))
            historyfile = open(historyname, 'w')
            if args.nointrof == None:
                historyfile.write('[*restarted]\n')
            global passwordp
            if args.language == "SK":
                typewriter(printnlog('\nZačínam rozbaľovať\n', toprint=False))
            elif args.language == "EN":
                typewriter(printnlog('\nStarting to extract\n', toprint=False))
            elif args.language == "JP":
                typewriter(printnlog("\n抽出開始\n", toprint=False))
            sleep(0.25)
            try:

                """
                Extract the zip file containing the data.
                @param cachename - the name of the zip file containing the data.
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
                                sleep(0.01)
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
                                sleep(0.01)
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
                                sleep(0.01)
                            except zipfile.error as e:
                                pass
                    zip.close()
                if args.language == "SK":
                    typewriter(printnlog('Hotovo\n', toprint=False))
                    sleep(0.25)
                    typewriter(printnlog("Rozbaľujem druhu časť...\n", toprint=False))
                elif args.language == "EN":
                    typewriter(printnlog('Done\n', toprint=False))
                    sleep(0.25)
                    typewriter(printnlog("Unpacking second part...\n", toprint=False))
                elif args.language == "JP":
                    typewriter(printnlog('終わり\n', toprint=False))
                    sleep(0.25)
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
                    shutil.copy('data', 'data_backup')
                    os.mkdir('apphtml')
                    os.mkdir('assets')
                except Exception:
                    pass
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
                for r, d, f in os.walk('data1/'):
                    for file in f:
                        printnlog(os.path.join('./', file))
                        shutil.move(os.path.join('data1/', file),
                                    os.path.join('/', file))
                shutil.rmtree('data1')
                sleep(1)
                os.remove(cachename)
                os.remove('data.xp3')
                if args.language == "SK":
                    printnlog('\nHotovo\n')
                elif args.language == "EN":
                    printnlog('\nDone\n')
                elif args.language == "JP":
                    printnlog('\n完了\n')
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
                sleep(0.5)
            except FileNotFoundError:
                pass
            if args.language == 'SK':
                typewriter(printnlog('Inicializácia VLC\n', toprint=False))
            elif args.language == 'EN':
                typewriter(printnlog('Initialization VLC\n', toprint=False))
            elif args.language == 'JP':
                typewriter(printnlog('初期化 VLC\n', toprint=False))
            sleep(0.25)
            media_player = vlc.MediaPlayer()
            sleep(0.25)
            if args.language == 'SK':
                typewriter(printnlog('KONIEC', toprint=False))
            elif args.language == 'EN':
                typewriter(printnlog('END', toprint=False))
            elif args.language == 'JP':
                typewriter(printnlog('終わり', toprint=False))
            sleep(0.25)
            move('ZnámE', -10, -10, screensize[0], screensize[1])
            if args.test != None:
                try:
                    window = pygetwindow.getWindowsWithTitle('ZnámE')[0]
                    window.maximize()
                except IndexError:
                    exit = True
                    error_get(IndexError, get_line_number(
                    ), 'Possible solution; run in cmd or python aplication not ide or put arguments \'--test\'')
            if args.restart != None:
                player = vlc.Instance('--fullscreen')
                media_list = player.media_list_new()  # type: ignore
                media_player = player.media_list_player_new()  # type: ignore
                media = player.media_new(
                    "assets/transition.mp4")  # type: ignore
                media_list.add_media(media)
                media_player.set_media_list(media_list)
                media_player.play()
            inactive1 = False
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
                            inactive1 = True
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
                if args.update == None:
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
            logged = False
            exit = False
            tologin = False
            restart = False
            topassword = False
            topasswordhelp = False
            loggedhelp = False
            firstlogin = True
            vstup = ''
            logins = 0
            help = ['help', 'pomoc', '-h', '-help', '?', '-?']
            advhelp = ['advanced help', 'ah', '-ah', '-advanced help']
            linenumber = 1  # type: ignore
            neko = False
            waifu = False
            waifuvid = False
            musicplay = False
            offline_game = False
            """
            If the user has not disabled the intro, play it. Otherwise, do nothing.
            @param None
            @return None
            """
            if args.restart != None:
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
            exit = getWindow()
            if args.nointro == None or config.get('basic info', 'intro').split(' ')[0] == 'False':
                pass
            else:
                window = pygetwindow.getWindowsWithTitle('frame2')[0]
                window.activate()
            getImg('assets/banner.png', 'banner', 0, 0,
                   screensize[0], int((round((322/1736)*screensize[0], 0))))
            move('ZnámE', 0, int((round((322/1736)*screensize[0], 0))-35), screensize[0], screensize[1]-int(
                (round((322/1736)*screensize[0], 0))))
            if args.test != None:
                try:
                    window = pygetwindow.getWindowsWithTitle('ZnámE')[0]
                    window.activate()
                except IndexError:
                    exit = True
                    error_get(IndexError, get_line_number(
                    ), 'Possible solution; run in cmd or python aplication not ide or put arguments \'--test\'')
            pg.press('win')
            sleep(0.1)
            pg.press('win')
            os.system('cls')
            if args.music != '0':
                mixer.init()
                mixer.music.load('assets/' + music[int(args.music)-1] + '.mp3')
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
            if args.restart == None:
                open('CONTINUE', 'x')
            while True:
                internet_check()
                if not exit:
                    global loginvstupuser
                    if logged:
                        if firstlogin:
                            logins += 1
                            firstlogin = False
                            shutil.copy2('data', 'data_backup')
                            """
                            If the user wants to save their login credentials, save them to a file.
                            @param loginvstupuser - the username for the login credentials
                            @param password - the password for the login credentials
                            @param savefilemode - whether or not we are saving the file or not
                            """
                            if savefilemode:   # type: ignore
                                flvstup = ''
                                linenumber -= 1
                            elif args.language == "SK":
                                flvstup = input(
                                    str(linenumber) + "Chcete si uložiť svoje prihlasovacie údaje? (y/N) > ")
                            elif args.language == "EN":
                                flvstup = input(
                                    str(linenumber) + "Do you want to save your login credentials? (y/N) > ")
                            elif args.language == "JP":
                                flvstup = input(
                                    str(linenumber) + "ログイン資格情報を保存しますか? (y/N) > ")
                            else:
                                flvstup = input(
                                    "Do you want to save your login credentials? (y/N) > ")
                            flvstup.lower()
                            if flvstup == "y":
                                if not os.path.exists("C:/Users/" + os.getlogin() + "/AppData/Local/ZnámE/"):
                                    os.mkdir(
                                        "C:/Users/" + os.getlogin() + "/AppData/Local/ZnámE/")
                                savelog = open(
                                    "C:/Users/" + os.getlogin() + "/AppData/Local/ZnámE/saved", "w")
                                tolog = str(code(str(loginvstupuser), str(
                                    passwordp[0]), mode=1))  # type: ignore
                                tolog = tolog[2:len(tolog)-2]
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
                                typewriter("'zz' to display marks\n'pz' to add marks")
                            elif args.language == "JP":
                                typewriter('「zz」でマークを表示\n「pz」でマークを追加')
                            loggedhelp = False
                        vstup = input(str(linenumber) + ' > ')
                        linenumber += 1
                        historyfile.write(
                            '[' + str(linenumber) + ', ' + vstup + ']\n')
                        vstup.lower()
                        historyfile.close()
                        historyfile = open(historyname, 'a')
                        """
                        Check if the user has asked for help. If so, print the help message.
                        @param vstup - the user input string
                        @returns True if the user has asked for help, False otherwise
                        """
                        help = ['help', 'pomoc', '-h', '-help', '?', '-?']
                        for i in range(len(help)):
                            if vstup == help[i]:
                                loggedhelp = True
                        if loggedhelp:
                            continue
                        if vstup == 'delsavlog':
                            uninstall()
                        if vstup == "zz":
                            passwordfile = open(
                                passwordp[1], 'r')  # type: ignore
                            countersubject = 0
                            counter = 6
                            counterfirst = True
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
                                        countersubject = 0
                                    counterfirst = True
                                    countersubject += 1
                                    print(i, end="")
                                    if countersubject > 2:
                                        typewriter(" | ", end="")
                            passwordfile.close()
                        """
                        This function is used to add a new subject to the database. It is called when the user
                        enters the subject and mark for a new subject. It will then call the code function to
                        encrypt the data and save it to the database.
                        @param subject - the subject to be added to the database.
                        @param mark - the mark for the subject.
                        """
                        if vstup == "pz":
                            if args.language == "SK":
                                subject = input(
                                    str(linenumber) + ' Predmet > ')
                                historyfile.write(
                                    '[' + str(linenumber) + ', ' + subject + ']\n')
                                vstup.lower()
                                historyfile.close()
                                historyfile = open(historyname, 'a')
                                if subject == 'quit':
                                    exit = True
                                    continue
                                if subject == 'back':
                                    continue
                                mark = input(str(linenumber) + ' Známka > ')
                                historyfile.write(
                                    '[' + str(linenumber) + ', ' + mark + ']\n')
                                vstup.lower()
                                historyfile.close()
                                historyfile = open(historyname, 'a')
                            elif args.language == "EN":
                                subject = input(
                                    str(linenumber) + ' Subject > ')
                                historyfile.write(
                                    '[' + str(linenumber) + ', ' + subject + ']\n')
                                vstup.lower()
                                historyfile.close()
                                historyfile = open(historyname, 'a')
                                if subject == 'quit':
                                    exit = True
                                    continue
                                if subject == 'back':
                                    continue
                                mark = input(str(linenumber) + ' Mark > ')
                                historyfile.write(
                                    '[' + str(linenumber) + ', ' + (mark) + ']\n')
                                vstup.lower()
                                historyfile.close()
                                historyfile = open(historyname, 'a')
                            elif args.language == "JP":
                                subject = input(str(linenumber) + ' 主題 > ')
                                historyfile.write(
                                    '[' + str(linenumber) + ', ' + subject + ']\n')
                                vstup.lower()
                                historyfile.close()
                                historyfile = open(historyname, 'a')
                                if subject == 'quit':
                                    exit = True
                                    continue
                                if subject == 'back':
                                    continue
                                mark = input(str(linenumber) + ' マーク > ')
                                historyfile.write(
                                    '[' + str(linenumber) + ', ' + mark + ']\n')
                                vstup.lower()
                                historyfile.close()
                                historyfile = open(historyname, 'a')
                            else:
                                subject = input(
                                    str(linenumber) + ' Subject > ')
                                historyfile.write(
                                    '[' + str(linenumber) + ', ' + subject + ']\n')
                                vstup.lower()
                                historyfile.close()
                                historyfile = open(historyname, 'a')
                                if subject == 'quit':
                                    exit = True
                                    continue
                                if subject == 'back':
                                    continue
                                mark = input(str(linenumber) + ' Mark > ')
                                historyfile.write(
                                    '[' + str(linenumber) + ', ' + mark + ']\n')
                                vstup.lower()
                                historyfile.close()
                                historyfile = open(historyname, 'a')
                            if subject == 'quit' or mark == 'quit':
                                exit = True
                                continue
                            if subject == 'back' or mark == 'back':
                                continue
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
                    if topassword:
                        if savefilemode:   # type: ignore
                            vstup = savefile[9:15]   # type: ignore
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
                        help = ['help', 'pomoc', '-h', '-help', '?', '-?']
                        for i in range(len(help)):
                            if vstup == help[i]:
                                topasswordhelp = True
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
                            topasswordhelp = False
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
                            topassword = False
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
                            exit = True
                        if args.language == "SK":
                            Thread(target=progress_bar, args=(
                                'Preverujem', 2,), daemon=True).start()
                        elif args.language == "EN":
                            Thread(target=progress_bar, args=(
                                'Checking', 2,), daemon=True).start()
                        elif args.language == "JP":
                            Thread(target=progress_bar, args=(
                                'チェック中', 2,), daemon=True).start()
                        passwordp = password(decode(loginvstupuser + 'crypted', True))  # type: ignore
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
                            counter = 0
                            for i in passwordfile.read():
                                passwordfile1.write(i)
                            passwordfile.close()
                            passwordfile1.close()
                            os.remove(loginvstupuser)
                            os.rename(loginvstupuser + '1', loginvstupuser)
                            topassword = False
                            logged = True
                            if os.path.exists("restart.py"):
                                os.remove('restart.py')
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
                                if args.language == 'SK':
                                    typewriter(
                                        "Všetko je nastavené!!!\nMôžete použiť program\n")
                                elif args.language == 'EN':
                                    typewriter("All is set!!!\nYou can use progam\n")
                                elif args.language == 'JP':
                                    typewriter("すべてが設定されました!!!\nプログラムを使用できます\n")
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
                            topassword = False
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
                    if args.neko == None:
                        sleep(1)
                        pg.write("nekon\n")
                    if args.waifu == None:
                        sleep(1)
                        pg.write("waifun\n")
                    """
                        this function is used to get the input from the user and write it to the history file.
                    @param vstup - the input from the user.
                    @param history - the history file.
                    @param linenumber - the line number of the history file.
                    """
                    if not tologin and not logged:
                        vstup = input(str(linenumber) + ' > ')
                        historyfile.write(
                            '[' + str(linenumber) + ', ' + vstup + ']\n')
                        vstup.lower()
                        historyfile.close()
                        historyfile = open(historyname, 'a')
                        linenumber += 1
                    inactivelogout = inactive()
                    if vstup in ['settings', 'setup']:
                        while True:
                            setvstup = input(
                                "1. basic info\n2. waifu setting\n3. neko settings\n4. game settings\n5. back\n> ")
                            if setvstup == '1':
                                while True:
                                    setvstup = input('1. lang = ' + config.get('basic info', 'lang').split(' ')[0] + '\n2. enviroment = ' + config.get('basic info', 'enviroment').split(' ')[0] + '\n3. intro (toggle) = ' + config.get('basic info', 'intro').split(' ')[
                                                     0] + '\n4. inactivelimit = ' + config.get('basic info', 'inactivelimit').split(' ')[0] + '\n5. music = ' + config.get('basic info', 'music').split(' ')[0] + '\n6. musiclist = ' + config.get('basic info', 'musiclist').split(' ')[0] + '\n7. back\n> ')
                                    if setvstup == '1':
                                        while True:
                                            setvstup = input(
                                                '1. SK\n2. EN\n3. JP\n4. back\n> ')
                                            if setvstup == '1':
                                                set_config(
                                                    'basic info', 'lang', 'SK')
                                                break
                                            elif setvstup == '2':
                                                set_config(
                                                    'basic info', 'lang', 'EN')
                                                break
                                            elif setvstup == '3':
                                                set_config(
                                                    'basic info', 'lang', 'SK')
                                                break
                                            elif setvstup == '4':
                                                break
                                    elif setvstup == '2':
                                        setvstup = input('Set enviroment\n> ')
                                        set_config(
                                            'basic info', 'enviroment', setvstup)
                                    elif setvstup == '3':
                                        if config.get('basic info', 'intro').split(' ')[0] == "True":
                                            set_config(
                                                'basic info', 'intro', 'False')
                                        elif config.get('basic info', 'intro').split(' ')[0] == "False":
                                            set_config(
                                                'basic info', 'intro', 'True')
                                    elif setvstup == '4':
                                        setvstup = input(
                                            'Set inactivelimit\n> ')
                                        set_config(
                                            'basic info', 'inactivelimit', setvstup)
                                        if logged:
                                            if args.language == 'SK':
                                                print(
                                                    'Na vykonanie zmeny je potrebný reštart')
                                            if args.language == 'EN':
                                                print(
                                                    'Needed restart to take change')
                                            if args.language == 'JP':
                                                print('変更するには再起動が必要')
                                    elif setvstup == '5':
                                        if config.get('basic info', 'music').split(' ')[0] == "enable":
                                            set_config(
                                                'basic info', 'music', 'disable')
                                        elif config.get('basic info', 'music').split(' ')[0] == "disable":
                                            set_config(
                                                'basic info', 'music', 'enable')
                                    elif setvstup == '6':
                                        setvstup = input(
                                            'Set musiclist' + str(music) + '\n> ')
                                        set_config(
                                            'basic info', 'musiclist', setvstup)
                                    elif setvstup == '7':
                                        break
                            elif setvstup == '2':
                                while True:
                                    setvstup = input('1. type = ' + config.get('waifu settings', 'type').split(' ')[
                                                     0] + '\n2. category = ' + config.get('waifu settings', 'category').split(' ')[0] + '\n3. back\n> ')
                                    if setvstup == '1':
                                        while True:
                                            setvstup = input(
                                                '1. SFW\n2. NSFW\n3. back\n> ')
                                            if setvstup == '1':
                                                set_config(
                                                    'waifu settings', 'type', 'sfw')
                                                setvstup = '2'
                                                break
                                            elif setvstup == '2':
                                                setvstup = input(
                                                    'Do you have 18+ (y/N) > ').lower()
                                                if setvstup == 'y':
                                                    set_config(
                                                        'waifu settings', 'type', 'nsfw')
                                                    setvstup = '2'
                                                    break
                                                else:
                                                    break
                                            elif setvstup == '3':
                                                break
                                    if setvstup == '2':
                                        if config.get('waifu settings', 'type').split(' ')[0] == 'sfw':
                                            category = ["waifu", "neko", "shinobu", "megumin", "bully", "cuddle", "cry", "hug", "awoo", "kiss", "lick", "pat", "smug", "bonk", "yeet", "blush",
                                                        "smile", "wave", "highfive", "handhold", "nom", "bite", "glomp", "slap", "kill", "kick", "happy", "wink", "poke", "dance", "cringe", "back"]
                                            while True:
                                                for i in range(0, len(category)):
                                                    typewriter(str(i + 1) +
                                                          '. ' + category[i])
                                                setvstup = int(input("> "))
                                                if category[setvstup-1] == 'back':
                                                    break
                                                try:
                                                    set_config(
                                                        'waifu settings', 'category', category[setvstup-1])
                                                    break
                                                except Exception:
                                                    continue
                                        elif config.get('waifu settings', 'type').split(' ')[0] == 'nsfw':
                                            category = [
                                                'waifu', 'neko', 'trap', 'blowjob', 'back']
                                            while True:
                                                for i in range(0, len(category)):
                                                    typewriter(str(i + 1) +
                                                          '. ' + category[i])
                                                setvstup = int(input("> "))
                                                if category[setvstup-1] == 'back':
                                                    break
                                                try:
                                                    set_config(
                                                        'waifu settings', 'category', category[setvstup-1])
                                                    break
                                                except Exception:
                                                    continue
                                    elif setvstup == '3':
                                        break
                            elif setvstup == '3':
                                while True:
                                    setvstup = input('1. server\n2. back\n> ')
                                    if setvstup == '1':
                                        while True:
                                            setvstup = input(
                                                '1. nekos.best\n2. waifu.pics\n3. back\n> ')
                                            if setvstup == '1':
                                                set_config(
                                                    'neko settings', 'server', 'nekos.best')
                                                break
                                            elif setvstup == '2':
                                                set_config(
                                                    'neko settings', 'server', 'waifu.pics')
                                                break
                                            elif setvstup == '3':
                                                break
                                    elif setvstup == '2':
                                        break
                            elif setvstup == '4':
                                while True:
                                    setvstup = input('1. goal_score = ' + config.get('game settings', 'goal_score').split(' ')[
                                                        0] + '\n2. computer_power = ' + config.get('game settings', 'computer_power').split(' ')[0] + '\n3. back\n> ')
                            elif setvstup == '5':
                                break
                        print('')
                    if vstup == 'playvideo':
                        while True:
                            videovstup = input('1. Dan Dan Don Don\n2. back\n> ')
                            if videovstup == '1':
                                try:
                                    mixer.music.pause()
                                except Exception:
                                    pass
                                PlayVideo('assets/Dan_Dan_Don_Don.mp4')
                                try:
                                    mixer.music.unpause()
                                except Exception:
                                    pass
                            elif videovstup == '2':
                                break
                        
                    if vstup == 'music':
                        mixer.init()
                        for i in range(0, len(music)):
                            typewriter(str(i + 1) + ') ' + music[i])
                        musicvstup = int(input('> '))
                        args.music = str(musicvstup)
                        try:
                            if musicvstup == len(music)+1:
                                continue
                            mixer.music.load(
                                'assets/' + music[musicvstup-1] + '.mp3')
                        except IndexError:
                            pg.write('music\n')
                        mixer.music.play()
                        musicplay = True
                    if vstup == 'quitmusic':
                        mixer.music.stop()
                        musicplay = False
                    if vstup == 'save':
                        if waifu or neko or waifuvid:
                            imagetime = str(
                                datetime.now().strftime("%H-%M-%S"))
                            try:
                                os.mkdir('download/')
                                typewriter('Making directory \'download\'', end='\r')
                            except Exception:
                                pass
                            if neko:
                                typewriter('Copying neko to download folder', end='\r')
                                shutil.copy(
                                    'assets/neko.png', 'download/neko-' + imagetime + '.png')
                            elif waifuvid:
                                typewriter('Copying waifu video to download folder', end='\r')
                                shutil.copy(
                                    'assets/waifu.mp4', 'download/waifu-' + imagetime + '.mp4')
                            elif waifu:
                                typewriter('Copying waifu to download folder', end='\r')
                                shutil.copy(
                                    'assets/waifu.png', 'download/waifu-' + imagetime + '.png')
                            typewriter('Done                                            ')
                        else:
                            if args.language == 'SK':
                                typewriter('Nemáte obrázok na uloženie')
                            elif args.language == 'EN':
                                typewriter("You don't have image to save")
                            elif args.language == 'JP':
                                typewriter('保存する画像がありません')
                    if vstup == 'offlinegame':
                        offline_game = True
                        create_gamefiles()
                    if vstup == 'game':
                        if waifu or waifuvid or neko:
                            if args.language == 'SK':
                                typewriter('Najprv musíte ukončiť neko alebo waifu')
                            if args.language == 'EN':
                                typewriter('First you need to quit neko or waifu')
                            if args.language == 'JP':
                                typewriter('まず、nekoまたはwaifuを終了する必要があります')
                            continue
                        mixer.music.pause()
                        game()
                        mixer.music.unpause()
                        os.system('title ZnámE')
                        os.system('cls')
                        verzia = open('version', 'r')
                        if args.language == "SK":
                            typewriter('Používate ZnámE ' + verzia.read() + "\n")
                        elif args.language == "EN":
                            typewriter('You\'re using ZnámE ' +
                                  verzia.read() + "\n")
                        elif args.language == "JP":
                            typewriter('ZnámE を使用しています ' + verzia.read() + "\n")
                        verzia.close()
                    if vstup == 'motivational':
                        resp = requests.get(
                            "https://animechan.vercel.app/api/random")
                        data = resp.json()
                        anime = data["anime"]
                        character = data["character"]
                        quote = data["quote"]
                        sleep(1)
                        typewriter("Anime: " + anime + '\nCharacter: ' +
                              character + "\nQuote: " + quote)
                    if vstup == 'anotherneko':
                        pg.write("quitneko\nneko\n")
                    if vstup[0:4] == 'neko':
                        if neko:
                            if args.language == 'SK':
                                typewriter('Prepáč, že nemôžeš mať dve neko')
                            elif args.language == 'EN':
                                typewriter("Sorry you can't have two nekos")
                            elif args.language == 'JP':
                                typewriter('ごめんね、ネコを2匹飼えないよ')
                            continue
                        if waifu:
                            if args.language == 'SK':
                                typewriter(
                                    'Prepáčte, že nemôžete mať neko, ak máte waifu')
                            elif args.language == 'EN':
                                typewriter("Sorry you can't have neko if you have waifu")
                            elif args.language == 'JP':
                                typewriter('すみません、ワイフを持っているならネコを持ってはいけない')
                            continue
                        if args.language == 'SK':
                            typewriter('ČAKAJ')
                        elif args.language == 'EN':
                            typewriter('WAIT')
                        elif args.language == 'JP':
                            typewriter('待つ')
                        if args.neko != None:
                            if config.get('neko settings', 'server').split(' ')[0] == 'nekos.best':
                                if args.language == 'SK':
                                    typewriter(
                                        'Získavanie obrazu zo servera nekos.best')
                                elif args.language == 'EN':
                                    typewriter('Getting image from nekos.best server')
                                elif args.language == 'JP':
                                    typewriter('nekos.best サーバーから画像を取得する')
                                resp = requests.get("https://nekos.best/api/v2/neko")
                                data = resp.json()
                                res = requests.get(
                                    data["results"][0]["url"], stream=True)  # type: ignore
                            elif config.get('neko settings', 'server').split(' ')[0] == 'waifu.pics':
                                if args.language == 'SK':
                                    typewriter(
                                        'Získavanie obrazu zo servera waifu.pics')
                                elif args.language == 'EN':
                                    typewriter('Getting image from waifu.pics server')
                                elif args.language == 'JP':
                                    typewriter('waifu.pics サーバーから画像を取得する')
                                resp = requests.get(
                                    "https://api.waifu.pics/sfw/neko")
                                data = resp.json()
                                res = requests.get(data["url"], stream=True)
                            else:
                                if args.language == 'SK':
                                    typewriter('Nie je poskytnutý žiadny server')
                                elif args.language == 'EN':
                                    typewriter('No server provided')
                                elif args.language == 'JP':
                                    typewriter('サーバーが提供されていません')
                                continue
                            typewriter('Downloading image')
                            if res.status_code == 200:
                                if config.get('neko settings', 'server').split(' ')[0] == 'nekos.best':
                                    download(data["results"][0]["url"], 'assets/neko.png')
                                elif config.get('neko settings', 'server').split(' ')[0] == 'waifu.pics':
                                    download(data['url'], 'assets/neko.png')
                        else:
                            args.neko = object()
                        typewriter('Setting image          ', end='\r')
                        img = Image.open('assets/neko.png')
                        typewriter('Opening image          ', end='\r')
                        img.show()
                        sleep(0.1)
                        typewriter('DONE                          ', end='\r')
                        pg.keyDown('win')
                        typewriter('......', end='\r')
                        pg.press('right')
                        typewriter('.......', end='\r')
                        pg.keyUp('win')
                        pg.press('esc')
                        typewriter('Getting cli in foreground     ', end='\r')
                        window = pygetwindow.getWindowsWithTitle('ZnámE')[0]
                        window.activate()
                        mixer.Channel(0).play(mixer.Sound('assets/neko.mp3'))
                        typewriter('Playing sound                 ', end='\r')
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
                                typewriter(':( Nemôžeš mať -1 neko')
                            elif args.language == 'EN':
                                typewriter(":( You can't have -1 neko")
                            elif args.language == 'JP':
                                typewriter(':( 猫を-1にすることはできません')
                            continue
                        typewriter('Closing image', end='\r')
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
                        typewriter('Done             ', end='\r')
                        sleep(0.1)
                        typewriter('Removeing image', end='\r')
                        os.remove('assets/neko.png')
                        typewriter('Resizing cli', end='\r')
                        move('ZnámE', 0, int((round((322/1736)*screensize[0], 0))-35), screensize[0], screensize[1]-int(
                            (round((322/1736)*screensize[0], 0))))
                        typewriter('Done             ')
                        neko = False
                    if vstup == 'anotherwaifu':
                        pg.write("quitwaifu\nwaifu\n")
                    if vstup[0:5] == 'waifu':
                        if waifu:
                            if args.language == 'SK':
                                typewriter('Prepáčte, nemôžete mať dve waifu')
                            elif args.language == 'EN':
                                typewriter("Sorry you can't have two waifu")
                            elif args.language == 'JP':
                                typewriter('申し訳ありませんが、ワイフを 2 つ持つことはできません')
                            continue
                        if neko:
                            if args.language == 'SK':
                                typewriter('Prepáčte, že nemôžete mať waifu a neko')
                            elif args.language == 'EN':
                                typewriter("Sorry you can't have waifu and neko")
                            elif args.language == 'JP':
                                typewriter('ごめんなさい、ワイフとネコは使えません')
                            continue
                        if args.language == 'SK':
                            typewriter('ČAKAJ')
                        elif args.language == 'EN':
                            typewriter('WAIT')
                        elif args.language == 'JP':
                            typewriter('待つ')
                        if args.waifu != None:
                            if args.language == 'SK':
                                typewriter('Získavanie obrazu zo servera waifu.pics')
                            elif args.language == 'EN':
                                typewriter('Getting image from waifu.pics server')
                            elif args.language == 'JP':
                                typewriter('waifu.pics サーバーから画像を取得する')
                            resp = requests.get("https://api.waifu.pics/" + config.get('waifu settings', 'type').split(
                                ' ')[0] + "/" + config.get('waifu settings', 'category').split(' ')[0])
                            data = resp.json()
                            img_data = requests.get(data["url"]).content
                            typewriter('Downloading image')
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
                                waifuvid = True
                                sleep(1)
                            elif data["url"].split('.')[-1] != 'gif':
                                res = requests.get(data["url"], stream=True)
                                if res.status_code == 200:
                                    download(data['url'], 'assets/waifu.png')
                        elif args.waifuvid == None:
                            data = {'url': 'https://api.waifu.pics/waifu.mp4'}
                            waifuvid = True
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
                        elif args.waifu == None:
                            args.waifu = UNSPECIFIED
                            data = {'url': 'https://api.waifu.pics/waifu.png'}
                        typewriter('Setting image    ', end='\r')
                        if data["url"].split('.')[-1] != 'gif' and data["url"].split('.')[-1] != 'mp4':
                            img = Image.open('assets/waifu.png')
                            typewriter('Opening image   ', end='\r')
                            img.show()
                        elif data["url"].split('.')[-1] == 'gif' or data["url"].split('.')[-1] == 'mp4':
                            sleep(0.2)
                            typewriter('Getting video in foreground', end='\r')
                            window = pygetwindow.getWindowsWithTitle(
                                'VLC (Direct3D11 Output)')[0]
                            window.activate()
                            sleep(0.1)
                        sleep(0.1)
                        # type: ignore
                        pg.keyDown('win')
                        typewriter('......                        ', end='\r')
                        pg.press('right')
                        typewriter('.......', end='\r')
                        pg.keyUp('win')
                        typewriter('........', end='\r')
                        pg.press('esc')
                        typewriter('Getting cli in foreground', end='\r')
                        window = pygetwindow.getWindowsWithTitle('ZnámE')[0]
                        window.activate()
                        sleep(0.5)
                        typewriter('..........                  ', end='\r')
                        sleep(0.25)
                        typewriter('.............', end='\r')
                        if args.language == 'SK':
                            typewriter('HOTOVO         ')
                        elif args.language == 'EN':
                            typewriter('DONE           ')
                        elif args.language == 'JP':
                            typewriter('終わり          ')
                        # if config.get('waifu settings', 'type') == 'sfw' and config.get('waifu settings', 'category') in ['kiss', 'lick']:
                        #     mixer.init()
                        #     mixer.music.load('assets/' + str(random.randint(1,4)) +'.mp3')
                        #     mixer.music.play()
                        move("ZnámE", 0, int((round((322/1736)*screensize[0], 0))-35), int(screensize[0]/2), int(
                            (round((0.95-(0.31203703703703706))*screensize[1], 0))))  # 337/1080
                        waifu = True
                    if vstup == 'quitwaifu':
                        if not waifu:
                            if args.language == 'SK':
                                print(':( Nemôžeš mať -1 waifu')
                            elif args.language == 'EN':
                                print(":( You can't have -1 waifu")
                            elif args.language == 'JP':
                                print(':( -1ワイフを持つことはできません')
                            continue
                        elif waifuvid:
                            typewriter('Stoping video', end='\r')
                            media_player.stop()  # type: ignore
                            waifuvid = False
                            typewriter('Removing video   ', end='\r')
                            os.remove('assets/waifu.mp4')
                        else:
                            typewriter('Closing image', end='\r')
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
                        typewriter('Resizing cli      ', end='\r')
                        move('ZnámE', 0, int((round((322/1736)*screensize[0], 0))-35), screensize[0], screensize[1]-int(
                            (round((322/1736)*screensize[0], 0))))
                        try:
                            typewriter('Removing image', end='\r')
                            os.remove('assets/waifu.png')
                        except Exception:
                            pass
                        waifu = False
                        typewriter('Done               ')
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
                        restart = True
                        exit = True
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
                        logged = False
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
                        continue
                    """
                    If the user has logged in and is inactive for a long time, log them out.
                    @param logged - whether the user is logged in or not.
                    @param inactivelogout - whether the user is inactive or not.
                    @param restart - whether the user has restarted the program or not.
                    """
                    if logged and inactivelogout and restart:
                        logged = False
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
                        logged = False
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
                        exit = True
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
                                advhelpcont = False
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
                                        advhelpcont = True
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
                            loginvstupuser = ''
                            tologin = False
                            savefilemode = False
                            """
                            If the user wants to login, check if the user wants to restart the program. If the user wants to restart the program,
                            set the restart flag to true. If the user does not want to restart the program, set the restart flag to false.
                            @param logins - the number of logins since the last restart.
                            @param args - the arguments from the command line.
                            @returns the restart flag and the exit flag.
                            """
                            if logins == 1:
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
                                    restart = True
                                    exit = True
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
                                    savefilemode = True
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
                            tologinhelp = False
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
                                exit = True
                                continue
                            help = ['help', 'pomoc', '-h', '-help', '?', '-?']
                            for i in range(len(help)):
                                if loginvstupuser == help[i]:
                                    tologinhelp = True
                            if tologinhelp:
                                if args.language == "SK":
                                    print(
                                        "'back' pre menu\n'quit' alebo 'koniec' pre koniec")
                                elif args.language == "EN":
                                    print(
                                        "'back' for menu\n'quit' or 'end' for end")
                                elif args.language == "JP":
                                    print("メニューの「戻る」\n 'quit' または 'end' で終了")
                                tologin = True
                                continue
                            elif not loginvstupuser.isnumeric():
                                if args.language == "SK":
                                    print('PID neobsahuje písmená alebo znaky!!!')
                                elif args.language == "EN":
                                    print(
                                        'The PID does not contain letters or characters!!!')
                                elif args.language == "JP":
                                    print('PID に文字が含まれていません!!!')
                                tologin = True
                                continue
                            if len(str(loginvstupuser)) == 6:
                                exit = False
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
                                    logged = False
                                    os.remove(loginvstupuser + 'crypted')
                                    progress_bar_check = 100
                                    sleep(0.1)
                                    if args.language == "SK":
                                        print("ZLÉ PID!!!")
                                    elif args.language == "EN":
                                        print("WRONG PID!!!")
                                    elif args.language == "JP":
                                        print('間違った PID !!!')
                                    tologin = True
                                    continue
                                topassword = True
                            else:
                                if args.language == "SK":
                                    print('PID má byt 6 čísel dlhé!!!')
                                elif args.language == "EN":
                                    print('The PID should be 6 numbers long!!!')
                                elif args.language == "JP":
                                    print('PID は 6 桁の長さでなければなりません!!!')
                                tologin = True
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
                            os.remove('CONTINUE')
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
                        typewriter(
                            "ODSTRAŇOVANIE NEPOTREBNÝCH SÚBOROV\n\nPísanie histórie\n")
                    elif args.language == "EN":
                        typewriter("DELETING UNNECESSARY FILES\n\nWriting history\n")
                    elif args.language == "JP":
                        typewriter('不要なファイルを削除しています\n\n執筆履歴\n')
                    start = time.time()
                    sleep(0.25)
                    version = open('version', 'r')
                    versionlist = version.readlines()[0].split('.')
                    version.close()
                    version = open('version', 'w')
                    version.write(versionlist[0] + '.' + versionlist[1] + '.' + versionlist[2] + '.' + str(
                                  datetime.today().strftime("%Y%m%d.%H%M%S")))
                    version.close()
                    historylist = []
                    try:
                        historyfile = open(historyname, 'r')
                        for i in historyfile.readlines():
                            historylist.append(i.strip('\n'))
                    except Exception:
                        pass
                    set_config('user history', historyname, str(
                                     datetime.today().strftime("%d-%m-%Y__time__%H-%M-%S")) + str(historylist))
                    typewriter(historyname + ' ' + str(
                                     datetime.today().strftime("%d-%m-%Y__time__%H-%M-%S")) + str(historylist) + '\n')
                    historyfile.close()
                    try:
                        os.remove(historyname)
                    except Exception:
                        pass
                    if args.language == "SK":
                        typewriter("Hotovo\n")
                    elif args.language == "EN":
                        typewriter("Done\n")
                    elif args.language == "JP":
                        typewriter('終わり\n')
                    playhtml('apphtml\\end', 1, 3)
                    try:
                        os.remove('data_backup')
                    except Exception:
                        pass
                    typewriter('.', end='\r')
                    sleep(0.2)
                    try:
                        os.mkdir('datafolder')
                    except FileExistsError:
                        pass
                    sleep(0.2)
                    try:
                        shutil.move('data', 'datafolder/')
                    except Exception:
                        quit()
                    source_dir = 'assets/'
                    os.mkdir('datafolder/' + source_dir)
                    for file_name in os.listdir(source_dir):
                        shutil.move(os.path.join(source_dir, file_name),
                                    'datafolder/' + source_dir)
                    source_dir = 'apphtml/'
                    os.mkdir('datafolder/' + source_dir)
                    for file_name in os.listdir(source_dir):
                        shutil.move(os.path.join(source_dir, file_name),
                                    'datafolder/' + source_dir)
                    sleep(0.2)
                    if args.language == "SK":
                        typewriter("ZABAĽUJEM DATA\n")
                        sleep(0.2)
                        subprocess.call([sys.executable, 'xp3.py', 'datafolder',
                                        'data.xp3', '-mode', 'repack', '-e', 'neko_vol0_steam'])
                    elif args.language == "EN":
                        typewriter("PACKING DATA\n")
                        sleep(0.2)
                        subprocess.call([sys.executable, 'xp3.py', 'datafolder', 'data.xp3',
                                        '-mode', 'repack', '-e', 'neko_vol0_steam', '-lang', 'EN'])
                    elif args.language == "JP":
                        typewriter("梱包データ\n")
                        sleep(0.2)
                        subprocess.call([sys.executable, 'xp3.py', 'datafolder', 'data.xp3',
                                        '-mode', 'repack', '-e', 'neko_vol0_steam', '-lang', 'JP'])
                    shutil.rmtree('datafolder')
                    shutil.rmtree('apphtml')
                    shutil.rmtree('assets')
                    if args.language == "SK":
                        typewriter("\nHOTOVO\n")
                        sleep(0.5)
                        cv2.destroyAllWindows()
                        typewriter("ZABAĽUJEM DRUHÚ ČASŤ DATA\n")
                    elif args.language == "EN":
                        typewriter("\nCOMPLETE\n")
                        sleep(0.5)
                        cv2.destroyAllWindows()
                        typewriter("PACKING SECOND PART OF DATA\n")
                    elif args.language == "JP":
                        typewriter("\n完了\n")
                        sleep(0.5)
                        cv2.destroyAllWindows()
                        typewriter("データの 2 番目の部分のパッキング\n")
                    zipfiles = ['tests.py', 'xp3.py',
                                'xp3reader.py', 'xp3writer.py', 'data.xp3']
                    zipfileswopath = ['tests.py', 'xp3.py',
                                      'xp3reader.py', 'xp3writer.py', 'data.xp3']
                    folders = ['structs']
                    for i in range(0, len(folders)):
                        for path, directories, files in os.walk(folders[i]):
                            for file in files:
                                file_name = os.path.join(path, file)
                                zipfiles.append(file_name)
                                zipfileswopath.append(file)
                    with zipfile.ZipFile(cachename, mode='w', compresslevel=5) as zip:
                        zip_kb_old = 0
                        zipfilesnumber = len(zipfiles)
                        if args.language == "SK":
                            bar = tqdm(range(0, len(zipfiles)),
                                       desc="Zabaľujem ")
                            for i in bar:
                                zip.write(zipfiles[i])
                                filesize = sum(
                                    [zinfo.file_size for zinfo in zip.filelist])
                                sleep(0.04)
                                tqdm.write(zipfileswopath[i] + "(" + str(os.path.getsize(
                                    zipfiles[i])) + " KB) -> " + str(round(filesize - zip_kb_old, 2)) + " KB")
                                zip_kb_old = filesize
                                os.remove(zipfiles[i])
                                if i == len(zipfiles)-1:
                                    tqdm.write("\n")
                            filesize = sum(
                                [zinfo.file_size for zinfo in zip.filelist])
                            typewriter("\nZabalené data majú > " +
                                       str(filesize) + " KB")
                        elif args.language == "EN":
                            bar = tqdm(range(0, len(zipfiles)),
                                       desc="Packing ")
                            for i in bar:
                                zip.write(zipfiles[i])
                                filesize = sum(
                                    [zinfo.file_size for zinfo in zip.filelist])
                                sleep(0.02)
                                tqdm.write(zipfileswopath[i] + "(" + str(os.path.getsize(
                                    zipfiles[i])) + " KB) -> " + str(round(filesize - zip_kb_old, 2)) + " KB")
                                zip_kb_old = filesize
                                os.remove(zipfiles[i])
                                if i == len(zipfiles)-1:
                                    tqdm.write("\n")
                            filesize = sum(
                                [zinfo.file_size for zinfo in zip.filelist])
                            typewriter("\nPacked data have > " +
                                       str(filesize) + " KB")
                        elif args.language == "JP":
                            bar = tqdm(range(0, len(zipfiles)), desc="梱包 ")
                            for i in bar:
                                zip.write(zipfiles[i])
                                filesize = sum(
                                    [zinfo.file_size for zinfo in zip.filelist])
                                sleep(0.02)
                                tqdm.write(zipfileswopath[i] + "(" + str(os.path.getsize(
                                    zipfiles[i])) + " KB) -> " + str(round(filesize - zip_kb_old, 2)) + " KB")
                                zip_kb_old = filesize
                                os.remove(zipfiles[i])
                                if i == len(zipfiles)-1:
                                    tqdm.write("\n")
                            filesize = sum(
                                [zinfo.file_size for zinfo in zip.filelist])
                            typewriter("\nパックされたデータは > " +
                                       str(filesize) + " KB")
                        zip.close()
                    for i in range(0, len(folders)):
                        shutil.rmtree(folders[i])
                    sleep(0.2)
                    if args.language == "SK":
                        typewriter("\nHOTOVO\n")
                    elif args.language == "EN":
                        typewriter("\nCOMPLETE\n")
                    elif args.language == "JP":
                        typewriter('\n未完了\n')
                    end = time.time()
                    sleep(0.2)
                    if args.language == "SK":
                        typewriter('Uplynutý čas balenia: ' +
                              str(end-start-1.75-zipfilesnumber*0.02) + '\n')
                    elif args.language == "EN":
                        typewriter('Elapsed time of packing: ' +
                              str(end-start-1.75-zipfilesnumber*0.02) + '\n')
                    elif args.language == "JP":
                        typewriter('梱包経過時間: ' + str(end-start -
                              1.75-zipfilesnumber*0.02) + '\n')
                    sleep(0.5)
                    if restart:
                        if args.language == "SK":
                            typewriter('Program sa automaticky reštartuje.')
                        elif args.language == "EN":
                            typewriter('The program will restart automatically.')
                        elif args.language == "JP":
                            typewriter('プログラムが自動的に再起動します。')
                    elif not restart:
                        if args.endf == None:
                            pass
                        else:
                            if args.language == "SK":
                                typewriter('Program sa automaticky vypne.')
                            elif args.language == "EN":
                                typewriter('The program will automatically shut down.')
                            elif args.language == "JP":
                                typewriter('プログラムは自動的にシャットダウンします。')
                    sleep(0.5)
                    count = 0
                    for root_dir, cur_dir, files in os.walk(r"C:/Users/" + os.getlogin() + "/AppData/Local/ZnámE/backup/"):
                        count += len(files)
                    if not os.path.exists("C:/Users/" + os.getlogin() + "/AppData/Local/ZnámE/backup/"):
                        os.mkdir("C:/Users/" + os.getlogin() +
                                 "/AppData/Local/ZnámE/backup/")
                        shutil.copy('data.xp2', "C:/Users/" + os.getlogin() + "/AppData/Local/ZnámE/backup/backup-" + str(
                            datetime.now().strftime("%y-%m-%d-%H-%M-%S")) + '.xp2')
                        x = open("C:/Users/" + os.getlogin() +
                                 "/AppData/Local/ZnámE/backup/info.txt", 'w')
                        x.write(
                            'Rename \'xp2\' file to \'data.xp2\' and move it to your \'ZnámE\' directory')
                        x.close()
                    else:
                        if count >= 11:
                            for root_dir, cur_dir, files in os.walk(r"C:/Users/" + os.getlogin() + "/AppData/Local/ZnámE/backup/"):
                                os.remove("C:/Users/" + os.getlogin() +
                                          "/AppData/Local/ZnámE/backup/" + files[0])
                        shutil.copy('data.xp2', "C:/Users/" + os.getlogin() + "/AppData/Local/ZnámE/backup/backup-" + str(
                            datetime.now().strftime("%y-%m-%d-%H-%M-%S")) + '.xp2')
                    if args.endf != None and not restart:
                        sleep(2.5)
                    if not offline_game:
                        try:
                            shutil.rmtree('game')
                        except Exception:
                            pass
                    if restart:
                        crrestart = open("restart.py", "w")
                        crrestart.write(restartapp)
                        crrestart.close()
                        os.remove('END')
                        if not inactivelogout and os.path.isfile("C:/Users/" + os.getlogin() + "/AppData/Local/ZnámE/saved"):
                            if args.language == "SK":
                                typewriter(
                                    "!\n!!\n!!!\nUPOZORNENIE\nČAKAJTE, KÝM VÁM PROGRAM POVIE ŽE MÔŽETE\n!!!\n!!\n!\n")
                            elif args.language == "EN":
                                typewriter(
                                    "!\n!!\n!!!\nWARNING\nWAIT UNTIL PROGRAM SAYS YOU CAN\n!!!\n!!\n!\n")
                            elif args.language == "JP":
                                typewriter(
                                    "!\n!!\n!!!\n警告\nプログラムができると言うまで待ってください\n!!!\n!!\n!\n")
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
                                        os.remove('CONTINUE')
                                    except Exception:
                                        pass
                                os.remove('crash_dump-' + datelog + '.txt')
                                quit()
                            elif vstup in ['', 'y']:
                                os.system('cls')
                                sys.stdout.flush()
                                if os.path.isfile("C:/Users/" + os.getlogin() + "/AppData/Local/ZnámE/saved"):
                                    if waifuvid:
                                        subprocess.check_output(
                                            'start restart.py --waifu --autol', shell=True)
                                        sys.stdout.flush()
                                        subprocess.check_output(
                                            'start edupage.py --restart --nointrof --waifu --waifuvid -lang ' + args.language + ' --music ' + args.music, shell=True)
                                    elif neko:
                                        subprocess.check_output(
                                            'start restart.py --neko --autol', shell=True)
                                        sys.stdout.flush()
                                        subprocess.check_output(
                                            'start edupage.py --restart --nointrof --neko -lang ' + args.language + ' --music ' + args.music, shell=True)
                                    elif waifu:
                                        subprocess.check_output(
                                            'start restart.py --waifu --autol', shell=True)
                                        sys.stdout.flush()
                                        subprocess.check_output(
                                            'start edupage.py --restart --nointrof --waifu -lang ' + args.language + ' --music ' + args.music, shell=True)
                                    else:
                                        subprocess.check_output(
                                            'start restart.py --autol', shell=True)
                                        sys.stdout.flush()
                                        subprocess.check_output(
                                            'start edupage.py --restart --nointrof -lang ' + args.language + ' --music ' + args.music, shell=True)
                                    os.remove('crash_dump-' + datelog + '.txt')
                        else:
                            os.system('cls')
                            sys.stdout.flush()
                            if neko or waifu:
                                if os.path.isfile("C:/Users/" + os.getlogin() + "/AppData/Local/ZnámE/saved"):
                                    subprocess.check_output(
                                        'start restart.py --neko --autol', shell=True)
                                    sys.stdout.flush()
                                else:
                                    subprocess.check_output(
                                        'start restart.py --neko', shell=True)
                                    sys.stdout.flush()
                            elif inactivelogout:
                                if os.path.isfile("C:/Users/" + os.getlogin() + "/AppData/Local/ZnámE/saved"):
                                    subprocess.check_output(
                                        'start restart.py --autol', shell=True)
                                    sys.stdout.flush()
                                else:
                                    subprocess.check_output(
                                        'start restart.py', shell=True)
                                    sys.stdout.flush()
                            else:
                                subprocess.check_output(
                                    'start restart.py', shell=True)
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
                            quit()
                    elif not restart:
                        os.remove('END')
                        if args.endf == None:
                            if args.language == "SK":
                                input(str(linenumber) + " 'ENTER' NA KONIEC")
                            elif args.language == "EN":
                                input(str(linenumber) + " 'ENTER' TO END")
                            elif args.language == "JP":
                                input(str(linenumber) + " 「ENTER」で終了")
                            if os.path.exists('restart.py'):
                                os.remove('restart.py')
                            os.remove('crash_dump-' + datelog + '.txt')
                            quit()
                        else:
                            if os.path.exists('restart.py'):
                                os.remove('restart.py')
                            os.remove('crash_dump-' + datelog + '.txt')
                            quit()
        except Exception as e:
            x = open('error_log.txt', 'a')
            printnlog('Writing an error to \'error_log.txt\'!!!')
            exception_type, exception_object, exception_traceback = sys.exc_info()
            line_number = exception_traceback.tb_lineno
            error_get(eval(type(e).__name__), line_number, '')
            printnlog('End')
            sleep(1)
            quit()
    typewriter(printnlog('Function: main\n', toprint=False))
    typewriter(printnlog('Done defining functions\n', toprint=False))

    if '__main__' == __name__:
        main()
    else:
        os.remove('crash_dump-' + datelog + '.txt')
except Exception as e:
    import os
    import sys
    from time import sleep
    x = open('error_log.txt', 'a')
    printnlog('Writing an error to \'error_log.txt\'!!!')  # type: ignore
    exception_type, exception_object, exception_traceback = sys.exc_info()
    line_number = exception_traceback.tb_lineno  # type: ignore
    error_get(eval(type(e).__name__), line_number, '')  # type: ignore
    printnlog('End')  # type: ignore
    sleep(1)
    quit()
