import sqlite3
import hashlib
import msvcrt  # Only for Windows password input with *

DATABASE_FILE = "users.db"


def hash_password(password):
    return hashlib.sha256(password.encode()).hexdigest()


# Simple password input with asterisks (works on Windows)
def get_password(prompt="Enter password: "):
    print(prompt, end='', flush=True)
    password = ""
    while True:
        char = msvcrt.getch()
        if char in (b'\r', b'\n'):      # Enter
            print()
            break
        elif char in (b'\x08', b'\x7f'):  # Backspace
            if password:
                password = password[:-1]
                print('\b \b', end='', flush=True)
        elif char.isalnum() or char in b'!@#$%^&*()_+-=[]{}|;:\'",.<>/?':
            password += char.decode('utf-8')
            print('*', end='', flush=True)
    return password


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
# LOGIN OR SIGN UP
# =========================
def login_or_signup():
    while True:
        print("\n==============================")
        print("   Login or User Sign Up")
        print("==============================")
        print("1. Login")
        print("2. Sign Up") 
        print("3. Exit")
        print("==============================")

        choice = input("Select options: ").strip()

        if choice == "1":
            return "login"
        elif choice == "2":
            return "signup"
        elif choice == "3":
            return "cancel"
        else:
            print("Invalid choice. Please try again.")


# =========================
# SIGN UP
# =========================
def sign_up():
    print("\n==============================")
    print("          SIGN UP")
    print("==============================")

    username = input("Enter username: ")
    password = get_password("Enter password: ")
    security_question = input("Enter security question: ")
    security_answer = input("Enter answer: ")

    conn = sqlite3.connect(DATABASE_FILE)
    cursor = conn.cursor()

    cursor.execute("SELECT username FROM users WHERE username = ?", (username,))
    if cursor.fetchone():
        print("\nPRINT: Account existing. Sign up new account")
        conn.close()
        return

    hashed_pw = hash_password(password)
    cursor.execute('''
        INSERT INTO users (username, password, security_question, security_answer)
        VALUES (?, ?, ?, ?)
    ''', (username, hashed_pw, security_question, security_answer))
    
    conn.commit()
    conn.close()
    print("\nprint: account created successfully")


# =========================
# LOGIN
# =========================
def login():
    print("\n==============================")
    print("           LOGIN")
    print("==============================")

    username = input("Enter username: ")
    password = get_password("Enter password: ") 

    conn = sqlite3.connect(DATABASE_FILE)
    cursor = conn.cursor()
    cursor.execute("SELECT password FROM users WHERE username = ?", (username,))
    result = cursor.fetchone()
    conn.close()

    if result and result[0] == hash_password(password):
        print("\nPRINT: Welcome User")
        main_menu_file()
        return True
    else:
        print("\nPRINT: Incorrect username or password. Try again.")
        forgot_or_back()
        return False


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
        return

    print(f"\nAnswer: {user[0]}")
    answer = input("Your answer: ")

    if answer.lower() == user[1].lower():
        new_password = get_password("\nINPUT: Enter new password: ")

        conn = sqlite3.connect(DATABASE_FILE)
        cursor = conn.cursor()
        hashed_pw = hash_password(new_password)
        cursor.execute("UPDATE users SET password = ? WHERE username = ?", (hashed_pw, username))
        conn.commit()
        conn.close()

        print("Password updated successfully.")
        return
    else:
        print("\nPRINT: security question Incorrect answer")
        forgot_or_back()


def forgot_or_back():
    while True:
        print("\n==============================")
        print("1. Forgot Password?")
        print("2. Back to Login")
        print("==============================")

        choice = input("Enter choice: ")

        if choice == "1":
            forgot_password()
            return
        elif choice == "2":
            return
        else:
            print("Invalid choice. Please try again.")


# =========================
# MAIN MENU
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
        elif action == "cancel":
            print("\nExiting program.........")
            break


if __name__ == "__main__":
    main()