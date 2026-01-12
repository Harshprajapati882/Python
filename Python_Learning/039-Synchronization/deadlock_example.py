import threading
import time

lock1 = threading.Lock()
lock2 = threading.Lock()

def thread1_action():
    print("Thread 1: Acquiring lock 1...")
    lock1.acquire()
    print("Thread 1: Acquired lock 1.")
    time.sleep(1)
    print("Thread 1: Acquiring lock 2...")
    lock2.acquire()
    print("Thread 1: Acquired lock 2.")
    lock2.release()
    lock1.release()

def thread2_action():
    print("Thread 2: Acquiring lock 2...")
    lock2.acquire()
    print("Thread 2: Acquired lock 2.")
    time.sleep(1)
    print("Thread 2: Acquiring lock 1...")
    lock1.acquire()
    print("Thread 2: Acquired lock 1.")
    lock1.release()
    lock2.release()

if __name__ == "__main__":
    thread1 = threading.Thread(target=thread1_action)
    thread2 = threading.Thread(target=thread2_action)

    thread1.start()
    thread2.start()

    thread1.join()
    thread2.join()

    print("Finished. This will not be printed in case of a deadlock.")
