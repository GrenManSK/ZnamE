import subprocess
import os
from .writing import printnlog


def run_voicevox(env):
    if os.path.exists('VOICEVOX'):
        subprocess.call([env, '-m', 'VOICEVOX'])
    else:
        printnlog('VOICEVOX not found')
        while True:
            vstup = input(printnlog("To install VOICEVOX run this command \'git clone https://github.com/GrenManSK/VOICEVOX.git\'\n Do you want to complete this action automatically (Y/n) > ", toprint=False)).lower()
            if vstup in ['', 'y']:
                break
            elif vstup == 'n':
                return
            else:
                printnlog('Wrong character')
        os.system('git clone https://github.com/GrenManSK/VOICEVOX.git')
        os.system(env + ' -m pip install -r VOICEVOX/requirements.txt')
        subprocess.call([env, '-m', 'VOICEVOX'])
