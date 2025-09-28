def caesar_cipher(text, shift, mode='encrypt'):
    
    result = ""
    
    for char in text:
        if char.isalpha():
            #upper or lowercase letters check
            base = ord('A') if char.isupper() else ord('a')

            #if 'encrypt' shift character forward by shift amount within 26 letters of alphabet 
            if mode == 'encrypt':
                result += chr((ord(char) - base + shift) % 26 + base)
            elif mode == 'decrypt':
                result += chr((ord(char) - base - shift) % 26 + base)

        else:
            #non-alphabetical characters remain unchanged
            result += char
    return result



def main():

    print("Caesar Cipher Encryption/Decryption")
    
    #mode selection
    mode = input("Type 'encrypt' to encrypt or 'decrypt' to decrypt: ").strip().lower()
    
    #input validation
    while mode not in ['encrypt', 'decrypt']:
        mode = input("Invalid input. Please enter 'encrypt' or 'decrypt': ").strip().lower()

    #Enter the text to be encrypted/decrypted
    text = input("Enter the text: ")

    while True:
        try:
            shift = int(input("Enter the shift (key) as an integer: "))
            break
        
        except ValueError:
            print("Invalid input. Please enter an integer for the shift.")

    result = caesar_cipher(text, shift, mode)
    print(f"Result: {result}")

if __name__ == "__main__":
    main()
