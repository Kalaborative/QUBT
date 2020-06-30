from time import sleep
from threading import Thread

def some_task():
    while True:
        pass

t = Thread(target=some_task)

t.daemon = True

t.start()

snooze = 3
sleep(snooze)