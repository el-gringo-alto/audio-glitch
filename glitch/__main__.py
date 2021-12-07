import subprocess
from tempfile import TemporaryDirectory
from pathlib import Path
import random

from PIL import Image



def rand(num=None):
    ''' Output a random number to be used in the effects list '''
    if not num:
        rand_str = f"{round(random.random(), 1)}"
    else:
        rand_str = f"{random.randrange(0, num)}"
    return rand_str


# list of effects can be found @ http://sox.sourceforge.net/sox.html
# put all the effects into a list
fxs = [
    ['echo', rand(), rand(), rand(1000), rand()],
    # ['flanger'],
    # ['phaser', rand(), rand(), rand(5), rand(), rand(), '-t']
]


def glitch(in_img, out_img, *effects):
    ''' Glich an image using Sox effects '''
    with TemporaryDirectory() as temd:
        pre_glitch = Path(temd) / 'to_glitch.bmp'
        post_glitch = Path(temd) / 'glitch.bmp'

        with Image.open(in_img) as img:
            img.save(pre_glitch)

        cmd = ['sox', '-t', 'ul', '-c', '1', '-r', '48k', str(pre_glitch),
            '-t', 'ul', str(post_glitch), 'trim', '0', '200s', ':']

        for effect in effects:
            # phaser = ['phaser', '0.3', '0.9', '1', '0.7', '0.5', '-t']
            # cmd += effect.split(' ')
            cmd += effect

        print(cmd)

        subprocess.run(cmd, check=True)

        with Image.open(post_glitch) as img:
            img.save(out_img)

glitch('imgs/stock.jpg', 'imgs/final.jpg', *fxs)


# glitch(
#     'stock.jpg',
#     'final.jpg',
#     'phaser 0.3 0.9 1 0.7 0.5 -t',
#     'flanger',
#     'echo 0.4 0.8 10 0.9')
