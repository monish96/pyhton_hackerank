import re

if __name__ == '__main__':
    phone_numbers = []
    for _ in range(int(input())):
        phone_number = str(input())
        phone_numbers.append(phone_number)
    for i in phone_numbers:
        test = re.search('[7-9][0-9]{9}', i)
        if test and len(i) == 10:
            print('YES')
        else:
            print('NO')
