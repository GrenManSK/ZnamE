from .voicevox import run_voicevox
from .cbzprintable import run_cbz
from .kayopy import run_kayopy
from .manga_translator import run_manga_image_translator
from ..system.conda import env_menu
import os


functions = {
    "voicevox": {"function": run_voicevox, "args": [env_menu, [True]]},
    "cbz": {
        "function": run_cbz,
    },
    "kayopy": {
        "function": run_kayopy,
    },
    "manga_image_translator": {
        "function": run_manga_image_translator,
        "args": [env_menu, [True]],
    },
}


def run_app(func):
    os.system(f"title {func.title()}")
    try:
        try:
            if isinstance(functions[func]["args"], list):
                functions[func]["function"](
                    functions[func]["args"][0](*functions[func]["args"][1])
                )
            if not isinstance(functions[func]["args"], list):
                functions[func]["function"](functions[func]["args"])
        except KeyError:
            functions[func]["function"]()
        print("\n")
    except KeyboardInterrupt:
        print("\n")

    os.system("title ZnámE")
