import subprocess
import os
import sys
from ..functions.writing import printnlog, typewriter


def get_envs(info: bool = False) -> dict:
    """
    The get_envs function returns a dictionary of conda environments.
    The keys are the names of the environments, and the values are their paths.
    
    :param info: bool: Print the command that is being run
    :return: A dictionary of all the conda environments on your system
    """
    with open("condaEnvList", "w") as file:
        try:
            if info:
                typewriter(
                    printnlog("Running command: conda env list", toprint=False),
                    ttime=0.01,
                )
            subprocess.check_call(["conda", "env", "list"], stdout=file)
        except FileNotFoundError:
            if info:
                typewriter(
                    printnlog("Command not found; Returning emtpy dict", toprint=False)
                )
            return {}
    with open("condaEnvList", "r") as file:
        fr = file.readlines()[2:-1]
    conda = {}
    for env in fr:
        name, path = env.split(" ")[0], env.split(" ")[-1].strip() + "\\python.exe"
        conda[name] = path
    os.remove("condaEnvList")
    return conda


def env_menu(info: bool = False):
    """
    The env_menu function is used to select the environment in which you want to run your code.
    It prints out all of the environments that are available on your computer, and then asks for a number input.
    The number corresponds with an environment name, and when you enter it, it returns the path to that environment.
    
    :param info: bool: Determine whether the function should return a dictionary of all environments or just their names
    :return: The path to the selected environment
    """
    conda = get_envs(info)
    times = -1
    for times, env in enumerate(conda):
        print(times + 1, env)
    print(times + 2, sys.executable)
    first1 = conda.items()
    try:
        first = list(first1)[cislo := int(input("Select env > ")) - 1][1]
    except IndexError:
        if cislo == times + 1:
            return sys.executable
    return first
