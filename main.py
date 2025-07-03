from auth import register, login
from utils import file_exists

FILE_PATH = 'users.txt'
file_exists(FILE_PATH)

def menu():
    print("\n=== User Login System ===")
    print("1. Register")
    print("2. Login")
    print("3. Exit")

while True:
    menu()
    choice = input("Choose an option: ")

    if choice == '1':
        uname = input("Enter username: ")
        pwd = input("Enter password: ")
        register(uname, pwd, FILE_PATH)
        print("✅ Registered successfully!")

    elif choice == '2':
        uname = input("Enter username: ")
        pwd = input("Enter password: ")
        if login(uname, pwd, FILE_PATH):
            print("🎉 Login successful!")
        else:
            print("❌ Login failed. Check your credentials.")

    elif choice == '3':
        print("Goodbye!")
        break

    else:
        print("Invalid choice!")
