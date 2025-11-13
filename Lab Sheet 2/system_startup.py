import multiprocessing
import time
import logging

# Sub-Task 1: Initialize logging
logging.basicConfig(
    filename='process_log.txt',
    level=logging.INFO,
    format='%(asctime)s - %(processName)s - %(message)s'
)

# Sub-Task 2: Define a simulated process task
def system_process(task_name):
    logging.info(f"{task_name} started")
    time.sleep(2)  # Simulate work
    logging.info(f"{task_name} ended")

if __name__ == '__main__':
    print("System Starting...")

    # Sub-Task 3: Create and start processes
    p1 = multiprocessing.Process(name='Process-1', target=system_process, args=('Process-1',))
    p2 = multiprocessing.Process(name='Process-2', target=system_process, args=('Process-2',))
    p1.start()
    p2.start()

    # Sub-Task 4: Join processes and shutdown
    p1.join()
    p2.join()

    print("System Shutdown.")
