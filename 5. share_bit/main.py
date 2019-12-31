from secrets import randbits
from Crypto.Cipher import AES
from hashlib import md5


def main():
    print("Storing bit by symmetric encryption")
    encrypt()
    print()
    print("Storing bit by hashing")
    hashing()


def encrypt():
    key = randbits(16 * 8)
    r = randbits(15 * 8 + 7)
    b = randbits(1)
    input_bytes = r << 1 | b
    aes = AES.new(key.to_bytes(16, "big"))
    encrypted_data = aes.encrypt(input_bytes.to_bytes(16, "big"))
    print("Alice send to Bob: " + str(encrypted_data) + "," + str(r))
    b2 = randbits(1)
    print("Bob send to Alice: " + str(b2))
    print("Alice send to Bob: " + str(key))
    decrypted_date = aes.decrypt(encrypted_data)
    b3 = int.from_bytes(decrypted_date, "big") & 1
    print("Bob decrypt data and get " + str(b3))
    if b2 == b3:
        print("bits are the same")
    else:
        print("bits are different")


def hashing():
    r1 = randbits(7 * 8)
    r2 = randbits(8 * 8)
    b = randbits(1)
    print(b)
    input_bytes = r1 << 8 * 8 | r2 << 1 | b
    hashed_data = md5(input_bytes.to_bytes(16, "big"))
    print("Alice send to Bob: " + str(hashed_data) + "," + str(r1))
    b2 = randbits(1)
    print("Bob send to Alice: " + str(b2))
    print("Alice send to Bob: " + str(r2))
    input_bytes2 = r1 << 8 * 8 | r2 << 1 | b2
    hashed_data2 = md5(input_bytes2.to_bytes(16, "big"))
    if hashed_data.hexdigest() == hashed_data2.hexdigest():
        print("bits are the same")
    else:
        print("bits are different")


if __name__ == '__main__':
    main()
