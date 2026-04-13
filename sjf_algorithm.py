# sjf_algorithm.py
# Shortest Job First CPU Scheduling (Non-Preemptive)

def sjf():

    #==============================
    # INPUT
    #==============================

    while True:
        try:
            process_count = int(input("ENTER process count: "))
            if process_count < 1:
                print("Process count must be at least 1.")
                continue
            break
        except ValueError:
            print("Invalid input! Please enter a positive integer.")

    print("ENTER arrival times:")
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

    print("ENTER burst times:")
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

    # Track completed processes
    completed = [False] * process_count

    start_time = [0] * process_count
    finish_time = [0] * process_count

    current_time = 0
    done = 0

    gantt_chart = []
    gantt_time = [0]

    cpu_idle_time = 0

    #==============================
    # Main SJF loop
    #==============================
    while done < process_count:

        idx = -1
        min_burst = float('inf')

        # Find the shortest job among the arrived processes
        for i in range(process_count):
            if arrival_time[i] <= current_time and not completed[i]:
                if burst_time[i] < min_burst:
                    min_burst = burst_time[i]
                    idx = i

        # If no process available, CPU is Idle
        if idx == -1:
            gantt_chart.append("Idle")
            gantt_time.append(current_time)
            cpu_idle_time += 1
            current_time += 1
            continue

        # Execute selected process
        start_time[idx] = current_time
        gantt_chart.append(f"P{idx+1}")

        current_time += burst_time[idx]

        finish_time[idx] = current_time
        gantt_time.append(current_time)

        completed[idx] = True
        done += 1

    #==============================
    # COMPUTE PROCESS TABLE
    #==============================
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

    #==============================
    # COMPUTE SYSTEM PERFORMANCE
    #==============================
    cpu_busy_time = sum(burst_time)
    total_time = gantt_time[-1]

    cpu_util = (cpu_busy_time / total_time) * 100
    throughput = process_count / total_time

    #==============================
    # PRINT GANTT CHART
    #==============================
    print("\nGANTT CHART:")
    for p in gantt_chart:
        print(f"| {p} ", end="")
    print("|")

    for t in gantt_time:
        print(t, end="    ")
    print()

    #==============================
    # PRINT PROCESS TABLE
    #==============================
    print("\nPROCESS TABLE")
    print("Process\tTurnaround\tWaiting")

    for i in range(process_count):
        print(f"P{i+1}\t{turnaround_time[i]}\t\t{waiting_time[i]}")

    #==============================
    # PRINT SYSTEM PERFORMANCE
    #==============================
    print("\nSYSTEM PERFORMANCE")
    print("CPU Busy Time:", cpu_busy_time)
    print("CPU Idle Time:", cpu_idle_time)
    print("CPU Utilization:", cpu_util)
    print("Throughput:", throughput)
    print("Average Waiting Time:", total_waiting/process_count)
    print("Average Turnaround Time:", total_turnaround/process_count)


# ===============================
# MAIN LOOP - Added as per your request
# ===============================
print("=== Shortest Job First (SJF) Scheduling Simulator ===")

while True:
    sjf()

    # Ask if user wants to use the algorithm again
    while True:
        again = input("\nDo you want to use the algorithm again? (Y/N): ").strip().upper()
        
        if again in ["Y", "N", "y", "n"]:
            break
        else:
            print("Please enter Y or N only.")

    if again != "Y":
        print("\nReturning to main menu...")
        print("Goodbye!")
        break

    print("\n" + "-" * 60)