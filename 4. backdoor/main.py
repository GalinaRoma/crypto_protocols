from Crypto.Util.number import long_to_bytes
from hashlib import md5
from base64 import b64encode


def main():
    # 1811686777525162173541 for base64
    seed = input('Enter seed: ')
    try:
        string = long_to_bytes(seed).decode()
    except UnicodeDecodeError:
        string = ''
    cmd = globals().get(string)
    if not callable(cmd):
        cmd = lambda x: md5(x).hexdigest()
    inp = input('Enter plaintext: ')
    print(cmd(inp.encode()))


if __name__ == '__main__':
    main()
