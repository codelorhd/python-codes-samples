"""
Simple cotyledon program
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
