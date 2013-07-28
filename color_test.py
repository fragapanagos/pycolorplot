import matplotlib.pyplot as plt
from colorgen import ColorGenerator 
import numpy as np

NCURVES = 8
curves = np.arange(64)
curves = np.reshape(curves, (-1, NCURVES))

cgen = ColorGenerator('red')

fig = plt.figure()
ax = fig.add_subplot(111)
ax.set_color_cycle(cgen.get_color_list(NCURVES))
ax.plot(curves)

fig = plt.figure()
plt.pcolor(curves, cmap=cgen.get_color_map())
plt.colorbar()

plt.show()

