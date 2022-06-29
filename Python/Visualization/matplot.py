import matplotlib.pyplot as plt

fig1 = plt.figure("Histogram")

ax = fig1.add_subplot(
    2, 2, 1
)  # divides vertically and horizontally by 2, then adds to the 1st spot
ax.hist(
    [10, 20, 23, 35, 45, 60, 33, 22, 56, 34, 28, 40, 41],
    bins=20,
    facecolor="g",
    density=True,
    stacked=False,
)
plt.title("Distribution1")
ax1 = fig1.add_subplot(
    2, 2, 4
)  # divides vertically and horizontally by 2; then adds to the 4th spot
ax1.hist(
    [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13],
    bins=78,
    facecolor="g",
    density=False,
    stacked=True,
)
plt.title("Distribution2")
plt.xlabel("Range")
plt.ylabel("Amount")
# plt.show()

# fig2 = plt.figure("Box-plot")
ax2 = fig1.add_subplot(
    3, 2, 2
)  # divides vertically by 3 and horizontally by 2, then adds to the 2nd spot
plt.title("Box-Plot")
ax2.boxplot([10, 20, 23, 35, 45, 60, 33, 22, 56, 34, 28, 40, 41])
# plt.show()

fig3 = plt.figure("Bar")
ax3 = fig1.add_subplot(3, 3, 7)  # dikeyde ve yatayda 3'e bölüp 7.bölgeye atama
ax3.set_xlabel("X")
ax3.set_ylabel("T")
ax3.set_title("Bars")
ax3.bar([0, 1, 2, 3], [5, 10, 15, 5], [0.5, 1, 1.3, 1], color=["b", "r"])
# plt.show()

fig4 = plt.figure("Line")
ax4 = fig4.add_subplot(1, 1, 1)
ax4.set_xlim([0, 5])
ax4.set_ylim([0, 100])
ax4.set_xlabel("Mode")
ax4.set_ylabel("Average Time")
ax4.set_title("PAPI_DATA")
ax4.plot(
    [0, 1, 2, 3, 4, 5],
    [65.957, 60.667, 60.750, 64.317, 85.960, 91.7],
    "blue",
    label="N=2048, int32",
)
ax4.plot(
    [0, 1, 2, 3, 4, 5],
    [62.553, 61.827, 62.017, 65.177, 85.567, 85.563],
    "gray",
    label="N=2048, int64",
)
ax4.plot(
    [0, 1, 2, 3, 4, 5],
    [7.78, 7.74, 7.743, 8.08, 9.417, 9.423],
    "red",
    label="N=1024, int32",
)
ax4.plot(
    [0, 1, 2, 3, 4, 5],
    [22.031, 32.167, 33.943, 63.21, 62.11, 72.834],
    "orange",
    label="N=1526,int64",
)
ax4.legend(loc="upper left")
ticks_x = [i for i in range(0, 6)]
mode = {"Mode": ["ijk", "ikj", "jik", "jki", "kij", "kji"]}
# b_width = 0.5
plt.xticks(ticks_x, mode["Mode"])
ticks_y = [7.74, 61.827, 85.960, 91.7, 22.031, 32.167, 72.834]
plt.yticks(ticks_y)
plt.ylim([0.0, float(max(ticks_y) + 5)])
plt.xlim([min(ticks_x) - 0.5, max(ticks_x) + 0.5])
# plt.show()

data = {
    "Player": ["Wade", "James", "Bryant", "Carter"],
    "First": [10, 10, 8, 12],
    "Second": [12, 8, 13, 9],
    "Third": [15, 12, 8, 8],
    "Fourth": [18, 20, 15, 8],
}
fig5 = plt.figure("Stacked bar")
ax5 = fig5.add_subplot(1, 1, 1)
bar_width = 0.5
bars = [i + 1 for i in range(len(data["First"]))]
ticks = [i for i in bars]
ax5.bar(bars, data["First"], width=bar_width, label="First Quarter", color="#AA5439")
ax5.bar(
    bars,
    data["Second"],
    width=bar_width,
    bottom=data["First"],
    label="Second Quarter",
    color="#FFD600",
)
ax5.bar(
    bars,
    data["Third"],
    width=bar_width,
    bottom=[i + j for i, j in zip(data["First"], data["Second"])],
    label="Third Quarter",
    color="#FF9200",
)
ax5.bar(
    bars,
    data["Fourth"],
    width=bar_width,
    bottom=[i + j + k for i, j, k in zip(data["First"], data["Second"], data["Third"])],
    label="Fourth Quarter",
    color="r",
)

plt.xticks(ticks, data["Player"])
ax5.set_xlabel("Total")
ax5.set_ylabel("Player")
ax5.legend(loc="upper right")
plt.xlim([min(ticks) - bar_width, max(ticks) + bar_width])
plt.show()
