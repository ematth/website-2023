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

$$x(t) = A\sin(\omega t + \phi)$$


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


<!-- # References

- [Global JOS Index: Amplitude](https://ccrma.stanford.edu/~jos/filters/Units.html#19668) -->