---
title: "Update: Python Compatability"
date: 2023-06-08
categories:
    - Updates
tags:
    - Python
draft: false
disable_comments: false
enable_python: true
---
<!-- Py-Config header -->
<head>
<py-config hidden src="pyconfig.toml">
[[fetch]]
files = ["./updatecode.py", "./reunion.wav"]
</py-config>
</head>

<!-- Content -->

Hey everyone,

My website now has support for Python code using [PyScript](https://pyscript.net/)! This means that, on top of formatting code for LaTeX formulas...

```python
    sr1, sample1 = wavread('./reunion.wav')
    sample1 = sample1[:int(len(sample1)/4)]
    figure, axs = plt.subplots(1,2)
    figure.set_size_inches(18, 8)
    figure.suptitle("Chopin Op.28 No. 1 \"Reunion\"")
    axs[0].plot(sample1); axs[0].set_title("Waveform")
    a = spectrogram(axs[1], sample1, sr1)
    display(figure, target="plot")
```

<audio controls>
<source alt="Chopin's Op. 28 No. 1" src="reunion.wav" type="audio/wav">
</audio>

<div id="plot"></div>
<py-script src="updatecode.py"></py-script>

...my website can now show implementations of formulas and display and plot code output! I hope to start using this feature for my future **Audio Processing** articles by directly implementing Python code into the page. However, if it starts to take too long to load, I might just go back to the tried and true method of uploading screenshots of graphs.

*-Evan*




