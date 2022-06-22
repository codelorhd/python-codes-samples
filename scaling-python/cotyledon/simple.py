"""
Simple cotyledon

Now that we have become aware of the difference between 
multithreading and multiprocessing in Python, it becomes 
more clear that using multiple processes to schedule 
different jobs is efficient.

A widespread use case is to run long-running, background processes 
(often called daemons) that are responsible for scheduling 
some tasks regularly or processing jobs from a queue.
"""

import threading
import time
import cotyledon


class PrinterService(cotyledon.Service):
    """Simple printer class"""

    name = "printer"

    def __init__(self, worker_id):
        super(PrinterService, self).__init__(worker_id)
        self._shutdown = threading.Event()

    def run(self):
        while not self._shutdown.is_set():
            print("Doing stuff")
            time.sleep(1)

    def terminate(self):
        self._shutdown.set()


# Create a manager
manager = cotyledon.ServiceManager()
# Add 2 PrinterService to run
manager.add(PrinterService, 2)
# Run all of that
manager.run()
