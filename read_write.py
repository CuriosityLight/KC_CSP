# KC, reading and writing to files

with open("practice.txt", "r") as file:
    content = file.read()
    content = content + "\nYUMMYY"


with open("practice.txt", "a") as file:
    file.write("\nBROWNIES AND COOKIEEESS")
# a, w, r, r+

with open("practice.txt", "r+") as file:
    content = file.read()
    content = "cupcakes" + content + "\nYUMMYY"
    file.write(content)
# reading and appending