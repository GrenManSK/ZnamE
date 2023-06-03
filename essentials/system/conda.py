import subprocess
import os
import sys
from ..functions.writing import printnlog, typewriter


def get_envs(info: bool = False) -> dict:
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
            return dict()
    with open("condaEnvList", "r") as file:
        fr = file.readlines()[2:-1]
    conda = {}
    for env in fr:
        name, path = env.split(" ")[0], env.split(" ")[-1].strip() + "\\python.exe"
        conda[name] = path
    os.remove("condaEnvList")
    return conda


def env_menu(info: bool = False):
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
