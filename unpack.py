import zipfile
import os
import subprocess
import sys
import shutil
from time import sleep
from tqdm import tqdm


def unpack(cachename):
    with zipfile.ZipFile(cachename, mode='r') as zip:
        for member in tqdm(iterable=zip.namelist(), total=len(zip.namelist()), desc='Rozbaľujem '):
            try:
                zip.extract(member)
                tqdm.write(
                    f"{os.path.basename(member)}(" + str(os.path.getsize(member)) + "B)")
                print(f"{os.path.basename(member)}(" +
                      str(os.path.getsize(member)) + "B)")
                sleep(0.01)
            except zipfile.error as e:
                pass
        zip.close()
    subprocess.call([sys.executable, 'xp3.py', 'data.xp3',
                    'data1', '-e', 'neko_vol0_steam', '-lang', 'EN'])
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
                print(os.path.join('./', file))
                shutil.move(os.path.join('data1/apphtml/', file),
                            os.path.join('apphtml/', file))
        for r, d, f in os.walk('data1/assets/'):
            for file in f:
                print(os.path.join('./', file))
                shutil.move(os.path.join('data1/assets/', file),
                            os.path.join('assets/', file))
        for r, d, f in os.walk('data1/'):
            for file in f:
                print(os.path.join('./', file))
                shutil.move(os.path.join('data1/', file),
                            os.path.join('/', file))
        shutil.rmtree('data1')
        sleep(1)
    os.remove(cachename)
    os.remove('data.xp3')


if __name__ == '__main__':
    datafiles = []
    for file in os.listdir("./"):
        if file.startswith("data"):
            if file.endswith('.xp2'):
                datafiles.append(file)
    for i in range(1, len(datafiles)+1):
        unpack(datafiles[-i])

    sleep(1)
