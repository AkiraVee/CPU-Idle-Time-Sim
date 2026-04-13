import sqlite3

DATABASE_FILE = "users.db"


# =========================
# INITIALIZE DATABASE
# =========================
def initialize_database():
    conn = sqlite3.connect(DATABASE_FILE)
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS users (
            username TEXT PRIMARY KEY,
            password TEXT NOT NULL,
            security_question TEXT NOT NULL,
            security_answer TEXT NOT NULL
        )
    ''')
    conn.commit()
    conn.close()


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
    print("\n==============================")
    print("          SIGN UP")
    print("==============================")

    username = input("Enter username: ")
    password = input("Enter password: ")
    security_question = input("Enter security question: ")
    security_answer = input("Enter answer: ")

    conn = sqlite3.connect(DATABASE_FILE)
    cursor = conn.cursor()

    # Check if username already exists
    cursor.execute("SELECT username FROM users WHERE username = ?", (username,))
    if cursor.fetchone():
        print("\nPRINT: Account existing. Sign up new account")
        conn.close()
        return

    # Add new user
    cursor.execute('''
        INSERT INTO users (username, password, security_question, security_answer)
        VALUES (?, ?, ?, ?)
    ''', (username, password, security_question, security_answer))
    
    conn.commit()
    conn.close()
    print("\nprint: account created successfully")


# =========================
# LOGIN: USERNAME, PASSWORD
# =========================
def login():
    print("\n==============================")
    print("           LOGIN")
    print("==============================")

    username = input("Enter username: ")
    password = input("Enter password: ") 

    conn = sqlite3.connect(DATABASE_FILE)
    cursor = conn.cursor()
    cursor.execute("SELECT password FROM users WHERE username = ?", (username,))
    result = cursor.fetchone()
    conn.close()

    if result and result[0] == password:
        print("\nPRINT: Welcome User")
        main_menu_file()
        return True
    else:
        print("\nPRINT: Incorrect username or password. Try again.")
        forgot_or_back()
        return False


# =========================
# PRESS: 1 FORGOT PASSWORD? 2 BACK TO LOGIN
# =========================
def forgot_or_back():
    while True:
        print("\n==============================")
        print("1. Forgot Password?")
        print("2. Back to Login")
        print("==============================")

        choice = input("Enter choice: ")

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
    print("\n==============================")
    print("      FORGOT PASSWORD")
    print("==============================")

    username = input("INPUT: Enter username: ")

    conn = sqlite3.connect(DATABASE_FILE)
    cursor = conn.cursor()
    cursor.execute("SELECT security_question, security_answer FROM users WHERE username = ?", (username,))
    user = cursor.fetchone()
    conn.close()

    if not user:
        print("\nprint: invalid username, try again")
        forgot_or_back()
        return

    print(f"\nAnswer: {user[0]}")
    answer = input("Your answer: ")

    if answer.lower() == user[1].lower():
        new_password = input("\nINPUT: Enter new password: ")

        conn = sqlite3.connect(DATABASE_FILE)
        cursor = conn.cursor()
        cursor.execute("UPDATE users SET password = ? WHERE username = ?", (new_password, username))
        conn.commit()
        conn.close()

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
    main()