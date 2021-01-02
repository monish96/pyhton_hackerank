def print_formatted(number, w):
    # your code goes here
    for i in range(1, number + 1):
        print(
            "{0} {1} {2} {3}".format(decimal_func(i, w), octal_func(i, w), hexa_func(i, w), binary_func(i, w), width=w))


def decimal_func(number, w):
    return str(number).rjust(w, ' ')


def octal_func(number, w):
    return str(oct(number).lstrip("0o").rstrip("L")).rjust(w, ' ')


def hexa_func(number, w):
    return str(hex(number).lstrip("0x").rstrip("L").upper()).rjust(w, ' ')


def binary_func(number, w):
    return str(bin(number).lstrip("0b").rstrip("L")).rjust(w, ' ')


if __name__ == '__main__':
    n = int(input())
    width = len("{0:b}".format(n))
    print_formatted(n, width)
