import hashlib


def main():
    hsh = hashlib.md5("hello".encode())
    print(hsh.hexdigest())
    pass


if __name__ == '__main__':
    main()