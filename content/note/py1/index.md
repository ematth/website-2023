---
title: Cool Python tidbits I enjoy using
date: 2024-02-16
author: Evan Matthews
categories:
    - Coding
tags:
    - python
draft: false
---

# Semicolons

Languages such as Java and C/C++ used a *terminator* to indicate the end of a line of code- most often the *semicolon* ( ; ). While this is not a mandatory feature for Python, you can still use semicolons as line separators. I personally use semicolons to make the most out of horizontal space in my code by combing initialization lines or similar expressions.

<table>
<tr>
<td>

```python
a = 1
b = 3.14
c = 'statement'
d = False
```

<td>
<td>

```python
a = 1; b = 3.14 # numbers
c = 'statement' # strings
d = False # bools
```

<td>
</tr>
</table>

<hr>

# Ternary Operator

Have you ever felt like some if-else cases appear to use too many lines?

```python
x = 3; y = 4
if x < y:
    return 0
else:
    return 1
```

Enter the *ternary operator*, a one-line method of the form `a if b else c`, where `b` is your condition, 
`a` is your expression for the condition returning true, and `c` is the value passed is the condition returns false.

```python 
x = 3; y = 4
z = 0 if x < y else 1
```

Ternary operations can also be used as values inside other ternary operators!

```python
x = 3; y = 4
s = "equal" if x == y else "less than" if x < y else "greater than"
print(s)
```

<hr>

# Type Hints and Annotations

```python
def func(a: int, b: int = 1) -> int:
    return a + b - 5
```

```python
def func(a: "fun value", b: "also a fun value" = 1) -> "sum of fun values":
    return a + b - 5
```

You can access the annotations by calling `func.__annotations__`, which returns the list of annotations in order. 

<hr>

# Decorators

```python
def decorator(func):
    def wrapper(*args, **kwargs):
        # decorator function code
        pass
return wrapper(*args, **kwargs)

@decorator
def func(x):
    return x + 1
```

<hr>

# Colon-Equals Operator (:=)

Similar to equals (=), Colon-Equals (:=) allows you to assign values to variables, with the added benefit of being able to do this in expressions! This is especially helpful when you would otherwise calculate a value twice, (once for use in the expression, and once in the post-condition).

```python
def powers(x):
    # This list includes the value f(x) while assigning it to the variable y
    return [y := f(x), y**2, y**3, y**4]

```

<hr>

# The Integer Cache

Did you know that Python maintains a list of pre-defined objects for integers in the range [-5, 256]?
To everyone's surprise, this cache also comes with some quirks, especially if you do some comparisons at the edge of its range:

```python
>>> a = 1
>>> b = 1
>>> a is b
True

>>> a = 257
>>> b = 257
>>> a is b
False
```

... unless you run the assignments and expression in-line with semi-colons, in which case the comparison works outside of the integer cache range.

```python
>>> a = 257; b = 257; a is b
True
```

<hr>

# Zip and Enumerate

<hr>

# String multiplication

Strings in Python come with a lot of freedom compared to other programming langauges. There's a lot of cool
tricks that most programmers already take advantage of, (treating strings as list for indexing, string addition), but you can also perform *string multiplication*. This feature allows you to perform a large number of string additions more efficiently.

```python
string_3 = 'string_' * 3
print(string_3) # -> 'string_string_string' 
```

<hr>

# Built-in Import Easter eggs

There's a few built-in imports with fun Easter eggs for the truly curious...

`import this` -> prints 19 guiding principles for writing computer programs, by Tim Peters

`import antigravity` -> directly links to an XKCD comic.

<hr>