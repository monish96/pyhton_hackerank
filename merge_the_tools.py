def merge_the_tools(string, k):
    arr = [string[i: i + k] for i in range(0, len(string), k)]
    for i in arr:
        print(''.join(
            [char for index, char in enumerate(i) if char not in i[0:index]]))


if __name__ == '__main__':
    string, k = input(), int(input())
    merge_the_tools(string, k)