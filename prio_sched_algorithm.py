# prio_sched_algorithm.py
# Priority Scheduling Simulator (Non-preemptive)

def priority_scheduling():

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
    current_time = 0

    start_time = [0] * process_count
    finish_time = [0] * process_count

    gantt_chart = []
    gantt_time = [0]

    done = 0

    # ==============================
    # MAIN SCHEDULING LOOP
    # ==============================

    while done < process_count:

        ready = [
            i for i in range(process_count)
            if arrival_time[i] <= current_time and not completed[i]
        ]

        # CPU IDLE
        if not ready:
            gantt_chart.append("IDLE")
            current_time += 1
            gantt_time.append(current_time)
            continue

        # pick highest priority (lowest number)
        idx = ready[0]
        for i in ready:
            if priority_list[i] < priority_list[idx]:
                idx = i

        start_time[idx] = current_time
        gantt_chart.append(f"P{idx+1}")

        current_time += burst_time[idx]
        finish_time[idx] = current_time
        gantt_time.append(current_time)

        completed[idx] = True
        done += 1

    # ==============================
    # OUTPUT SECTION
    # ==============================

    print("\nGANTT CHART:")
    for p in gantt_chart:
        print(f"| {p} ", end="")
    print("|")

    for t in gantt_time:
        print(f"{t:<5}", end="")
    print()

    print("\nPROCESS TABLE")
    print("Process\tTurnaround\tWaiting")

    total_turnaround = 0
    total_waiting = 0

    for i in range(process_count):
        tat = finish_time[i] - arrival_time[i]
        wt = tat - burst_time[i]

        total_turnaround += tat
        total_waiting += wt

        print(f"P{i+1}\t{tat}\t\t{wt}")

    # ==============================
    # SYSTEM PERFORMANCE
    # ==============================

    cpu_busy_time = sum(burst_time)
    total_time = gantt_time[-1]

    cpu_idle_time = total_time - cpu_busy_time
    cpu_utilization = (cpu_busy_time / total_time) * 100
    throughput = process_count / total_time

    print("\nSYSTEM PERFORMANCE:\n")
    print(f"CPU Busy Time: {cpu_busy_time}")
    print(f"CPU Idle Time: {cpu_idle_time}")
    print(f"CPU Utilization: {cpu_utilization:.2f}%")
    print(f"Throughput: {throughput:.2f} processes/unit time")
    print(f"Average Waiting Time: {total_waiting / process_count:.2f}")
    print(f"Average Turnaround Time: {total_turnaround / process_count:.2f}")


# ==============================
# MAIN LOOP
# ==============================

while True:
    print("=== Priority Scheduling (Non-Preemptive) Scheduling Simulator ===")

    priority_scheduling()

    while True:
        again = input("\nDo you want to use the algorithm again? (Y/N): ").strip().upper()

        if again in ["Y", "N"]:
            break
        else:
            print("Please enter Y or N only.")

    if again != "Y":
        print("\nReturning to main menu...")
        print("Goodbye!")
        break

    print("\n" + "-" * 60)