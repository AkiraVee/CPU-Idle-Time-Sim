# round_robin_algorithm.py
# Round Robin CPU Scheduling (Preemptive)

def round_robin():

    while True:

        print("\n=== Round Robin Scheduling Algorithm (Preemptive) ===")

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

        #==============================
        # INITIALIZATION
        #==============================

        remaining_burst = burst_time.copy()
        start_time = [-1] * process_count
        finish_time = [0] * process_count

        current_time = 0
        queue = []
        completed = 0
        cpu_idle_time = 0

        entered = [False] * process_count

        # Gantt as INTERVALS (IMPORTANT FIX)
        gantt_chart = []   # (label, start, end)

        #==============================
        # MAIN LOOP
        #==============================
        while completed < process_count:

            # Add newly arrived processes
            for i in range(process_count):
                if arrival_time[i] <= current_time and not entered[i]:
                    queue.append(i)
                    entered[i] = True

            # IDLE CASE (MERGED)
            if not queue:
                start = current_time
                current_time += 1
                cpu_idle_time += 1
                end = current_time

                if gantt_chart and gantt_chart[-1][0] == "ID" and gantt_chart[-1][2] == start:
                    gantt_chart[-1] = ("ID", gantt_chart[-1][1], end)
                else:
                    gantt_chart.append(("ID", start, end))

                continue

            # PROCESS EXECUTION
            current = queue.pop(0)

            if start_time[current] == -1:
                start_time[current] = current_time

            execute_time = min(time_quantum, remaining_burst[current])

            start = current_time
            current_time += execute_time
            remaining_burst[current] -= execute_time
            end = current_time

            label = f"P{current+1}"

            # MERGE SAME PROCESS BLOCKS
            if gantt_chart and gantt_chart[-1][0] == label and gantt_chart[-1][2] == start:
                gantt_chart[-1] = (label, gantt_chart[-1][1], end)
            else:
                gantt_chart.append((label, start, end))

            # Add arrivals that happened during execution
            for i in range(process_count):
                if arrival_time[i] <= current_time and not entered[i]:
                    queue.append(i)
                    entered[i] = True

            # Requeue or finish
            if remaining_burst[current] > 0:
                queue.append(current)
            else:
                finish_time[current] = current_time
                completed += 1

        #==============================
        # COMPUTE TIMES
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
        # GANTT OUTPUT 
        #==============================
        print("\nGANTT CHART:")

        for block in gantt_chart:
            print(f"| {block[0]} ", end="")
        print("|")

        for block in gantt_chart:
            print(f"{block[1]:<5}", end="")
        print(f"{gantt_chart[-1][2]:<5}")

        #==============================
        # PROCESS TABLE
        #==============================
        print("\nPROCESS TABLE")
        print("-" * 75)
        print(f"{'Process ID':<12}|{'Arrival Time':<15}|{'Burst Time':<12}|{'Turnaround':<12}|{'Waiting Time':<12}|")
        print("-" * 75)

        for i in range(process_count):
            print(f"{'P'+str(i+1):<12}|{arrival_time[i]:<15}|{burst_time[i]:<12}|{turnaround_time[i]:<12}|{waiting_time[i]:<12}|")

        print("-" * 75)
        print(f"{'Total':<12}|{'':<15}|{'':<12}|{total_turnaround:<12}|{total_waiting:<12}|")
        print("-" * 75)

        #==============================
        # SYSTEM PERFORMANCE
        #==============================
        cpu_busy_time = sum(burst_time)
        total_time = gantt_chart[-1][2]

        print("\nSYSTEM PERFORMANCE")
        print("CPU Busy Time:", cpu_busy_time)
        print("CPU Idle Time:", cpu_idle_time)
        print("CPU Utilization:", (cpu_busy_time / total_time) * 100)
        print("Throughput:", process_count / total_time)
        print("Average Waiting Time:", total_waiting / process_count)
        print("Average Turnaround Time:", total_turnaround / process_count)

        while True:
            cont = input("\nDo you want to run Round Robin again? (Y/N): ").upper()
            if cont == "Y":
                break
            elif cont == "N":
                print("\nReturning to Preemptive Scheduling Menu...")
                return
            else:
                print("Invalid input: Please enter Y or N.")
