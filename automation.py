import os
import datetime

def show_current_time():
    now = datetime.datetime.now()
    print("Current Date & Time:", now.strftime("%Y-%m-%d %H:%M:%S"))

def list_files():
    files = os.listdir(".")
    print("Files in current directory:")
    for f in files:
        print("-", f)

def main():
    print("Python Automation Suite")
    print("1. Show current date & time")
    print("2. List files in directory")
    print("3. Exit")

    choice = input("Enter choice: ")

    if choice == "1":
        show_current_time()
    elif choice == "2":
        list_files()
    elif choice == "3":
        print("Exiting automation suite...")
    else:
        print("Invalid choice")

if __name__ == "__main__":
    main()
