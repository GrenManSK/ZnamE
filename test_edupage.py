import os, subprocess, sys

def test_main():
    old = open('edupage.py', 'r', encoding='utf-8')
    new = open('edupage_test.py','w', encoding='utf-8')
    for i in old.readlines():
        if i == "if '__main__' == __name__:\n":
            break
        new.write(i)
    old.close()
    new.close()
    subprocess.check_call([sys.executable, 'test_edupage.py','-lang','SK'], shell=True)
    subprocess.check_call([sys.executable, 'test_edupage.py','-lang', 'EN'], shell=True)
    subprocess.check_call([sys.executable, 'test_edupage.py','-lang', 'JP'], shell=True)
    subprocess.check_call([sys.executable, 'test_edupage.py','--version'], shell=True)
    subprocess.check_call([sys.executable, 'test_edupage.py','--update'], shell=True)
    subprocess.check_call([sys.executable, 'test_edupage.py','--endf'], shell=True)
    subprocess.check_call([sys.executable, 'test_edupage.py','--inactive'], shell=True)
    os.remove('edupage_test.py')