# KC, ceaser cipher
encrypt_decrypt = ""
amount_shift = 0
message = ""
shifted_messages = []
shift = ""
print(ord("Z"))
print(ord("z"))
def ceaser_cipher(encrypt_decrypt, amount_shift, message, shifted_messages, shift):
    encrypt_decrypt = input("would you like to encrypt or decrypt? ")
    if encrypt_decrypt == "encrypt":
        amount_shift = int(input("amount of shift: "))
        message = str(input("message to be encrypt: "))
        for letter in message:
            if letter in "abcdefghijklmnopqrstuvwxyzABCEFGIHJKLMNOPQRSTUVWXYZ":
                if letter.isupper():
                    if (ord(letter) + amount_shift) > 90:
                        wrap = (ord(letter) + amount_shift) - 91
                        letters = shifted_messages.append(chr((ord("A") + wrap)))
                    else:
                        letters = shifted_messages.append(chr(ord(letter) + amount_shift))
                elif letter.islower():
                    if (ord(letter) + amount_shift) > 122:
                        wrap = (ord(letter) + amount_shift) - 123
                        letters = shifted_messages.append(chr((ord("a") + wrap)))
                    else:
                        letters = shifted_messages.append(chr(ord(letter) + amount_shift))
            else:
                letters = shifted_messages.append(letter)
            shift += str(letters)
        print(shift)
        
    elif encrypt_decrypt == "decrypt":
        print("unfinished")



    elif encrypt_decrypt == "decrypt":
        amount_shift = int(input("amount of shift"))

ceaser_cipher(encrypt_decrypt, amount_shift, message, shifted_messages, shift)
