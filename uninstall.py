import os
import shutil
if os.path.isfile("C:/Users/" + os.getlogin() + "/AppData/Local/ZnámE/saved"):
    os.remove("C:/Users/" + os.getlogin() + "/AppData/Local/ZnámE/saved")
    shutil.rmtree("C:/Users/" + os.getlogin() + "/AppData/Local/ZnámE/")
