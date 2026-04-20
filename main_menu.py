# main_menu.py

import preemptive_menu
import non_preemptive_menu
import sys   # Needed for proper exit

def main_menu():
    while True:
        print("\n====================================")
        print(" CPU SCHEDULING MAIN MENU")
        print("====================================")
        print("A. Preemptive")
        print("B. Non-Preemptive")
        print("C. Exit")

        choice = input("\nSelect (A/B/C): ").upper()

        if choice == "A":
            print("\nYou selected Preemptive Scheduling")
            preemptive_menu.preemptive_menu()

        elif choice == "B":
            print("\nYou selected Non-Preemptive Scheduling")
            non_preemptive_menu.non_preemptive_menu()

        elif choice == "C":
            print("\nExiting...")
            sys.exit(0)  # Proper exit with status code 0

        else:
            print("\nInvalid choice: Must be A, B, or C. Please try again.")


if __name__ == "__main__":
    main_menu()