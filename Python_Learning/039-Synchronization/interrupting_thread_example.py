import threading
import time

def interruptible_task(stop_event):
    while not stop_event.is_set():
        print("Worker thread is running...")
        time.sleep(1)
    print("Worker thread is stopping.")

if __name__ == "__main__":
    stop_event = threading.Event()
    worker_thread = threading.Thread(target=interruptible_task, args=(stop_event,))

    worker_thread.start()

    try:
        time.sleep(5)
    finally:
        print("Main thread is interrupting the worker thread.")
        stop_event.set()
        worker_thread.join()
        print("Main thread finished.")
