def encrypt(message, shift):
    encrypted_text = ""
    for char in message:
        if char.isalpha():
            ascii_offset = ord('a') if char.islower() else ord('A')
            encrypted_char = chr((ord(char) - ascii_offset + shift) % 26 + ascii_offset)
            encrypted_text += encrypted_char
        else:
            encrypted_text += char
    return encrypted_text

def decrypt(encrypted_message, shift):
    return encrypt(encrypted_message, -shift)

def main():
    message = input("Enter the message: ")
    shift = int(input("Enter the shift value: "))

    encrypted_message = encrypt(message, shift)
    print(f"Encrypted Message: {encrypted_message}")

    decrypted_message = decrypt(encrypted_message, shift)
    print(f"Decrypted Message: {decrypted_message}")

if __name__ == "__main__":
    main()
