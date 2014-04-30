import os
import sys
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter
from reportlab.lib.units import cm, mm, inch, pica
from PIL import Image
from multiprocessing import Pool


SIZE = (760, 1080)
SAVE_DIR = 'tmp'

def get_image_paths(folder):
    return (os.path.join(folder, f) for f in os.listdir(folder)
     if (f.endswith('.jpg') or f.endswith('.gif')))


def reduce_size(filename):
    im = Image.open(filename)
    im.thumbnail(SIZE, Image.ANTIALIAS)
    base, fname = os.path.split(filename)
    save_path = os.path.join(base, SAVE_DIR, fname)
    im.save(save_path)

def reduce_all_files(folder):
    if not os.path.exists(os.path.join(folder, SAVE_DIR)):
        os.makedirs(os.path.join(folder, SAVE_DIR))

    images = get_image_paths(folder)
    print("Reducing sizes")
    pool = Pool()
    pool.map(reduce_size, images)
    pool.close()
    pool.join()
    print("Terminated of reduce size")


def delete_tmp(folder):
    folder = os.path.join(folder, SAVE_DIR)
    if os.path.exists(folder):
        for f in get_image_paths(folder):
            os.remove(f)
        os.removedirs(folder)

def pdfDirectory(imageDirectory, outputPDFName):
    dirim = str(imageDirectory)
    output = str(outputPDFName)
    c = canvas.Canvas(output, pagesize=SIZE)
    try:
        reduce_all_files(dirim) #Reducing all :)
        for root, dirs, files in os.walk(os.path.join(dirim,SAVE_DIR)):
            for name in files:
                lname = name.lower()
                if lname.endswith(".jpg") or lname.endswith(".gif") or lname.endswith(".png"):
                    filepath = os.path.join(root, name)
                    c.drawImage(filepath, 0, 0)
                    c.showPage()
                    c.save()
        print("PDF of Image directory created")
    except:
        print("Failed creating PDF")
    finally:
        delete_tmp(dirim)



if __name__ == "__main__":
    pdfDirectory(sys.argv[1], sys.argv[2])