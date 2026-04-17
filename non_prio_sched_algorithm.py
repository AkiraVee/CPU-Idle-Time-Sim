# prio_sched_algorithm.py
# Priority Scheduling Simulator (Non-Preemptive - FIXED Gantt)

def non_preemptive_priority_scheduling():

    # ==============================
    # INPUT SECTION
    # ==============================

    while True:
        try:
            process_count = int(input("\nENTER process count: "))
            if process_count < 1:
                print("Process count must be at least 1.")
                continue
            break
        except ValueError:
            print("Invalid input! Please enter a positive integer.")

    arrival_time = []
    burst_time = []
    priority_list = []

    print("\nENTER arrival times:")
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

    print("\nENTER priority (lower number = higher priority):")
    for i in range(process_count):
        while True:
            try:
                pr = int(input(f"P{i+1}: "))
                priority_list.append(pr)
                break
            except ValueError:
                print("Invalid input! Please enter an integer.")

    # ==============================
    # INITIALIZATION
    # ==============================

    completed = [False] * process_count
    start_time = [0] * process_count
    finish_time = [0] * process_count

    current_time = 0
    done = 0

    gantt_chart = []   # [label, start, end]
    gantt_time = [0]

    # ==============================
    # MAIN LOOP
    # ==============================

    while done < process_count:

        ready = [
            i for i in range(process_count)
            if arrival_time[i] <= current_time and not completed[i]
        ]

        # ==============================
        # IDLE CASE
        # ==============================
        if not ready:
            if gantt_chart and gantt_chart[-1][0] == "ID":
                gantt_chart[-1][2] = current_time + 1
            else:
                gantt_chart.append(["ID", current_time, current_time + 1])

            current_time += 1
            gantt_time.append(current_time)
            continue

        # ==============================
        # PICK HIGHEST PRIORITY
        # ==============================
        idx = ready[0]
        for i in ready:
            if priority_list[i] < priority_list[idx]:
                idx = i

        start_exec = current_time

        start_time[idx] = current_time
        current_time += burst_time[idx]
        finish_time[idx] = current_time

        # ==============================
        # FIXED GANTT MERGE
        # ==============================
        label = f"P{idx+1}"

        if gantt_chart and gantt_chart[-1][0] == label:
            gantt_chart[-1][2] = current_time
        else:
            gantt_chart.append([label, start_exec, current_time])

        gantt_time.append(current_time)

        completed[idx] = True
        done += 1

    # ==============================
    # GANTT CHART OUTPUT
    # ==============================

    print("\nGANTT CHART:")

    for block in gantt_chart:
        print(f"| {block[0]} ", end="")
    print("|")

    for block in gantt_chart:
        print(f"{block[1]:<5}", end="")
    print(gantt_chart[-1][2])

    # ==============================
    # PROCESS TABLE
    # ==============================

    print("\nPROCESS TABLE")
    print("-" * 90)
    print(f"{'Process ID':<12}|{'Arrival Time':<15}|{'Burst Time':<12}|{'Priority':<10}|{'Turnaround':<12}|{'Waiting Time':<12}|")
    print("-" * 90)

    total_turnaround = 0
    total_waiting = 0

    for i in range(process_count):
        tat = finish_time[i] - arrival_time[i]
        wt = tat - burst_time[i]

        total_turnaround += tat
        total_waiting += wt

        print(f"{'P'+str(i+1):<12}|{arrival_time[i]:<15}|{burst_time[i]:<12}|{priority_list[i]:<10}|{tat:<12}|{wt:<12}|")

    print("-" * 90)
    print(f"{'Total':<12}|{'':<15}|{'':<12}|{'':<10}|{total_turnaround:<12}|{total_waiting:<12}|")
    print("-" * 90)

    # ==============================
    # SYSTEM PERFORMANCE
    # ==============================

    cpu_busy_time = sum(burst_time)
    total_time = gantt_time[-1]

    cpu_idle_time = total_time - cpu_busy_time
    cpu_utilization = (cpu_busy_time / total_time) * 100
    throughput = process_count / total_time

    print("\nSYSTEM PERFORMANCE")
    print("CPU Busy Time:", cpu_busy_time)
    print("CPU Idle Time:", cpu_idle_time)
    print("CPU Utilization:", cpu_utilization)
    print("Throughput:", throughput)
    print("Average Waiting Time:", total_waiting / process_count)
    print("Average Turnaround Time:", total_turnaround / process_count)


# ==============================
# MAIN LOOP
# ==============================

while True:
    print("\n=== Priority Scheduling (Non-Preemptive) Scheduling Simulator ===")

    priority_scheduling()

    while True:
        again = input("\nDo you want to use the algorithm again? (Y/N): ").strip().upper()
        if again in ["Y", "N"]:
            break
        print("Please enter Y or N only.")

    if again != "Y":
        print("\nGoodbye!")
        break

    print("\n" + "-" * 60)