import matplotlib.pyplot as plt

fig6 = plt.figure("Scatter")
ax5 = fig6.add_subplot(1, 1, 1)
# 1st param:x-axis
# 2nd param: y-axis
# 3rd param: bubble-width
# 4th param: color
ax5.scatter(
    [-1, 0, 2, 3, 5],
    [2, 1, 3, 0.5, 4],
    [120, 200, 300, 150, 30],
    ["r", "g", "b", "#BCDFF0", "#BB5500"],
)
# plt.show()

fig7 = plt.figure("Pie")
sizes = [50, 50, 44, 36]
labels = ["Wade", "James", "Kobe", "Carter"]
explode = (0.1, 0.1, 0, 0)
colors = ["r", "purple", "y", "b"]
plt.pie(
    sizes,
    explode=explode,
    labels=labels,
    colors=colors,
    autopct="%1.1f%%",
    shadow=True,
    startangle=140,
)
plt.axis("equal")
plt.show()
