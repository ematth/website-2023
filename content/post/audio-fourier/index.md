---
title: "Fourier Transform"
date: '2023-07-04'
categories:
  - Audio Processing
tags:
  - Python
draft: true
disable_comments: true
enable_python: false
---

# Fourier Transform

The **Fourier Transform** is a transformation of a time-series function which returns a respective frequency-series function, or an equivalent function who takes a frequency $f$ as an input rather than a time $t$.

$$\hat{f}(\xi) = \int_{-\infty}^{\infty} f(t) e^{-i2\pi\xi t} dt$$

where $f(t)$ is the original function for our sound in terms of time $t$, and $\hat{f}(\xi)$ is an equivalent function in terms of frequency $\xi$. In essence, this function takes in a frequency and, across all time values t in f(t)- hence why we're integrating with respect to time- determines that frequency's *intensity*. For example, if we have a sound and want to know if the frequency A4 = 440 was used, we can compute $\hat{f}(440)$ to figure out whether or not there's a "peak" for this frequency, (hence it is exists in our sound.) 

However, this formula is much more complicated then a summation over time series. For that, we'll need to understand how $e^{-i2\pi\xi t}$ and the complex plane plays into the Fourier Transform.

<hr>


# References

- 3Blue1Brown: "But what is the Fourier Transform? A visual introduction."
    https://www.youtube.com/watch?v=spUNpyF58BY&ab_channel=3Blue1Brown

- Julius O. Smith: "FOURIER TRANSFORMS FOR CONTINUOUS/DISCRETE TIME/FREQUENCY"
    https://www.dsprelated.com/freebooks/sasp/Fourier_Transforms_Continuous_Discrete_Time_Frequency.html#chap:fourcases

- Wikipedia: "Fourier Transform"
    https://en.wikipedia.org/wiki/Fourier_transform