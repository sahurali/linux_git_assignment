import sys

def encode(message, shift):
    # Convert message to all uppercase
    message = message.upper()

    # Initialize the encoded message
    encoded_message = ""

    # Loop through each character in the message
    for char in message:
        # Check if the character is a letter
        if char.isalpha():
            # Shift the character
            shifted_char = chr((ord(char) - ord('A') + shift) % 26 + ord('A'))
            # Append the shifted character to the encoded message
            encoded_message += shifted_char

    # Add spaces after every five letters
    encoded_message = ' '.join([encoded_message[i:i+5] for i in range(0, len(encoded_message), 5)])

    # Return the encoded message
    return encoded_message

if __name__ == "__main__":
    # Check if the shift value is provided as an argument
    if len(sys.argv) < 2:
        print("Please provide the shift value as an argument.")
    else:
        try:
            shift = int(sys.argv[1])
            message = input("Enter a message: ")
            encoded_message = encode(message, shift)
            print(encoded_message)
        except ValueError:
            print("The shift value should be an integer.")
