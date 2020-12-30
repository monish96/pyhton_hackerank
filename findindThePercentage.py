"""
A dictionary is a data type which stores values in pairs. For each element in the dictionary,
there is a unique key that points to a value. A dictionary is mutable. It can be changed.
For example:

a_dict = {'one': 1} # Here 'one' is the key.
"""


def find_average_of_a_key(query_name, student_marks):
    student_obj = student_marks.get(query_name)
    formatted_float = "{:.2f}".format(sum(student_obj)/len(student_obj))
    return formatted_float


if __name__ == '__main__':
    n = int(input())
    student_marks = {}
    for _ in range(n):
        name, *line = input().split()
        scores = list(map(float, line))
        student_marks[name] = scores
    query_name = input()
    print(find_average_of_a_key(query_name, student_marks))
