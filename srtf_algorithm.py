# srtf.py
# Shortest Remaining Time First (Preemptive - Clean Gantt Output)

def srtf():

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

    # ==============================
    # INITIALIZATION
    # ==============================

    remaining = burst_time.copy()
    finish_time = [0] * process_count

    current_time = 0
    completed = 0

    gantt_chart = []
    gantt_time = []

    last_label = None  # 🔥 prevents duplication

    # ==============================
    # MAIN LOOP
    # ==============================

    while completed < process_count:

        shortest = -1
        min_remaining = float('inf')

        for i in range(process_count):
            if arrival_time[i] <= current_time and remaining[i] > 0:
                if remaining[i] < min_remaining:
                    min_remaining = remaining[i]
                    shortest = i

        # ==============================
        # IDLE CASE
        # ==============================
        if shortest == -1:
            if last_label != "ID":
                gantt_chart.append("ID")
                gantt_time.append(current_time)
                last_label = "ID"

            current_time += 1
            continue

        process_label = f"P{shortest+1}"

        # ==============================
        # PROCESS SWITCH ONLY
        # ==============================
        if last_label != process_label:
            gantt_chart.append(process_label)
            gantt_time.append(current_time)
            last_label = process_label

        # execute 1 unit
        remaining[shortest] -= 1
        current_time += 1

        if remaining[shortest] == 0:
            finish_time[shortest] = current_time
            completed += 1

    # add final time
    gantt_time.append(current_time)

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

    total_tat = 0
    total_wt = 0

    for i in range(process_count):
        tat = finish_time[i] - arrival_time[i]
        wt = tat - burst_time[i]

        total_tat += tat
        total_wt += wt

        print(f"P{i+1}\t{tat}\t\t{wt}")

    # ==============================
    # PERFORMANCE
    # ==============================

    cpu_busy = sum(burst_time)
    total_time = gantt_time[-1]

    cpu_idle = total_time - cpu_busy
    cpu_util = (cpu_busy / total_time) * 100
    throughput = process_count / total_time

    print("\nSYSTEM PERFORMANCE:\n")
    print(f"CPU Busy Time: {cpu_busy}")
    print(f"CPU Idle Time: {cpu_idle}")
    print(f"CPU Utilization: {cpu_util:.2f}%")
    print(f"Throughput: {throughput:.2f} processes/unit time")
    print(f"Average Waiting Time: {total_wt / process_count:.2f}")
    print(f"Average Turnaround Time: {total_tat / process_count:.2f}")


# ==============================
# MAIN LOOP
# ==============================

while True:
    print("=== SRTF (Preemptive) Scheduling Simulator ===")

    srtf()

    while True:
        again = input("\nDo you want to use the algorithm again? (Y/N): ").strip().upper()

        if again in ["Y", "N"]:
            break
        else:
            print("Please enter Y or N only.")

    if again != "Y":
        print("\nGoodbye!")
        break

    print("\n" + "-" * 60)