"""
Implement a job scheduler which takes in a function f
and an integer n, and calls f after n milliseconds.
"""

import threading
import time
from datetime import datetime


class WorkerExample(threading.Thread):
    die = False
    def __init__(self, name:str, delay:int, f):
        threading.Thread.__init__(self)
        self.name = name
        self.delay = delay
        self.f = f

    def run(self):
        while not self.die:
            time.sleep(self.delay)

            now = datetime.now().strftime("%H:%M:%S")
            print(f"{now}| Hello from worker {self.name}")
            self.f() # Function call

    def join(self):
        self.die = True
        super().join()

def job_scheduler(f_function, n_in_milliseconds):
    worker = WorkerExample(name="example", delay=n_in_milliseconds//1000, f= f_function)
    worker.start()

    try:
        while True:
            pass
    except KeyboardInterrupt:
        worker.join()

def test_function():
    print("Hello World!")

job_scheduler(test_function, n_in_milliseconds = 1000)