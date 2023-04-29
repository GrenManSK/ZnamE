from .writing import printnlog
from .system_info import get_line_number
from .internet import download
from .writing import typewriter
import requests
import semantic_version
from time import sleep
import zipfile
from tqdm import tqdm
import os
import sys
import shutil
import subprocess
import pyautogui as pg
from dotenv import load_dotenv
from pathlib import Path
from threading import Thread
from final.mathematical import get_id
load_dotenv('.env')

updateapp: str = str(
    'import argparse, shutil, os, subprocess, yaml, sys\nfrom time import sleep\nUNSPECIFIED = object()\nglobal parser\nparser = argparse.ArgumentParser()\nparser.add_argument(\'-ef\', \'--endf\', help=\'Will not automatically end program\', default=UNSPECIFIED, nargs=\'?\')\nparser.add_argument(\'-lang\', \'--language\', choices=[\'SK\',\'EN\',\'JP\'], help=\'Language selection\', nargs=\'?\')\nparser.add_argument(\'input\', help=\'Input folder\', nargs=\'?\')\nargs = parser.parse_args()\nconfig = yaml.safe_dump(open(\'config.yml\', \'r\'))\nargs.language = config[\'basic info\'][\'lang\']\nif args.input != \"\":\n    sleep(0.5)\n    shutil.move(\'edupage.py\', \'old/edupage.py\')\n    shutil.move(args.input + \'/edupage.py\', \'edupage.py\')\n    sleep(0.2)\n    shutil.rmtree(args.input)\n    shutil.rmtree(\'old\')\n    if args.endf == None:\n        subprocess.call(sys.executable + \' edupage.py -lang \' + args.language + \' -endf -update\', shell=True)\n    else:\n        subprocess.call(sys.executable + \' edupage.py -lang \' + args.language + \' -update\', shell=True)\n    sys.exit(0)')


def update_app(args, logger):
    datelog = os.getenv('DATELOG')
    try:
        url = 'https://raw.githubusercontent.com/GrenManSK/ZnamE/main/version'
        page = requests.get(url)
        verzia = open('version', 'r')
        if semantic_version.Version(page.text[1:]) <= semantic_version.Version(verzia.read()[1:]):
            logger.next(
                printnlog('You have the latest version', toprint=False))
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

                "If program fails to download update refer user to website"

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
                sys.exit(1)
            os.mkdir('old')
            shutil.move('data.xp2', 'old/data.xp2')
            shutil.move('help.txt', 'old/help.txt')
            shutil.move('LICENSE', 'old/LICENSE')
            shutil.move('README.md', 'old/README.md')
            shutil.move('version', 'old/version')
            shutil.copyfile('config.yml', 'config_old.yml')
            sleep(0.5)
            shutil.move(directory + "/data.xp2", 'data.xp2')
            shutil.move(directory + "/help.txt", 'help.txt')
            shutil.move(directory + "/LICENSE", 'LICENSE')
            shutil.move(directory + "/README.md", 'README.md')
            shutil.move(directory + "/version", 'version')
            shutil.move(directory + "/config.yml", 'config.yml')
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
            sys.exit(0)
    except requests.ConnectionError:  # type: ignore
        line_number: int = get_line_number()
        pass
    verzia.close()


class installing_carousel:
    def __init__(self, package: str, comment: str = 'Installing', bar: bool = False, move_by_command: bool = False):
        self.package = package
        self.comment = comment
        self.bar = bar
        self.move_by_command = move_by_command
        self._move = 0
        self.id = get_id()

    def start(self):
        """
        The start function is the main function of the class. It starts a thread that runs init()

        :param self: Represent the instance of the class
        :return: Nothing, so the return statement is never reached
        """

        Thread(target=self.init).start()

    def pause(self):
        """
        The pause function is used to pause the installation of a package.

        :param self: Represent the instance of the class
        :return: Nothing, it just creates a file
        """
        open(f"INSTALL_PAUSE{self.id}", 'x')

    def unpause(self):
        open(f"INSTALL_UNPAUSE{self.id}", 'x')

    def stop(self, mode='s'):
        """
        The stop function is called when the user wants to stop the installation.

        :param self: Represent the instance of the class
        :param mode: Determine what file is created
        :return: The name of the file that is created
        """
        if mode == 's':
            open(f"INSTALL_DONE{self.id}", 'x')
        if mode == 'e':
            open(f"INSTALL_ERROR{self.id}", 'x')
        if mode == 'ali':
            open(f"INSTALL_ALINST{self.id}", 'x')

    def move(self):
        self._move += 1

    def init(self):
        """
        The init function is used to initialize the package installation.
        It will print a loading bar until it finds an INSTALL_DONE, INSTALL_ERROR or 
        INSTALL_ALINST file in the current directory. If it finds an INSTALL_DONE file, 
        it will print DONE after the package name and if it finds an INSTALL_ERROR file, 
        it will print ERROR after the package name. If it finds an INSTALL_ALINST file, 
        it will print ALREADY INSTALLED after the package name.

        :param self: Represent the instance of the class
        :return: Nothing, so the return statement is not needed
        """
        error = False
        alinst = False
        number = 0
        char = ['|', '/', '-', '\\']
        while True:
            if os.path.isfile(f'INSTALL_DONE{self.id}'):
                break
            if os.path.isfile(f'INSTALL_ERROR{self.id}'):
                error = True
                break
            if os.path.isfile(f'INSTALL_ALINST{self.id}'):
                alinst = True
                break
            if os.path.isfile(f'INSTALL_PAUSE{self.id}'):
                if not self.bar:
                    print(
                        '                                            ', end='\r')
                if self.bar:
                    tqdm.write(
                        '                                            ')
                os.remove(f'INSTALL_PAUSE{self.id}')
                while not os.path.isfile(f'INSTALL_UNPAUSE{self.id}'):
                    sleep(0.1)
                os.remove(f'INSTALL_UNPAUSE{self.id}')
            if not self.bar:
                print(
                    f'{self.comment} {self.package} {char[number]}               ', end='\r')
            if self.bar:
                tqdm.write(
                    f'{self.comment} {self.package} {char[number]}               ')
            if not self.move_by_command or self._move != 0 and self.move_by_command:
                number += 1
                if self.move_by_command:
                    self._move -= 1
            if number >= len(char):
                number = 0
            sleep(0.1)
        if error:
            if not self.bar:
                print(f'{self.comment} {self.package} ERROR             ')
            if self.bar:
                tqdm.write(f'{self.comment} {self.package} ERROR             ')
        elif alinst:
            if not self.bar:
                print(
                    f'{self.comment} {self.package} ALREADY INSTALLED             ')
            if self.bar:
                tqdm.write(
                    f'{self.comment} {self.package} ALREADY INSTALLED             ')
        else:
            if not self.bar:
                print(f'{self.comment} {self.package} DONE             ')
            if self.bar:
                tqdm.write(f'{self.comment} {self.package} DONE             ')
        try:
            os.remove(f'INSTALL_DONE{self.id}')
        except Exception:
            pass
        try:
            os.remove(f'INSTALL_ERROR{self.id}')
        except Exception:
            pass
        try:
            os.remove(f'INSTALL_ALINST{self.id}')
        except Exception:
            pass


def choco_install(*packages: str):
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
            carousel = installing_carousel(package)
            Thread(target=carousel.start()).start()
            Thread(target=choco_check, args=(package, carousel)).start()
            subprocess.run(['choco', 'install', package,
                            version, '-y'], stdout=file, text=True)
        with open('choco_output', 'r') as file:
            alinst = False
            for line, content in enumerate(file.readlines()):
                if 'already installed.' in content and package in content:
                    carousel.stop('ali')
                    alinst = True
                    alinst_number += 1
                    break
        try:
            open('choco_end', 'x')
        except Exception:
            pass
        if not alinst:
            carousel.stop()
            inst_number += 1
        sleep(2)
    return (inst_number, alinst_number)


def choco_check(module: str, carousel: installing_carousel) -> None:
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
            carousel.pause()
            sleep(0.25)
            carousel.unpause()
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


def install_choco(logger):

    datelog = os.getenv('DATELOG')
    with open('choco.ps1', 'w') as file:
        file.write('$InstallDir=\'C:\ProgramData\chocoportable\'\n$env:ChocolateyInstall="$InstallDir"\nSet-ExecutionPolicy Bypass -Scope Process -Force;\niex ((New-Object System.Net.WebClient).DownloadString(\'https://community.chocolatey.org/install.ps1\'))')
    logger.next(
        "Checking if chocolatey is installed if not downloading\n")
    carousel = installing_carousel('chocolatey')
    Thread(target=carousel.start()).start()
    Thread(target=choco_check, args=('chocolatey', carousel)).start()
    with open('choco_output', 'w') as file:
        choco = subprocess.run(
            ['powershell.exe', '-file', 'choco.ps1', '--quiet', '--no-verbose'], stdout=file, text=True)
    with open('choco_output', 'r') as file:
        for line in file.readlines():

            "If system don\'t allow running powershell scripts navigate user to allow it"

            if 'cannot be loaded because running scripts is disabled on this system' in line:
                carousel.stop('e')
                logger.stay(
                    'Run Powershell as administrator and type \'Set-ExecutionPolicy RemoteSigned\' type Y and press \'enter\'')
                with open('set_permissions.txt', 'w') as file:
                    file.write(
                        'Run Powershell as administrator and type following code press \'enter\' type Y and press \'enter\'\n\nSet-ExecutionPolicy RemoteSigned')
                os.system("notepad.exe set_permissions.txt")
                input('Enter to continue ...')
                os.remove('set_permissions.txt')
                with open('choco_output', 'w') as file:
                    choco = subprocess.run(
                        ['powershell.exe', '-file', 'choco.ps1', '--quiet', '--no-verbose'], stdout=file, text=True)
    open('choco_end', 'x')
    carousel.stop()
    logger.prev('')
    sleep(1)
    os.remove(f"crash_dump-{datelog}.txt")
    open('INSTALL', 'x')
    open('INSTALL_RESTART', 'x')
    os.remove('choco.ps1')
    os.remove('choco_output')
    sleep(1)
    from .system_operations import checkAdmin
    checkAdmin()
    sys.exit(0)


def install_packages(args, logger):
    datelog = os.getenv('DATELOG')
    os.remove('INSTALL')

    "Downloading dependencies using chocolatey"

    choco_packages: list[str] = [
        'ffmpeg --version 5.1.2', 'vlc --version 3.0.18', 'vcredist2015 --version 14.0.24215.20170201', 'grep --version 3.7']

    "inst_number is number of installed packages; alinst_number is number of already installed"

    inst_number, alinst_number = choco_install(*choco_packages)
    if inst_number == 0:
        pass
    else:
        logger.stay("Restarting program ...")
        sleep(1)
        subprocess.check_output(
            'start edupage.py --language ' + args.language, shell=True)
        os.remove(f"crash_dump-{datelog}.txt")
    os.remove('choco_output')
    try:
        os.remove('choco_end')
    except Exception:
        pass
    if inst_number != 0:
        sys.exit(0)
