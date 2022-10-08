import os, subprocess, sys
from time import sleep

def test_main():
    old = open('edupage.py', 'r', encoding='utf-8')
    new = open('edupage_test.py','w', encoding='utf-8')
    for i in old.readlines():
        if i == "if '__main__' == __name__:\n":
            break
        new.write(i)
    old.close()
    new.close()
    subprocess.check_output([sys.executable , "edupage_test.py" ,"-lang", "SK" ,"--test"])
    subprocess.check_output([sys.executable , "edupage_test.py" ,"-lang", "EN" ,"--test"])
    subprocess.check_output([sys.executable , "edupage_test.py" ,"-lang", "JP" ,"--test"])
    subprocess.check_output([sys.executable , "edupage_test.py" ,"--version" ,"--test"])
    subprocess.check_output([sys.executable , "edupage_test.py" ,"--update" ,"--test"])
    subprocess.check_output([sys.executable , "edupage_test.py" ,"--endf" ,"--test"])
    subprocess.check_output([sys.executable , "edupage_test.py" ,"--inactive" ,"--test"])
    os.remove('edupage_test.py')