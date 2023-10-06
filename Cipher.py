def caesar_encrypt(text, shift):
    encrypted_text = ""
    for char in text:
        if char.isalpha():
            ascii_offset = ord('a') if char.islower() else ord('A')
            encrypted_char = chr((ord(char) - ascii_offset + shift) % 26 + ascii_offset)
            encrypted_text += encrypted_char
        else:
            encrypted_text += char
    return encrypted_text

def caesar_decrypt(encrypted_text, shift):
    return caesar_encrypt(encrypted_text, -shift)

text = input("Enter the text: ")
shift = 91 % 26  # Ensure shift is in the range 0 to 25

choice = int(input("Choose an option:\n1. Encrypt\n2. Decrypt\nEnter your choice: "))

if choice == 1:
    encrypted_text = caesar_encrypt(text, shift)
    print("Encrypted text:", encrypted_text)
elif choice == 2:
    decrypted_text = caesar_decrypt(text, shift)
    print("Decrypted text:", decrypted_text)
else:
    print("Invalid choice")