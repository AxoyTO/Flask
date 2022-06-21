import time
import multiprocessing
import concurrent.futures
import psutil

start = time.perf_counter()


def do_something(sec):
    print(f"Sleeping for {sec} second(s)...")
    time.sleep(sec)
    print(f"Awaken from sleep after {sec}...")
    return f"Returned after sleeping for {sec}"


def serial():
    p1 = multiprocessing.Process(target=do_something, args=[1])
    p2 = multiprocessing.Process(target=do_something, args=[1])

    p1.start()
    p2.start()

    p1.join()
    p2.join()


def multiprocessing_pool():
    pool = []
    for _ in range(psutil.cpu_count(logical=False)):
        p = multiprocessing.Process(target=do_something, args=[_ + 1])
        p.start()
        pool.append(p)

    for p in pool:
        p.join()


def concurrent_futures_pool():
    with concurrent.futures.ProcessPoolExecutor() as executor:
        """
        f1 = executor.submit(do_something, 1)
        f2 = executor.submit(do_something, 1)
        print(f1.result())
        print(f2.result())
        """

        secs = [x for x in range(psutil.cpu_count(logical=False), 0, -1)]

        """
        results = [executor.submit(do_something, sec) for sec in secs]
        for f in concurrent.futures.as_completed(results):
            print(f.result())
        """

        results = executor.map(do_something, secs)
        for result in results:
            print(result)


if __name__ == "__main__":
    # serial()
    # multiprocessing_pool()
    concurrent_futures_pool()

    finish = time.perf_counter()
    print(f"Finished in {round(finish-start, 2)} second(s)")
