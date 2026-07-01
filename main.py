from cipher import encrypt, decrypt

print("========== Caesar Cipher ==========")

while True:
    print("\n1. Encrypt")
    print("2. Decrypt")
    print("3. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        text = input("Enter message: ")
        shift = int(input("Enter shift value: "))
        print("Encrypted Text:", encrypt(text, shift))

    elif choice == "2":
        text = input("Enter encrypted message: ")
        shift = int(input("Enter shift value: "))
        print("Decrypted Text:", decrypt(text, shift))

    elif choice == "3":
        print("Thank you!")
        break

    else:
        print("Invalid choice!")
