import hashlib

def hash_password(password):
    return hashlib.sha256(password.encode()).hexdigest()

def register(username, password, filepath):
    hashed = hash_password(password)
    with open(filepath, 'a') as file:
        file.write(f"{username},{hashed}\n")
    return True

def login(username, password, filepath):
    hashed = hash_password(password)
    with open(filepath, 'r') as file:
        users = file.readlines()
        for user in users:
            stored_user, stored_pass = user.strip().split(',')
            if stored_user == username and stored_pass == hashed:
                return True
    return False
