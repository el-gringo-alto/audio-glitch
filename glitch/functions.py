''' Functions to be used for the script '''
import subprocess
from tempfile import TemporaryDirectory
from pathlib import Path
import random

from PIL import Image



def r_num(num=None):
    ''' Output a random number as a string to be used in the effects list '''
    if not num:
        rand_str = f"{round(random.random(), 1)}"
    else:
        rand_str = f"{random.randrange(0, num)}"
    return rand_str


def r_effects(effects, from_num=1, to_num=5):
    ''' Randomize the effects list '''
    return random.choices(effects, k=random.randrange(from_num, to_num))


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
            cmd += effect

        subprocess.run(cmd, check=True)

        with Image.open(post_glitch) as img:
            img.save(out_img)
