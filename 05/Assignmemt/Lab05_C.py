# 05-C
import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(0, 12.5, 1000)
𝑦 = np.sin(𝑥) + np.sin(3 * 𝑥)

plt.xlim(0, 14)
plt.xlabel("x-axis", c="#33FF00")

plt.xticks(np.arange(0, 15, 2), c="#33FF00")
plt.plot(x, y, "#FF00CC", linewidth=3)


ax = plt.subplot()
# ax.get_yaxis().set_visible(False)
ax.spines["bottom"].set_color("#33FF00")
ax.spines["top"].set_color("#33FF00")
ax.tick_params(axis="x", colors="#33FF00", direction="in")

ax.set_xticks(np.arange(2, 14, 2), minor=True)
ax.xaxis.grid(color="#33FF00")

y1 = -1
ax.axhline(y1, color="black")
y2 = -0.3
ax.axhline(y2, color="black")
y3 = 0.1
ax.axhline(y3, color="black")
y4 = 1
ax.axhline(y4, color="black")
y5 = [-1, -0.3, 0.1, 1]

text = ["Minimum", "Critical", "Collapse", "maximum"]
plt.yticks(y5)
ax.set_yticklabels(labels=text, color="black")
plt.show()
