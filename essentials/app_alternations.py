from .functions.writing import printnlog, typewriter
from .system.system_info import get_line_number
from .internet import download
import requests
import semantic_version
from time import sleep
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
from .data.app import updateapp
import glob
import stat
import json
import pkg_resources
load_dotenv('.env')


def update_app(args, logger):
    datelog = os.getenv('DATELOG')
    try:
        url = 'https://raw.githubusercontent.com/GrenManSK/ZnamE/main/version'
        page = requests.get(url)
        with open('version', 'r') as verzia:
            version = verzia.read()[1:]
        if semantic_version.Version(page.text[1:]) <= semantic_version.Version(version):
            logger.next(
                printnlog('You have the latest version', toprint=False))
            logger.prev('')
        else:
            printnlog("Newer version was found: " + page.text)
            os.system(f"git clone https://github.com/GrenManSK/ZnamE.git")
            directory = None
            for path, currentDirectory, files in os.walk(Path.cwd()):
                for directory1 in currentDirectory:
                    if directory1.startswith("ZnamE"):
                        printnlog(directory1)
                        directory = directory1
                        break
            if directory is None:

                "If program fails to download update refer user to website"

                printnlog(
                    "DOWNLOADING ERROR\nManually download newer version from\n'https://github.com/GrenManSK/ZnamE'")
                input()
                sys.exit(1)
            os.mkdir('old')
            shutil.move('data.xp2', 'old/data.xp2')
            shutil.move('help.txt', 'old/help.txt')
            shutil.move('LICENSE', 'old/LICENSE')
            shutil.move('README.md', 'old/README.md')
            shutil.move('version', 'old/version')
            shutil.move('config.yml', 'config_old.yml')
            for file_name in glob.glob('./ZnamE/**/**/*', recursive=True):
                if os.path.isdir(file_name):
                    continue
                print(file_name)
                print(file_name.replace('ZnamE\\', ''))
                try:
                    shutil.move(file_name, file_name.replace('ZnamE\\', ''))
                except FileNotFoundError:
                    break
            crupdate = open("update.py", "w")
            crupdate.write(updateapp)
            crupdate.close()
            print('Waiting 2 seconds to clear Access Denied Error')
            sleep(2)
            for i in os.listdir('ZnamE'):
                if i.endswith('git'):
                    tmp = os.path.join('ZnamE', i)
                    while True:
                        subprocess.call(['attrib', '-H', tmp])
                        break
                    shutil.rmtree(tmp, onerror=on_rm_error)
            print('Waiting 2 seconds to clear Access Denied Error')
            sleep(2)
            os.remove('crash_dump-' + datelog + '.txt')
            shutil.rmtree('ZnamE', onerror=on_rm_error)
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
            if args.endf is None:
                subprocess.call(sys.executable + ' update.py ' + directory +
                                ' -endf', shell=True)
            else:
                subprocess.call(sys.executable + ' update.py ' +
                                directory, shell=True)
            sys.exit(0)
    except requests.ConnectionError:  # type: ignore
        line_number: int = get_line_number()
        pass


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
            package = pack[0].split(' ')[2]
            command = pack[0].split(' ')[1]
        with open('choco_output', 'w') as file:
            carousel = installing_carousel(package)
            Thread(target=carousel.start()).start()
            Thread(target=choco_check, args=(package, carousel)).start()
            subprocess.run(['choco', command, package,
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
    from .system.system_operations import checkAdmin
    checkAdmin()
    sys.exit(0)


def get_packages() -> list[str]:
    with open('choco_packages.json') as json_file:
        data = json.load(json_file)
        return_data = []
        for package in data.values():
            return_data.append(
                f"{package['command']} {package['package']} --version {package['version']} {package['additional-command']}")
    return return_data


def install_packages(args, logger):
    datelog = os.getenv('DATELOG')
    os.remove('INSTALL')

    "Downloading dependencies using chocolatey"

    choco_packages: list[str] = get_packages()

    "inst_number is number of installed packages; alinst_number is number of already installed"

    inst_number, alinst_number = choco_install(*choco_packages)
    if inst_number != 0:
        logger.stay("Restarting program ...")
        sleep(1)
        subprocess.check_output(
            'start edupage.py ', shell=True)
        os.remove(f"crash_dump-{datelog}.txt")
    os.remove('choco_output')
    try:
        os.remove('choco_end')
    except Exception:
        pass
    if inst_number != 0:
        sys.exit(0)


def on_rm_error(func, path, exc_info):
    os.chmod(path, stat.S_IWRITE)
    os.unlink(path)


def python_update(args, logger):
    datelog = os.getenv('DATELOG')
    printnlog('')
    potrebne: set[str] = {'idna', 'commonmark', 'click', 'charset-normalizer', 'certifi', 'brotli', 'psutil', 'tqdm', 'spotdl', 'pyunpack', 'semantic-version', 'patool', 'gputil', 'py-cpuinfo', 'tabulate', 'opencv-python', 'glob2', 'wmi', 'translate', 'show-in-file-manager', 'verbose', 'numpy', 'opencv-python', 'pillow', 'python-vlc', 'pywinauto',
                          'keyboard', 'cpufreq', 'pywin32', 'pypiwin32', 'pyautogui', 'moviepy', 'playsound', 'python-vlc', 'pygetwindow', 'pygame', 'pytube', 'bs4', 'uuid', 'pyreadline3', 'python-dotenv', 'lxml', 'mutagen', 'pyyaml', 'pycryptodomex', 'py-cpuinfo', 'pygments', 'requests', 'rich', 'setuptools', 'shellingham', 'typer', 'typing', 'yt-dlp'}
    printnlog('Libraries needed: ', end='')
    potrebne1: list[str] = list(potrebne)
    for i in range(0, len(potrebne1)):
        printnlog(potrebne1[i], end=' ')
    printnlog("\n\nChecking for updates\n")
    nainstalovane: set[str] = {
        pkg.key for pkg in pkg_resources.working_set}
    nenajdene: set[str] = potrebne - nainstalovane
    if args.version is None:

        "Printing out version and possible updates"

        with open('version', 'r') as verzia:
            logger.stay(printnlog(verzia.read(), toprint=False))
        if nenajdene:
            print('Update is available: ', *nenajdene)
        os.remove('crash_dump-' + datelog + '.txt')
        sys.exit(1)
    if __name__ == '__main__':
        if nenajdene:
            printnlog('\nUpdate is available: ' + str(nenajdene))
            vstup: str = input(
                f'Do you want to install following modules? {nenajdene} (Y/n)> ').lower()
            if vstup in ['', 'y']:
                printnlog("\nDownloading updates")
                subprocess.check_call(
                    ['python', '-m', 'pip', 'install', *nenajdene])
                if 'pytube' in nenajdene:
                    import site
                    site_packages = site.getsitepackages()[1]
                    input('Now you will be transferred to the script file in which you need to change code in line 411\nto \'transform_plan_raw = js\'\n!!! This is important without it downloading music won\'t work')
                    os.system(
                        f'notepad.exe {site_packages}/pytube/cipher.py')
                printnlog("The program is restarting!!!")
                sleep(1)
                os.system('cls')
                os.remove('crash_dump-' + datelog + '.txt')
                subprocess.call(
                    [sys.executable, os.path.realpath(__file__)] + sys.argv[1:])
                sys.exit(0)
            else:
                sys.exit(0)
        printnlog('DONE\n')
