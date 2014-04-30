import os
import urllib.request
from tqdm import *

from threading import Thread

class DownloadThread(Thread):
    """Download a file"""
    def __init__(self, url, name):
        Thread.__init__(self)
        self.name = name
        self.url = url

    def run(self):
        """run overwrite"""
        peticion = urllib.request.urlopen(self.url)
        filename = os.path.basename(self.url)
        filename = filename.split("?")[0]
        with open(filename, "wb") as f:
            while True:
                data = peticion.read(1024)
                if not data:
                    break
                f.write(data)
        print("{0} ha terminado de descargar {1}".format(self.name, self.url))


def main(urls):
    """main program"""
    for item, url in enumerate(urls):
        name = "Thread {}".format(item+1)
        thread = DownloadThread(url, name)
        thread.start()


if __name__ == "__main__":
    urls = [
            "https://did3ct2sntthk.cloudfront.net/issue/12335/1/full_size_image/1.jpg?Expires=1398381054&Signature=oSpWWg3FiAfKOMLa1mSt2x1kiq-fIMHt7gTRM5GjyWzQLxl33X4rb~oyZOJm6KECZPqyC-nspJjFfwjSQYH-XLqLyJ51Uxm0w2HBc9KBfy0J66tWxmYd15v2mSa7HkXJ3rBPd-d3MQXPop972E4BqgHG-QiA57Xj25LkzCFG2ztkTtKEDMQiWag2jU1rMRtn7aEVBv~~BzW5qVrBNVtYDHZqbhNtixCVjNhTY5-xlM62BfZoATTI2UDcSUcZERymKqGYB7k9MsNhSMF2kEDZE92nZUl-iX~bQYPvMiTksQwWKG908YvzjFFuaELVLLm-JCZr0qHk4HpV39o3598Iew__&Key-Pair-Id=APKAIK2TEQCWIQY3C5OA",
            "https://did3ct2sntthk.cloudfront.net/issue/12335/1/full_size_image/3.jpg?Expires=1398381054&Signature=Hwiza7B8jkvqwyeF~wpzsxHqcZFV0aX11Wi48i0OhGumwYJDNFqjGPRx51Q3tt~3MwmQ-sY92CyHJ0e1Poy4KPosX4ZbcaWsoVjjHZwYyiJ9tOL74~BpMzvwJBCk34CYRFuqGXFtThjO8wAvq81i149ARqX7qMa2KNImVlxRYOxeILj4UuA12qBaxipuOd5p3FIfDJpk44Izjh0ERU~K8M8I319KULGnGIycnQ1CjVkFFS5hVQmfUkDWBwTNbkjc-bp7edFwNYWXXVf3h40PZUK8tC8g9LyxP1TRapexRhlKW6ESSUS17K6JrUxu24vcI6p1ZlaIcn5F5eJL5l-IyQ__&Key-Pair-Id=APKAIK2TEQCWIQY3C5OA",
            "https://did3ct2sntthk.cloudfront.net/issue/12335/1/full_size_image/4.jpg?Expires=1398381054&Signature=CLA5E4ilJtpo14XkKizFilegyGEc6J7nt7qEv4Pwk77kfLJaqBT4o307L9YxAlVN~ac~UPWMi6ocA1tJ2aR5gQlnfpMqULIwUqG0TqgGKuzwaP-Uj5EFHmfhWKJRDieexdqeIoq2U~3ZW3TxhL4zsDF6rJLAbhdxxuEq89vaTwbyIJn00hJYIDWR97MVPcoiFOJx3NOG9HtqrboPOfR~UFQ1ORRuy4CvKvlrBB8FgKK1qy92DjNcks65wkptjcOwmuLmjtgtcn~8D1SbJnP1OPIkECwb--Dt~ivaN6VIdmDqcsN2AClQ7LUGcr3qUAeznnI0kSPSD1c0rcUTrsFmOQ__&Key-Pair-Id=APKAIK2TEQCWIQY3C5OA",
            "https://did3ct2sntthk.cloudfront.net/issue/12335/1/full_size_image/6.jpg?Expires=1398381054&Signature=S82rVv4lJ2jgT408pFH0USP4ERelQPXI8TH47SooqaD4nGhbxwWYBa2Xk8u8Fwlt5q8TyX0zDdYju7ApyySErU645IyTdhbgYmI88p-k842rZkI4U1kxgbyWixjqyaDsCqG5TouC0T1ow0PHLFRkoy1XERjS9Owq6WZdN5x9Z-wJIiJuyzJQ2Zd38P12Qr5XpYGT9uKJAdx4AF0-k1EFsrGpVfmFYfc90Z5lJn40nxiCDwl2Na7RHB4cUly1lIH~QZeUUG8PhzQT9a~C~lCQGGkTP8C4mCD~eIFyxOFe3ZkWETr29BllXV0zA7bvz15xDp4u~Xd5~SR0bog~uHINBw__&Key-Pair-Id=APKAIK2TEQCWIQY3C5OA"
            ]
    main(urls)
