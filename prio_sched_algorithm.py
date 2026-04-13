# prio_sched_algorithm.py
# Priority Scheduling Simulator (Non-preemptive)

#==============================
# INPUT SECTION
#==============================

print("=== Priority Scheduling Simulator (Non-preemptive) ===")

while True:

    process_count = int(input("\nENTER process count: "))

    arrival_time = []
    burst_time = []
    priority = []

    print("\nENTER arrival times:")
    for i in range(process_count):
        arrival_time.append(int(input(f"P{i+1}: ")))

    print("\nENTER burst times:")
    for i in range(process_count):
        burst_time.append(int(input(f"P{i+1}: ")))

    print("\nENTER priority (lower number = higher priority):")
    for i in range(process_count):
        priority.append(int(input(f"P{i+1}: ")))


    #==============================
    # INITIALIZATION
    #==============================
    processes = list(range(process_count))
    completed = [False] * process_count

    current_time = 0

    start_time = [0] * process_count
    finish_time = [0] * process_count

    gantt_chart = []
    gantt_time = [0]


    #==============================
    # MAIN SCHEDULING LOOP
    #==============================
    done = 0

    while done < process_count:

        # find ready processes
        ready = []

        for i in range(process_count):
            if arrival_time[i] <= current_time and not completed[i]:
                ready.append(i)

        # CPU IDLE
        if len(ready) == 0:
            gantt_chart.append("IDLE")
            current_time += 1
            gantt_time.append(current_time)
            continue

        # pick highest priority (lowest number)
        idx = ready[0]

        for i in ready:
            if priority[i] < priority[idx]:
                idx = i

        start_time[idx] = current_time
        gantt_chart.append(f"P{idx+1}")

        current_time += burst_time[idx]
        finish_time[idx] = current_time

        gantt_time.append(current_time)

        completed[idx] = True
        done += 1


    #==============================
    # PROCESS TABLE
    #==============================
    print("\nGANTT CHART:")

    for p in gantt_chart:
        print(f"| {p} ", end="")
    print("|")

    for t in gantt_time:
        print(t, end="    ")
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


    #==============================
    # SYSTEM PERFORMANCE
    #==============================
    cpu_busy_time = sum(burst_time)
    total_time = gantt_time[-1]

    cpu_idle_time = total_time - cpu_busy_time
    cpu_utilization = (cpu_busy_time / total_time) * 100
    throughput = process_count / total_time

    avg_waiting_time = total_waiting / process_count
    avg_turnaround_time = total_turnaround / process_count


    print("\nSYSTEM PERFORMANCE")
    print("CPU Busy Time:", cpu_busy_time)
    print("CPU Idle Time:", cpu_idle_time)
    print("CPU Utilization:", cpu_utilization)
    print("Throughput:", throughput)
    print("Average Waiting Time:", avg_waiting_time)
    print("Average Turnaround Time:", avg_turnaround_time)


    #==============================
    # SIMULATE AGAIN
    #==============================
    again = input("\nDo you want to simulate another scheduling? (Y/N): ").strip().upper()

    if again in ["Y", "N", "y", "n"]:
            break
    else:
            print("Please enter Y or N only.")

    if again != "Y":
        print("\nReturning to main menu...") 
        break
    print("\n" + "-" * 50)