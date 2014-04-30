import os
from multiprocessing import Pool
from PIL import Image
from time import time

SIZE = (75, 75)
SAVE_DIR = 'thumbs'

def get_image_paths(folder):
    return (os.path.join(folder, f) for f in os.listdir(folder) if 'jpg' in f)

def create_thumbnail(filename):
    im = Image.open(filename)
    im.thumbnail(SIZE, Image.ANTIALIAS)
    base, fname = os.path.split(filename)
    save_path = os.path.join(base, SAVE_DIR, fname)
    im.save(save_path)

folder = os.path.join(os.path.expanduser("~"), "Imágenes", "Wallpapers", "tothumbs")
if not os.path.exists(os.path.join(folder, SAVE_DIR)):
    os.mkdir(os.path.join(folder, SAVE_DIR))

images = get_image_paths(folder)
print("Going to create thumbnails.")
start_time = time()
for image in images:
    create_thumbnail(image)
print("Terminated, I used {0}s".format(time() - start_time))
