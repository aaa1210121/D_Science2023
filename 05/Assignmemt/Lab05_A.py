# 05-A
import matplotlib.pyplot as plt
import numpy as np

x = np.arange(6)
y = [13, 5, 7, 14, 10, 12]
X_Month = ["Jun", "Feb", "March", "April", "May", "June"]
plt.xticks(x, X_Month)
plt.yticks(np.arange(0, 20, 5))
plt.xlim(0, 5)
plt.ylim(0, 15)

plt.xlabel("Month", fontsize=14)
plt.ylabel("Monthly Sales ($1000)", fontsize=14)
plt.title("Print Sales for January to June, 2022", fontsize=16)
plt.plot(x, y, "-co", linewidth=2, markerfacecolor="None", markersize=10, clip_on=False)
plt.show()
