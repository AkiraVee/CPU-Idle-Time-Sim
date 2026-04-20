# preemptive_menu.py
import main_menu
import round_robin_algorithm
import srtf_algorithm
import pp_algorithm

def preemptive_menu():
    while True:
        print("\n==============================")
        print(" PREEMPTIVE SCHEDULING MENU")
        print("==============================")
        print("1. Round Robin (Preemptive)")
        print("2. Shortest Remaining Time First (SRTF)(Preemptive)")
        print("3. Priority Scheduling (Preemptive)")
        print("4. Back")

        choice = input("\nSelect an option: ")

        if choice == "1":
            print("\nYou have selected Round Robin (Preemptive)")
            round_robin_algorithm.round_robin()


        elif choice == "2":
            print("\nYou have selected Shortest Remaining Time First (Preemptive)")
            srtf_algorithm.srtf_algorithm()

        elif choice == "3":
            print("\nYou have selected Priority Scheduling (Preemptive)")
            pp_algorithm.pp_algorithm()

        elif choice == "4":
            print("\nReturning to main menu...")
            main_menu.main_menu()
            break

        else:
            print("Invalid choice: Must be 1, 2, 3, or 4. Please try again.")

if __name__ == "__main__":
    preemptive_menu()