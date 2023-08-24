import os
import sys
from time import sleep
from dotenv import load_dotenv

load_dotenv(".env")

try:
    quiet = eval(os.getenv("QUIET"))
except TypeError:
    quiet = False


def printnlog(msg: str, end: str = "\n", toprint: bool = True) -> str:
    """
    The printnlog function is a wrapper for the print function that also writes to a log file.

    :param msg: str: Specify the message that will be printed and logged
    :param end: str: Specify the end of the line
    :param toprint: bool: Determine whether or not to print the message
    :return: The message that was printed
    """
    datelog = os.getenv("DATELOG")
    with open(f"crash_dump-{datelog}.txt", "a", encoding="utf-8") as crashfile:
        if toprint and not quiet:
            print(msg, end=end)
        crashfile.write(msg + end)
    return msg


def to_info(
    msg: str,
    end: str = "\n",
    file: str = "info.txt",
    mode: str = "a",
    toprint: bool = True,
) -> str:
    """
    The to_info function takes a message and an end character, and prints the message to the console
    and to a file. It is used for logging purposes.

    :param msg: Print the message to the console and log file
    :param end: Determine what character will be printed at the end of the message
    :param file: Specify the file to which the message will be printed
    :param mode: Determine whether the file is being read or written to
    :return: The message that was passed to it
    """
    datelog = os.getenv("DATELOG")
    with open(f"crash_dump-{datelog}.txt", "a", encoding="utf-8") as crashfile:
        if toprint and not quiet:
            print(msg, end=end)
        crashfile.write(msg + end)
        crashfile.close()
        crashfile1 = open(
            f"C:/Users/{os.getlogin()}/AppData/Local/ZnámE/{file}",
            mode,
            encoding="utf-8",
        )
        crashfile1.write(msg + end)
    return msg


def log(msg: str, end: str = "\n") -> str:
    """
    It opens a file, writes a message to it, and closes the file

    :param msg: The message to be logged
    :param end: The character that will be used to end the line, defaults to \n (optional)
    """
    datelog = os.getenv("DATELOG")
    with open(f"crash_dump-{datelog}.txt", "a", encoding="utf-8") as crashfile:
        crashfile.write(msg + end)
    return msg


def typewriter(word: str, ttime: float = 0.001, end: str = "\n") -> None:
    """
    The typewriter function prints each character in a word with a delay.
    The default time between characters is 0.01 seconds, but the user can specify
    their own value for the time.

    :param word: Pass the word that needs to be printed
    :param time=0.001: Set the time between each character printed out
    :param end='\n': Print the output on a new line
    :return: A string
    """
    if not quiet:
        for char in word:
            sleep(ttime)
            sys.stdout.write(char)
            sys.stdout.flush()
        sys.stdout.write(end)


def show_version(args):
    """
    The show_version function prints the version of Známé to the user.
    
    :param args: Pass arguments to the function
    :return: The version of the program
    """
    with open("version", "r") as verzia:
        typewriter(f"You're using ZnámE {verzia.read()}" + "\n")


def change_quiet(to):
    """
    The change_quiet function changes the quiet variable to True or False.
    
    :param to: Set the global variable quiet to true or false
    :return: Nothing
    """
    from .textractor import change_quiet_textractor
    from ..system.file_operations import change_quiet_file_op

    global quiet
    if to in [True, False]:
        quiet = to
        change_quiet_file_op(to)
        change_quiet_textractor(to)
