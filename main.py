import requests
from PIL import Image
import io
import random


API_KEY = 'JBuGtYcdod8udN03Io2XfuD5FejXbhYvwWUkwE2y'


def get_mars_image_url_from_nasa(rover):
    while True:
        param = {'api_key': API_KEY}
        sol = int(requests.get(f'https://api.nasa.gov/mars-photos/api/v1/rovers/{rover}/', params=param).json()['rover']['max_sol'])
        params = {'sol': sol, 'api_key': API_KEY}
        rover_url = f'https://api.nasa.gov/mars-photos/api/v1/rovers/{rover}/photos'
        with requests.get(rover_url, params=params) as resp:
            resp_dict = resp.json()
        if 'photos' not in resp_dict:
            raise Exception
        photos = resp_dict['photos']
        if not photos:
            continue
        return [photo['img_src'] for photo in photos]


def get_mars_photo(rover):
    images_urls = get_mars_image_url_from_nasa(rover)
    images = []
    for i, image_url in enumerate(images_urls):
        image_bytes = requests.get(image_url).content
        image = Image.open(io.BytesIO(image_bytes))
        images.append(image.resize((800, 600)))
        print(f'Photo {i + 1} in {image.size} has added...')
    gif = Image.new('RGB', (800, 600), (255, 255, 255))
    gif.save('mars.gif', 'GIF', append_images=images, loop=0, duration=300, save_all=True)
    print('Done!')


get_mars_photo('perseverance')
