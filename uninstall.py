import os
import shutil
if __name__ == '__main__':
    from edupage import get_line_number, error_log, error_get


def uninstall():
    """
    It deletes the file "saved" and the folder "ZnámE" in the user's AppData/Local folder.
    """
    if __name__ == '__main__':
        try:
            if os.path.isfile("C:/Users/" + os.getlogin() + "/AppData/Local/ZnámE/saved"):
                os.remove("C:/Users/" + os.getlogin() +
                          "/AppData/Local/ZnámE/saved")
                shutil.rmtree("C:/Users/" + os.getlogin() +
                              "/AppData/Local/ZnámE/")
        except Exception as e:
            error_get(eval(type(e).__name__),
                      get_line_number(), 'Unknown error')
    else:
        if os.path.isfile("C:/Users/" + os.getlogin() + "/AppData/Local/ZnámE/saved"):
            os.remove("C:/Users/" + os.getlogin() +
                      "/AppData/Local/ZnámE/saved")
            shutil.rmtree("C:/Users/" + os.getlogin() +
                          "/AppData/Local/ZnámE/")


if __name__ == '__main__':
    uninstall()
