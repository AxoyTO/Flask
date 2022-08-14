import matplotlib.pyplot as plt
import concurrent.futures
import time


def draw_serial(all_values):
    for i, value in enumerate(all_values, start=1):
        fig, ax = plt.subplots(1, 1, figsize=(10, 3))

        # remove all markers
        for line in ax.lines:
            line.set_marker(None)

        for axes in [ax]:  # remove all borders
            plt.setp(axes.get_xticklabels(), visible=False)
            plt.setp(axes.get_yticklabels(), visible=False)
            plt.setp(axes.get_xticklines(), visible=False)
            plt.setp(axes.get_yticklines(), visible=False)
            plt.setp(axes.spines.values(), visible=False)

        plt.plot(value, color='#4bc0c0', linewidth=6.0)

        # save
        fig.savefig(
            f'cointracker/static/img/sparkline{i}.png', transparent=True)
        plt.close()


def draw_parallel(all_values):
    with concurrent.futures.ProcessPoolExecutor() as executor:
        #executor.map(filter_image_multiprocessing, img_names)
        pass


def draw_sparkline(all_values):
    start = time.perf_counter()
    draw_serial(all_values)
    # draw_parallel(all_values)
    finish = time.perf_counter()
    print(f"Finished in {round(finish-start, 2)} second(s).")
