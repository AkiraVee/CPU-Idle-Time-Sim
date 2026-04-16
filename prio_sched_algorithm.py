# prio_sched_algorithm.py
# Priority Scheduling Simulator (Non-preemptive)

def priority_scheduling():

    print("=== Priority Scheduling Simulator (Non-preemptive) ===")

    while True:

        # ==============================
        # INPUT SECTION
        # ==============================
        process_count = int(input("\nENTER process count: "))

        arrival_time = []
        burst_time = []
        priority_list = []

        print("\nENTER arrival times:")
        for i in range(process_count):
            arrival_time.append(int(input(f"P{i+1}: ")))

        print("\nENTER burst times:")
        for i in range(process_count):
            burst_time.append(int(input(f"P{i+1}: ")))

        print("\nENTER priority (lower number = higher priority):")
        for i in range(process_count):
            priority_list.append(int(input(f"P{i+1}: ")))

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
        # PROCESS TABLE
        # ==============================
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

        # ==============================
        # SYSTEM PERFORMANCE
        # ==============================
        cpu_busy_time = sum(burst_time)
        total_time = gantt_time[-1]

        cpu_idle_time = total_time - cpu_busy_time
        cpu_utilization = (cpu_busy_time / total_time) * 100
        throughput = process_count / total_time

    print("\nSystem Performance:\n")
    print(f"CPU Busy Time: {busy_time}")
    print(f"CPU Idle Time: {total_idle}")
    print(f"CPU Utilization: {utilization:.2f}%")
    print(f"Throughput: {throughput:.2f} processes/unit time")
    print(f"Average Waiting Time: {avg_wt:.2f}")
    print(f"Average Turnaround Time: {avg_tat:.2f}")


# ===============================
# MAIN
# ===============================
print("=== Priority Scheduling Simulator (Non-preemptive) ===")

while True:

    processes = get_processes()

    print_generated(processes)

    timeline = priority_sched(processes)

    print_gantt(timeline)

    compute_metrics(processes, timeline)

    again = input("\nDo you want to simulate another scheduling? (Y/N): ").strip().upper()

    if again != "Y":
        print("\nGoodbye!")
        break

    print("\n" + "-"*50)