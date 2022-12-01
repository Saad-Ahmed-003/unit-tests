alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")


def encrypt(plain_text, shift_amount):
    cipher_text = ""
    for letter in plain_text:
        position = alphabet.index(letter)
        new_position = position + shift_amount
        cipher_text += alphabet[new_position]
    print(f"The encoded text is {cipher_text}")
    return cipher_text

#TODO-1: Create a different function called 'decrypt' that takes the 'text' and 'shift' as inputs.
def decript(plain_text, shift_amount):
#TODO-2: Inside the 'decrypt' function, shift each letter of the 'text' *backwards* in the alphabet by the shift amount and print the decrypted text.  
#e.g. 
#cipher_text = "mjqqt"
#shift = 5
#plain_text = "hello"
#print output: "The decoded text is hello"
    decript_text = ""
    for i in list(plain_text):
        position = alphabet.index(i)
        decript_text += alphabet[ position - shift_amount ]
    print(decript_text)
    return decript_text


#TODO-3: Check if the user wanted to encrypt or decrypt the message by checking the 'direction' variable.
#Then call the correct function based on that 'drection' variable. You should be able to test the code to encrypt *AND* decrypt a message.

msg = ""

if direction == "encode":
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))
    msg = encrypt(plain_text=text, shift_amount=shift)
if direction == "decode":
    msg = input("type the encoded text")
    shift = int(input("Type the shift number:\n"))
    decript(plain_text = msg, shift_amount = shift)

#encrypt(plain_text=text, shift_amount=shift)
#decript(plain_text=text, shift_amount=shift)