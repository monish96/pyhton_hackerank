def solve(s):
    text = s
    for x in s.split():
        text = text.replace(x, x.capitalize())
    return text

if __name__ == '__main__':
    s = input()
    print(solve(s))
