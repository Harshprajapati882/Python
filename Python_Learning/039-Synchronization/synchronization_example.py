import threading
import time

# Shared resource
shared_resource = 0
lock = threading.Lock()

def increment():
    global shared_resource
    for _ in range(1000000):
        lock.acquire()
        shared_resource += 1
        lock.release()

def decrement():
    global shared_resource
    for _ in range(1000000):
        lock.acquire()
        shared_resource -= 1
        lock.release()

if __name__ == "__main__":
    thread1 = threading.Thread(target=increment)
    thread2 = threading.Thread(target=decrement)

    thread1.start()
    thread2.start()

    thread1.join()
    thread2.join()

    print(f"Final value of shared resource: {shared_resource}")
