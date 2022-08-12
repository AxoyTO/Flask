import matplotlib.pyplot as plt


def draw_sparkline():
    # create some random data
    x = np.cumsum(np.random.rand(1000) - 0.5)

    # plot it
    fig, ax = plt.subplots(1, 1, figsize=(10, 3))
    plt.plot(x, color='k')
    plt.plot(len(x) - 1, x[-1], color='r', marker='o')

    # remove all the axes
    for k, v in ax.spines.items():
        v.set_visible(False)
    ax.set_xticks([])
    ax.set_yticks([])

    # show it
    plt.show()
