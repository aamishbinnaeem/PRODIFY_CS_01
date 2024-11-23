# Simple Caesar Cipher program to encrypt or decrypt messages
# Let's get started!

def caesar_cipher(text, shift, mode):
    # This function handles both encryption and decryption
    result = ""
    for char in text:
        if char.isalpha():  # Only process letters, skip others
            # Check if the letter is uppercase or lowercase
            shift_base = 65 if char.isupper() else 97
            if mode == "encrypt":
                # Move forward by 'shift' positions
                result += chr((ord(char) - shift_base + shift) % 26 + shift_base)
            elif mode == "decrypt":
                # Move backward by 'shift' positions
                result += chr((ord(char) - shift_base - shift) % 26 + shift_base)
        else:
            # Just add non-alphabetical characters as-is
            result += char
    return result


def main():
    print("Welcome to the Caesar Cipher Program!")
    print("You can encrypt or decrypt your messages here.\n")
    
    # Ask the user what they want to do
    mode = input("Do you want to 'encrypt' or 'decrypt' a message? ").strip().lower()
    if mode not in ["encrypt", "decrypt"]:
        print("Oops! Please type 'encrypt' or 'decrypt'.")
        return

    # Get the actual message from the user
    text = input("Enter your message: ")
    
    # Get the shift value (try to ensure it's an integer)
    try:
        shift = int(input("Enter the shift value (e.g., 3): "))
    except ValueError:
        print("Hmm, that doesn't look like a number. Try again!")
        return

    # Call the cipher function and show the result
    result = caesar_cipher(text, shift, mode)
    print(f"\nYour result is: {result}")


# This ensures the program runs only when executed directly
if __name__ == "__main__":
    main()
