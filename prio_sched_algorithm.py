# prio_sched_algorithm.py
# Priority Scheduling Simulator (Non-preemptive)

# ===============================
# PROCESS CLASS
# ===============================
class Process:
    def __init__(self, pid, arrival, burst, priority):
        self.pid = pid
        self.arrival = arrival
        self.burst = burst
        self.remaining = burst
        self.priority = priority  # lower number = higher priority
        self.completion = 0
        self.turnaround = 0
        self.waiting = 0


# ===============================
# INPUT
# ===============================
def get_processes():
    while True:
        try:
            n = int(input("\nEnter number of processes: "))
            if n < 1:
                print("Number must be at least 1.")
                continue
            break
        except ValueError:
            print("Enter a valid number.")

    processes = []

    print("\n(lower priority number = higher priority)")
    for i in range(n):
        print(f"\nProcess {i+1}")

        while True:
            try:
                arrival = int(input("Arrival Time: "))
                if arrival < 0:
                    print("Arrival time cannot be negative.")
                    continue
                break
            except ValueError:
                print("Enter a valid integer.")

        while True:
            try:
                burst = int(input("Burst Time: "))
                if burst <= 0:
                    print("Burst time must be positive.")
                    continue
                break
            except ValueError:
                print("Enter a valid integer.")

        while True:
            try:
                priority = int(input("Priority: "))
                break
            except ValueError:
                print("Enter a valid integer.")

        processes.append(Process(f"P{i+1}", arrival, burst, priority))

    return processes


# ===============================
# PRINT GENERATED PROCESSES
# ===============================
def print_generated(processes):
    print("\nGenerated Processes:\n")
    for p in processes:
        print(f"{p.pid} | AT: {p.arrival} | BT: {p.burst} | PR: {p.priority}")


# ===============================
# PRIORITY SCHEDULING
# ===============================
def priority_sched(processes):
    time = 0
    timeline = []
    processes_left = list(processes)

    while processes_left:

        ready = [p for p in processes_left if p.arrival <= time]

        if ready:
            p = min(ready, key=lambda x: x.priority)

            start = time
            time += p.burst

            timeline.append((p.pid, start, time))

            p.completion = time

            processes_left.remove(p)

        else:
            next_arrival = min(p.arrival for p in processes_left)
            timeline.append(("IDLE", time, next_arrival))
            time = next_arrival

    return timeline


# ===============================
# GANTT CHART
# ===============================
def print_gantt(timeline):

    print("\nGantt Chart:\n")

    for _ in timeline:
        print("+--------", end="")
    print("+")

    for pid, start, end in timeline:
        print(f"| {pid:^6} ", end="")
    print("|")

    for _ in timeline:
        print("+--------", end="")
    print("+")

    print(f"{timeline[0][1]:<8}", end="")
    for pid, start, end in timeline:
        print(f"{end:<8}", end="")
    print()


# ===============================
# METRICS
# ===============================
def compute_metrics(processes, timeline):

    total_idle = sum(end - start for pid, start, end in timeline if pid == "IDLE")
    total_time = timeline[-1][2]
    busy_time = total_time - total_idle

    print("\nProcess Table:\n")

    total_tat = 0
    total_wt = 0

    for p in processes:

        p.turnaround = p.completion - p.arrival
        p.waiting = p.turnaround - p.burst

        total_tat += p.turnaround
        total_wt += p.waiting

        print(f"{p.pid} | Waiting Time: {p.waiting} | Turnaround Time: {p.turnaround}")

    avg_tat = total_tat / len(processes)
    avg_wt = total_wt / len(processes)

    utilization = (busy_time / total_time) * 100
    throughput = len(processes) / total_time

    print("\nSystem Performance:\n")
    print(f"CPU Busy Time: {busy_time}")
    print(f"CPU Idle Time: {total_idle}")
    print(f"CPU Utilization: {utilization:.2f}%")
    print(f"Throughput: {throughput:.2f} processes/unit time")
    print(f"Average Waiting Time: {avg_wt:.2f}")
    print(f"Average Turnaround Time: {avg_tat:.2f}")


# ===============================
# MAIN
# ===============================
print("=== Priority Scheduling Simulator (Non-preemptive) ===")

while True:

    processes = get_processes()

    print_generated(processes)

    timeline = priority_sched(processes)

    print_gantt(timeline)

    compute_metrics(processes, timeline)

    while True:
        again = input("\nDo you want to simulate another scheduling? (Y/N): ").strip().upper()

        if again in ["Y", "N", "y", "n"]:
            break
        else:
            print("Please enter Y or N only.")

    if again != "Y":
        print("\nReturning to main menu...") 
        break

    print("\n" + "-"*50)