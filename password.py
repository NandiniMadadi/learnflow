import os
import json
import getpass
import secrets
from cryptography.fernet import Fernet

# File to store encrypted passwords
PASSWORD_FILE = "passwords.json"

# Key for encryption (should be stored securely in a real application)
KEY = Fernet.generate_key()
cipher_suite = Fernet(KEY)

def generate_strong_password(length=16):
    alphabet = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!@#$%^&*()-_=+"
    return ''.join(secrets.choice(alphabet) for _ in range(length))

def encrypt_password(plaintext, cipher):
    ciphertext = cipher.encrypt(plaintext.encode())
    return ciphertext.decode()

def decrypt_password(ciphertext, cipher):
    plaintext = cipher.decrypt(ciphertext.encode())
    return plaintext.decode()

def load_passwords():
    if os.path.exists(PASSWORD_FILE):
        with open(PASSWORD_FILE, "r") as file:
            return json.load(file)
    return {}

def save_passwords(passwords):
    with open(PASSWORD_FILE, "w") as file:
        json.dump(passwords, file, indent=4)

def add_password(category, service, username, password):
    passwords = load_passwords()
    if category not in passwords:
        passwords[category] = {}
    encrypted_password = encrypt_password(password, cipher_suite)
    passwords[category][service] = {"username": username, "password": encrypted_password}
    save_passwords(passwords)
    print(f"Password for {service} added successfully under {category} category.")

def retrieve_password(category, service):
    passwords = load_passwords()
    if category in passwords and service in passwords[category]:
        encrypted_password = passwords[category][service]["password"]
        username = passwords[category][service]["username"]
        decrypted_password = decrypt_password(encrypted_password, cipher_suite)
        return username, decrypted_password
    else:
        print(f"No password found for {service} under {category} category.")
        return None, None

def main():
    while True:
        print("\nPassword Manager")
        print("1. Add a new password")
        print("2. Retrieve a password")
        print("3. Generate a strong password")
        print("4. Exit")
        choice = input("Enter your choice: ")

        if choice == "1":
            category = input("Enter the category: ")
            service = input("Enter the service name: ")
            username = input("Enter the username: ")
            password = getpass.getpass("Enter the password: ")
            add_password(category, service, username, password)

        elif choice == "2":
            category = input("Enter the category: ")
            service = input("Enter the service name: ")
            username, password = retrieve_password(category, service)
            if username and password:
                print(f"Username: {username}\nPassword: {password}")

        elif choice == "3":
            length = int(input("Enter the desired length for the password: "))
            print("Generated password: ", generate_strong_password(length))

        elif choice == "4":
            print("Exiting...")
            break

        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
      main()