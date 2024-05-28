alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

choice = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n" )
message = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))

def encrypt(message, shift):
    cipher_text = ""
    for i in message:
        position = alphabet.index(i)
        new_position = position + shift
        new_letter = alphabet[new_position]
        cipher_text += new_letter
    print(f"The encoded text is: {cipher_text}")

encrypt(message=message, shift=shift)