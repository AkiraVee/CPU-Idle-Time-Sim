# prio_preemptive.py
# Priority Scheduling Simulator (Preemptive)

def pp_algorithm():

    # ==============================
    # INPUT
    # ==============================

    while True:
        try:
            n = int(input("\nENTER process count: "))
            if n < 1:
                print("Process count must be at least 1.")
                continue
            break
        except ValueError:
            print("Invalid input!")

    arrival = []
    burst = []
    priority = []

    print("\nENTER arrival times:")
    for i in range(n):
        arrival.append(int(input(f"P{i+1}: ")))

    print("\nENTER burst times:")
    for i in range(n):
        burst.append(int(input(f"P{i+1}: ")))

    print("\nENTER priority (lower = higher priority):")
    for i in range(n):
        priority.append(int(input(f"P{i+1}: ")))

    # ==============================
    # INITIALIZATION
    # ==============================

    remaining = burst[:]
    completed = [False] * n

    start = [-1] * n
    finish = [0] * n

    time = 0
    done = 0

    gantt = []      # [label, start, end]
    gantt_time = [0]

    last = None

    # ==============================
    # MAIN LOOP (PREEMPTIVE)
    # ==============================

    while done < n:

        # pick highest priority available
        idx = -1
        best = float("inf")

        for i in range(n):
            if arrival[i] <= time and remaining[i] > 0:
                if priority[i] < best:
                    best = priority[i]
                    idx = i

        # ==============================
        # IDLE CASE
        # ==============================
        if idx == -1:
            if gantt and gantt[-1][0] == "ID":
                gantt[-1][2] += 1
            else:
                gantt.append(["ID", time, time + 1])

            time += 1
            gantt_time.append(time)
            last = "ID"
            continue

        label = f"P{idx+1}"

        # start time
        if start[idx] == -1:
            start[idx] = time

        # ==============================
        # GANTT MERGE LOGIC
        # ==============================
        if gantt and gantt[-1][0] == label:
            gantt[-1][2] += 1
        else:
            gantt.append([label, time, time + 1])

        # execute 1 unit
        remaining[idx] -= 1
        time += 1
        gantt_time.append(time)

        # finish check
        if remaining[idx] == 0:
            finish[idx] = time
            completed[idx] = True
            done += 1

    # ==============================
    # GANTT OUTPUT 
    # ==============================

    print("\nGANTT CHART:")

    for g in gantt:
        print(f"| {g[0]} ", end="")
    print("|")

    for g in gantt:
        print(f"{g[1]:<5}", end="")
    print(gantt[-1][2])


    # ==============================
    # PROCESS TABLE
    # ==============================

    print("\nPROCESS TABLE")
    print("-" * 90)
    print(f"{'Process ID':<12}|{'Arrival':<10}|{'Burst':<10}|{'Priority':<10}|{'Turnaround':<12}|{'Waiting':<10}|")
    print("-" * 90)

    total_tat = 0
    total_wt = 0

    for i in range(n):
        tat = finish[i] - arrival[i]
        wt = tat - burst[i]

        total_tat += tat
        total_wt += wt

        print(f"P{i+1:<11}|{arrival[i]:<10}|{burst[i]:<10}|{priority[i]:<10}|{tat:<12}|{wt:<10}|")

    print("-" * 90)
    print(f"{'Total':<12}|{'':<10}|{'':<10}|{'':<10}|{total_tat:<12}|{total_wt:<10}|")
    print("-" * 90)


    # ==============================
    # PERFORMANCE
    # ==============================

    cpu_busy = sum(burst)
    total_time = gantt_time[-1]

    cpu_idle = total_time - cpu_busy
    util = (cpu_busy / total_time) * 100
    throughput = n / total_time

    print("\nSYSTEM PERFORMANCE")
    print("CPU Busy Time:", cpu_busy)
    print("CPU Idle Time:", cpu_idle)
    print("CPU Utilization:", util)
    print("Throughput:", throughput)
    print("Average Waiting Time:", total_wt / n)
    print("Average Turnaround Time:", total_tat / n)


# ==============================
# MAIN LOOP
# ==============================

while True:
    print("\n=== Priority Scheduling (Preemptive) Scheduling Simulator ===")

    pp_algorithm()

    while True:
        again = input("\nDo you want to use the algorithm again? (Y/N): ").strip().upper()
        if again in ["Y", "N"]:
            break
        print("Please enter Y or N only.")

    if again != "Y":
        print("\nGoodbye!")
        break

    print("\n" + "-" * 60)