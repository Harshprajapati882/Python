import threading
import queue
import time

def producer(q):
    for i in range(5):
        print(f"Producing item {i}")
        q.put(i)
        time.sleep(1)
    q.put(None)  # Sentinel value to signal completion

def consumer(q):
    while True:
        item = q.get()
        if item is None:
            break
        print(f"Consuming item {item}")
        time.sleep(2)

if __name__ == "__main__":
    q = queue.Queue()
    thread1 = threading.Thread(target=producer, args=(q,))
    thread2 = threading.Thread(target=consumer, args=(q,))

    thread1.start()
    thread2.start()

    thread1.join()
    thread2.join()

    print("Main thread finished.")
