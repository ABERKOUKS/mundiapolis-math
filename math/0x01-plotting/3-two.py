#!/usr/bin/env python3
import numpy as np
import matplotlib.pyplot as plt

x = np.arange(0, 21000, 1000)
r = np.log(0.5)
t1 = 5730
t2 = 1600
y1 = np.exp((r / t1) * x)
y2 = np.exp((r / t2) * x)

fig, ax = plt.subplots()
ax.set_xlabel('Time (years)')
ax.set_ylabel('Fraction Remaining')
fig.suptitle('Exponential Decay of Radioactive Elements')
ax.set(xlim=(0, 20000), ylim=(0,1))
line_labels=["C-14","Ra-226"]
ax.plot(x, y1, 'r--')
ax.plot(x, y2, 'g-')
ax.legend(   
           labels=line_labels,
           loc="upper right"   
           )
plt.show()
