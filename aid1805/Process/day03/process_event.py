from multiprocessing import Process
from multiprocessing import Event
import time


# 生成事件对象
e = Event()


def wait_event():
    print("wait for event setting")
    e.wait()
    print("wait_for_event01", e.is_set())


def wait_event_timeout():
    print("wait for event setting or timeout")
    e.wait(2)
    print("wait_for_event02", e.is_set())


p1 = Process(name='block', target=wait_event)
p1.start()

p2 = Process(name='non-block', target=wait_event_timeout)
p2.start()

print("main:setting the event")
time.sleep(3)
e.set()
print("event is set")
