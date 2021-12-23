import shutil
import subprocess
import tempfile
from pathlib import Path

from PIL import Image as Im



class Image():
    ''' Glitch an image using audio effects.
        List of effects can be found @ http://sox.sourceforge.net/sox.html#effects

        in_file: image to be glitched
        output: output filename. Default is input name + _glitch
        g_ext: extension of the glitch file. Default is tiff
    '''

    def __init__(self, in_file):
        self.in_file = Path(in_file)
        self.effects = []

    def contrast(self, enhancement_amount):
        ''' Comparable with compression, this effect modifies an audio signal
            to make it sound louder. enhancement-amount controls the amount of
            the enhancement and is a number in the range 0−100. Note that
            enhancement-amount = 0 still gives a significant contrast enhancement. '''

        if enhancement_amount < 0:
            enhancement_amount = 0
        elif enhancement_amount > 100:
            enhancement_amount = 100

        self.effects += ['contrast', str(enhancement_amount)]

    def echo(self):
        pass

    def flanger(self):
        pass

    def hilbert(self):
        pass

    def phaser(self):
        pass

    def build(self, output=None, g_ext='tiff'):
        ''' Run the command and close the temporary directory '''

        if output:
            output = Path(output)
        else:
            output = Path(f"{self.in_file.stem}_glitch.{g_ext}")

        with tempfile.TemporaryDirectory() as tempdir:
            tempdir = Path(tempdir)
            pre_glitch = tempdir / f"pre_glitch.{g_ext}"
            with Im.open(self.in_file) as img:
                img.save(pre_glitch)

            cmd = ['sox', '-t', 'ul', '-c', '1', '-r', '96k',
                   str(pre_glitch), '-t', 'ul', str(output), 'trim', '0',
                   '200s', ':'] + self.effects

            subprocess.run(cmd, check=True)
        print(f"Image created @ {output}")
