import os
import shutil

def uninstall():
    """
    Remove the saved file and the directory containing the saved file.
    """
    if os.path.isfile("C:/Users/" + os.getlogin() + "/AppData/Local/ZnámE/saved"):
        os.remove("C:/Users/" + os.getlogin() + "/AppData/Local/ZnámE/saved")
        shutil.rmtree("C:/Users/" + os.getlogin() + "/AppData/Local/ZnámE/")
 
if __name__ == '__main__':
     uninstall()
