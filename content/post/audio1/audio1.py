# Imports
import sys
sys.path.insert(1, '/Users/ematth/Documents/website/audioutils')
from audioplot import *
from spectralfactor import *
import numpy as np
import matplotlib.pyplot as plt
from scipy.io.wavfile import read, write

SINE = lambda x, a=1, b=0 : (a * np.sin(2*np.pi*x)) + b

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
    wave_plot(ax, sample, xbins=0, ybins=0, 
                    xbinlabels=[], ybinlabels=[],
                    xlabel='', ylabel='', title='', grid=True)

    ax2 = fig.add_subplot(1,2,2)
    wave_plot(ax2, sample, xbins=0, ybins=0, 
                    xbinlabels=[], ybinlabels=[],
                    xlabel='', ylabel='', title='', grid=True)
    
    
    
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
                    xlabel='Channel Difference', ylabel='', title='', grid=True, color='green')
    
    fig.set_size_inches(18,8)
    fig.tight_layout()
    fig.savefig('plot3.png')


# def fig4(k=4):
#     fig = plt.figure()

#     sr, sample = wavread('staywithme.wav'); 
#     sample = np.sum(sample, axis=1)
#     sample = sample[:5*sr]

#     sample_stft = np.absolute(stft(sample)).T

#     h, w = spectral_components(sample_stft, 4)

#     colors=['blue', 'red', 'green', 'orange']
#     for i in range(k):
#         ax = fig.add_subplot(1, k, i+1)
#         wave_plot(ax, h[i], xbins=2, ybins=2, 
#                     xbinlabels=['',''], ybinlabels=['',''],
#                     xlabel='', ylabel='', title='', grid=True, color=colors[i])
        
#     fig.set_size_inches(18,8)
#     fig.tight_layout()
#     fig.savefig('plot4.png')



if __name__ == '__main__':
    # fig1()
    fig2()
    fig3()
    # fig4()