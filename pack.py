import os
import shutil
import subprocess
import sys
import zipfile
from tqdm import tqdm
from time import sleep
datapart = 0
breaked = True


def pack():
    global datapart
    global breaked
    datapart += 1
    try:
        os.mkdir('datafolder')
    except FileExistsError:
        pass
    if datapart == 1:
        cachename = 'data.xp2'
    else:
        cachename = 'data_part' + str(datapart) + '.xp2'
    sleep(0.2)
    try:
        shutil.move('data', 'datafolder/')
    except Exception:
        pass
    total_size = 0
    breaked = False
    try:
        source_dir = 'apphtml/'
        os.mkdir('datafolder/' + source_dir)
        for file_name in os.listdir(source_dir):
            file_stats = os.stat(source_dir + file_name)
            filesize = file_stats.st_size / (1024 * 1024)
            total_size += filesize
            print(f'File Size in MegaBytes is {filesize}')
            if total_size > 95:
                breaked = True
                break
            shutil.move(os.path.join(source_dir, file_name),
                        'datafolder/' + source_dir)
    except Exception:
        pass
    source_dir = 'assets/'
    os.mkdir('datafolder/' + source_dir)
    for file_name in os.listdir(source_dir):
        file_stats = os.stat(source_dir + file_name)
        filesize = file_stats.st_size / (1024 * 1024)
        total_size += filesize
        print(f'File Size in MegaBytes is {filesize}')
        if total_size > 95:
            breaked = True
            break
        shutil.move(os.path.join(source_dir, file_name),
                    'datafolder/' + source_dir)
    sleep(0.2)
    print("PACKING DATA\n")
    sleep(0.2)
    subprocess.call([sys.executable, 'xp3.py', 'datafolder', 'data.xp3',
                    '-mode', 'repack', '-e', 'neko_vol0_steam', '-lang', 'EN'])
    shutil.rmtree('datafolder')
    if total_size > 95:
        zipfiles = ['data.xp3']
        zipfileswopath = ['data.xp3']
    else:
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
        print("\nPacked data have > " +
              str(filesize) + " KB")
        zip.close()
    return breaked


if __name__ == "__main__":
    while True:
        breaked = pack()
        if not breaked:
            break
    try:
        shutil.rmtree('assets')
        shutil.rmtree('apphtml')
        shutil.rmtree('structs')
    except:
        pass

    sleep(1)
