# sjf.py
# Shortest Job First CPU Scheduling (Non-Preemptive)

def sjf():

    # { ENTER INPUTS }
    process_count = int(input("ENTER process count: "))

    arrival_time = []
    burst_time = []

    print("ENTER arrival times:")
    for i in range(process_count):
        arrival_time.append(int(input(f"P{i+1}: ")))

    print("ENTER burst times:")
    for i in range(process_count):
        burst_time.append(int(input(f"P{i+1}: ")))

    # { INITIALIZE VARIABLES }
    completed = [False] * process_count
    start_time = [0] * process_count
    finish_time = [0] * process_count

    current_time = 0
    done = 0

    gantt_chart = []
    gantt_time = [0]

    # { MAIN SJF LOOP }
    while done < process_count:

        idx = -1
        min_burst = float('inf')

        for i in range(process_count):
            if arrival_time[i] <= current_time and not completed[i]:
                if burst_time[i] < min_burst:
                    min_burst = burst_time[i]
                    idx = i

        if idx == -1:
            current_time += 1
            continue

        start_time[idx] = current_time
        gantt_chart.append(f"P{idx+1}")

        current_time += burst_time[idx]

        finish_time[idx] = current_time
        gantt_time.append(current_time)

        completed[idx] = True
        done += 1

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


# run program
sjf()