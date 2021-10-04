from contextlib import ContextDecorator
from datetime import datetime
from time import sleep


class LoggingDecorator(ContextDecorator):

    def __init__(self, func):
        self.func = func
        self.log_file = open("exec_time.txt", "w")
        self.start_time = datetime.now().second
        self.finish_time = 0

    def __enter__(self):
        return self.func()

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.finish_time = datetime.now().second
        try:
            self.log_file.write("Time of execution = " + str(self.finish_time - self.start_time) + " seconds")
            print("Time of execution writed in exec_time.txt file")
        except Exception as err:
            print(err)
        return True


def function():
    for i in range(6):
        print(i)
        sleep(1)


with LoggingDecorator(func=function) as log:
    print("Finish")
