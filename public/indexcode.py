# Imports
import sys
sys.path.insert(1, '../audioutils')
from audioplot import *
from spectralfactor import *
import numpy as np
import matplotlib.pyplot as plt

sr, sample = wavread('dolphin.wav')
sample = np.sum(sample, axis=1)
sample = sample[2*sr:5*sr]

def test1():
    fig = plt.figure()
    spec = fig.add_gridspec(1, 3)

    ax = fig.add_subplot(spec[0, 0])
    wave_plot(ax, sample, xbins=0, ybins=0, 
                        xbinlabels=[], ybinlabels=[],
                        xlabel='', ylabel='', title='', grid=True)

    ax2 = fig.add_subplot(spec[0, 1])
    spec_plot(ax2, sample, sr, 5)

    ax3 = fig.add_subplot(spec[0, 2], projection='3d')
    spec3d_plot(ax3, sample, sr, 5)

    fig.tight_layout()
    fig.savefig('graph.png')


def test2():
    fig = plt.figure()
    spec = fig.add_gridspec(1, 1)

    ax = fig.add_subplot(spec[0, 0])
    spec_plot(ax, sample, sr)
    fig.tight_layout()
    fig.savefig("graph.png")


def test3():
    fig = plt.figure()
    spec = fig.add_gridspec(1, 1)

    ax = fig.add_subplot(spec[0, 0], projection='3d')
    spec3d_plot(ax, sample, sr, xbins=4)
    fig.tight_layout()
    fig.savefig("graph.png")

if __name__ == '__main__':
    test3()
