import fcfs_algorithm
import sjf_algorithm
import round_robin_algorithm
import npp_algorithm
import pp_algorithm
import srtf_algorithm

def main_menu():

    while True:
        print("\n" + "=" * 40)
        print("   CPU SCHEDULING SIMULATOR")
        print("=" * 40)
        print("1. FCFS (Non-Preemptive)")
        print("2. SJF (Non-Preemptive)")
        print("3. Priority (Non-Preemptive)")
        print("4. Round Robin (Preemptive)")
        print("5. Priority (Preemptive)")
        print("6. SRTF (Preemptive)")
        print("7. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            while True:
                print("\nRunning FCFS...\n")
                fcfs_algorithm.fcfs()

                again = input("\nUse FCFS again? (Y/N): ").strip().upper()
                if again != "Y":
                    break

        elif choice == "2":
            while True:
                print("\nRunning SJF...\n")
                sjf_algorithm.sjf()

                again = input("\nUse SJF again? (Y/N): ").strip().upper()
                if again != "Y":
                    break

        elif choice == "3":
            while True:
                print("\nRunning Priority (Non-Preemptive)...\n")
                npp_algorithm.pp()

                again = input("\nUse again? (Y/N): ").strip().upper()
                if again != "Y":
                    break

        elif choice == "4":
            while True:
                print("\nRunning Round Robin...\n")
                round_robin_algorithm.round_robin()

                again = input("\nUse again? (Y/N): ").strip().upper()
                if again != "Y":
                    break

        elif choice == "5":
            while True:
                print("\nRunning Priority (Preemptive)...\n")
                pp_algorithm.pp()

                again = input("\nUse again? (Y/N): ").strip().upper()
                if again != "Y":
                    break

        elif choice == "6":
            while True:
                print("\nRunning SRTF...\n")
                srtf_algorithm.srtf()

                again = input("\nUse again? (Y/N): ").strip().upper()
                if again != "Y":
                    break

        elif choice == "7":
            print("Exiting...")
            break

        else:
            print("Invalid choice.")


if __name__ == "__main__":
    main_menu()