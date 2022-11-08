import os
import shutil


def uninstall():
    try:
        """
        Remove the saved file and the directory containing the saved file.
        """
        if os.path.isfile("C:/Users/" + os.getlogin() + "/AppData/Local/ZnámE/saved"):
            os.remove("C:/Users/" + os.getlogin() +
                      "/AppData/Local/ZnámE/saved")
            shutil.rmtree("C:/Users/" + os.getlogin() +
                          "/AppData/Local/ZnámE/")
    except Exception as e:
        import os
        import sys
        from time import sleep
        x = open('error_log.txt', 'a')
        exc_type, exc_obj, exc_tb = sys.exc_info()
        fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
        x.write('Type of error: ' + str(exc_type) + ' | In file: ' +
                str(fname) + ' | On line: ' + str(exc_tb.tb_lineno) + '\n')
        x.close()


if __name__ == '__main__':
    uninstall()
