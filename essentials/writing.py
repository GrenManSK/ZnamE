import os
import sys
from time import sleep
from dotenv import load_dotenv
load_dotenv('.env')


def printnlog(msg: str, end: str = '\n', toprint: bool = True) -> str:
    """
    It takes a message and an end character, and prints the message to the console and to a file

    :param msg: The message to be printed and logged
    :param end: The character that will be printed at the end of the message, defaults to \n
    (optional)
    """
    datelog = os.getenv('DATELOG')
    with open(f"crash_dump-{datelog}.txt", 'a', encoding='utf-8') as crashfile:
        if toprint:
            print(str(msg), end=str(end))
        crashfile.write(str(msg) + str(end))
    return msg


def to_info(msg: str, end: str = '\n', file: str = 'info.txt', mode: str = 'a', toprint: bool = True) -> str:
    """
    The to_info function takes a message and an end character, and prints the message to the console 
    and to a file. It is used for logging purposes.

    :param msg: Print the message to the console and log file
    :param end: Determine what character will be printed at the end of the message
    :param file: Specify the file to which the message will be printed
    :param mode: Determine whether the file is being read or written to
    :return: The message that was passed to it
    """
    datelog = os.getenv('DATELOG')
    with open(f"crash_dump-{datelog}.txt", 'a', encoding='utf-8') as crashfile:
        if toprint:
            print(str(msg), end=str(end))
        crashfile.write(str(msg) + str(end))
        crashfile.close()
        crashfile1 = open(
            f"C:/Users/{os.getlogin()}/AppData/Local/ZnámE/{file}", mode, encoding='utf-8')
        crashfile1.write(str(msg) + str(end))
    return msg


def log(msg: str, end: str = '\n') -> str:
    """
    It opens a file, writes a message to it, and closes the file

    :param msg: The message to be logged
    :param end: The character that will be used to end the line, defaults to \n (optional)
    """
    datelog = os.getenv('DATELOG')
    with open(f"crash_dump-{datelog}.txt", 'a', encoding='utf-8') as crashfile:
        crashfile.write(str(msg) + str(end))
    return msg


def typewriter(word: str, ttime: float = 0.001, end: str = '\n') -> None:
    """
    The typewriter function prints each character in a word with a delay.
    The default time between characters is 0.01 seconds, but the user can specify
    their own value for the time.

    :param word: Pass the word that needs to be printed
    :param time=0.01: Set the time between each character printed out
    :param end='\n': Print the output on a new line
    :return: A string
    """
    for char in word:
        sleep(ttime)
        sys.stdout.write(char)
        sys.stdout.flush()
    sys.stdout.write(end)


def show_version(args):
    verzia = open('version', 'r')
    typewriter('You\'re using ZnámE ' + verzia.read() + "\n")
    verzia.close()
