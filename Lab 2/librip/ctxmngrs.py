import time


class timer:

    def __enter__(self):
        self.t = time.clock()

    def __exit__(self, exc_type, exc_val, exc_tb):
        print (time.clock() - self.t)

