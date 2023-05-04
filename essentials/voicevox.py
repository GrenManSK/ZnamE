import subprocess
import os
from time import sleep
from .writing import printnlog, typewriter
from .app_alternations import on_rm_error
import shutil


def get_size(start_path='.'):
    total_size = 0
    for dirpath, dirnames, filenames in os.walk(start_path):
        for f in filenames:
            fp = os.path.join(dirpath, f)
            # skip if it is symbolic link
            if not os.path.islink(fp):
                total_size += os.path.getsize(fp)

    return total_size


def run_voicevox(env):
    damaged = False
    if os.path.exists('VOICEVOX'):
        size = get_size('VOICEVOX')/1024/1024
        if size < 1000:
            damaged = True
    if os.path.exists('VOICEVOX') and not damaged:
        typewriter(printnlog(
            f'Running VOICEVOX\nRunning command: {env} -m VOICEVOX\n', toprint=False), ttime=0.01)
        sleep(1)
        subprocess.call([env, '-m', 'VOICEVOX'])
    else:
        if os.path.exists('VOICEVOX'):
            typewriter(printnlog(f'Found damaged VOICEVOX\nDeleting ...', toprint=False), ttime=0.01)
            print('Waiting 2 seconds to clear Access Denied Error')
            sleep(2)
            for i in os.listdir('VOICEVOX'):
                if i.endswith('git'):
                    tmp = os.path.join('VOICEVOX', i)
                    while True:
                        subprocess.call(['attrib', '-H', tmp])
                        break
                    shutil.rmtree(tmp, onerror=on_rm_error)
            print('Waiting 2 seconds to clear Access Denied Error')
            sleep(2)
            shutil.rmtree('VOICEVOXq', onerror=on_rm_error)
        else:
            printnlog('VOICEVOX not found')
        while True:
            vstup = input(printnlog(
                "To install VOICEVOX run this command \'git clone https://github.com/GrenManSK/VOICEVOX.git\'\n Do you want to complete this action automatically (Y/n) > ", toprint=False)).lower()
            if vstup in ['', 'y']:
                break
            elif vstup == 'n':
                return
            else:
                printnlog('Wrong character')
        typewriter(printnlog('Downloading VOICEVOX\n',
                   toprint=False), ttime=0.01)
        os.system('git clone https://github.com/GrenManSK/VOICEVOX.git')
        typewriter(printnlog(
            f'Downloading pip requirements\nRunning command: {env} -m pip install -r VOICEVOX/requirements.txt\n', toprint=False), ttime=0.01)
        sleep(1)
        os.system(env + ' -m pip install -r VOICEVOX/requirements.txt')
        subprocess.call([env, '-m', 'VOICEVOX'])
