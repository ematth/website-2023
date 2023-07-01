# Imports
import sys
sys.path.insert(1, '/Users/ematth/Documents/website/audioutils')
from audioplot import *
from spectralfactor import *
import numpy as np
import matplotlib.pyplot as plt
from scipy.io.wavfile import read, write

SINE = lambda x, f=1, a=1, b=0 : (a * np.sin(f*2*np.pi*x)) + b

t = np.linspace(0, 1)

def fig1():
    fig = plt.figure(); ax = fig.add_subplot(131)

    wave_plot(ax, SINE(t), xbins=2, ybins=2, 
                    xbinlabels=['$0$', '$1$'], ybinlabels=['$-\\alpha$', '$0$', '$\\alpha$'],
                    xlabel='', ylabel='', title='', grid=True)
    
    t2 = np.arange(0, 4, 0.001)
    ax2 = fig.add_subplot(132)
    wave_plot(ax2, SINE(t2), xbins=3, ybins=2, 
                    xbinlabels=['$0$', '$...$', '$4$'], ybinlabels=['$-\\alpha$', '$0$', '$\\alpha$'],
                    xlabel='', ylabel='', title='', grid=True)
    
    t3 = np.arange(0, 100, 0.01)
    ax2 = fig.add_subplot(133)
    wave_plot(ax2, SINE(t3), xbins=3, ybins=2, 
                    xbinlabels=['$0$', '$...$', '$n$'], ybinlabels=['$-\\alpha$', '$0$', '$\\alpha$'],
                    xlabel='', ylabel='', title='', grid=True)
    
    fig.set_size_inches(18,8)
    fig.supxlabel('samples', fontsize=20)
    fig.supylabel('amplitude', fontsize=20)
    fig.tight_layout()
    fig.savefig('plot1.png')


def fig2():
    fig = plt.figure(); 

    sr, sample = wavread('staywithme.wav'); sample = np.sum(sample, axis=1)
    sample=sample[:5*sr]

    ax = fig.add_subplot(1,2,1)
    wave_plot(ax, sample[20000:20180], xbins=0, ybins=0, 
                    xbinlabels=[], ybinlabels=[],
                    xlabel='A couple samples...', ylabel='', title='', grid=True)

    ax2 = fig.add_subplot(1,2,2)
    wave_plot(ax2, sample, xbins=0, ybins=0, 
                    xbinlabels=[], ybinlabels=[],
                    xlabel='and a lot more samples!', ylabel='', title='', grid=True)
    
    
    
    fig.set_size_inches(18,8)
    fig.tight_layout()
    fig.savefig('plot2.png')
    

def fig3():
    sr, sample = wavread('staywithme.wav')
    sample = sample[:5*sr]
    chan = np.split(sample, 2, axis=1)

    fig = plt.figure()
    ax = fig.add_subplot(1,3,1)
    wave_plot(ax, chan[0], xbins=0, ybins=0, 
                    xbinlabels=[], ybinlabels=[],
                    xlabel='Left Channel', ylabel='', title='', grid=True, color='red')

    ax2 = fig.add_subplot(1,3,2)
    wave_plot(ax2, chan[1], xbins=0, ybins=0, 
                    xbinlabels=[], ybinlabels=[],
                    xlabel='Right Channel', ylabel='', title='', grid=True, color='green')
    
    ax3 = fig.add_subplot(1,3,3)
    wave_plot(ax3, chan[0], xbins=0, ybins=0, 
                    xbinlabels=[], ybinlabels=[],
                    xlabel='', ylabel='', title='', grid=True, color='red')
    wave_plot(ax3, chan[1], xbins=0, ybins=0, 
                    xbinlabels=[], ybinlabels=[],
                    xlabel='Channel Overlap', ylabel='', title='', grid=True, color='green')
    
    fig.set_size_inches(18,8)
    fig.tight_layout()
    fig.savefig('plot3.png')

def audio1():
    sine = lambda t, f, a=1: np.array(a * np.sin(f * 2 * np.pi * t)).astype('float32') # general sine function
    sr = 8000 # sample rate
    duration = 3 # number of seconds to play the sample for
    t = np.linspace(0, duration, num=sr * duration) # time space for our sine function.

    fig = plt.figure()

    ax = fig.add_subplot(1,1,1)
    wave_plot(ax, SINE(np.linspace(0, duration/440, 48000), 440), xbins=2, ybins=2, legend='440 Hz')

    wave_plot(ax, SINE(np.linspace(0, duration/440, 48000), 554.37), xbins=2, ybins=2, legend='554.37 Hz', color='red')

    wave_plot(ax, SINE(np.linspace(0, duration/440, 48000), 669.25), xbins=0, ybins=2, title='A-Major Chord', xlabel='', legend='669.25 Hz', color='green')

    fig.set_size_inches(15, 6)

    ax.legend(loc='lower right')

    fig.tight_layout()
    fig.savefig('plot4.png')

def audio2():
    def sine(time:float, freqs:list[float]=[440], amp:float=1) -> list[float]:
        signal = np.zeros_like(time)
        for f in freqs:
            signal += np.sin(f * 2 * np.pi * t)
        return (amp/len(freqs) * signal).astype('float32')
    
    # Lambda version
    #sine = lambda time, freqs=[440], amp=1: (np.sum([np.sin(f * 2 * np.pi * time) for f in freqs], axis=0) * (amp/len(freqs))).astype('float32')

    sr = 8000 # sample rate
    duration = 3 # number of seconds to play the sample for
    t = np.linspace(0, duration, num=sr * duration) # time space for our sine function.

    a_natural = sine(t, [440])
    write('a440.wav', sr, a_natural)

    c_sharp = sine(t, [554.37])
    write('c554.wav', sr, c_sharp)

    a_major = sine(t, [440, 554.37, 669.25])
    write('a_major.wav', sr, a_major)
    


if __name__ == '__main__':
    fig1()
    fig2()
    fig3()
    audio1()
    audio2()