import json
import os

DATABASE_FILE = "users.json"


# =========================
# INITIALIZE DATABASE
# =========================
def initialize_database():
    if not os.path.exists(DATABASE_FILE):
        with open(DATABASE_FILE, "w") as file:
            json.dump({}, file)


def load_users():
    with open(DATABASE_FILE, "r") as file:
        return json.load(file)


def save_users(users):
    with open(DATABASE_FILE, "w") as file:
        json.dump(users, file, indent=4)


# =========================
# PRINT: LOGIN OR SIGN UP
# =========================
def login_or_signup():
    while True:
        print("\n==============================")
        print("   Login or User Sign Up")
        print("==============================")
        print("1. Login")
        print("2. Sign Up")

        choice = input("Select option (1 or 2): ")

        if choice == "1":
            return "login"
        elif choice == "2":
            return "signup"
        else:
            print("Invalid choice. Please try again.")


# =========================
# SIGN UP YOUR CREDENTIALS
# =========================
def sign_up():
    users = load_users()

    print("\n==============================")
    print("          SIGN UP")
    print("==============================")

    username = input("Enter username: ")
    password = input("Enter password: ")
    security_question = input("Enter security question: ")
    security_answer = input("Enter answer: ")

    # < Credentials already exist? >
    if username in users:
        print("\nPRINT: Account existing. Sign up new account")
        return

    # Add credentials to database
    users[username] = {
        "password": password,
        "security_question": security_question,
        "security_answer": security_answer
    }

    save_users(users)
    print("\nprint: account created successfully")


# =========================
# LOGIN: USERNAME, PASSWORD
# =========================
def login():
    users = load_users()

    print("\n==============================")
    print("           LOGIN")
    print("==============================")

    username = input("Enter username: ")
    password = input("Enter password: ")

    # < User enters correct credentials? >
    if username in users and users[username]["password"] == password:
        print("\nPRINT: Welcome User")
        main_menu_file()
        return True
    else:
        print("\nPRINT: Incorrect username or password. Try again.")
        forgot_or_back()
        return False


# =========================
# PRESS: 1 FORGOT PASSWORD?
# 2 BACK TO LOGIN
# =========================
def forgot_or_back():
    while True:
        print("\n==============================")
        print("1. Forgot Password?")
        print("2. Back to Login")
        print("==============================")

        choice = input("Enter choice: ")

        # < if you press 1 >
        if choice == "1":
            forgot_password()
            break
        elif choice == "2":
            return
        else:
            print("Invalid choice. Please try again.")


# =========================
# FORGOT PASSWORD
# =========================
def forgot_password():
    users = load_users()

    print("\n==============================")
    print("      FORGOT PASSWORD")
    print("==============================")

    username = input("INPUT: Enter username: ")

    # < if username is correct? >
    if username not in users:
        print("\nprint: invalid username, try again")
        forgot_or_back()
        return

    print(f"\nAnswer: {users[username]['security_question']}")
    answer = input("Your answer: ")

    # < if security question is correct? >
    if answer.lower() == users[username]["security_answer"].lower():
        new_password = input("\nINPUT: Enter new password: ")

        # UPDATE password in database
        users[username]["password"] = new_password
        save_users(users)

        print("\nINPUT: Enter new password, to update your password")
        print("Password updated successfully.")
        return
    else:
        print("\nPRINT: security question Incorrect answer")
        forgot_or_back()


# =========================
# PENTAGON D - MAIN MENU FILE
# =========================
def main_menu_file():
    print("\n==============================")
    print("     MAIN MENU FILE")
    print("==============================")
    print("You have successfully entered the main menu.")
    print("(This is where your next file/system will continue.)")


# =========================
# START
# =========================
def main():
    initialize_database()

    while True:
        action = login_or_signup()

        if action == "signup":
            sign_up()
        elif action == "login":
            login()


if __name__ == "__main__":
    main() # edit 
    # i love roara's big tits