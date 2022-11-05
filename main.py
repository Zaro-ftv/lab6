def encode(password):               # function to encode user's password
    encoded_password = ""
    for digit in password:
        encoded_password = encoded_password + str((int(digit) + 3) % 10)
    return encoded_password


def decode(password):               # function to decode the user's password
    decoded_password = ""
    for digit in password:
        decoded_password = decoded_password + str((int(digit) - 3) % 10)
    return decoded_password


if __name__ == '__main__':

    while True:             # displays menu options
        print('Menu')
        print('-------------')
        print('1. Encode')
        print('2. Decode')
        print('3. Quit')
        print()

        option = int(input('Please enter an option: '))
        if 1 <= option <= 3:
            pass
        else:
            print('Error')
        if option == 1:
            password = int(input('Please enter your password to encode: '))
            print('Your password has been encoded and stored!')
        if option == 2:
            decoded_password = decode(password)
            print('The encoded password is' + decoded_password + 'and the original password is' + password + ".")
        if option == 3:
            break


