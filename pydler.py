'''Usage: pydler
    pydler -h | --help
    pydler --config=<CFG>

Options:
    -h --help       Show this screen
    --config=<CFG>  Use this config file (json) for macro [default: conf/macro.json]
'''

from docopt import docopt
import time
import keyboard
import json
import random
import os


def main(args):
    print(os.path.join(os.getcwd(), args['--config']))
    move_map = {'forward': 'w',
                'backward': 's',
                'left': 'a',
                'right': 'd'}

    with open(os.path.join(os.getcwd(), args['--config'])) as pydler_cfg:
        config = json.load(pydler_cfg)

    l1_key = ['moves', 'emotes']
    # basic config
    # moves:
    #   options: [forward, left, right, backward]            // will map to keys
    #   duration: <number of seconds>   // can be fractional
    # emote:
    #   options: [<emotes>]             // [dance, drink, spit, fart, snicker, etc...]
    #   duration: <number of seconds>

    print(json.dumps(config, indent=4))
    while True:
        action = l1_key[random.randint(0, len(l1_key)-1)]

        if action == 'moves':
            duration = config[action]['duration']  # convert to milliseconds
            key = move_map[config[action]['options'][random.randint(0, len(config[action]['options'])-1)]]
            print(f' >> duration {duration} key {key}')
            while duration > 0:
                keyboard.press(key)
                time.sleep(0.1)
                duration -= 0.1
                print(f' >> remaining {duration}\r')
            keyboard.release(key)
            print(' >> ')

        if action == 'emotes':
            duration = config[action]['duration']
            emote = config[action]['options'][random.randint(0, len(config[action]['options'])-1)]
            print(f' >> duration {duration} emote {emote}')
            keyboard.write(f'/{emote}')
            keyboard.send('enter')
            time.sleep(duration)


if __name__ == '__main__':
    args = docopt(__doc__)
    main(args)
