import threading
import time
import logging
from concurrent.futures import ThreadPoolExecutor

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(threadName)s - %(message)s')

# 1. Creating a Thread using a function
def worker(name, delay):
    """A simple worker function that simulates a task."""
    logging.info(f"Starting task: {name}")
    time.sleep(delay)
    logging.info(f"Finished task: {name}")

# 2. Creating a Thread by subclassing Thread
class MyThread(threading.Thread):
    def __init__(self, name, delay):
        super().__init__()
        self.name = name
        self._delay = delay

    def run(self):
        """The entry point for the thread."""
        logging.info(f"Starting task: {self.name}")
        time.sleep(self._delay)
        logging.info(f"Finished task: {self.name}")

# 3. Main Thread and Naming Threads
def main_thread_example():
    logging.info("Main thread starting.")
    
    # Create and start a thread with a custom name
    thread1 = threading.Thread(target=worker, args=("Task 1", 2), name="WorkerThread1")
    thread1.start()
    
    # Create and start a thread using the custom class
    thread2 = MyThread("Task 2", 3)
    thread2.start()

    logging.info(f"Active threads: {threading.active_count()}")
    
    # 4. Joining Threads
    thread1.join()
    thread2.join()
    
    logging.info("Main thread finished.")

# 5. Daemon Threads
def daemon_thread_example():
    logging.info("Daemon thread example starting.")
    
    # Create a daemon thread
    daemon_thread = threading.Thread(target=worker, args=("DaemonTask", 5), name="DaemonThread")
    daemon_thread.daemon = True
    daemon_thread.start()
    
    # The main thread will not wait for the daemon thread to finish
    logging.info("Main thread exiting (daemon example).")

# 6. Thread Synchronization (Lock)
class SharedCounter:
    def __init__(self):
        self._value = 0
        self._lock = threading.Lock()

    def increment(self):
        with self._lock:
            # This block is synchronized
            current_value = self._value
            time.sleep(0.1) # Simulate some work
            self._value = current_value + 1

    @property
    def value(self):
        return self._value

def synchronization_example():
    logging.info("Synchronization example starting.")
    counter = SharedCounter()
    
    threads = []
    for i in range(5):
        thread = threading.Thread(target=counter.increment)
        threads.append(thread)
        thread.start()
        
    for thread in threads:
        thread.join()
        
    logging.info(f"Final counter value: {counter.value}")
    logging.info("Synchronization example finished.")

# 7. Thread Pools
def thread_pool_example():
    logging.info("Thread pool example starting.")
    
    with ThreadPoolExecutor(max_workers=3) as executor:
        tasks = [("Task A", 2), ("Task B", 3), ("Task C", 1), ("Task D", 4)]
        
        # Submit tasks to the thread pool
        futures = [executor.submit(worker, name, delay) for name, delay in tasks]
        
        # Wait for all tasks to complete
        for future in futures:
            future.result() # Calling result() will re-raise exceptions if any occurred
            
    logging.info("Thread pool example finished.")


if __name__ == "__main__":
    print("--- Main Thread and Joining Example ---")
    main_thread_example()
    print("\n" + "="*40 + "\n")
    
    print("--- Daemon Thread Example ---")
    daemon_thread_example()
    # Note: You might not see the "Finished task: DaemonTask" log message
    # because the main thread exits before the daemon thread completes.
    time.sleep(1) # Give the daemon a moment to start
    print("\n" + "="*40 + "\n")

    print("--- Synchronization Example ---")
    synchronization_example()
    print("\n" + "="*40 + "\n")
    
    print("--- Thread Pool Example ---")
    thread_pool_example()
    print("\n" + "="*40 + "\n")
