encoded_password = ""
def encode(password):
    global encoded_password
    encoded_password = ''
    for digit in password:
        encoded_password += str((int(digit) + 3) % 10)
    print("The original password is", password, ", and the encoded password is", encoded_password)
    
    
def decode(encoded_password):
    decoded_password = ''
    for digit in encoded_password:
        decoded_password += str((int(digit) - 3) % 10)
    print("The encoded password is", encoded_password, ", and the original password is", decoded_password)


#Start of the loop
while True:
    #Menu with first input by user
    print("Menu \n-------------\n1. Encode\n2. Decode\n3. Quit")
    choice = int(input("Please enter an option:"))
#This is the encoder option. It encodes the password.
    if choice == 1:
        password = input("Please enter your password to encode: ")
        encode(password)
#This is the decoder option. It decodes the original encoded password.
    elif choice == 2:
        decode(encoded_password)
    elif choice == 3:
        break
