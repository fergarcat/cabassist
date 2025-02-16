import bcrypt
import json
import os

USER_DB = "users.json"

def load_users():
    if not os.path.exists(USER_DB):
        return {}
    with open(USER_DB, "r") as file:
        return json.load(file)

def save_users(users):
    with open(USER_DB, "w") as file:
        json.dump(users, file)

def register_user(username, password):
    users = load_users()
    if username in users:
        return "El usuario ya existe."
    hashed = bcrypt.hashpw(password.encode(), bcrypt.gensalt())
    users[username] = hashed.decode()
    save_users(users)
    return "Usuario registrado correctamente."

def authenticate_user(username, password):
    users = load_users()
    if username not in users:
        return False
    return bcrypt.checkpw(password.encode(), users[username].encode())

def delete_user(username):
    users = load_users()
    if username in users:
        del users[username]  # Eliminar el usuario del diccionario
        save_users(users)  # Guardar los cambios en users.json

def list_users():
    users = load_users()
    if users:
        print("Registered users:")
        for user in users.keys():
            print(f"- {user}")
    else:
        print("No users found.")


## Para crear el usuario admin
# usr = input("Nuevo usuario: ")
# pwd = input("Nueva contraseña: ")
# print(register_user(usr, pwd))


