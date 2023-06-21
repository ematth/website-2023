import numpy as np
import matplotlib.pyplot as plt
from scipy.io.wavfile import read
from scipy.signal import spectrogram
from matplotlib import cm
import math

## FUNCTIONS

def plot_range(dist: list[int or float] = (0, 1), bins: int = 0, decimal: int = 0) -> list[int or float]:
    """
    Given a range to mark on an axis, returns a list of evenly-spaced values for the axis.

    Args:
        dist (list, optional): range of values to span in axis. Defaults to [0, 1].
        bins (int, optional): number of markers to divide the axis evenly by. If bins=0, an empty range is given. Defaults to 3.
        decimal (int, optional): number of decimal places to round values to. Defaults to 2.

    Returns:
        list[int or float]: list of value markers. if round=0, value type is int.
    """  
    if bins <= 0: 
        return []
    elif bins == 1: 
        return [dist[0]]
    else:
        return [round(i, decimal) for i in range(dist[0], dist[1], dist[1] // (bins - 1))] + [dist[1]]

def wavread(path):
    sr, s = read(path)
    return sr, s.astype('float32')/32768

# Plot waveform of an audio file
def wave_plot(plot, sample, xbins=2, ybins=2,
              xbinlabels=[], ybinlabels=[],
              xlabel='time (s)', ylabel='Amplitude', title='Waveform',
              grid=False, color='C0'):
    plot.plot(sample, color=color)

    xrange = plot_range([0, len(sample)], xbins)
    plot.set_xticks(xrange, labels=xbinlabels if xbinlabels else [f'${i}$' for i in range(len(xrange))])

    yrange = plot_range((round(np.min(sample)), round(np.max(sample))), ybins)
    plot.set_yticks(yrange, labels=ybinlabels if ybinlabels else [f'${i}$' for i in range(len(yrange))])

    # Plot appearance
    plot.tick_params(axis='both', which='major', labelsize=15)
    plot.set_frame_on(False)
    plot.grid(grid, axis='y')
    plot.set_xlabel(xlabel, fontsize=20)
    plot.set_ylabel(ylabel, fontsize=20)
    plot.set_title(title)

# Plot waveform of an audio file
def spec_plot(plot, sample, sr, interval, nfft=2048):
    f, t, s = spectrogram(sample, sr, axis=0, nfft=nfft)
    plot.pcolormesh(t, f, 10.0*np.log10(s), shading="auto")
    plot.locator_params(axis='x', nbins=interval*2)
    plot.set_xlabel('time (s)')
    freq_range = range(0, sr//2, 1000*interval)
    plot.set_yticks([i for i in freq_range], [f'{i//1000}' for i in freq_range])
    plot.set_ylabel('Frequency (kHz)')
    plot.set_title('Spectrogram')

def spec3d_plot(plot, sample, sr, interval, nfft=2048):
    f, t, s = spectrogram(sample, sr, axis=0, nfft=nfft)
    plot.plot_surface(f[:, None], t[None, :], 10.0*np.log(s), cmap=cm.viridis)
    plot.set_title('3D Spectrogram')
    freq_range = range(0, sr//2, 1000*interval)
    plot.set_xticks([i for i in freq_range], [f'{i//1000}' for i in freq_range])
    plot.set_xlabel('Frequency (kHz)')
    plot.set_ylabel('time(s)')


# def audioplot(sample, sr):

#     fig = plt.figure()

#     ax1 = fig.add_subplot(1,3,1); ax1.set_yticks([])
#     ax2 = fig.add_subplot(1,3,2)
#     ax3 = fig.add_subplot(1,3,3, projection='3d')
#     fig.set_size_inches(12, 6)
#     fig.suptitle("Chopin Op.28 No.1")

#     wave_plot(ax1, sample1, sr1, 5)
#     spec_plot(ax2, sample1, sr1, 5)
#     spec3d_plot(ax3, sample1, sr1, 5)
#     sm = cm.ScalarMappable(cmap=cm.viridis)
#     fig.colorbar(sm, ax=ax3, pad=0.15)
#     fig.tight_layout(pad=2.0)
#     plt.show()

# if __name__ == '__main__':
#     sr1, sample1 = wavread('./reunion.wav')
#     sample1 = np.sum(sample1, axis=1)
#     audioplot(sample1, sr1)