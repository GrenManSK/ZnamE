import argparse
import sys
import os
import yaml
from .internet import get_line_number
from .functions.writing import printnlog, typewriter
from .system.exceptions import (
    argenvironmentError,
    argInactiveLimitError,
    argIntroError,
    argMusicError,
    argWaifuError,
    argNekoError,
    argGameError,
    argTranslateError,
    argTranslatorError,
    argQuietError,
)
from verbose import inbetween, get_logger
from .system.exceptions import error_get
from .data.translate import t_languages, t_translators
from dotenv import load_dotenv

load_dotenv()


def arguments(config):
    """
    The arguments function is used to set up the arguments for the program.
    It also sets up a list of music that can be played in-game, and it returns
    the parser object, the music list, and an unspecified value.
    
    :param config: Get the config file
    :return: The parser, music and unspecified
    """
    parser = argparse.ArgumentParser()
    UNSPECIFIED = object()

    "Setting up music if none leaving empty list"

    music: list[str] = list(set(str(config["music"]["musiclist"]).split(",")[0:]))
    if music[0] == "None":
        music = []
    else:
        for i in music:
            if i == "":
                music.remove("")
    musicchoices: list[str] = ["0"]
    for i in range(1, len(music) + 1):
        musicchoices.append(str(i))
    _music = str([i for i in music])
    parser.add_argument(
        "-v",
        "--version",
        choices=[],
        help="Show version of this program",
        default=UNSPECIFIED,
        nargs="?",
    )
    parser.add_argument(
        "-ef",
        "--endf",
        choices=[],
        help="Will not automatically end program",
        default=UNSPECIFIED,
        nargs="?",
    )
    parser.add_argument(
        "-ni",
        "--nointro",
        choices=[],
        help="Will not start intro",
        default=UNSPECIFIED,
        nargs="?",
    )
    parser.add_argument(
        "-nif",
        "--nointrof",
        choices=[],
        help="Will not start intro",
        default=UNSPECIFIED,
        nargs="?",
    )
    parser.add_argument(
        "-co",
        "--configoptions",
        choices=[],
        help="Make a file with all config options",
        default=UNSPECIFIED,
        nargs="?",
    )
    parser.add_argument(
        "-log",
        "--log",
        choices=[],
        help="!!! Argument for program to use",
        default=UNSPECIFIED,
        nargs="?",
    )
    parser.add_argument(
        "-music",
        "--music",
        choices=musicchoices,
        help="Starts music; you can select from: " + _music,
        default=0,
        nargs="?",
    )
    parser.add_argument(
        "-quiet", "--quiet", choices=[], help="", default=UNSPECIFIED, nargs="?"
    )
    parser.add_argument(
        "-translate",
        "--translate",
        choices=t_languages,
        help="",
        default=UNSPECIFIED,
        nargs="?",
    )

    "These are arguments for program to use"

    parser.add_argument(
        "-neko",
        "--neko",
        choices=[],
        help="Easter egg was activated",
        default=UNSPECIFIED,
        nargs="?",
    )
    parser.add_argument(
        "-waifu",
        "--waifu",
        choices=[],
        help="Easter egg was activated",
        default=UNSPECIFIED,
        nargs="?",
    )
    parser.add_argument(
        "-waifuvid",
        "--waifuvid",
        choices=[],
        help="Easter egg was activated",
        default=UNSPECIFIED,
        nargs="?",
    )
    parser.add_argument(
        "-inactive",
        "--inactive",
        choices=[],
        help="!!! Argument for program to use",
        default=UNSPECIFIED,
        nargs="?",
    )
    parser.add_argument(
        "-restart",
        "--restart",
        choices=[],
        help="!!! Argument for program to use",
        default=UNSPECIFIED,
        nargs="?",
    )
    parser.add_argument(
        "-update",
        "--update",
        choices=[],
        help="!!! Argument for program to use (this command won't update this program, it does it automatically)",
        default=UNSPECIFIED,
        nargs="?",
    )
    parser.add_argument(
        "-autol",
        "--autologin",
        choices=[],
        help="!!! Argument for program to use",
        default=UNSPECIFIED,
        nargs="?",
    )
    parser.add_argument(
        "-test",
        "--test",
        choices=[],
        help="!!! Argument for program to use",
        default=UNSPECIFIED,
        nargs="?",
    )
    parser.add_argument(
        "-debug",
        "--debug",
        choices=[],
        help="Debugging enabled",
        default=UNSPECIFIED,
        nargs="?",
    )
    return parser, music, UNSPECIFIED


def check_correctness(args, config, logger: get_logger, music):
    hexnumber: list[str] = [
        "0",
        "1",
        "2",
        "3",
        "4",
        "5",
        "6",
        "7",
        "8",
        "9",
        "a",
        "b",
        "c",
        "d",
        "e",
        "f",
    ]
    logger.next(
        printnlog("Checking config correctness", toprint=False), where=inbetween
    )
    if not str(config["basic info"]["environmentA"]).split(" ")[0] in hexnumber:
        raise argenvironmentError(
            f"Wrong choice 'basic info' => environmentA character | Not allowed character | Allowed: {hexnumber}"
        )
    else:
        logger.stay(printnlog("basic info => environmentA", toprint=False))
    if not str(config["basic info"]["environmentB"]).split(" ")[0] in hexnumber:
        raise argenvironmentError(
            f"Wrong choice 'basic info' => environmentB character | Not allowed character | Allowed: {hexnumber}"
        )
    else:
        logger.stay(printnlog("basic info => environmentB", toprint=False))
    try:
        int(config["basic info"]["inactivelimit"])
        logger.stay(printnlog("basic info => inactivelimit", toprint=False))
    except ValueError:
        raise argInactiveLimitError("Wrong choice in 'basic info' => inactivelimit | Take only numbers")
    if not config["basic info"]["intro"] in [True, False]:
        raise argIntroError("Wrong choice in 'basic info' => intro | Only 'True' or 'False'")
    else:
        logger.stay(printnlog("basic info => intro", toprint=False))
    if config["music"]["music"].split(" ")[0] == "enable":
        args.music = config["music"]["musicnumber"]
        logger.stay(printnlog("music => music", toprint=False))
    elif config["music"]["music"].split(" ")[0] == "disable":
        logger.stay(printnlog("music => music", toprint=False))
        pass
    else:
        raise argMusicError("Wrong choice in 'music' => music | Only 'enable' or 'disable'")
    if not config["waifu settings"]["type"].split(" ")[0] in ["sfw", "nsfw"]:
        raise argWaifuError("Wrong choice in 'waifu settings' => type | Only 'sfw' or 'nsfw'")
    else:
        logger.stay(printnlog("waifu settings => type", toprint=False))
    if config["waifu settings"]["type"] == "sfw":
        category: list[str] = [
            "waifu",
            "neko",
            "shinobu",
            "megumin",
            "bully",
            "cuddle",
            "cry",
            "hug",
            "awoo",
            "kiss",
            "lick",
            "pat",
            "smug",
            "bonk",
            "yeet",
            "blush",
            "smile",
            "wave",
            "highfive",
            "handhold",
            "nom",
            "bite",
            "glomp",
            "slap",
            "kill",
            "kick",
            "happy",
            "wink",
            "poke",
            "dance",
            "cringe",
        ]
        if not config["waifu settings"]["category"].split(" ")[0] in category:
            raise argWaifuError("Wrong choice in 'waifu settings' => category | Use 'waifu' and see option in setup function")
        else:
            logger.stay(printnlog("waifu settings => category", toprint=False))
    elif config["waifu settings"]["type"] == "nsfw":
        category: list[str] = ["waifu", "neko", "trap", "blowjob"]
        if not config["waifu settings"]["category"].split(" ")[0] in category:
            raise argWaifuError("Wrong choice in 'waifu settings' => category | Use 'waifu' and see option in setup function")
        else:
            logger.stay(printnlog("waifu settings => category", toprint=False))
    server: list[str] = ["nekos.best", "waifu.pics", "kyoko", "nekos_api"]
    if not config["neko settings"]["server"] in server:
        raise argNekoError(f"Wrong choice in 'neko settings' => server | Only take {str(server)}")
    else:
        logger.stay(printnlog("neko settings => server", toprint=False))
    try:
        int(config["game settings"]["goal_score"])
    except ValueError:
        raise argGameError("Wrong choice in 'game settings' => goal_score | Take only numbers")
    try:
        if 10 <= int(config["game settings"]["goal_score"]):
            logger.stay(printnlog("game settings => goal_score", toprint=False))
        else:
            raise ValueError
    except ValueError:
        argGameError("Wrong choice in 'game settings' => goal_score | Minimum is 10")
    try:
        float(config["game settings"]["computer_power"])
        logger.stay(printnlog("game settings => computer_power", toprint=False))
    except ValueError:
        argGameError("Wrong choice in 'game settings' => computer_power | Take only numbers")
    if config["music"]["music"] == "enable":
        musiclimittext: bool = False
        lenmusic = len(music)
        configlenmusic = int(config["music"]["musicnumber"])
        while lenmusic < configlenmusic:
            if not musiclimittext:
                typewriter(
                    printnlog(
                        "music => musicnumber; you have exceeded the limit by "
                        + str(int(config["music"]["musicnumber"]) - len(music)),
                        toprint=False,
                    )
                )
                musiclimittext: bool = True
            config = set_config("music", "musicnumber", int(args.music) - 1)
            configlenmusic = int(config["music"]["musicnumber"])
            args.music = int(args.music) - 1
    if not str(config["translator"]["translate"]).split(" ")[0] in t_languages + [""]:
        raise argTranslateError(f"Wrong choice 'translator' => translate character | Not allowed language | Allowed: {t_languages}")
    else:
        logger.stay(printnlog("translator => translate", toprint=False))
    if not str(config["translator"]["translator"]).split(" ")[0] in t_translators:
        raise argTranslatorError(f"Wrong choice 'translator' => translator character | Not allowed language | Allowed: {t_translators}")
    else:
        logger.stay(printnlog("translator => translator", toprint=False))
    if not eval(str(config["basic info"]["quiet"]).split(" ")[0]) in [True, False]:
        argTranslatorError("Wrong choice 'basic info' => quiet character | Not allowed option | Allowed: True/False")
    else:
        logger.stay(printnlog("basic info => quiet", toprint=False))
    logger.prev(printnlog("DONE", toprint=False), where=inbetween)


def print_config(logger: get_logger, config):
    logger.stay(
        printnlog(
            "environmentA: " + str(config["basic info"]["environmentA"]).split(" ")[0],
            toprint=False,
        )
    )
    logger.stay(
        printnlog(
            "environmentB: " + str(config["basic info"]["environmentB"]).split(" ")[0],
            toprint=False,
        )
    )
    logger.stay(
        printnlog(
            "Intro: " + str(config["basic info"]["intro"]).split(" ")[0], toprint=False
        )
    )
    logger.stay(
        printnlog(
            "Inactivelimit: "
            + str(config["basic info"]["inactivelimit"]).split(" ")[0],
            toprint=False,
        )
    )
    logger.stay(
        printnlog(
            "Music: " + config["music"]["music"].split(" ")[0], toprint=False
        )
    )
    logger.stay(
        printnlog(
            "Musiclist: " + str(str(config["music"]["musiclist"]).split(",")),
            toprint=False,
        )
    )
    logger.stay(
        printnlog("Translate: " + str(config["translator"]["translate"]), toprint=False)
    )
    logger.stay(
        printnlog(
            "Translator: " + str(config["translator"]["translator"]), toprint=False
        )
    )
    logger.stay(
        printnlog("User history: " + str(config["user history"]), toprint=False)
    )


def write_config_options(server):
    """
    The write_config_options function writes the CONFIG_OPTIONS.txt file, which is used to store all of the configuration options for NekoBot.
    
    :param server: Write the server name in the config_options
    :return: Nothing
    """
    datelog = os.getenv("DATELOG")
    with open("CONFIG_OPTIONS.txt", "w") as config_file:
        config_file.write("basic info:\n")
        config_file.write(f"  environmentA: '[0-f]'\n")
        config_file.write(f"  environmentB: '[0-f]'\n")
        config_file.write(f"  inactivelimit: [Any number]\n")
        config_file.write(f"  intro: [True/False]\n")
        config_file.write(f"  music: [disable/enable]\n")
        config_file.write(f"  musiclist: [Any Youtube video title, divided by comma]\n")
        config_file.write(
            f"  musicnumber: [Any number; Max is number of items in musiclist]\n"
        )
        config_file.write(
            f"  translate: [''|'Afrikaans','Albanian','Amharic','Arabic','Armenian','Assamese','Aymara','Azerbaijani','Bambara','Basque','Belarusian','Bengali','Bhojpuri','Bosnian','Bulgarian','Catalan','Cebuano','Chichewa','Chinese (Simplified)','Chinese (Traditional)','Corsican','Czech','Danish','Dhivehi','Dogri','Dutch','English','Esperanto','Estonian','Ewe','Filipino','Finnish','French','Frisian','Galician','Georgian','German','Greek','Guarani','Gujarati','Haitian Creole','Hausa','Hawaiian','Hindi','Hmong','Hungarian','Icelandic','Igbo','Ilocano','Indonesian','Irish','Italian','Japanese','Javanese','Kannada','Kazakh','Khmer','Kinyarwanda','Konkani','Korean','Krio','Kurdish (Kurmanji)','Kurdish (Sorani)','Kyrgyz','Lao','Latvian','Lingala','Lithuanian','Luganda','Luxembourgish','Macedonian','Maithili','Malagasy','Malay','Malayalam','Maltese','Maori','Marathi','Meiteilon (Manipuri)','Mizo','Mongolian','Myanmar (Burmese)','Nepali','Norwegian','Odia (Oriya)','Oromo','Pashto','Polish','Portuguese','Punjabi','Quechua','Romanian','Russian','Samoan','Sanskrit','Scots Gaelic','Sepedi','Serbian','Sesotho','Shona','Si ndhi','Sinhala','Slovak','Slovenian','Somali','Spanish','Sundanese','Swahili','Swedish','Tamil','Tatar','Telugu','Thai','Tigrinya','Tsonga','Turkish','Turkmen','Twi','Ukrainian','Urdu','Uyghur','Uzbek','Vietnamese','Welsh','Xhosa','Yiddish','Yoruba','Zulu']"
        )
        config_file.write(f"  translator: [Bing|Google]")
        config_file.write(f"  vlc-path: C:/Program Files/VideoLAN/VLC/vlc.exe")
        config_file.write("game settings:\n")
        config_file.write(f"  computer_power: [Any number; Lower the powerfull]\n")
        config_file.write(f"  goal_score: [Any number]\n")
        config_file.write(f"  offline_game: [true/false]\n")
        config_file.write(f"neko settings:\n")
        config_file.write(f"  server: {server}\n")
        config_file.write(f"user history:\n")
        category: list[str] = [
            "waifu",
            "neko",
            "shinobu",
            "megumin",
            "bully",
            "cuddle",
            "cry",
            "hug",
            "awoo",
            "kiss",
            "lick",
            "pat",
            "smug",
            "bonk",
            "yeet",
            "blush",
            "smile",
            "wave",
            "highfive",
            "handhold",
            "nom",
            "bite",
            "glomp",
            "slap",
            "kill",
            "kick",
            "happy",
            "wink",
            "poke",
            "dance",
            "cringe",
        ]
        config_file.write(f"waifu settings:\n")
        config_file.write(f"  category (sfw) = {category}\n")
        category: list[str] = ["waifu", "neko", "trap", "blowjob"]
        config_file.write(f"  category (nsfw) = {category}\n")
        config_file.write("  type: [sfw/nsfw]\n")
    os.remove(f"crash_dump-{datelog}.txt")
    sys.exit(1)


def set_config(section: str, name: str, info: any) -> any:
    """
    The set_config function is used to set a value in the config.yml file.
        It takes three arguments: section, name, and info. Section is the section of the config file you want to edit (e.g., 'user history'). Name is what you want to change (e.g., 'username'), and info is what you want it changed to.

    :param section: str: Specify which section of the config
    :param name: str: Specify the name of the key in the yaml file
    :param info: any: Store the value that is being set
    :return: The info that you pass to it
    """
    global config
    config = yaml.safe_load(open("config.yml", "r"))
    if not isinstance(config["user history"], dict):
        config["user history"] = {}
    config[section][name] = info
    os.remove("config.yml")
    with open("config.yml", "w") as configfile:
        yaml.dump(config, configfile)
    config = yaml.safe_load(open("config.yml", "r"))
    return config


def music2str(musiclistnew):
    """
    The music2str function takes a list of music and converts it to a string.
        It then sets the config file's musiclist value to that string.
    
    :param musiclistnew: Store the musiclistnew variable, which is a list of all the songs in the playlist
    :return: A string with all the music in it
    """
    musiclistnewstring: str = ""
    for i in range(len(musiclistnew)):
        musiclistnewstring += str(musiclistnew[i]) + ","
    config = set_config("music", "musiclist", str(musiclistnewstring[0:-1]))
    return config
