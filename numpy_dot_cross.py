from numpy import *


if __name__ == '__main__':
    n = int(input())
    a_array = []
    b_array = []
    for i in range(n):
        a_dum = list(map(int, input().split()))
        a_array.append(a_dum)
    for i in range(n):
        b_dum = list(map(int, input().split()))
        b_array.append((b_dum))
    print(dot(a_array, b_array))