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
    subprocess.check_output([sys.executable , "edupage_test.py" ,"-lang", "SK"])
    subprocess.check_output([sys.executable , "edupage_test.py" ,"-lang", "EN"])
    subprocess.check_output([sys.executable , "edupage_test.py" ,"-lang", "JP"])
    subprocess.check_output([sys.executable , "edupage_test.py" ,"--version", ])
    subprocess.check_output([sys.executable , "edupage_test.py" ,"--update", ])
    subprocess.check_output([sys.executable , "edupage_test.py" ,"--endf", ])
    subprocess.check_output([sys.executable , "edupage_test.py" ,"--inactive", ])
    os.remove('edupage_test.py')