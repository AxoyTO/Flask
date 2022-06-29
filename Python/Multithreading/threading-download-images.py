import concurrent.futures
import threading
import psutil
import requests
import time


def serial(img_urls):
    print("Executing code serial.")
    for img_url in img_urls:
        print("Downloading image...", end=" ")
        img_bytes = requests.get(img_url).content
        img_name = img_url.split("/")[3]
        img_name = f"{img_name}.jpg"
        with open(img_name, "wb") as img_file:
            img_file.write(img_bytes)
            print(f"100% Downloaded")


def download_img(img_url):
    print(f"{threading.current_thread().name} started downloading")
    img_bytes = requests.get(img_url).content
    img_name = img_url.split("/")[3]
    img_name = f"{img_name}.jpg"
    with open(img_name, "wb") as img_file:
        img_file.write(img_bytes)
        print(f"{img_name} is downloaded by {threading.current_thread().name}...")


def threading_pool(img_urls):
    print("Executing code in parallel(threading module)")
    threads = [
        threading.Thread(target=download_img, args=[img_url]) for img_url in img_urls
    ]

    k = 1
    for thread in threads:
        thread.name = "Thread %d" % k
        k += 1
        thread.start()

    for thread in threads:
        thread.join()


def parallel_pool(img_urls):
    print("Executing code in parallel(concurrent module)")
    with concurrent.futures.ThreadPoolExecutor() as executor:
        executor.map(download_img, img_urls)


if __name__ == "__main__":
    start = time.perf_counter()

    img_urls = [
        "https://images.unsplash.com/photo-1516117172878-fd2c41f4a759",
        "https://images.unsplash.com/photo-1532009324734-20a7a5813719",
        "https://images.unsplash.com/photo-1524429656589-6633a470097c",
        "https://images.unsplash.com/photo-1530224264768-7ff8c1789d79",
        "https://images.unsplash.com/photo-1564135624576-c5c88640f235",
        "https://images.unsplash.com/photo-1541698444083-023c97d3f4b6",
        "https://images.unsplash.com/photo-1522364723953-452d3431c267",
        "https://images.unsplash.com/photo-1513938709626-033611b8cc03",
        "https://images.unsplash.com/photo-1507143550189-fed454f93097",
        "https://images.unsplash.com/photo-1493976040374-85c8e12f0c0e",
        "https://images.unsplash.com/photo-1504198453319-5ce911bafcde",
        "https://images.unsplash.com/photo-1530122037265-a5f1f91d3b99",
        "https://images.unsplash.com/photo-1516972810927-80185027ca84",
        "https://images.unsplash.com/photo-1550439062-609e1531270e",
        "https://images.unsplash.com/photo-1549692520-acc6669e2f0c",
    ]

    # serial(img_urls)
    # threading_pool(img_urls)
    parallel_pool(img_urls)

    finish = time.perf_counter()
    print(f"Finished in {round(finish-start, 2)} second(s)")
