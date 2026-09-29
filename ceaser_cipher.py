# KC, ceaser cipher
encrypt_decrypt = ""
amount_shift = 0
message = ""
shifted_message = []


def ceaser_cipher(encrypt_decrypt, amount_shift, message, shifted_message):
    encrypt_decrypt = input("would you like to encrypt or decrypt? ")
    if encrypt_decrypt == "encrypt":
        amount_shift = int(input("amount of shift: "))
        message = str(input("message to be encrypt"))
        for letter in message:
            shifted_message.append(chr(ord(letter) + amount_shift))
        print(shifted_message)
    elif encrypt_decrypt == "decrypt":
        amount_shift = int(input("amount of shift"))

ceaser_cipher(encrypt_decrypt, amount_shift, message, shifted_message)