# main_menu.py
# Main Menu for CPU Scheduling Simulator

import fcfs_algorithm
import sjf_algorithm
import round_robin_algorithm
import npp_algorithm
import pp_algorithm

def main_menu():

 while True:
        print("\n" + "=" * 40)
        print("   CPU SCHEDULING SIMULATOR")
        print("=" * 40)
        print("1. First Come First Serve (FCFS)")
        print("2. Shortest Job First (SJF)")
        print("3. Round Robin")
        print("4. Priority Scheduling")
        print("5. Exit")
        print("=" * 40)

        choice = input("Enter your choice: ")

        if choice == "1":
            print("\nRunning FCFS...\n")
            fcfs_algorithm.fcfs()

        elif choice == "2":
            print("\nRunning SJF...\n")
            sjf_algorithm.sjf()

        elif choice == "3":
            print("\nRunning Round Robin...\n")
            round_robin_algorithm.round_robin()

        elif choice == "4":
            print("\nRunning Priority Scheduling...\n")

        elif choice == "5":
            print("\nExiting program. Goodbye!")
            break

        else:
            print("\nInvalid choice. Please try again.")


# run program
if __name__ == "__main__":
    main_menu()