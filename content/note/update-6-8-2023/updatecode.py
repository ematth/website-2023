import numpy as np
from matplotlib import pyplot as plt
from scipy.io.wavfile import read

def wavread(path):
    sr, s = read(path)
    return sr, s.astype('float32')/32768

from scipy import fft
# STFT Function
DFT_SIZE = 4096
HOP_SIZE = 128
WINDOW = np.hanning(DFT_SIZE)
def stft( input_sound, dft_size, hop_size, zero_pad=0, window=WINDOW):
    frames = []
    # zero-padding for equally sized frames
    input_sound = np.append(input_sound, np.zeros(len(input_sound) % dft_size))

    for i in range(0, len(input_sound) - dft_size, hop_size):
        frame = input_sound[i : i + dft_size] * window
        frames.append(frame)

    spectrogram = np.array([(fft.rfft(f, dft_size + zero_pad)) for f in frames])
    # Return a complex-valued spectrogram (frequencies x time)
    return spectrogram

def spectrogram(plot, sample, sr, title="Spectrogram", xLabel="Time (seconds)", yLabel="Frequency (KHz)"):
    nyq = sr/2
    from math import ceil
    stft_result = np.absolute(stft(sample, DFT_SIZE, HOP_SIZE, 0, WINDOW))**0.3
    x_axis = np.linspace(0, len(sample)/sr, stft_result.shape[0])
    y_cutoff = 5000
    y_axis = np.linspace(0, y_cutoff, int(y_cutoff // (nyq / stft_result.shape[1]) + 1))

    plot.pcolormesh(x_axis, y_axis, stft_result.T[:][:int(y_cutoff /(nyq / stft_result.shape[1]) + 1)], shading='auto');
    plot.set_title(title)
    plot.set_xlabel(xLabel) 
    plot.set_ylabel(yLabel)
    return plot


sr1, sample1 = wavread('./reunion.wav');
sample1 = sample1[:int(len(sample1)/4)]
figure, axs = plt.subplots(1,2); figure.set_size_inches(18, 8); figure.suptitle("Stayin' Alive")
axs[0].plot(sample1); axs[0].set_title("Waveform")
a = spectrogram(axs[1], sample1, sr1)
display(figure, target="plot"); 
