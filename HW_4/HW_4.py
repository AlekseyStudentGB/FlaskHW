
import multiprocessing as mp
import threading
import time
import aiofiles
import requests
import asyncio as asy
import aiohttp as aio
from werkzeug.utils import secure_filename
import sys

threads = []
list_link = ['https://koshka.top/uploads/posts/2021-12/1639894342_27-koshka-top-p-kotiki-na-rabochii-29.jpg',
             'https://masyamba.ru/картинки-котят/52-милый-котенок.jpg',
             'https://koshka.top/uploads/posts/2021-12/1639894342_27-koshka-top-p-kotiki-na-rabochii-29.jpg',
             'https://masyamba.ru/картинки-котят/52-милый-котенок.jpg'
             ]


def download(link_img):
    s_time_load_file =time.time()
    response = requests.get(link_img, allow_redirects=True)
    file_name = secure_filename(link_img)
    with open(file_name, 'wb') as f:
        f.write(response.content)
    print(f'file {file_name:<100} download in {time.time()-s_time_load_file:.2f}')


async def download_async(link_img):
    file_name = secure_filename(link_img)
    s_time_load_file = time.time()
    async with aio.ClientSession() as session:
        async with session.get(link_img) as resp:
            f = await aiofiles.open(file_name, mode='wb')
            await f.write(await resp.read())
            await f.close()
            print(f'file {file_name:<100} download in {time.time()-s_time_load_file:.2f}')


async def main():
    tasks = []
    for link_img in list_link:
        task = asy.create_task(download_async(link_img))
        tasks.append(task)
    await asy.gather(*tasks)


if __name__ == '__main__':
    if len(sys.argv) > 1:
        list_link = []
        for i in range(1, len(sys.argv)):
            list_link.append(str(sys.argv[i]))
    s_time = time.time()
    for link in list_link:
        t = threading.Thread(target=download, args=[link])
        threads.append(t)
        t.start()
    for thread in threads:
        thread.join()
    print(f'общее время выполнения программы через модуль "threading" :{time.time() - s_time}', end='\n\n')
    s_time = time.time()
    for link in list_link:
        t = mp.Process(target=download, args=[link])
        threads.append(t)
        t.start()
    for thread in threads:
        thread.join()
    print(f'общее время выполнения программы через модуль "multiprocessing" :{time.time() - s_time}', end='\n\n')
    s_time = time.time()
    asy.run(main())
    print(f'общее время выполнения программы через модуль "asyncio" :{time.time() - s_time}', end='\n\n')
