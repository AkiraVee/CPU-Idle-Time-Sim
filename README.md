# CPU-Idle-Time-Sim

Files and Folders for the CPU Idle Time Simulator

--------------------------------------------------------------------------------------------------------------------------------------------------------

# 04/11/2026 (Saturday Update)

Fixes:

FCFS:

- Added structure comments
- Minor improvements and added a CPU Idle Handling

To add:

- User can use the algorithm again or not
- Can go back to main menu
- Error handling
- Visualization of Idle time in Gantt Chart

SJF

- Declared cpu_idle_time
- Fixed duplicate IDLE insertion in loop
- Added missing gantt_time update
- Corrected repeated header print inside loop
- Fixed undefined variables in averages
- Standardized IDLE lab

To add:

- User can use the algorithm again or not
- Can go back to main menu
- Error handling
- Visualization of Idle time in Gantt Chart

--------------------------------------------------------------------------------------------------------------------------------------------------------


# 04/14/2026 (Monday Update)

Main Menu
 - Imported and integrated all CPU scheduling algorithms
 - 

FCFS, SJF, RR
 - Added error handling for invalid inputs
 - Added “simulate again” option after execution

Prio
 - Refactored output to match the other Algorithm style format
Login System
 - Login
 - Json -> Sqlite
 - updated "user.db"

IMPORTANT SETUP
 - Install SQLite
 - Install SQLite Viewer
 - Add extension to view .db files
 - Make sure users.db is included

To be fix:
Main Menu
 - Navigation Flow Between Algorithms
 - Improve user interaction structure

Algorithms
 - FCFS: - Idle time is not displayed in the Gantt chart
 - SJF: - Execution stops prematurely after the last burst is added
 - RR:
    - Idle time handling in the Gantt chart is inconsistent or incorrect
    - Possible incorrect computation
 - PS: Idle time handling in the Gantt chart is inconsistent or incorrect

Login
 - Need to implement change password, cancel option, otp via gmail, admin acc access

