---
title: LaTeX for Note-Taking
date: 2023-06-03
author: Evan Matthews
categories:
    - Coding
tags:
    - markdown
    - latex
draft: false
---

# $\LaTeX$

LaTeX, pronounced "lah-tech" or "lay-tech", is a typesetting system based on the TeX language. It was developed in 1985 by American computer scientist Leslie Lamport, who wrote the package due to his frequent use of shortcuts for mathematical and scientific symbols in his own writing. Since then, it has become a staple in the world of academia as one of the premier document-writing tools with numerous integrations and extensions to the LaTeX package.

In this blog, **I'd like to introduce LaTeX as a useful tool for anyone looking improve their notes.** I first got into taking my notes in LaTeX back in my sophomore year of undergrad when a friend recommended I use [Notion](https://www.notion.so/) for organizing my schedule and college coursework. Since then, I've taken notes on everything from MATH 257: Linear Algebra with Computational Applications, to CS 374: Introduction to Algorithms & Models of Computation, and everything in between. This page should hopefully serve as a introductory resource to the language.

<hr>

# The Basics

Here's all the LaTeX symbols you'll need start writing expressions:

- `$ expressions $` -> wrapped in **single dollar-signs** for "inline" math mode. These can be written alongside normal lines of text $\text{like this: f(x) = mx + b }$, then return to normal text.

- `$$ expressions $$` -> **double dollar-signs** for "display" math mode, making them stand out as something important with respect to the document's material:

    $$\int_{0}^{5} x^2 dx \ne 10...\quad \int_{0}^{5} x^2 dx = \frac{x^3}{3}\Biggr|_0^5 = \frac{(125)}{3} - \frac{(0)}{3} = \frac{125}{3} = 41.\bar{6} \approx 41.6667$$

    > Note: while **$$** notation is still the go-to for display math mode, a number of tools, including the TeX editor and Overleaf, now recommend using **`[\ ... \]`** as delimiters. This is the standard set by LaTeX itself, while the use of dollar signs and double dollar signs remains a standard set by TeX.  

- `\keyword` -> the **backslash** (`\`) is used to indicate keywords in the LaTeX package.

    -   `"\alpha, \beta, \gamma, \delta..."` ->  $ "\alpha, \beta, \gamma, \delta..."$

- `\bar{(36 + b)}` -> **curly brackets** (`{}`) are used to indicate grouping for expressions.

    -   `\overline(36+b)` -> $\overline(36+b)$ ❌

    -   `\overline{(36+b)}` -> $\overline{(36+b)}$ ✅

- `x_{1}, y^{2}` -> the **underscore** (`_`) and **caret** (`^`) are used to indicate subscript (*slightly below*) and superscript (*slightly above*), respectively. Some expressions, like `\frac` (*fraction*) and `\int` (*integral*), use these characters to indicate what is placed above and below the expression.

    -   `x_{1}, y^{2}` -> $x_{1},\space y^{2}$

    -   `\frac{A}{B} + 5, \int_{A}^{B} c + 3 dc` -> $\frac{A}{B} + 5,\quad \int_{A}^{B} c + 3 \space dc$

- `\begin{keyword} ... \end{keyword}` -> there are a number of keywords used by **`\begin`** for aligning or formatting expressions within your document. In these types of expressions, **ampersand** (`&`) splits expressions by column, and **double-backslash** (`\\`) splits expression by row. There's a lot you can do with this, especially if you're working with matrices.

    -   `\begin{bmatrix} 
        1 & 2 & 3 \\
        a & b & c
    \end{bmatrix}` -> 
    $\begin{bmatrix} 
        1 & 2 & 3 \\\\
        a & b & c
    \end{bmatrix}$

> Note: backslash (\\) is often used as an "escape character" in some tools, meaning that some **programs won't be able to render single backslashes.** To circumvent this, you may need to type single backslashes as '\\' and double backslashes as `\\\\`, which will allow it to render as \\\\ for `\begin-\end` formatting.

<hr>

# Where can I start using LaTeX?

There are several ways to start writing and exporting documents with LaTeX:

<img src="markdown.png" style="max-width:10%;min-width:40px;float:right;" alt="Markdown logo" />

- **The easiest way to start:** Markdown documents support the use of embedded graphics and LaTeX formulas. Just open a new .md file on your [IDE](https://en.wikipedia.org/wiki/Integrated_development_environment) of your choosing, and starting typing!

<img src="notion.png" style="max-width:10%;min-width:30px;float:right;" alt="Overleaf logo" />

- **Another easier way:** As I've mentioned earlier, [Notion](https://www.notion.so) is a fantastic free organizational webapp with support for Markdown and LaTeX. If you're already used to typing your notes and are in the need for an organizational tool, then Notion will feel right at home.

<img src="overleaf.png" style="max-width:10%;min-width:30px;float:right;" alt="Overleaf logo" />

- **Less easier, but more robust ways:** I may have lied to you about how much formatting LaTeX can actually encompass. However, my methodology has reasoning: LaTeX/TeX are capable of organizing and formatting entire pages and finer details such as document types, metadata, titles, headers and footers, along with what I've already described. If you're digging into more complex uses of LaTeX or writing scientific/academic papers, then TeX editors such as [Overleaf](https://www.overleaf.com/), [TeXshop](https://pages.uoregon.edu/koch/texshop/) and [TeXstudio](https://www.texstudio.org/) might better suit your needs. I chose not to discuss the document-related functionality as to not scare anyone away from using LaTeX.

<hr>

# Easy to learn, hard to master

Much like programming, note-taking in LaTeX can seem pretty difficult at first. The number of specific keywords to memorize combined with unique symbols and parentheses/bracket-grouping makes it difficult to type rather quickly. I discovered this very quickly when I found myself keeping multiple LaTeX cheat-sheet tabs open while I typed my notes. And while I can say that I still don't know all the Greek letters by memory, I believe that forcing myself to type LaTeX in realtime helped both my typing accuracy and my ability to take worthwhile notes. 

$$P(A\mid B) = \frac{P(B \mid A)\cdot P(A)}{P(B)}$$

$$E[X] = \sum_x P(X = x)\cdot x$$

<hr>

# Examples

I'll add some typed-out examples here very soon 😉

<hr>

# References

- Britannica, The Editors of Encyclopaedia. "LaTeX". Encyclopedia Britannica, 17 Mar. 2023, https://www.britannica.com/technology/LaTeX-computer-programming-language.

- Overleaf, the Online LaTeX Editor. “Learn LaTeX in 30 Minutes - Overleaf, Online LaTeX Editor.” Overleaf.com, 2014, www.overleaf.com/learn/latex/Learn_LaTeX_in_30_minutes.

<hr>

‌