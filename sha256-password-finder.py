import hashlib
import logging

logging.basicConfig(level=logging.INFO, format='%(message)s')

print("SHA256 Password Finder\nWritten by [MOE EL JAMMAL AKA 0xS4k0us4]\n\n\n")

while True:
    target_hash = input("Enter the SHA256 hash to crack (64 characters): ")
    if len(target_hash) == 0:
        print("Input cannot be empty. Please try again.\n")
        continue
    elif len(target_hash) != 64:
        print("Invalid input. The SHA256 hash must be 64 characters long. Please try again.\n")
        continue
    else:
        break

password_file = "/usr/share/wordlists/rockyou.txt"
attempts = 0

with open(password_file, "r", encoding='latin-1') as password_list:
    for password in password_list:
        password = password.strip("\n").encode('latin-1')
        password_hash = hashlib.sha256(password).hexdigest()
        if password_hash == target_hash:
            logging.info("\nPassword hash found after {} attempts! \n\n{}:{}".format(attempts, password.decode('latin-1'), password_hash))
            exit()
        attempts += 1

logging.info("Password hash not found after {} attempts!".format(attempts))
