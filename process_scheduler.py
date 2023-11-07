import queue
import time

class Process:
    def __init__(self, process_id, name, priority, io_bound, total_cpu_time):
        self.process_id = process_id
        self.name = name
        self.priority = priority
        self.io_bound = io_bound
        self.total_cpu_time = total_cpu_time
        self.remaining_cpu_time = total_cpu_time

ready_queue = queue.Queue()
active_process = None

def create_process(process_id, name, priority, io_bound, total_cpu_time):
    global ready_queue
    process = Process(process_id, name, priority, io_bound, total_cpu_time)
    ready_queue.put(process)

def round_robin_scheduling(quantum):
    global active_process, ready_queue

    while not ready_queue.empty():
        if active_process is None or active_process.remaining_cpu_time == 0:
            active_process = ready_queue.get()
        
        print(f"Process {active_process.process_id} - {active_process.name} is running")
        active_process.remaining_cpu_time -= 1
        time.sleep(quantum)
        
        if active_process.remaining_cpu_time > 0:
            ready_queue.put(active_process)

        active_process = None

create_process(1, "Process 1", 1, True, 5)
create_process(2, "Process 2", 2, False, 3)
create_process(3, "Process 3", 1, True, 4)

round_robin_scheduling(1)  # Usando um quantum de 1 unidade de tempo
