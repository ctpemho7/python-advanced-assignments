import aiohttp
import asyncio
import argparse
from datetime import datetime
import os


async def download_image(session, url, save_path):
    """ Асинхронная задача для скачивания изображения """
    try:
        async with session.get(url) as response:
            if response.status == 200:
                data = await response.read()
                with open(save_path, 'wb+') as f:
                    f.write(data)
                print(f"[{datetime.now().time()}] Downloaded {save_path}")
            else:
                print(f"[{datetime.now().time()}] Failed to download {url}: HTTP {response.status}")
    except Exception as e:
        print(f"[{datetime.now().time()}] Error downloading {url}: {str(e)}")


async def download_images(url, num_images, output_dir):
    """ Собираем асинхронные задачи в один список """

    os.makedirs(output_dir, exist_ok=True)
    async with aiohttp.ClientSession() as session:
        tasks = []
        for i in range(num_images):
            filename = f"image_{i}.jpg"
            save_path = os.path.join(output_dir, filename)
            tasks.append(download_image(session, url, save_path))
        
        await asyncio.gather(*tasks)

if __name__ == "__main__":
    url = "https://random-image-pepebigotes.vercel.app/api/skeleton-random-image"
    
    parser = argparse.ArgumentParser(description='Асинхронное скачивание изображений.')
    parser.add_argument('num_images', type=int, help='Количество изображений')
    parser.add_argument('--url', type=str, default=url, help=f'Ссылка на сайт, который отдает картинки по HTTP-запросу. По умолчанию {url}')
    parser.add_argument('--output', type=str, default='downloads', help='Папка для загрузки (по умочанию: downloads)')
    
    args = parser.parse_args()
    
    asyncio.run(download_images(args.url, args.num_images, args.output))
    