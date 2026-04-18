# srtf_algorithm.py
# Shortest Remaining Time First (Preemptive)

def srtf():

    #==============================
    # INPUT
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

    #==============================
    # INITIALIZATION
    #==============================
    remaining = burst_time.copy()
    finish_time = [0] * process_count

    current_time = 0
    done = 0
    cpu_idle_time = 0

    # MERGED GANTT STORAGE
    gantt = []  # (label, start, end)

    last_label = None
    segment_start = 0

    #==============================
    # MAIN LOOP
    #==============================
    while done < process_count:

        idx = -1
        min_remaining = float('inf')

        for i in range(process_count):
            if arrival_time[i] <= current_time and remaining[i] > 0:
                if remaining[i] < min_remaining:
                    min_remaining = remaining[i]
                    idx = i

        #==============================
        # IDLE CASE
        #==============================
        if idx == -1:
            label = "ID"

            if last_label != label:
                if last_label is not None:
                    gantt.append((last_label, segment_start, current_time))
                segment_start = current_time
                last_label = label

            current_time += 1
            cpu_idle_time += 1
            continue

        label = f"P{idx+1}"

        #==============================
        # PROCESS SWITCH
        #==============================
        if last_label != label:
            if last_label is not None:
                gantt.append((last_label, segment_start, current_time))
            segment_start = current_time
            last_label = label

        # execute 1 unit time
        remaining[idx] -= 1
        current_time += 1

        if remaining[idx] == 0:
            finish_time[idx] = current_time
            done += 1

    # flush last segment
    if last_label is not None:
        gantt.append((last_label, segment_start, current_time))

    # ==============================
    # COMPUTATION
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
    total_time = current_time

    cpu_util = (cpu_busy_time / total_time) * 100
    throughput = process_count / total_time

    #==============================
    # GANTT OUTPUT 
    #==============================
    print("\nGANTT CHART:")

    for g in gantt:
        print(f"| {g[0]} ", end="")
    print("|")

    for g in gantt:
        print(f"{g[1]:<5}", end="")
    print(f"{gantt[-1][2]:<5}")

    # ==============================
    # PROCESS TABLE
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
    print("CPU Utilization:", cpu_util)
    print("Throughput:", throughput)
    print("Average Waiting Time:", total_waiting / process_count)
    print("Average Turnaround Time:", total_turnaround / process_count)


# ==============================
# MAIN LOOP
# ==============================
while True:
    print("\n=== SRTF (Preemptive) Scheduling Simulator ===")

    srtf()

    while True:
        again = input("\nDo you want to use the algorithm again? (Y/N): ").strip().upper()
        if again in ["Y", "N"]:
            break
        print("Please enter Y or N only.")

    if again != "Y":
        print("\nReturning to main menu...")
        break

    print("\n" + "-" * 60)

if __name__ == "__main__":
    srtf()