''' Audio effects '''
import random



def r_num(num=None):
    ''' Output a random number as a string to be used in the effects list '''
    if not num:
        rand_str = f"{round(random.random(), 1)}"
    else:
        rand_str = f"{random.randrange(0, num)}"
    return rand_str


# list of effects can be found @ http://sox.sourceforge.net/sox.html
EFFECTS = [
    ['allpass'],
    ['band'],
    ['bandpass'],
    ['bandreject'],
    ['bass'],
    ['bend'],
    ['biquad'],
    ['chorus'],
    ['channels'],
    ['compand'],
    ['contrast'],
    ['dcshift'],
    ['deemph'],
    ['delay'],
    ['dither'],
    ['divide+'],
    ['downsample'],
    ['earwax'],
    ['echo', r_num(), r_num(), r_num(1000), r_num()],
    ['echos'],
    ['equalizer'],
    ['fade'],
    ['fir'],
    ['firfit+'],
    ['flanger'],
    ['gain'],
    ['highpass'],
    ['hilbert'],
    ['input#'],
    ['loudness'],
    ['lowpass'],
    ['mcompand'],
    ['noiseprof'],
    ['noisered'],
    ['norm'],
    ['oops'],
    ['output#'],
    ['overdrive'],
    ['pad'],
    ['phaser', r_num(), r_num(), r_num(5), r_num(), r_num(), '-t'],
    ['pitch'],
    ['rate'],
    ['remix'],
    ['repeat'],
    ['reverb'],
    ['reverse'],
    ['riaa'],
    ['silence'],
    ['sinc'],
    ['spectrogram'],
    ['speed'],
    ['splice'],
    ['stat'],
    ['stats'],
    ['stretch'],
    ['swap'],
    ['synth'],
    ['tempo'],
    ['treble'],
    ['tremolo'],
    ['upsample'],
    ['vad'],
    ['vol']
]
