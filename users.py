from storage import load_data, save_data

USERS_FILE = "users.json"

def register():
    users = load_data(USERS_FILE, [])

    username = input("Username: ")
    for u in users:
        if u["username"] == username:
            print("Username already exists.")
            return

    password = input("Password (min 6 chars): ")
    if len(password) < 6:
        print("Password too short.")
        return

    users.append({"username": username, "password": password})
    save_data(USERS_FILE, users)
    print("Registered successfully.")

def login():
    users = load_data(USERS_FILE, [])
    username = input("Username: ")
    password = input("Password: ")

    for u in users:
        if u["username"] == username and u["password"] == password:
            print("Login successful.")
            return username

    print("Invalid login.")
    return None