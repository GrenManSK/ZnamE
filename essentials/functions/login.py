import os
from edupage import decode


def auto_login(linenumber):
    savefilemode = False
    savefile = False
    if os.path.isfile("C:/Users/" + os.getlogin() + "/AppData/Local/ZnámE/saved"):
        loginvstupuser = ""
        savefile = decode(
            "1", "C:/Users/" + os.getlogin() + "/AppData/Local/ZnámE/saved", mode=1
        )
        loginvstupuser = input(str(linenumber) + " Do you want to auto-login? (Y/n) > ")
        linenumber += 1
        loginvstupuser.lower()
        if loginvstupuser in ["", "y"]:
            savefilemode: bool = True
    return savefilemode, savefile
