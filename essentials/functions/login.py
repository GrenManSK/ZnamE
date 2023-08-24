import os
from edupage import decode


def auto_login(linenumber):
    """
    The auto_login function checks if the user has a saved file in their AppData folder.
    If they do, it asks them if they want to auto-login with that account. If so, it returns True and the savefile.
    
    :param linenumber: Print the line number of the input
    :return: A tuple, so you need to unpack it into two variables
    """
    savefilemode = False
    savefile = False
    if os.path.isfile(f"C:/Users/{os.getlogin()}/AppData/Local/ZnámE/saved"):
        loginvstupuser = ""
        savefile = decode(
            "1", f"C:/Users/{os.getlogin()}/AppData/Local/ZnámE/saved", mode=1
        )
        loginvstupuser = input(
            f"{str(linenumber)} Do you want to auto-login? (Y/n) > "
        )
        linenumber += 1
        loginvstupuser.lower()
        if loginvstupuser in ["", "y"]:
            savefilemode: bool = True
    return savefilemode, savefile
