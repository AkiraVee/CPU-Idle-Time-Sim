import sqlite3
import hashlib
import msvcrt  # Only for Windows password input with *
import os

# NOTE:
# The database file was being created in unexpected directories because of two issues:
#
# 1) The database path must be anchored to this script’s location, not the current
#    working directory. Using os.path.abspath(__file__) ensures SQLite always uses
#    the same users.db file regardless of how the program is run.
#
# 2) Defining DATABASE_FILE = "users.db" again later in the file overwrote the correct
#    absolute path and caused SQLite to silently create a new database elsewhere.
#    There must be ONLY ONE definition of DATABASE_FILE.
#
# Correct usage:
# BASE_DIR = os.path.dirname(os.path.abspath(__file__))
# DATABASE_FILE = os.path.join(BASE_DIR, "users.db")

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DATABASE_FILE = os.path.join(BASE_DIR, "users.db")

# >>> ADD FOR ADMIN <<<
# Reserved administrator username
ADMIN_USERNAME = "admin"


# =========================
# >>> UI ADDITION <<<
# Consistent section header display
# =========================
def display_header(title):
    print("\n==============================")
    print(f"{title:^30}")
    print("==============================")


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


# >>> ADD FOR ADMIN <<<
# Safely add role column if missing
def add_role_column_if_missing():
    conn = sqlite3.connect(DATABASE_FILE)
    cursor = conn.cursor()

    cursor.execute("PRAGMA table_info(users)")
    columns = [c[1] for c in cursor.fetchall()]

    if "role" not in columns:
        cursor.execute(
            "ALTER TABLE users ADD COLUMN role TEXT DEFAULT 'user'"
        )
        conn.commit()

    conn.close()


# >>> ADD FOR ADMIN <<<
# Create default admin account automatically
def create_default_admin():
    conn = sqlite3.connect(DATABASE_FILE)
    cursor = conn.cursor()

    cursor.execute(
        "SELECT username FROM users WHERE username = ?",
        (ADMIN_USERNAME,)
    )

    if not cursor.fetchone():
        cursor.execute('''
            INSERT INTO users (
                username, password,
                security_question, security_answer,
                role
            )
            VALUES (?, ?, ?, ?, ?)
        ''', (
            ADMIN_USERNAME,
            hash_password("admin123"),
            "Default admin question",
            "admin",
            "admin"
        ))
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
        print(f"\nSelect options: {choice}")  # >>> UI ADDITION <<<

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
    display_header("SIGN UP")  # >>> UI ADDITION <<<

    username = input("Enter username: ")

     # >>> ADD FOR ADMIN <<<
    # Prevent use of reserved admin username
    if username.lower() == ADMIN_USERNAME:
        print("This username is reserved.")
        return
    
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

    cursor.execute('''
        INSERT INTO users VALUES (?, ?, ?, ?, ?)
    ''', (
        username,
        hash_password(password),
        security_question,
        security_answer,
        "user"
    ))

    conn.commit()
    conn.close()
    print("\nprint: account created successfully")


# =========================
# LOGIN
# =========================
def login():
    display_header("LOGIN")  # >>> UI ADDITION <<<

    username = input("Enter username: ")
    password = get_password("Enter password: ") 

    conn = sqlite3.connect(DATABASE_FILE)
    cursor = conn.cursor()

    # >>> ADD FOR ADMIN <<<
    cursor.execute(
        "SELECT password, role FROM users WHERE username = ?",
        (username,)
    )
    result = cursor.fetchone()
    conn.close()

    if result and result[0] == hash_password(password):
        if result[1] == "admin":
            admin_menu()
        else:
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
    display_header("FORGOT PASSWORD")  # >>> UI ADDITION <<<1

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
# ADMIN MENU
# =========================
def admin_menu():
    while True:
        display_header("ADMIN MENU")  # >>> UI ADDITION <<<
        print("1. View users")
        print("2. Reset user password")
        print("3. Promote user to admin")
        print("4. Logout")

        choice = input("Select: ")

        if choice == "1":
            view_users()
        elif choice == "2":
            reset_user_password()
        elif choice == "3":
            promote_user()
        elif choice == "4":
            break
        else:
            print("Invalid choice.")


# =========================
# ADMIN FEATURE 1
# =========================
def view_users():
    display_header("USERS LIST")
    conn = sqlite3.connect(DATABASE_FILE)
    cursor = conn.cursor()
    cursor.execute("SELECT username, role FROM users")
    for u in cursor.fetchall():
        print(f"- {u[0]} ({u[1]})")
    conn.close()


# =========================
# ADMIN FEATURE 2
# =========================
def reset_user_password():
    display_header("RESET PASSWORD")
    username = input("User to reset password: ")
    temp_password = "Temp123"

    conn = sqlite3.connect(DATABASE_FILE)
    cursor = conn.cursor()
    cursor.execute(
        "UPDATE users SET password = ? WHERE username = ?",
        (hash_password(temp_password), username)
    )
    conn.commit()
    conn.close()

    print("Password reset to temporary password: Temp123")


# =========================
# ADMIN FEATURE 3
# =========================
def promote_user():
    display_header("PROMOTE USER")
    username = input("Username to promote: ")

    conn = sqlite3.connect(DATABASE_FILE)
    cursor = conn.cursor()
    cursor.execute(
        "UPDATE users SET role = 'admin' WHERE username = ?",
        (username,)
    )
    conn.commit()
    conn.close()

    print("User promoted to admin (if user exists).")


# =========================
# MAIN MENU
# =========================
def main_menu_file():
    display_header("MAIN MENU FILE")  # >>> UI ADDITION <<<
    print("You have successfully entered the main menu.")
    print("(This is where your next file/system will continue.)")


# =========================
# START
# =========================
def main():
    initialize_database()
    add_role_column_if_missing()     # >>> ADD FOR ADMIN <<<
    create_default_admin()           # >>> ADD FOR ADMIN <<<

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