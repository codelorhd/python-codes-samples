"""
Producer / Consumer
In this pattern, a service fills a queue (the producer), 
and other services (the consumers) consume the jobs to execute them
"""

import multiprocessing
import time
import cotyledon


class Manager(cotyledon.ServiceManager):
    def __init__(self):
        super(Manager, self).__init__()

        # setup the queue both producer and consumer wil use
        #
        # The multiprocessing.queues.Queue object eases the
        # communication between different processes. It is
        # safe to use across threads and processes, as it
        # leverages locks internally to guarantee data safety.
        queue = multiprocessing.Manager().Queue()

        # set up producer
        # By default, the add method will make use of 1 worker,
        # i.e. pass 1 as the value for the workers parameter
        self.add(
            ProducerService,
            args=(queue,),
        )

        # setup consumer
        self.printer = self.add(PrinterService, args=(queue,), workers=2)

        # * register hooks/event
        # * others include on_terminate, on_new_worker, on_dead_worker
        self.register_hooks(on_reload=self.reload)

    def reload(self):
        print("Reloading")
        # Reconfigure, and spawn 5 processes.
        self.reconfigure(self.printer, 5)


class ProducerService(cotyledon.Service):
    def __init__(self, worker_id, queue):
        super(ProducerService, self).__init__(worker_id)
        self.queue = queue

    def run(self):
        i = 0
        while True:
            self.queue.put(i)
            i += 1
            time.sleep(1)


class PrinterService(cotyledon.Service):
    name = "printer"

    def __init__(self, worker_id, queue):
        super(PrinterService, self).__init__(worker_id)
        self.queue = queue

    def run(self):
        while True:
            job = self.queue.get(block=True)
            print(
                "I am Worker: %d PID: %d and I print %s"
                % (self.worker_id, self.pid, job)
            )


Manager().run()
