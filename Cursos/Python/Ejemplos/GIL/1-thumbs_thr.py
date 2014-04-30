import os
import threading
from queue import Queue
from PIL import Image
from time import time

SIZE = (75, 75)
SAVE_DIR = 'thumbs'

class Resize(threading.Thread):
    def __init__(self, filename):
        threading.Thread.__init__(self)
        self.filename = filename
    def run(self):
        im = Image.open(self.filename)
        im.thumbnail(SIZE, Image.ANTIALIAS)
        base, fname = os.path.split(self.filename)
        save_path = os.path.join(base, SAVE_DIR, fname)
        im.save(save_path)

def get_image_paths(folder):
    return (os.path.join(folder, f) for f in os.listdir(folder) if 'jpg' in f)


folder = os.path.join(os.path.expanduser("~"), "Imágenes", "Wallpapers", "tothumbs")
if not os.path.exists(os.path.join(folder, SAVE_DIR)):
    os.mkdir(os.path.join(folder, SAVE_DIR))

images = get_image_paths(folder)
thrds = []
print("Going to create thumbnails.")
start_time = time()
for image in images:
    t = Resize(image)
    t.start()
    thrds.append(t)
for i in thrds:
    i.join()
print("Terminated, I used {0}s".format(time() - start_time))

