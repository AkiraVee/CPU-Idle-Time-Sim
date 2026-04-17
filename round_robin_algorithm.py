# round_robin_algorithm.py
# Round Robin CPU Scheduling (FIXED GANTT VERSION)

def round_robin():

    #==============================
    # INPUT SECTION
    #==============================
    while True:
        try:
            process_count = int(input("\nENTER process count: "))
            if process_count < 1:
                print("Process count must be at least 1.")
                continue
            break
        except ValueError:
            print("Invalid input! Please enter a positive integer.")

    print("\nENTER arrival times:")
    arrival_time = []
    for i in range(process_count):
        while True:
            try:
                at = int(input(f"P{i+1}: "))
                if at < 0:
                    print("Arrival time cannot be negative.")
                    continue
                arrival_time.append(at)
                break
            except ValueError:
                print("Invalid input! Please enter an integer.")

    print("\nENTER burst times:")
    burst_time = []
    for i in range(process_count):
        while True:
            try:
                bt = int(input(f"P{i+1}: "))
                if bt <= 0:
                    print("Burst time must be positive.")
                    continue
                burst_time.append(bt)
                break
            except ValueError:
                print("Invalid input! Please enter a positive integer.")

    while True:
        try:
            time_quantum = int(input("\nENTER time quantum: "))
            if time_quantum <= 0:
                print("Time quantum must be positive.")
                continue
            break
        except ValueError:
            print("Invalid input! Please enter a positive integer.")

    # ==============================
    # INITIALIZATION
    # ==============================

    remaining_burst = burst_time.copy()

    start_time = [-1] * process_count
    finish_time = [0] * process_count

    current_time = 0

    queue = []
    completed = 0
    cpu_idle_time = 0

    gantt_chart = []   # (label, start, end)
    gantt_time = [0]

    # ==============================
    # MAIN LOOP
    # ==============================

    while completed < process_count:

        # add arrived processes
        for i in range(process_count):
            if arrival_time[i] <= current_time and i not in queue and remaining_burst[i] > 0:
                queue.append(i)

        # IDLE CASE
        if not queue:
            if gantt_chart and gantt_chart[-1][0] == "ID":
                gantt_chart[-1][2] = current_time + 1
            else:
                gantt_chart.append(["ID", current_time, current_time + 1])

            current_time += 1
            gantt_time.append(current_time)
            cpu_idle_time += 1
            continue

        current = queue.pop(0)

        if start_time[current] == -1:
            start_time[current] = current_time

        # EXECUTION
        start_exec = current_time
        execute_time = min(time_quantum, remaining_burst[current])

        current_time += execute_time
        remaining_burst[current] -= execute_time
        gantt_time.append(current_time)

        # merge Gantt chart
        label = f"P{current+1}"
        if gantt_chart and gantt_chart[-1][0] == label:
            gantt_chart[-1][2] = current_time
        else:
            gantt_chart.append([label, start_exec, current_time])

        # add newly arrived processes
        for i in range(process_count):
            if arrival_time[i] <= current_time and remaining_burst[i] > 0 and i not in queue and i != current:
                queue.append(i)

        # requeue or finish
        if remaining_burst[current] > 0:
            queue.append(current)
        else:
            finish_time[current] = current_time
            completed += 1

    # ==============================
    # COMPUTE TIMES
    # ==============================

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

    cpu_busy_time = sum(burst_time)
    total_time = gantt_time[-1]

    cpu_utilization = (cpu_busy_time / total_time) * 100
    throughput = process_count / total_time

    # ==============================
    # GANTT CHART OUTPUT (FIXED)
    # ==============================

    print("\nGANTT CHART:")

    for item in gantt_chart:
        print(f"| {item[0]} ", end="")
    print("|")

    for item in gantt_chart:
        print(f"{item[1]:<5}", end="")
    print(f"{gantt_chart[-1][2]:<5}")

    # ==============================
    # PROCESS TABLE (same style)
    # ==============================

    print("\nPROCESS TABLE")
    print("-" * 75)
    print(f"{'Process ID':<12}|{'Arrival Time':<15}|{'Burst Time':<12}|{'Turnaround':<12}|{'Waiting Time':<12}|")
    print("-" * 75)

    for i in range(process_count):
        print(f"{'P'+str(i+1):<12}|{arrival_time[i]:<15}|{burst_time[i]:<12}|{turnaround_time[i]:<12}|{waiting_time[i]:<12}|")

    print("-" * 75)
    print(f"{'Total':<12}|{'':<15}|{'':<12}|{total_turnaround:<12}|{total_waiting:<12}|")
    print("-" * 75)

    # ==============================
    # SYSTEM PERFORMANCE
    # ==============================

    print("\nSYSTEM PERFORMANCE")
    print("CPU Busy Time:", cpu_busy_time)
    print("CPU Idle Time:", cpu_idle_time)
    print("CPU Utilization:", cpu_utilization)
    print("Throughput:", throughput)
    print("Average Waiting Time:", total_waiting / process_count)
    print("Average Turnaround Time:", total_turnaround / process_count)


# ===============================
# MAIN LOOP
# ===============================

while True:
    print("\n=== Round Robin (RR) Scheduling Simulator ===")

    round_robin()

    while True:
        again = input("\nDo you want to use the algorithm again? (Y/N): ").strip().upper()
        if again in ["Y", "N"]:
            break
        print("Please enter Y or N only.")

    if again != "Y":
        print("\nGoodbye!")
        break

    print("\n" + "-" * 60)