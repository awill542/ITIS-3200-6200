# Online Python Compiler

import os
import hashlib
import json

HASH_FILE = "hash_table.json"


def hash_file(file_path):
    with open(file_path, "rb") as file:
        data = file.read()

    return hashlib.sha256(data).hexdigest()


def generate_table():
    folder = input("Enter directory path: ")

    hashes = {}

    for file_name in os.listdir(folder):
        file_path = os.path.join(folder, file_name)

        if os.path.isfile(file_path):
            hashes[file_path] = hash_file(file_path)

    with open(HASH_FILE, "w") as file:
        json.dump(hashes, file, indent=4)

    print("Hash table generated")


def validate_hash():
    folder = input("Enter directory path: ")

    with open(HASH_FILE, "r") as file:
        old_hashes = json.load(file)

    current_files = []

    for file_name in os.listdir(folder):
        file_path = os.path.join(folder, file_name)

        if os.path.isfile(file_path):
            current_files.append(file_path)
            new_hash = hash_file(file_path)

            if file_path not in old_hashes:
                print(file_path, "is a new file")

            elif new_hash == old_hashes[file_path]:
                print(file_path, "hash is valid")

            else:
                print(file_path, "hash is invalid")

    for file_path in old_hashes:
        if file_path not in current_files:
            print(file_path, "has been deleted")


def main():
    print("1. Generate new hash table")
    print("2. Verify hashes")

    choice = input("Choose 1 or 2: ")

    if choice == "1":
        generate_table()

    elif choice == "2":
        validate_hash()

    else:
        print("Invalid choice")


main()
