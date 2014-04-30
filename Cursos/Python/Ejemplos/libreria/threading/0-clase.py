import random
import time

from threading import Thread

class MyThread(Thread):
    """Ejemplo thread"""

    def __init__(self, name):
        """Inicializacion"""
        Thread.__init__(self)
        self.name = name
    def run(self):
        """Lo que se ejecuta"""
        print("{0} empieza.".format(self.name))
        time.sleep(random.randint(3,15))
        print("{0} ha terminado.".format(self.name))

def create_threads():
    """Test"""
    for i in range(5):
        my_thr = MyThread("Thread #{0}".format(i+1))
        my_thr.start()

if __name__ == "__main__":
    create_threads()
