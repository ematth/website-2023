import matplotlib.pyplot as plt
from audio1 import make_x_and_y
x, y = make_x_and_y(n=1000)
fig, ax = plt.subplots()
ax.scatter(x, y)
display(fig, target="plot")