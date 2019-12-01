def get_digits(num):
    return tuple(int(i) for i in str(num))


if __name__ == '__main__':
    num = int(input('>'))
    print(get_digits(num))
