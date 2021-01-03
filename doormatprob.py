"""
print(n / 2)  # 1.0
print(n // 2) # 1

if __name__ == "__main__":
    n, m = map(int, input().split())
    pattern = [('.|.'*(2 * i + 1)).center(m, '-') for i in range(n // 2)]
    print('\n'.join(pattern + ['WELCOME'. center(m, '-')] + pattern[::-1]))

"""

if __name__ == "__main__":
    n, m = map(int, input().split())
    for i in range(n):
        if i < n // 2:
            print(('.|.' * (2 * i + 1)).center(m, '-'))
        elif i == n // 2:
            print(('WELCOME'.center(m, '-')))
        elif i > n // 2:
            print(('.|.' * (2 * (n - (i + 1)) + 1)).center(m, '-'))
