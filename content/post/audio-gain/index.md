---
title: "Amplitude"
date: '2023-07-03'
categories:
  - Audio Processing
tags:
  - Python
draft: true
disable_comments: true
enable_python: false
---

# Amplitude

The **amplitude** of a sound is physically defined as the amount of displacement produced by sound waves onto air particles. From the listener's point of view, this variable represents the "volume" of the sound.

$$S(t) = A\sin(\omega t + \phi)$$


Given a sinusoidal function, we define $A$ to be our peak amplitude, or the highest volume that our sound reaches. That is, $\forall t \in \Reals, \space x(t) \in [-A, A] $, (for all inputs $t$, representing time in our sinusoidal function, $x(t)$ will always be between and include $-A$ and $A$).

We can define the amplitude value $A$ in one of two ways:

1. as a constant $a \in \Reals$, where the volume remains the same for all $t$.

2. as a function $A(t)$, where $t\in\Reals$, and the volume can change over time.

Using amplitude as a function of time, we can freely define how sound is outputted over time. For example, suppose we want a sample $S$ that is $n$ seconds long to fade in over the course of $m$ seconds. We can define $A(t)$ as

$$A(t) = \begin{cases} \frac{t}{m} && t \lt m \\\\ 1 && m \le t \le n\end{cases}$$

where $A(t)$ is a *piecewise function* with two parts: in the first part, $A(t)$ linearly increases from $0$ to $1$ as $t$ approaches $m$; in the second part, $A(t)$ is a constant $1$ for the remainder of the function.

Similarly, we can define a function which fades out a sound for the last $m$ seconds as

$$A(t) = \begin{cases} 1 && t \le n - m \\\\ \frac{n - t}{m} && n - m \lt t \le n\end{cases}$$

where $A(t)$ is constant for $t\in [0, n-m)$ and linearly decreasing for $t\in (n-m, n]$.

Lastly, we can combine both filters into a single piecewise function, giving us the effects of both:

$$A(t) = \begin{cases} \frac{t}{m} && t \lt m \\\\ 1 && m \le t \le n - m \\\\ \frac{n - t}{m} && n - m \lt t \le n\end{cases}$$

<hr>

# Units

In practical application, it is better to define amplitude in some physical unit of loudness rather than just an arbitrary unit. Amplitude is commonly define in terms of **Decibels (dB)**, and the unit conversion is

$$\text{dB}(t) = \log10(\frac{A(t)}{|A_{\text{ref}}|})$$

where $|A_{\text{ref}}|$ is the greatest amplitude encountered in the entire sound. This function attempts to scale all amplitude values to the acceptable hearing range of $(-\infty, 0] \text{ dB}$, though that doesn't mean that values above $0 \text{ dB}$ aren't possible. Any values above $0 \text{ dB}$ represent undesirably loud values (which should be mitigated at all times, in order to protect your hearing and your audio equipment.)

For a practical example, suppose a sound $S$, normalized to amplitude values in the range $A(t)\in[-1.0, 1.0]$, contains some values that are too loud for normal listening. If we want a cutoff of $c = 0.8$ applied to the entire sound, we can substitute $A$ for

  $$A_\text{cutoff}(t) = \begin{cases} c && A(t) \ge c \\\\ A(t) && \text{otherwise}\end{cases}$$

which will "plateau" any values above $c$, essentially rescaling amplitude while maintaining the loudness of existing values in our sound.

<!-- # References

- [Global JOS Index: Amplitude](https://ccrma.stanford.edu/~jos/filters/Units.html#19668) -->