from collections import Counter

if __name__ == '__main__':
    v_list = []
    totalEarnings = 0
    n = int(input())
    v_list = (Counter(map(int, input().split())))
    for i in range(int(input())):
        size, price = map(int, input().split())
        if v_list[size]:
            print(price)
            totalEarnings += price
            v_list[size] -= 1
    print(totalEarnings)


