from numpy import *


if __name__ == '__main__':
    a_array = []
    b_array = []
    a_dum_array = list(map(int, input().split()))
    a_array.append(a_dum_array)
    b_dum_array = list(map(int, input().split()))
    b_array.append(b_dum_array)
    print(inner(array(a_array), array(b_array))[0][0])
    print(outer(array(a_array), array(b_array)))


