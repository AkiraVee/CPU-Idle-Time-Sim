# non_preemptive_menu.py
import main_menu
import fcfs_algorithm
import sjf_algorithm
import npp_algorithm

def non_preemptive_menu():
    while True:
        print("\n==============================")
        print(" NON-PREEMPTIVE SCHEDULING MENU")
        print("==============================")
        print("1. FCFS")
        print("2. SJF")
        print("3. Priority Scheduling (Non-Preemptive)")
        print("4. Back")

        choice = input("\nSelect an option: ")

        if choice == "1":
            print("\nYou have selected First-Come First-Served (Non-Preemptive)")
            fcfs_algorithm.fcfs()

        elif choice == "2":
            print("\nYou have selected Shortest Job First (Non-Preemptive)")
            sjf_algorithm.sjf()
        elif choice == "3":
            print("\nYou have selected Priority Scheduling (Non-Preemptive)")
            npp_algorithm.npp_algorithm()

        elif choice == "4":
            print("Returning to main menu...")
            main_menu.main_menu()
            break

        else:
            print("Invalid choice: Must be 1, 2, 3, or 4. Please try again.")

if __name__ == "__main__":
    non_preemptive_menu()