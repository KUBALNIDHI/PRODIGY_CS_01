def encrypt(text, shift):
    result = ""
    for char in text:
        if char.isupper():
            result += chr((ord(char) + shift - 65) % 26 + 65)
        elif char.islower():
            result += chr((ord(char) + shift - 97) % 26 + 97)
        else:
            result += char
    return result

def decrypt(text, shift):
    return encrypt(text, -shift)

print("Caesar Cipher Program")
choice = input("Do you want to Encrypt or Decrypt? (e/d): ").lower()

message = input("Enter your message: ")
shift = int(input("Enter the shift value (number): "))

if choice == 'e':
    encrypted = encrypt(message, shift)
    print("Encrypted Message:", encrypted)
elif choice == 'd':
    decrypted = decrypt(message, shift)
    print("Decrypted Message:", decrypted)
else:
    print("Invalid choice! Use 'e' to encrypt or 'd' to decrypt.")
