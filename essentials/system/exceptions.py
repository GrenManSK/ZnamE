from ..functions.writing import printnlog
import sys
import os
import glob
from dotenv import load_dotenv
from importlib import import_module

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
    exc_type, exc_obj, exc_tb = sys.exc_info()
    if None in line:
        line = []
    try:
        for times, error in enumerate(errors.exceptions):
            import_module(error.__module__, error)
            try:
                names = set(
                    os.path.basename(i)
                    for i in glob.glob("essentials/**/**/**.py", recursive=True)
                )
                error_tb = error.__traceback__
                error_tb_to_use = []
                while True:
                    if error_tb.tb_next is None:
                        fname = os.path.basename(error_tb.tb_frame.f_code.co_filename)
                        line.append(error_tb.tb_lineno)
                        break
                    if (
                        not os.path.basename(
                            error_tb.tb_next.tb_frame.f_code.co_filename
                        )
                        in names
                    ):
                        fname = os.path.basename(error_tb.tb_frame.f_code.co_filename)
                        line.append(error_tb.tb_lineno)
                        break
                    else:
                        error_tb_to_use.append(
                            f"In {os.path.basename( error_tb.tb_frame.f_code.co_filename)}:{error_tb.tb_lineno}"
                        )
                        error_tb = error_tb.tb_next
                error_tb_to_use.reverse()
                error_tb_format = f"{error.args[0]} ("
                for i in error_tb_to_use:
                    error_tb_format += "" + i + " => "
                error_tb_format = error_tb_format[0:-4] + ")"
                try:
                    raise eval(error.with_traceback.__qualname__.split(".")[0])(
                        error_tb_format
                    )
                except eval(error.with_traceback.__qualname__.split(".")[0]):
                    if len(line) == 1 and times > 0:
                        error_log(line[0], fname)
                    else:
                        error_log(line[times], fname)
            except NameError:
                names = set(
                    os.path.basename(i)
                    for i in glob.glob("essentials/**/**/**.py", recursive=True)
                )
                error_tb = error.__traceback__
                while True:
                    try:
                        if error_tb.tb_next is None:
                            file_name = os.path.basename(
                                error_tb.tb_frame.f_code.co_filename
                            )
                            break
                    except AttributeError:
                        pass
                    if (
                        not os.path.basename(
                            error_tb.tb_next.tb_frame.f_code.co_filename
                        )
                        in names
                    ):
                        file_name = os.path.basename(
                            error_tb.tb_frame.f_code.co_filename
                        )
                        break
                    else:
                        error_tb = error_tb.tb_next
                try:
                    raise SystemError(
                        error.with_traceback.__qualname__.split(".")[0]
                        + ": "
                        + str(error)
                        + f" | In file: {file_name}"
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
