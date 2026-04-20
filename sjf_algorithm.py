# sjf_algorithm.py
# Shortest Job First CPU Scheduling (Non-Preemptive)

def sjf():

    while True:

        print("\n=== Shortest Job First (SJF) Scheduling Algorithm (Non-Preemptive) ===")

        # ==============================
        # INPUT
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

        # ==============================
        # INITIALIZATION
        # ==============================

        completed = [False] * process_count
        start_time = [0] * process_count
        finish_time = [0] * process_count

        current_time = 0
        done = 0
        cpu_idle_time = 0

        gantt_chart = []
        gantt_time = [0]   # start timeline only ONCE


        while done < process_count:

            idx = -1
            min_burst = float('inf')

            # pick shortest job available
            for i in range(process_count):
                if arrival_time[i] <= current_time and not completed[i]:
                    if burst_time[i] < min_burst:
                        min_burst = burst_time[i]
                        idx = i

            # ==============================
            # IDLE CASE
            # ==============================
            if idx == -1:

                next_arrival = min(
                    arrival_time[i]
                    for i in range(process_count)
                    if not completed[i]
                )

                if current_time < next_arrival:
                    gantt_chart.append("ID")
                    cpu_idle_time += next_arrival - current_time
                    current_time = next_arrival
                    gantt_time.append(current_time)

                continue

            # ==============================
            # PROCESS EXECUTION
            # ==============================
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

        # ==============================
        # PRINT GANTT CHART
        # ==============================

        print("\nGANTT CHART:")

        for p in gantt_chart:
            print(f"| {p} ", end="")
        print("|")

        for t in gantt_time:
            print(f"{t:<5}", end="")
        print()

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
        
        # Totals
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

        while True:
            cont = input("\nDo you want to run SJF again? (Y/N): ").upper()
            if cont == "Y":
                break
            elif cont == "N":
                print("Returning to Non-Preemptive Scheduling Menu...")
                return
            else:
                print("Invalid input: Must be Y or N. Please try again.")
