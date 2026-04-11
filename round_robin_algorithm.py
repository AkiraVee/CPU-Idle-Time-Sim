
# round_robin.py
# Round Robin CPU Scheduling (CLI version)

def round_robin():

    # { ENTER INPUTS }
    process_count = int(input("ENTER process count: "))

    print("ENTER arrival times:")
    arrival_time = [int(input(f"P{i+1}: ")) for i in range(process_count)]
    
    print("ENTER burst times:")
    burst_time = [int(input(f"P{i+1}: ")) for i in range(process_count)]

    time_quantum = int(input("ENTER time quantum: "))


    # { INITIALIZE VARIABLES }
    remaining_burst = burst_time.copy()
    start_time = [-1] * process_count
    finish_time = [0] * process_count

    current_time = 0
    queue = []
    gantt_chart = []
    gantt_time = [0]

    completed = 0


    # { MAIN ROUND ROBIN LOOP }
    while completed < process_count:

        # queue management (add arrived processes)
        for i in range(process_count):
            if arrival_time[i] <= current_time and i not in queue and remaining_burst[i] > 0:
                queue.append(i)

        if not queue:
            current_time += 1
            continue

        current = queue.pop(0)

        if start_time[current] == -1:
            start_time[current] = current_time

        # { ESSENTIAL COMPUTATIONS }
        execute_time = min(time_quantum, remaining_burst[current])

        gantt_chart.append(f"P{current+1}")

        current_time += execute_time

        remaining_burst[current] -= execute_time

        gantt_time.append(current_time)

        # add newly arrived processes
        for i in range(process_count):
            if arrival_time[i] <= current_time and i not in queue and remaining_burst[i] > 0 and i != current:
                queue.append(i)

        if remaining_burst[current] > 0:
            queue.append(current)
        else:
            finish_time[current] = current_time
            completed += 1


    # { COMPUTE PROCESS TABLE }
    turnaround_time = []
    waiting_time = []

    total_turnaround = 0
    total_waiting = 0

    for i in range(process_count):

        tat = finish_time[i] - arrival_time[i]
        wt = tat - burst_time[i]

        turnaround_time.append(tat)
        waiting_time.append(wt)

        total_turnaround += tat
        total_waiting += wt


    # { SYSTEM PERFORMANCE }
    avg_waiting_time = total_waiting / process_count
    avg_turnaround_time = total_turnaround / process_count

    cpu_busy_time = sum(burst_time)
    total_time = gantt_time[-1]

    cpu_idle_time = total_time - cpu_busy_time
    cpu_utilization = (cpu_busy_time / total_time) * 100
    throughput = process_count / total_time


    # { PRINT GANTT CHART }
    print("\nGANTT CHART:")
    for p in gantt_chart:
        print(f"| {p} ", end="")
    print("|")

    for t in gantt_time:
        print(t, end="    ")
    print()


    # { PRINT PROCESS TABLE }
    print("\nPROCESS TABLE")
    print("Process\tTurnaround\tWaiting")

    for i in range(process_count):
        print(f"P{i+1}\t{turnaround_time[i]}\t\t{waiting_time[i]}")


    # { PRINT SYSTEM PERFORMANCE }
    print("\nSYSTEM PERFORMANCE")
    print("CPU Busy Time:", cpu_busy_time)
    print("CPU Idle Time:", cpu_idle_time)
    print("CPU Utilization:", cpu_utilization)
    print("Throughput:", throughput)
    print("Average Waiting Time:", avg_waiting_time)
    print("Average Turnaround Time:", avg_turnaround_time)

round_robin()