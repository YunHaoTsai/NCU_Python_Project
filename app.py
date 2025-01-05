# app.py
from sheet import User

def main():
    users = {}  # 用戶管理 (key: username, value: User object)
    while True:
        print("\n---------------Menu---------------")
        print("1. Create a user")
        print("2. Create a sheet")
        print("3. Check a sheet")
        print("4. Change a value in a sheet")
        print("5. Change a sheet's access right")
        print("6. Collaborate with another user")
        print("7. Exit")
        print("----------------------------------")
        
        choice = input("> ")
        if choice == "1":
            username = input("Enter user name: ").strip()
            if username in users:
                print(f"User '{username}' already exists.")
            else:
                users[username] = User(username)
                print(f"User '{username}' created.")

        elif choice == "2":
            username = input("Enter user name: ").strip()
            if username in users:
                sheet_name = input("Enter sheet name: ").strip()
                sheet = users[username].create_sheet(sheet_name)
                print(f"Sheet '{sheet.name}' created for user '{username}'.")
            else:
                print(f"User '{username}' does not exist.")

        elif choice == "3":
            username = input("Enter user name: ").strip()
            sheet_name = input("Enter sheet name: ").strip()
            user = users.get(username)
            if user:
                sheet = next((s for s in user.sheets if s.name == sheet_name), None)
                if sheet:
                    print("Sheet Content:")
                    print(sheet)
                else:
                    print(f"Sheet '{sheet_name}' not found for user '{username}'.")
            else:
                print(f"User '{username}' does not exist.")

        elif choice == "4":
            username = input("Enter user name: ").strip()
            sheet_name = input("Enter sheet name: ").strip()
            row = int(input("Enter row (0-2): "))
            col = int(input("Enter column (0-2): "))
            value = input("Enter value or expression (e.g., 5 or 1+2): ").strip()
            user = users.get(username)
            if user:
                sheet = next((s for s in user.sheets if s.name == sheet_name), None)
                if sheet:
                    try:
                        sheet.change_value(row, col, value, username)
                        print("Updated Sheet Content:")
                        print(sheet)
                    except (ValueError, PermissionError) as e:
                        print("Error:", e)
                else:
                    print(f"Sheet '{sheet_name}' not found for user '{username}'.")
            else:
                print(f"User '{username}' does not exist.")

        elif choice == "5":
            username = input("Enter user name: ").strip()
            sheet_name = input("Enter sheet name: ").strip()
            target_user = input("Enter the target user: ").strip()
            access_type = input("Enter access type ('ReadOnly' or 'Editable'): ").strip()
            user = users.get(username)
            if user:
                sheet = next((s for s in user.sheets if s.name == sheet_name), None)
                if sheet:
                    try:
                        sheet.share_with_user(target_user, access_type)
                        print(f"Sheet '{sheet_name}' shared with '{target_user}' as '{access_type}'.")
                    except ValueError as e:
                        print("Error:", e)
                else:
                    print(f"Sheet '{sheet_name}' not found for user '{username}'.")
            else:
                print(f"User '{username}' does not exist.")

        elif choice == "6":
            username = input("Enter user name: ").strip()
            sheet_name = input("Enter sheet name: ").strip()
            target_user = input("Enter the user to collaborate with: ").strip()
            user = users.get(username)
            if user:
                sheet = next((s for s in user.sheets if s.name == sheet_name), None)
                if sheet:
                    user.shared_sheets.append(sheet)
                    print(f"User '{target_user}' can now access '{sheet_name}'.")
                else:
                    print(f"Sheet '{sheet_name}' not found for user '{username}'.")
            else:
                print(f"User '{username}' does not exist.")

        elif choice == "7":
            print("Exiting...")
            break

        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()