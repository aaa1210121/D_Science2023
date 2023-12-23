import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.lines import Line2D

df = pd.read_csv("Pokemon_data.csv", delimiter=",", encoding="utf-8")
centroids = {
    0: (49.875000, 48.075000),
    1: (79.801887, 74.386792),
    2: (112.270833, 102.479167),
}
colors = {0: "magenta", 1: "green", 2: "cyan"}
plt.figure(figsize=(9, 8))

for i, color in colors.items():
    x = df.loc[df["cluster"] == i, "Attack"]
    y = df.loc[df["cluster"] == i, "Defense"]
    plt.scatter(x, y, c=color, alpha=0.4, s=10, label=f"Cluster {i}")
for j in centroids:
    c_x, c_y = centroids[j]
    plt.scatter(c_x, c_y, c=colors[j], marker="^", label=f"Cent. of cluster {j}")

plt.legend(loc="upper right", ncol=2)
plt.xlabel("Attack")
plt.ylabel("Defense")
plt.title("Scatter plot of pokemons")


plt.show()
