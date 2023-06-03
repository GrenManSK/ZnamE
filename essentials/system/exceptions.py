from ..functions.writing import printnlog
import sys
import os
from dotenv import load_dotenv

load_dotenv(".env")


class configNoOption(Exception):
    pass


class argIntroError(Exception):
    pass


class argInactiveLimitError(Exception):
    pass


class argMusicListError(Exception):
    pass


class argMusicError(Exception):
    pass


class argenvironmentError(Exception):
    pass


class argWaifuError(Exception):
    pass


class argNekoError(Exception):
    pass


class argGameError(Exception):
    pass


class argTranslateError(Exception):
    pass


class argTranslatorError(Exception):
    pass


class argQuietError(Exception):
    pass


def error_log(line: int, fname) -> None:
    """
    It writes the error to a file and prints it to the console

    :param line: The line number of the error
    """
    if fname[0] == "?":
        try:
            exc_type, exc_obj, exc_tb = sys.exc_info()
            fname: str = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
        except AttributeError:
            pass
    with open("error.log", "a", encoding="utf-8") as errorfile:
        exc_type, exc_obj, exc_tb = sys.exc_info()
        exc_type = exc_type.__qualname__
        errorfile.write(
            f"Type of error: {str(exc_type)} | Comment: {str(exc_obj)} | In file: {str(fname)} | On line: {str(line)}\n"
        )
    printnlog(
        f"Type of error: {str(exc_type)} | Comment: {str(exc_obj)} | In file: {str(fname)} | On line: {str(line)}"
    )


def error_get(errors, line: list, fname: None | str = None) -> None:
    """
    The error_get function is used to raise the errors that are found in the error_log function.
        The error_get function takes two arguments:
            1) errors - a list of exceptions that were raised by the code being tested.
            2) line - a list of strings containing information about each exception raised.

    :param errors: Store the errors that are raised by the function
    :param line: list: Store the line numbers of the errors
    :return: The error code and the line number of the error
    """

    try:
        if fname is None:
            exc_type, exc_obj, exc_tb = sys.exc_info()
            fname: str = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
    except AttributeError:
        pass
    try:
        for times, error in enumerate(errors.exceptions):
            try:
                try:
                    if fname is None:
                        fname = os.path.basename(
                            error.__traceback__.tb_frame.f_locals["__file__"]
                        )
                except AttributeError:
                    fname = "?edupage.py"
                try:
                    raise eval(error.with_traceback.__qualname__.split(".")[0])(error)
                except eval(error.with_traceback.__qualname__.split(".")[0]):
                    if len(line) == 1 and times > 0:
                        error_log(line[0], fname)
                    else:
                        error_log(line[times], fname)
            except NameError:
                try:
                    raise SystemError(
                        error.with_traceback.__qualname__.split(".")[0]
                        + ": "
                        + str(error)
                    )
                except SystemError:
                    if len(line) == 1 and times > 0:
                        error_log(line[0], fname)
                    else:
                        error_log(line[times], fname)
    except Exception:
        times = 0
        try:
            error_name = errors.with_traceback.__qualname__.split(".")[0]
            raise eval(error_name)(errors)
        except eval(error_name):
            if len(line) == 1 and times > 0:
                error_log(line[0], fname)
            else:
                error_log(line[times], fname)
