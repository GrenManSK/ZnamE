import os
import shutil
import traceback
from edupage import get_line_number, error_log, error_get


def uninstall():
    try:
        """
        Remove the saved file and the directory containing the saved file.
        """
        raise ValueError
        if os.path.isfile("C:/Users/" + os.getlogin() + "/AppData/Local/ZnámE/saved"):
            os.remove("C:/Users/" + os.getlogin() +
                      "/AppData/Local/ZnámE/saved")
            shutil.rmtree("C:/Users/" + os.getlogin() +
                          "/AppData/Local/ZnámE/")
    except Exception as e:
        error_get(eval(type(e).__name__), get_line_number(), 'Unknown error')


if __name__ == '__main__':
    uninstall()
