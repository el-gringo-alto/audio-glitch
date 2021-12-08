import subprocess
from tempfile import TemporaryDirectory
from pathlib import Path
import random

from PIL import Image

from effects import EFFECTS


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


# randomize the effects
r_effects = random.choices(EFFECTS, k=random.randrange(1, 5))
glitch('imgs/stock.jpg', 'stock_glitch.jpg', *r_effects)
