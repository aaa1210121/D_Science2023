# 5-B
import matplotlib.pyplot as plt
import numpy as np

plt.xticks(np.arange(0, 0.6, 0.1))
plt.xlim(0, 0.5)
plt.yticks(np.arange(-1.5, 1.6, 0.5))
plt.ylim(-1.5, 1.5)
plt.xlabel("Time (μs)", weight="bold")
plt.ylabel(" $\it'Normalize'$ Signals", fontsize=14)
plt.title("In-Phase $\it(solid)$ and Quardrature $\it(dotted)$ Signals", fontsize=14)
x = np.linspace(0, 0.5, 60)

plt.plot(x, np.cos(np.pi / 0.1 * x), "-ok", markerfacecolor="None", clip_on=False)

plt.plot(x, np.cos(np.pi / 0.1 * x - np.pi / 2), "-*c", clip_on=False)

plt.text(0.19, 1.25, r"$\frac{\pi}{2}$  phase lag ")
plt.arrow(0.23, 1.1, 0.01, 0,  head_width=0.05  ,head_length=0.01, fc ='black')
plt.arrow(0.23, 1.1, -0.025, 0,  head_width=0.05 , head_length=0.01,fc ='black')

plt.show()
