import concurrent.futures
import psutil
import threading
import time

start = time.perf_counter()


def do_something(seconds):
    print(f"Sleeping for {seconds} second(s)...")
    time.sleep(seconds)
    return f"Woke up after {seconds} second(s)..."


print(f"TOTAL CORES: {psutil.cpu_count(logical=False)}")
print(f"TOTAL THREADS: {psutil.cpu_count()}")

""" 
# Thread pooling in concurrent.futures
with concurrent.futures.ThreadPoolExecutor() as executor:
    secs = [5, 4, 3, 2, 1]
    # Executes every thread and yields outputs of each of them as it completes
    results = [executor.submit(do_something, sec) for sec in secs]
    for f in concurrent.futures.as_completed(results):
        print(f.result())

    # Executes every thread, and then prints all outputs together at the end
    results = executor.map(do_something, secs)
    for result in results:
        print(result)
"""
threads = []


# Classical thread pooling using the 'threading' module
for _ in range(5):
    t = threading.Thread(target=do_something, args=[1])
    t.start()
    threads.append(t)

for t in threads:
    t.join()

finish = time.perf_counter()

print(f"Finished in {round(finish-start, 2)} second(s)")
