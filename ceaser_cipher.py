# KC, ceaser cipher
encrypt_decrypt = ""
amount_shift = 0
message = ""
shifted_messages = []
def ceaser_cipher(encrypt_decrypt, amount_shift, message, shifted_messages,):
    encrypt_decrypt = input("would you like to encrypt or decrypt? ") .lower() .strip()
    if encrypt_decrypt == "encrypt":
        amount_shift = int(input("amount of shift: "))
        message = str(input("message to be encrypt: "))
        for letter in message:
            if letter in "abcdefghijklmnopqrstuvwxyzABCDEFGIHJKLMNOPQRSTUVWXYZ":
                if letter.isupper():
                    if (ord(letter) + amount_shift) > 90:
                        wrap = (ord(letter) + amount_shift) - 91
                        shifted_messages.append(chr((ord("A") + wrap)))
                    else:
                        shifted_messages.append(chr(ord(letter) + amount_shift))
                elif letter.islower():
                    if (ord(letter) + amount_shift) > 122:
                        wrap = (ord(letter) + amount_shift) - 123
                        shifted_messages.append(chr((ord("a") + wrap)))
                    else:
                        shifted_messages.append(chr(ord(letter) + amount_shift))
            else:
                shifted_messages.append(letter)
        print(str(shifted_messages).replace("['", "").replace("', '", "").replace("']", ""))
        return
    elif encrypt_decrypt == "decrypt":
        amount_shift = int(input("amount of shift:"))
        amount_shift *= -1
        message = str(input("message to decrypt: "))
        for letter in message:
            if letter in "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ":
                if letter.isupper():
                    if (ord(letter) + amount_shift) < 65:
                        wrap = (ord(letter) + amount_shift) - 64
                        shifted_messages.append(chr(ord("Z") + wrap))
                    else:
                        shifted_messages.append(chr(ord(letter) + amount_shift))
                elif letter.islower():
                    if (ord(letter) + amount_shift) < 97:
                        wrap = (ord(letter) + amount_shift) - 96
                        shifted_messages.append(chr(ord("z") + wrap))
                    else:
                        shifted_messages.append(chr(ord(letter) + amount_shift))
            else:
                shifted_messages.append(letter)
        print(str(shifted_messages).replace("['", "").replace("', '", "").replace("']", ""))
        return
    else:
        print("encrypt or decrypt")
ask = ""
while True:
    ask = input("would you like to use the ceasar cipher (yes or no): ") .lower() .strip()
    if ask == "yes":
        ceaser_cipher(encrypt_decrypt, amount_shift, message, shifted_messages,)
    elif ask == "no":
        break