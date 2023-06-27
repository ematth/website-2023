---
title: "Waveform and Audio Basics"
date: 2023-06-27
categories:
    - Audio Processing
tags:
    - Python
draft: true
disable_comments: true
enable_python: false
---
<!-- Py-Config header -->
<head>
<py-config hidden src="pyconfig.toml">
[[fetch]]
files = ["./audio1.py"]
</py-config>
</head>

<!-- Content -->

# Introduction

Understanding the mathematical logic behind sound- how certain factors effect what we hear and how we hear it- is the first step into audio signal processing. You should likely understand some basics about trigonometry and periodic functions to best understand the content. This article will run through basic vocabulary, explain how sound is processed and stored digitally, and demonstrate basic audio processing techniques in Python.

<div id="plot" style="width:100%;padding:0px;"></div>

<hr>

# Waveforms

**Sound** is the displacement of air particles over time. We can describe the displacement of air particles graphically as a **waveform**, which plots the displacement of particles (called *amplitude*) in terms of time $t$. Take, for example, a simple sine function $f(t) = \alpha\cdot \sin(t)$, where $\sin(t)$ *oscillates* (moves in a constant range indefinitely), and $\alpha$ is a constant defining the upper and lower bounds of the function's amplitude. Below, I've plotted one complete **wavelength** (the length of one complete cycle), four complete cycles, and a much larger number of cycles. 

<img src="plot1.png" alt="plot of a simple sine function">

Although all sounds can be defined as a collection of sine waves, the human ear doesn't *hear* the individual **samples**, or cycles of a oscillating function. Instead, samples are played at such a high rate that the human ear can't audibly pinpoint specific samples. Instead, the samples combine the into one cohesive sound. Standards for **sample rate**, or the number of samples played per second in **Hertz (Hz)**, can range from 44,100 Hz to nearly 192,000 Hz in professional studios.

If human hearing only spans the range of 20 Hz - 20,000 Hz, why do we use much higher sample rates? The answer is that, in order to process an audio signal without losing information, we need need to use a sample rate that is at least twice as big as the highest frequency sound in the signal. This is known as the **Nyquist Limit**, and is the reason signals typically use a sample rate in the 40-48 kHz range. And while human hearing isn't capable of capturing anything beyond this range, music producers often use even higher sample rates as a means of capturing higher-resolution audio.

<hr>

# Basic Waves and Sounds

All audio signals can be described as some manipulation of sine waves, through the processes of **additive and subtractive synthesis.** Essentially, this allows us to create whatever sounds we like by combining and manipulating simple sines waves to form much more complex sounds. Here's a plot of a couple of frames versus a much larger snippet of "Stay With Me" by Miki Matsubara.

<img src="plot2.png" alt="plot of an excerpt from 'Stay With Me' by Miki Matsubara">

<audio controls>
<source alt="Miki Matsubara - Stay With Me" src="staywithme.wav" type="audio/wav">
</audio>

From here, we can introduce more concepts related to audio signals. For example, sound can depend on the **number of channels** used to output an audio signal. You're likely used to hearing **stereophonic sound**, where a left and right channel output specific audio signals to the left and right side of a listening body. 

<img src="plot3.png">


This allows for some neat tricks, such as hearing something coming from one side of you and not another. In a similar vain, **monophonic sound** uses one channel for all audio, meaning that you'll hear the same sound across all speakers, even if you're wearing a pair of headphones or sitting in a multi-channel studio.

Another major concept to keep in mind is that, considering that all sounds are a combination of periodic functions, the process of editing sound is a matter of *transforming a sound's waveform mathematically* to make get a desired sound. As you read and run the provided code snippets, I highly suggest graphing and considering what sort of transformation you're applying to the waveform and how that changes the overall sound.

<hr>

# Audio Editing through Code

To start, in your Python development environment of choice, we'll import a couple important libraries:

```python3
import numpy as np
import matplotlib.pyplot as plt
from scipy.io.wavfile import read, write
```

**Numpy** is the go-to library for large, multi-dimensional arrays and contains a lot of powerful tools that we'll use to simplify our code on the mathematical side. **Matplotlib** is the standard Python library for representing data graphically, and we'll use *pyplot* to visualize our waveforms. Finally, **Scipy** is also a well-loved scientific computing library, and we'll import its *read* and *write* functions from the *io.wavfile* module to import .wav files.

> 💡 Plenty of other sound file types (mp3, aiff) and audio processing libraries (librosa) exist. While these are also worth checking out, it should be stated that .wav is the most common for audio processing.

With our necessary libraries imported, grab your favorite .wav sound file and load it with

```python3 
path = '/path/to/filename.wav'
sr, sample = read(path)
sample = sample.astype('float32')
```

where `sr` and `sample` are the sample rate and sample data of our sound, respectively. The last line uses `astype('float32')` to convert our data into the "float32" WAV format, which normalizes our data to the range [-1.0, 1.0]. There are also other type ranges which you can find the numpy dtypes to on the [scipy.io.wavfile.read documentation page](https://docs.scipy.org/doc/scipy/reference/generated/scipy.io.wavfile.read.html). 

> ⚠️ As I mentioned above about multi-channel sound, if you decided to use your own .wav file, your `sample` file likely contains more than one row, meaning it is a multi-channel sound file. For the time being, you can confirm this by printing `sample.shape` to check the number of rows, and convert this to a monophonic file by summing the rows together with `np.sum(sample, axis=1)`.

Without immediately discussing about periodic functions or other technical details, we can already do some basic audio processing. For example, we can grab sound snippets from the original sample with list splicing. The notation for python list splicing is `array[start:stop:step]`, where this variables represents the array in the range `[start, stop)` every `step` number of samples.

```python3
a = sample[0:3*sr] # Returns the first 3 seconds of the sound
b = sample[3*sr:] # Returns the last 3 seconds of the sound
c = sample[::2] # Returns every other sample in the array, (a terrible sound speed-up!)
```

