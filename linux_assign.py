import sys

def cipher(shift):
    message = input("Enter message to encode: ")
    message = message.upper()

    encoded_message = ""
    for letter in message:
        if letter.isalpha():
            shifted_letter = chr((ord(letter) - 65 + shift) % 26 + 65)
            encoded_message += shifted_letter

    output = ""
    count = 0
    for letter in encoded_message:
        output += letter
        count += 1
        if count == 5:
            output += " "
            count = 0

    print(output)

def main():
    shift = int(sys.argv[1])
    cipher(shift)
    
if __name__ == "__main__":
    shift = int(sys.argv[1])
    cipher(shift)


