import os, subprocess, sys, time

def test_main():
    old = open('edupage.py', 'r', encoding='utf-8')
    new = open('edupage_test.py','w', encoding='utf-8')
    for i in old.readlines():
        if i == "if '__main__' == __name__:\n":
            break
        new.write(i)
    old.close()
    new.close()
    subprocess.check_output('start edupage_test.py --language SK', shell=True)
    subprocess.check_output('start edupage_test.py --language EN', shell=True)
    subprocess.check_output('start edupage_test.py --language JP', shell=True)
    subprocess.check_output('start edupage_test.py --version', shell=True)
    subprocess.check_output('start edupage_test.py --update', shell=True)
    subprocess.check_output('start edupage_test.py --endf', shell=True)
    subprocess.check_output('start edupage_test.py --inactive', shell=True)
    time.sleep(3)
    os.remove('edupage_test.py')