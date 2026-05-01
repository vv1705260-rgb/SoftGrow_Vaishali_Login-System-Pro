import getpass
import datetime
import os

FILE = "users.txt"

def check_password(password):
    if len(password) < 6:
        return False, "❌ Password must be 6+ characters"
    if not any(c.isdigit() for c in password):
        return False, "❌ Add at least 1 number"
    if not any(c.isalpha() for c in password):
        return False, "❌ Add at least 1 letter"
    return True, "✅ Strong password"

def signup():
    username = input("Create username: ")

    if os.path.exists(FILE):
        with open(FILE, "r") as f:
            for line in f:
                if line.split(",")[0] == username:
                    print("❌ Username already exists")
                    return

    while True:
        password = getpass.getpass("Create password: ")
        valid, msg = check_password(password)
        print(msg)
        if valid: break

    with open(FILE, "a") as f:
        f.write(f"{username},{password},{datetime.date.today()}\n")
    print(f"✅ Signup successful! Welcome {username}")

def login():
    attempts = 3
    while attempts > 0:
        username = input("Enter username: ")
        password = getpass.getpass("Enter password: ")

        try:
            with open(FILE, "r") as f:
                for user in f.readlines():
                    u, p, date = user.strip().split(",")
                    if username == u and password == p:
                        print(f"✅ Login success! Welcome {username}")
                        print(f"Account created on: {date}")
                        return
        except FileNotFoundError:
            print("❌ No users found. Signup first.")
            return

        attempts -= 1
        print(f"❌ Wrong password. {attempts} attempts left")
    print("🔒 Too many failed attempts")

def view_users():
    print("\n--- Registered Users ---")
    try:
        with open(FILE, "r") as f:
            users = f.readlines()
            if not users:
                print("No users yet")
                return
            for i, line in enumerate(users, 1):
                u, _, date = line.strip().split(",")
                print(f"{i}. {u} - Joined: {date}")
    except FileNotFoundError:
        print("No users yet")

while True:
    print("\n=== SoftGrowTech Login System ===")
    choice = input("1. Signup\n2. Login\n3. View All Users\n4. Exit\nChoose: ")
    if choice == "1": signup()
    elif choice == "2": login()
    elif choice == "3": view_users()
    elif choice == "4":
        print("Goodbye!")
        break
    else: print("Invalid choice")
