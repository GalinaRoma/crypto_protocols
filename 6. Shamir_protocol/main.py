from itertools import cycle


def main():
    message = input("Enter message: ")

    a_key = input("Enter Alice key: ")
    message = encrypt(a_key, message)
    print("Alice encrypt message: " + message)

    b_key = input("Enter Bob key: ")
    message = encrypt(b_key, message)
    print("Bob encrypt message: " + message)

    message = decrypt(a_key, message)
    print("Alice decrypt message: " + message)

    message = decrypt(b_key, message)
    print("Bob decrypted message: " + message)
    print("Bob get original message!")


def encrypt(key: str, m: str):
    encrypted_data = ""

    for char, key_char in zip(m, cycle(key)):
        encrypted_data += chr((ord(char) + ord(key_char)) % 2048)

    return encrypted_data


def decrypt(key: str, c: str):
    decrypted_data = ""

    for char, key_char in zip(c, cycle(key)):
        decrypted_data += chr((ord(char) - ord(key_char) + 2048) % 2048)

    return decrypted_data


if __name__ == '__main__':
    main()
