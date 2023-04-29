import zipfile
from tqdm import tqdm
import os
from .writing import log, typewriter, printnlog
import subprocess
import sys
import shutil


def unpack(datelog, args, cachename: str) -> None:
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
        typewriter(
            printnlog("Rozbaľujem druhu časť...\n", toprint=False))
    elif args.language == "EN":
        typewriter(printnlog('Done\n', toprint=False))
        typewriter(
            printnlog("Unpacking second part...\n", toprint=False))
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


def extract(args, datelog):
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
            unpack(datelog, args, datafiles[-i])
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
