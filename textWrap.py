import textwrap

if __name__ == '__main__':
    s, w = input(), int(input())
    print(textwrap.fill(s, w))
