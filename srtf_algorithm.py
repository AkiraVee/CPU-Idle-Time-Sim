# srtf.py
# Shortest Remaining Time First (Preemptive)

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

    remaining_burst = burst_time.copy()
    start_time = [-1] * process_count
    finish_time = [0] * process_count

    current_time = 0
    completed = 0

    gantt_chart = []
    gantt_time = [0]

    # ==============================
    # MAIN SCHEDULING LOOP
    # ==============================

    while completed < process_count:

        shortest = -1
        min_remaining = float('inf')

        for i in range(process_count):
            if arrival_time[i] <= current_time and remaining_burst[i] > 0:
                if remaining_burst[i] < min_remaining:
                    min_remaining = remaining_burst[i]
                    shortest = i

        # CPU IDLE
        if shortest == -1:
            gantt_chart.append("IDLE")
            current_time += 1
            gantt_time.append(current_time)
            continue

        if start_time[shortest] == -1:
            start_time[shortest] = current_time

        gantt_chart.append(f"P{shortest+1}")
        current_time += 1
        remaining_burst[shortest] -= 1
        gantt_time.append(current_time)

        if remaining_burst[shortest] == 0:
            finish_time[shortest] = current_time
            completed += 1

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
# MAIN LOOP (same style as yours)
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
        print("\nReturning to main menu...")
        print("Goodbye!")
        break

    print("\n" + "-" * 60)