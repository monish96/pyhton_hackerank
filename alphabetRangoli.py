"""
Alphabet rangoli

# print(''.join([alpha[(n - 1) - i].center(round(n // 2), '-') for i in range(n)] + [alpha[n - j].center(round(n // 2), '-') for j in range(0, n)][::-1]))
    # print(''.center(round(n // 2), '-') + '-'.join([alpha[(n - 1) - i] for i in range(0, n, 1)]) + '-' + '-'.join([alpha[(n - 1) - i] for i in range(0, n - 1, 1)])[::-1] + ''.center(round(n // 2), '-'))

    # import string

# alpha = string.ascii_lowercase
#
# n = int(input())
# L = []
# for i in range(n):
#     s = "-".join(alpha[i:n])
#     L.append((s[::-1] + s[1:]).center(4 * n - 3, "-"))
# print('\n'.join(L[:0:-1] + L))
"""
import string

if __name__ == "__main__":
    n = int(input())
    alpha = list(string.ascii_lowercase)
    final = []
    for i in range(n):
        final.append(((("-".join(alpha[i:n]))[::-1]) + (("-".join(alpha[i:n]))[1:])).center(4 * n - 3, "-"))
    print('\n'.join(final[:0:-1] + final))

