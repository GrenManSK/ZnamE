import argparse
import sys
from .internet import get_line_number
from .writing import printnlog, typewriter
from .exceptions import argEnviromentError, argInactiveLimitError, argIntroError, argMusicError, argWaifuError, argNekoError, argGameError
from .exceptions import error_get


def arguments(config):
    parser = argparse.ArgumentParser()
    UNSPECIFIED = object()
    language: list[str] = ['SK', 'EN', 'JP']  # Supported languages

    "Setting up music if none leaving empty list"

    music: list[str] = list(
        set(str(config['basic info']['musiclist']).split(',')[0:]))
    if music[0] == 'None':
        music = []
    else:
        for i in music:
            if i == '':
                music.remove('')
    musicchoices: list[str] = ['0']
    for i in range(1, len(music) + 1):
        musicchoices.append(str(i))
    parser.add_argument('-lang', '--language', choices=language,
                        help='Language selection', nargs='?')
    parser.add_argument('-v', '--version', choices=[],
                        help='Show version of this program', default=UNSPECIFIED, nargs='?')
    parser.add_argument('-ef', '--endf', choices=[],
                        help='Will not automatically end program', default=UNSPECIFIED, nargs='?')
    parser.add_argument('-ni', '--nointro', choices=[],
                        help='Will not start intro', default=UNSPECIFIED, nargs='?')
    parser.add_argument('-nif', '--nointrof', choices=[],
                        help='Will not start intro', default=UNSPECIFIED, nargs='?')
    parser.add_argument('-co', '--configoptions', choices=[],
                        help='Make a file with all config options', default=UNSPECIFIED, nargs='?')
    parser.add_argument('-log', '--log', choices=[],
                        help='!!! Argument for program to use', default=UNSPECIFIED, nargs='?')
    parser.add_argument('-music', '--music', choices=musicchoices,
                        help='Starts music; you can select from: ' + str(i for i in music), default=0, nargs='?')

    "These are arguments for program to use"

    parser.add_argument('-neko', '--neko', choices=[],
                        help='Easter egg was activated', default=UNSPECIFIED, nargs='?')
    parser.add_argument('-waifu', '--waifu', choices=[],
                        help='Easter egg was activated', default=UNSPECIFIED, nargs='?')
    parser.add_argument('-waifuvid', '--waifuvid', choices=[],
                        help='Easter egg was activated', default=UNSPECIFIED, nargs='?')
    parser.add_argument('-inactive', '--inactive', choices=[],
                        help='!!! Argument for program to use', default=UNSPECIFIED, nargs='?')
    parser.add_argument('-restart', '--restart', choices=[],
                        help='!!! Argument for program to use', default=UNSPECIFIED, nargs='?')
    parser.add_argument('-update', '--update', choices=[],
                        help='!!! Argument for program to use (this command won\'t update this program, it does it automatically)', default=UNSPECIFIED, nargs='?')
    parser.add_argument('-autol', '--autologin', choices=[],
                        help='!!! Argument for program to use', default=UNSPECIFIED, nargs='?')
    parser.add_argument('-test', '--test', choices=[],
                        help='!!! Argument for program to use', default=UNSPECIFIED, nargs='?')
    parser.add_argument('-debug', '--debug', choices=[],
                        help='Debugging enabled', default=UNSPECIFIED, nargs='?')
    return parser, music, language, UNSPECIFIED


def check_correctness(args, config, logger, music, set_config):
    hexnumber: list[str] = ['0', '1', '2', '3', '4', '5', '6',
                            '7', '8', '9', 'a', 'b', 'c', 'd', 'e', 'f']
    logger.stay(printnlog("Checking config correctness", toprint=False))
    if not config['basic info']['enviroment'].split(' ')[0][0] in hexnumber:
        error_get(ExceptionGroup('', [argEnviromentError('Wrong choice \'basic info\' => enviroment first character'), ValueError(
            f'Not allowed character | Allowed: {hexnumber}')]), [get_line_number()])
        sys.exit(1)
    elif not config['basic info']['enviroment'].split(' ')[0][1] in hexnumber:
        error_get(ExceptionGroup('', [argEnviromentError('Wrong choice \'basic info\' => enviroment second character'), ValueError(
            f'Not allowed character | Allowed: {hexnumber}')]), [get_line_number()])
        sys.exit(1)
    else:
        printnlog('basic info => enviroment')
    try:
        int(config['basic info']['inactivelimit'])
        printnlog('basic info => inactivelimit')
    except ValueError:
        error_get(ExceptionGroup('', [argInactiveLimitError(
            'Wrong choice in \'basic info\' => inactivelimit'), ValueError('take only numbers')]), [get_line_number()])
        sys.exit(1)
    if not config['basic info']['intro'] in [True, False]:
        error_get(ExceptionGroup('', [argIntroError('Wrong choice in \'basic info\' => intro'), ValueError(
            'Only \'True\' or \'False\'')]), [get_line_number()])
        sys.exit(1)
    else:
        printnlog('basic info => intro')
    if config['basic info']['music'].split(' ')[0] == 'enable':
        args.music = config['basic info']['musicnumber']
        printnlog('basic info => music')
    elif config['basic info']['music'].split(' ')[0] == 'disable':
        printnlog('basic info => music')
        pass
    else:
        error_get(ExceptionGroup('', [argMusicError('Wrong choice in \'basic info\' => music'), ValueError(
            'Only \'enable\' or \'disable\'')]), [get_line_number()])
        sys.exit(1)
    if not config['waifu settings']['type'].split(' ')[0] in ['sfw', 'nsfw']:
        error_get(ExceptionGroup('', [argWaifuError('Wrong choice in \'waifu settings\' => type'), ValueError(
            'Only \'sfw\' or \'nsfw\'')]), [get_line_number()])
        sys.exit(1)
    else:
        printnlog('waifu settings => type')
    if config['waifu settings']['type'] == 'sfw':
        category: list[str] = ["waifu", "neko", "shinobu", "megumin", "bully", "cuddle", "cry", "hug", "awoo", "kiss", "lick", "pat", "smug", "bonk", "yeet",
                               "blush", "smile", "wave", "highfive", "handhold", "nom", "bite", "glomp", "slap", "kill", "kick", "happy", "wink", "poke", "dance", "cringe"]
        if not config['waifu settings']['category'].split(' ')[0] in category:
            error_get(ExceptionGroup('', [argWaifuError('Wrong choice in \'waifu settings\' => category'), ValueError(
                'Use \'waifu\' and see option in setup function')]), [get_line_number()])
            sys.exit(1)
        else:
            printnlog('waifu settings => category')
    elif config['waifu settings']['type'] == 'nsfw':
        category: list[str] = ['waifu', 'neko', 'trap', 'blowjob']
        if not config['waifu settings']['category'].split(' ')[0] in category:
            error_get(ExceptionGroup('', [argWaifuError('Wrong choice in \'waifu settings\' => category'), ValueError(
                'Use \'waifu\' and see option in setup function')]), [get_line_number()])
            sys.exit(1)
        else:
            printnlog('waifu settings => category')
    server: list[str] = ['nekos.best', 'waifu.pics', 'kyoko', 'nekos_api']
    if not config['neko settings']['server'] in server:
        error_get(ExceptionGroup('', [argNekoError('Wrong choice in \'neko settings\' => server'), ValueError(
            f'Only take {str(server)}')]), [get_line_number()])
        sys.exit(1)
    else:
        printnlog('neko settings => server')
    try:
        int(config['game settings']['goal_score'])
    except ValueError:
        error_get(ExceptionGroup('', [argGameError('Wrong choice in \'game settings\' => goal_score'), ValueError(
            'take only numbers')]), [get_line_number()])
        sys.exit(1)
    try:
        if 10 <= int(config['game settings']['goal_score']):
            printnlog('game settings => goal_score')
        else:
            raise ValueError
    except ValueError:
        error_get(ExceptionGroup('', [argGameError(
            'Wrong choice in \'game settings\' => goal_score'), ValueError('minimum is 10')]), [get_line_number()])
        sys.exit(1)
    try:
        float(config['game settings']['computer_power'])
        printnlog('game settings => computer_power')
    except ValueError:
        error_get(ExceptionGroup('', [argGameError('Wrong choice in \'game settings\' => computer_power'), ValueError(
            'take only numbers')]), [get_line_number()])
        sys.exit(1)
    if config['basic info']['music'] == 'enable':
        musiclimittext: bool = False
        lenmusic = len(music)
        configlenmusic = int(config['basic info']['musicnumber'])
        while lenmusic < configlenmusic:
            if not musiclimittext:
                typewriter(printnlog('basic info => musicnumber; you have exceeded the limit by ' +
                                     str(int(config['basic info']['musicnumber']) - len(music)), toprint=False))
                musiclimittext: bool = True
            set_config('basic info', 'musicnumber', int(args.music)-1)
            configlenmusic = int(config['basic info']['musicnumber'])
            args.music = int(args.music) - 1
