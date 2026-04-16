# srtf.py
# Shortest Remaining Time First (Preemptive)


def srtf():

    
    process_count = int(input("ENTER process count: "))

    arrival_time = []
    burst_time = []

    print("ENTER arrival times:")
    for i in range(process_count):
        arrival_time.append(int(input(f"P{i+1}: ")))

    print("ENTER burst times:")
    for i in range(process_count):
        burst_time.append(int(input(f"P{i+1}: ")))


    
    remaining_burst = burst_time.copy()
    start_time = [-1] * process_count
    finish_time = [0] * process_count

    current_time = 0
    completed = 0

    gantt_chart = []
    gantt_time = [0]


    
    while completed < process_count:

        shortest = -1
        min_remaining = float('inf')

        
        for i in range(process_count):
            if arrival_time[i] <= current_time and remaining_burst[i] > 0:
                if remaining_burst[i] < min_remaining:
                    min_remaining = remaining_burst[i]
                    shortest = i

       
        if shortest == -1:
            current_time += 1
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


   
    avg_waiting_time = total_waiting / process_count
    avg_turnaround_time = total_turnaround / process_count

    cpu_busy_time = sum(burst_time)
    total_time = gantt_time[-1]

    cpu_idle_time = total_time - cpu_busy_time
    cpu_utilization = (cpu_busy_time / total_time) * 100
    throughput = process_count / total_time


  
    print("\nGANTT CHART:")
    for p in gantt_chart:
        print(f"| {p} ", end="")
    print("|")

    for t in gantt_time:
        print(t, end="    ")
    print()


 
    print("\nPROCESS TABLE")
    print("Process\tTurnaround\tWaiting")

    for i in range(process_count):
        print(f"P{i+1}\t{turnaround_time[i]}\t\t{waiting_time[i]}")


 ;'an56'
    print("\nSYSTEM PERFORMANCE")
    print("CPU Busy Time:", cpu_busy_time)
    print("CPU Idle Time:", cpu_idle_time)
    print("CPU Utilization:", cpu_utilization)
    print("Throughput:", throughput)
    print("Average Waiting Time:", avg_waiting_time)
    print("Average Turnaround Time:", avg_turnaround_time)



srtf()
