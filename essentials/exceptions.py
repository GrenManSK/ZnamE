from .writing import printnlog
import sys
import os
from dotenv import load_dotenv
load_dotenv('.env')


class configNoOption(Exception):
    pass


class argLanguageError(Exception):
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


def error_log(line: int) -> None:
    """
    It writes the error to a file and prints it to the console

    :param line: The line number of the error
    """
    with open('error.log', 'a', encoding='utf-8') as errorfile:
        exc_type, exc_obj, exc_tb = sys.exc_info()
        exc_type = exc_type.__qualname__
        fname: str = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
        errorfile.write(
            f'Type of error: {str(exc_type)} | Comment: {str(exc_obj)} | In file: {str(fname)} | On line: {str(line)}\n')
    printnlog(
        f'Type of error: {str(exc_type)} | Comment: {str(exc_obj)} | In file: {str(fname)} | On line: {str(line)}')


def error_get(errors, line: list) -> None:
    """
    The error_get function is used to raise the errors that are found in the error_log function.
        The error_get function takes two arguments:
            1) errors - a list of exceptions that were raised by the code being tested.
            2) line - a list of strings containing information about each exception raised.

    :param errors: Store the errors that are raised by the function
    :param line: list: Store the line numbers of the errors
    :return: The error code and the line number of the error
    """

    for times, error in enumerate(errors.exceptions):
        try:
            try:
                raise eval(
                    error.with_traceback.__qualname__.split('.')[0])(error)
            except eval(error.with_traceback.__qualname__.split('.')[0]):
                if len(line) == 1 and times > 0:
                    error_log(line[0])
                else:
                    error_log(line[times])
        except NameError:
            try:
                raise SystemError(error.with_traceback.__qualname__.split('.')[
                                  0] + ': ' + str(error))
            except SystemError:
                if len(line) == 1 and times > 0:
                    error_log(line[0])
                else:
                    error_log(line[times])