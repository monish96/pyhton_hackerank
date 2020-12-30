"""
A nested list is a list that contains another list (i.e.: a list of lists).
It is also referred to as a multi-dimensional array. For example, a 2 dimensional array is used below:

nested_list = [['blue', 'green'], ['red', 'black'], ['blue', 'white']]
print len(nested_list)
# prints 3
print nested_list[1]
# prints ['red', 'black']
print nested_list[1][0]
# prints red


sorted(iterable, key=key, reverse=reverse)

Note: You cannot sort a list that contains BOTH string values AND numeric values.

float('inf')
As stated in answer above, float('inf') is used for setting a variable with an infinitely large value.

In simple words, it sets the value as +ve infinty.


"""


def find_second_lowest_grades(array):
    all_grades = []
    all_names = []
    for i in range(0, len(array)):
        all_grades.append(array[i][1])
    v_second_lowest_score = second_smallest(list(set(all_grades)))
    for j in range(0, len(array)):
        if array[j][1] == v_second_lowest_score:
            all_names.append(array[j][0])
    temp = sorted(all_names)
    print(temp)
    for k in temp:
        print(k)
        # print(v_second_lowest_score)


def second_smallest(numbers):
    m1, m2 = float('inf'), float('inf')
    for x in numbers:
        if x <= m1:
            m1, m2 = x, m1
        elif x < m2:
            m2 = x
    return m2


if __name__ == '__main__':
    nested_array = []
    for _ in range(int(input())):
        name = input()
        score = float(input())
        nested_array.append([name, score])
    find_second_lowest_grades(nested_array)
