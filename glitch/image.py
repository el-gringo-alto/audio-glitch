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

    def __init__(self, in_file, output=None, g_ext='tiff'):
        self.in_file = Path(in_file)
        self.g_ext = g_ext
        self.tempdir = Path(tempfile.mkdtemp())
        if output:
            self.output = Path(output)
        else:
            self.output = Path(f"{self.in_file.stem}_glitch.{self.g_ext}")

        pre_glitch = self.tempdir / f"pre_glitch.{self.g_ext}"
        with Im.open(self.in_file) as img:
            img.save(pre_glitch)

        self.cmd = ['sox', '-t', 'ul', '-c', '1', '-r', '96k',
                    str(pre_glitch), '-t', 'ul', str(self.output),
                    'trim', '0', '200s', ':']

    def contrast(self, enhancement_amount):
        ''' Comparable with compression, this effect modifies an audio signal
            to make it sound louder. enhancement-amount controls the amount of
            the enhancement and is a number in the range 0−100. Note that
            enhancement-amount = 0 still gives a significant contrast enhancement. '''
        if enhancement_amount < 0:
            enhancement_amount = 0
        elif enhancement_amount > 100:
            enhancement_amount = 100

        self.cmd += ['contrast', str(enhancement_amount)]

    def echo(self):
        pass

    def flanger(self):
        pass

    def hilbert(self):
        pass

    def phaser(self):
        pass

    def run(self):
        ''' Run the command and close the temporary directory '''
        subprocess.run(self.cmd, check=True)
        print(f"Image created @ {self.output}")

        if self.tempdir.exists():
            shutil.rmtree(self.tempdir)
