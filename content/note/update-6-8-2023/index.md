---
title: "Update: Python Compatability"
date: 2023-06-08
categories:
    - Updates
tags:
    - Python
draft: true
disable_comments: false
enable_python: true
---
<!-- Py-Config header -->
<head>
<py-config hidden src="pyconfig.toml">
[[fetch]]
files = ["./updatecode.py"]
</py-config>
</head>

<!-- Content -->

Hey Everyone,

My website now has support for Python code using [PyScript](https://pyscript.net/)! This means that, on top of formatting code for LaTeX formulas...

<div id="plot"></div>
<py-script src="updatecode.py"></py-script>

...my website can now show implementations of formulas and display and plot code output!




