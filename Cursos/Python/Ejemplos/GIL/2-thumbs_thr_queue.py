import os
import threading
from queue import Queue
from PIL import Image
from time import time

SIZE = (75, 75)
SAVE_DIR = 'thumbs'

class Resize(threading.Thread):
    def __init__(self, queue):
        threading.Thread.__init__(self)
        self.queue = queue
    def run(self):
        while True:
            filename = self.queue.get()
            self.create_thumbnail(filename)
            self.queue.task_done()
    def create_thumbnail(self, filename):
        im = Image.open(filename)
        im.thumbnail(SIZE, Image.ANTIALIAS)
        base, fname = os.path.split(filename)
        save_path = os.path.join(base, SAVE_DIR, fname)
        im.save(save_path)

def get_image_paths(folder):
    return (os.path.join(folder, f) for f in os.listdir(folder) if 'jpg' in f)


queue = Queue()
folder = os.path.join(os.path.expanduser("~"), "Imágenes", "Wallpapers", "tothumbs")
if not os.path.exists(os.path.join(folder, SAVE_DIR)):
    os.mkdir(os.path.join(folder, SAVE_DIR))

images = get_image_paths(folder)
print("Going to create thumbnails.")
start_time = time()
for i in range(10):
    t = Resize(queue)
    t.setDaemon(True)
    t.start()

for image in images:
    queue.put(image)

queue.join()
print("Terminated, I used {0}s".format(time() - start_time))
