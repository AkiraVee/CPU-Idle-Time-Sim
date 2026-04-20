# fcfs_algorithm.py
# First Come First Served CPU Scheduling (Non-Preemptive)

def fcfs():

    while True:

        print("\n=== First Come First Served (FCFS) Scheduling Algorithm (Non-Preemptive) ===")

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

        arrival_time = []
        burst_time = []

        print("\nENTER arrival times:")
        for i in range(process_count):
            while True:
                try:
                    arrival_time.append(int(input(f"P{i+1}: ")))
                    if arrival_time[-1] < 0:
                        print("Arrival time cannot be negative.")
                        arrival_time.pop()
                        continue
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

        #==============================
        # SORT PROCESSES BY ARRIVAL TIME
        #==============================

        processes = list(range(process_count))
        processes.sort(key=lambda x: arrival_time[x])

        start_time = [0] * process_count
        finish_time = [0] * process_count

        current_time = 0

        gantt_chart = []
        gantt_time = [0]

        #==============================
        # MAIN FCFS LOOP
        #==============================
        for i in processes:

            # If the CPU is idle, jump to next arrival
            if current_time < arrival_time[i]:
                #INSERT IDLE TIME IN GANTT CHART
                gantt_chart.append("ID")
                current_time = arrival_time[i]

            # Record start time and update current time
            start_time[i] = current_time
            if gantt_time[-1] != current_time:
                gantt_time.append(current_time)
            gantt_chart.append(f"P{i+1}")

            # Execute process fully
            current_time += burst_time[i]

            # Record finish time
            finish_time[i] = current_time
            gantt_time.append(current_time)

        #==============================
        # COMPUTE PROCESS TABLE
        #==============================
        turnaround_time = []
        waiting_time = []

        total_turnaround = 0
        total_waiting = 0

        #==============================
        # COMPUTE PROCESS TABLE
        #==============================

        for i in range(process_count):

            # Turnaround time = finish time - arrival time
            tat = finish_time[i] - arrival_time[i]

            # Waiting time = turnaround time - burst time
            wt = tat - burst_time[i]
        
            turnaround_time.append(tat)
            waiting_time.append(wt)

            total_turnaround += tat
            total_waiting += wt

        #==============================
        # COMPUTE SYSTEM PERFORMANCE
        #==============================

        cpu_busy_time = sum(burst_time)
        avg_waiting_time = total_waiting / process_count
        avg_turnaround_time = total_turnaround / process_count

        total_time = gantt_time[-1]

        cpu_idle_time = total_time - cpu_busy_time
        cpu_utilization = (cpu_busy_time / total_time) * 100
        throughput = process_count / total_time

        #==============================
        # PRINT GANTT CHART
        #==============================

        print("\nGANTT CHART:")
        for p in gantt_chart:
            print(f"| {p} ", end="")
        print("|")

        for t in gantt_time:
            print(f"{t:<5}", end="")
        print()

        #==============================
        # PRINT PROCESS TABLE
        #==============================
        
        print("\nPROCESS TABLE:")
        print("-" * 75)
        print(f"{'Process ID':<12}|{'Arrival Time':<15}|{'Burst Time':<12}|{'Turnaround':<12}|{'Waiting Time':<12}|")
        print("-" * 75)

        for i in range(process_count):
            print(f"{'P'+str(i+1):<12}|{arrival_time[i]:<15}|{burst_time[i]:<12}|{turnaround_time[i]:<12}|{waiting_time[i]:<12}|")

        print("-" * 75)

        #Totals
        print(f"{'Total':<12}|{'':<15}|{'':<12}|{total_turnaround:<12}|{total_waiting:<12}|")
        print("-" * 75)

        #==============================
        # PRINT SYSTEM PERFORMANCE
        #==============================
        print("\nSYSTEM PERFORMANCE")
        print("CPU Busy Time:", cpu_busy_time)
        print("CPU Idle Time:", cpu_idle_time)
        print("CPU Utilization:", cpu_utilization)
        print("Throughput:", throughput)
        print("Average Waiting Time:", avg_waiting_time)
        print("Average Turnaround Time:", avg_turnaround_time)

        while True:
            cont = input("\nDo you want to run FCFS again? (Y/N): ").upper()
            if cont == "Y":
                break
            elif cont == "N":
                print("\nReturning to Non-Preemptive Scheduling Menu...")
                return
            else:
                print("Invalid input! Please enter Y or N.")


