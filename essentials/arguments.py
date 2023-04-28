import argparse

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