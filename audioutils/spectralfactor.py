import numpy as np
from matplotlib import pyplot as plt
from scipy import fft


# STFT Function
DFT_SIZE = 2048
HOP_SIZE = 128
WINDOW = np.hanning(DFT_SIZE)
def stft( input_sound, dft_size=DFT_SIZE, hop_size=HOP_SIZE, zero_pad=0, window=WINDOW):
    frames = []
    # zero-padding for equally sized frames
    input_sound = np.append(input_sound, np.zeros(len(input_sound) % dft_size))

    for i in range(0, len(input_sound) - dft_size, hop_size):
        frame = input_sound[i : i + dft_size] * window
        frames.append(frame)

    spectrogram = np.array([(fft.rfft(f, dft_size + zero_pad)) for f in frames], dtype=complex)
    # Return a complex-valued spectrogram (frequencies x time)
    return spectrogram 


# Get spectral components for the given sample
EPSILON = 1e-7
ITERATE = 100
def spectral_components(sample_stft, k):
    
    w = np.random.randn(sample_stft.shape[0], k) + 10; 
    h = np.random.randn(k, sample_stft.shape[1]) + 10
    
    for i in range(k):
        w[:,i] /= np.sum(w[:,i])
    for _ in range(ITERATE):
        v = sample_stft / (w @ h + EPSILON)
        h *= (w.T @ v)
        w *= (v @ h.T)
        for i in range(k):
            w[:,i] /= np.sum(w[:,i])

    return h, w