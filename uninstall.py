import os
import shutil

if __name__ == "__main__":
    from essentials.system.exceptions import error_get
    from essentials.system.system_info import get_line_number


def uninstall():
    """
    It deletes the file "saved" and the folder "ZnámE" in the user's AppData/Local folder.
    """
    if __name__ == "__main__":
        try:
            try:
                shutil.rmtree("C:/Users/" + os.getlogin() + "/AppData/Local/ZnámE/")
            except Exception:
                pass
            try:
                os.remove("game.py")
            except Exception:
                pass
            try:
                shutil.rmtree("game/")
            except Exception:
                pass
        except* Exception as e:
            error_get(
                eval(type(e).__name__),
                get_line_number(),
                "Unknown error",
                fname="uninstall.py",
            )
    else:
        if os.path.isfile("C:/Users/" + os.getlogin() + "/AppData/Local/ZnámE/saved"):
            os.remove("C:/Users/" + os.getlogin() + "/AppData/Local/ZnámE/saved")


if __name__ == "__main__":
    uninstall()
