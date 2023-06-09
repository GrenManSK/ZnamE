from ..functions.writing import printnlog
import sys
import os
import glob
from dotenv import load_dotenv
from importlib import import_module
from inspect import signature

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


def error_log(line: int, fname, module, error) -> None:
    """
    The error_log function is used to log errors that occur in the program.
    It takes four arguments: line, fname, module and error.
    Line is the line number where the error occurred (this can be found using sys.exc_info()).
    Fname is a string containing the name of file where an error occurred (this can also be found using sys.exc_info()).
    Module and Error are strings containing information about what type of exception was raised.
    
    :param line: int: Specify the line number where the error occurred
    :param fname: Get the name of the file that is being executed
    :param module: Specify the module that the error occurred in
    :param error: Specify the type of error
    :return: None
    """
    with open("error.log", "a", encoding="utf-8") as errorfile:
        exc_type, exc_obj, exc_tb = sys.exc_info()
        if module is not None:
            errorfile.write(
                f"Type of error: {module}.{error} | Comment: {str(exc_obj)} | In file: {str(fname)} | On line: {str(line)}\n"
            )
            printnlog(
                f"Type of error: {module}.{error} | Comment: {str(exc_obj)} | In file: {str(fname)} | On line: {str(line)}"
            )
        else:
            errorfile.write(
                f"Type of error: {error} | Comment: {str(exc_obj)} | In file: {str(fname)} | On line: {str(line)}\n"
            )
            printnlog(
                f"Type of error: {error} | Comment: {str(exc_obj)} | In file: {str(fname)} | On line: {str(line)}"
            )


def error_get(errors, line: list, fname: None | str = None) -> None:
    """
    The error_get function is used to get the error that was raised and then
        raise it again with a traceback. This function also logs the error in a file
        called 'error_logs.txt'
    
    :param errors: Get the errors from the error_get function
    :param line: list: Get the line number of the error
    :param fname: None | str: Specify the file name of the error
    :return: The error and the line number of where it occured
    """
    debug = os.getenv("DEBUG")
    if debug is None:
        debug = False
    else:
        debug = eval(debug)
    exc_type, exc_obj, exc_tb = sys.exc_info()
    if None in line:
        line = []
    for times, error in enumerate(errors.exceptions):
        module = True
        try:
            module_obj = import_module(
                error.__module__, error.with_traceback.__qualname__.split(".")[0]
            )
            globals()[error.__module__] = module_obj
        except Exception:
            module = False
        names = set(
            os.path.basename(i)
            for i in glob.glob("essentials/**/**/**.py", recursive=True)
        )
        [names.add(i) for i in glob.glob("*.py")]
        error_tb = error.__traceback__
        error_tb_to_use = []
        while True:
            if error_tb.tb_next is None:
                fname = os.path.basename(error_tb.tb_frame.f_code.co_filename)
                line.append(error_tb.tb_lineno)
                args = "("
                _module = error_tb.tb_frame.f_globals["__name__"]
                try:
                    module_obj = import_module(_module)
                    globals()[_module] = module_obj
                    _module = getattr(globals()[_module], error_tb.tb_frame.f_code.co_name)
                    sig = str(signature(_module))
                    if debug:
                        sig = sig.split(' -> ')[0][1:-1].split(", ")
                        sig = [i.split(":")[0].split("**")[-1].split("*")[-1] for i in sig]
                except Exception:
                    sig = ""
                for i in error_tb.tb_frame.f_locals:
                    if debug:
                        if i in sig:
                            value = error_tb.tb_frame.f_locals[i]
                            if isinstance(value, str):
                                value = "'" + str(value) + "'"
                            elif isinstance(value, int):
                                value = str(value)
                            elif isinstance(value, dict):
                                value = str(value)
                            elif isinstance(value, list):
                                value = str(value)
                            elif isinstance(value, object):
                                value = str(value)[1:].split(" ")[0]
                            elif callable(value):
                                value = str(i) + "()"
                            args += str(i) + "=" + str(value) + ", "
                if not debug:
                    args = sig.split(")")[0] + ")"
                if len(args) > 1 and debug:
                    args = args[0:-2] + ")"
                elif debug:
                    args = ""
                error_tb_to_use.append(
                    f"In {os.path.basename(error_tb.tb_frame.f_code.co_filename)}:{error_tb.tb_frame.f_code.co_name}{args}:{error_tb.tb_lineno}"
                )
                break
            if (
                not os.path.basename(error_tb.tb_next.tb_frame.f_code.co_filename)
                in names
            ):
                fname = os.path.basename(error_tb.tb_frame.f_code.co_filename)
                line.append(error_tb.tb_lineno)
                break
            else:
                if error_tb.tb_frame.f_code.co_name == "<module>":
                    error_tb_to_use.append(
                        f"In {os.path.basename( error_tb.tb_frame.f_code.co_filename)}:{error_tb.tb_lineno}"
                    )
                else:
                    args = "("
                    _module = error_tb.tb_frame.f_globals["__name__"]
                    try:
                        module_obj = import_module(_module)
                        globals()[_module] = module_obj
                        _module = getattr(globals()[_module], error_tb.tb_frame.f_code.co_name)
                        sig = str(signature(_module))
                        if debug:
                            sig = sig.split(' -> ')[0][1:-1].split(", ")
                            sig = [i.split(":")[0].split("**")[-1].split("*")[-1] for i in sig]
                    except Exception:
                        sig = ""
                    for i in error_tb.tb_frame.f_locals:
                        if debug:
                            if i in sig:
                                value = error_tb.tb_frame.f_locals[i]
                                if isinstance(value, str):
                                    value = "'" + str(value) + "'"
                                elif isinstance(value, int):
                                    value = str(value)
                                elif isinstance(value, object):
                                    value = str(value)[1:].split(" ")[0]
                                elif callable(value):
                                    value = str(i) + "()"
                                args += str(i) + "=" + str(value) + ", "
                    if not debug:
                        args = sig.split(")")[0] + ")"
                    if len(args) > 1 and debug:
                        args = args[0:-2] + ")"
                    elif debug:
                        args = ""
                    error_tb_to_use.append(
                        f"In {os.path.basename(error_tb.tb_frame.f_code.co_filename)}:{error_tb.tb_frame.f_code.co_name}{args}:{error_tb.tb_lineno}"
                    )
                error_tb = error_tb.tb_next
        if len(error_tb_to_use) != 0:
            if len(error.args) > 0:
                error_message = error.args[0]
            else:
                error_message = ''
            error_tb_format = f"{error_message} ("
            for i in error_tb_to_use:
                error_tb_format += "" + i + " => "
            error_tb_format = error_tb_format[0:-4] + ")"
        else:
            error_tb_format = error.args[0]
        try:
            try:
                raise eval(error.with_traceback.__qualname__.split(".")[0])(
                    error_tb_format
                )
            except eval(error.with_traceback.__qualname__.split(".")[0]):
                if module:
                    error_log(
                        line[times],
                        fname,
                        error.__module__,
                        error.with_traceback.__qualname__.split(".")[0],
                    )
                else:
                    error_log(
                        line[times],
                        fname,
                        None,
                        error.with_traceback.__qualname__.split(".")[0],
                    )
        except NameError:
            try:
                raise eval(
                    error.__module__
                    + "."
                    + error.with_traceback.__qualname__.split(".")[0]
                )(error_tb_format)
            except eval(
                error.__module__ + "." + error.with_traceback.__qualname__.split(".")[0]
            ):
                error_log(
                    line[times],
                    fname,
                    error.__module__,
                    error.with_traceback.__qualname__.split(".")[0],
                )
