import concurrent.futures
import time
import sys
import psutil
import requests
from PIL import Image, ImageFilter
import os
import multiprocessing

DOWNLOAD = 1


def download_images_serial(img_urls):
    print(f"Started downloading in serial...")
    img_names = []
    for img_url in img_urls:
        img_bytes = requests.get(img_url).content
        img_name = img_url.split("/")[3]
        img_name = f"{img_name}.jpg"
        print(f"Downloading {img_name}...", end=" ")
        img_names.append(img_name)
        with open(img_name, "wb") as img_file:
            img_file.write(img_bytes)
            print(f"100% Downloaded")
    return img_names


def download_images_parallel(img_url):
    print(f"{multiprocessing.current_process().name} started downloading...", end="")
    img_bytes = requests.get(img_url).content
    img_name = img_url.split("/")[3]
    img_name = f"{img_name}.jpg"
    with open(img_name, "wb") as img_file:
        img_file.write(img_bytes)
        print(f"100% Downloaded")
    return img_name


def download_concurrent_futures(img_urls):
    with concurrent.futures.ProcessPoolExecutor() as executor:
        results = executor.map(download_images_parallel, img_urls)
        return results


def process_pool(img_urls):
    with multiprocessing.Pool(psutil.cpu_count(logical=False)) as p:
        results = p.map(download_images_parallel, img_urls)
        return results
    """  
    processes = [
        multiprocessing.Process(target=download_images_parallel, args=[img_url])
        for img_url in img_urls
    ]
    k = 1
    for p in processes:
        p.name = f"Process {k}"
        k += 1
        p.start()

    for p in processes:
        p.join() 
    """


def filter_image_serial(img_names):
    size = (1200, 1200)
    for img_name in img_names:
        img = Image.open(img_name)
        img = img.filter(ImageFilter.GaussianBlur(15))
        img.thumbnail(size)
        try:
            img.save(f"processed/{img_name}")
        except FileNotFoundError:
            os.system("mkdir processed")
            img.save(f"processed/{img_name}")
        print(f"{img_name} was processed...")


def filter_image_multiprocessing(img_name):
    print(f"{multiprocessing.current_process().name} -> ", end="")
    size = (1200, 1200)
    img = Image.open(img_name)
    img = img.filter(ImageFilter.GaussianBlur(15))
    img.thumbnail(size)
    try:
        img.save(f"processed/{img_name}")
    except FileNotFoundError:
        os.system("mkdir processed")
        img.save(f"processed/{img_name}")
    print(f"{img_name} was processed...")


def filter_multiprocessing(img_names):
    processes = [
        multiprocessing.Process(target=filter_image_multiprocessing, args=[img_name])
        for img_name in img_names
    ]
    for index, p in enumerate(processes, start=1):
        p.name = f"Process {index}"
        p.start()
    for p in processes:
        p.join()


def filter_concurrent_futures(img_names):
    with concurrent.futures.ProcessPoolExecutor() as executor:
        executor.map(filter_image_multiprocessing, img_names)


if __name__ == "__main__":
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

    img_names = []

    if DOWNLOAD == 0:
        t1 = time.perf_counter()
        # img_names = download_images_serial(img_urls)
        # img_names = process_pool(img_urls)
        img_names = download_concurrent_futures(img_urls)
        t2 = time.perf_counter()
        print(f"Finished downloading in {t2-t1} second(s).")
    else:
        img_names = [img_url.split("/") for img_url in img_urls]
        img_names = sum(img_names, [])
        img_names = [
            img_name + ".jpg" for img_name in img_names if img_name.startswith("ph")
        ]

    t1 = time.perf_counter()
    # filter_image_serial(img_names)
    # filter_multiprocessing(img_names)
    filter_concurrent_futures(img_names)
    t2 = time.perf_counter()
    print(f"Finished filtering in {t2-t1} second(s).")
