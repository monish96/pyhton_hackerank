"""
Consider a list (list = []). You can perform the following commands:

insert i e: Insert integer  at position .
print: Print the list.
remove e: Delete the first occurrence of integer .
append e: Insert integer  at the end of the list.
sort: Sort the list.
pop: Pop the last element from the list.
reverse: Reverse the list.
Initialize your list and read in the value of  followed by  lines of commands where each command will be of the  types listed above. Iterate through each command in order and perform the corresponding operation on your list.
"""

v_list = []


def insert(position, integer):
    v_list.insert(position, integer)


def extend(another_list):
    v_list.extend(another_list)


def append(integer):
    v_list.append(integer)


def remove(integer):
    v_list.remove(integer)


def pop():
    v_list.pop()


def index(position):
    v_list.index(position)


def count(integer):
    v_list.count(integer)


def sort():
    v_list.sort()


def reverse():
    v_list.reverse()


def printf():
    print(v_list)


def switcher(operation_name, index=0):
    switch = {
        'insert': insert,
        'print': printf,
        'remove': remove,
        'append': append,
        'sort': sort,
        'pop': pop,
        'reverse': reverse
    }
    func = switch.get(operation_name)
    return func(position=index, integer=0)


if __name__ == '__main__':
    for _ in range(int(input())):
        operations = input().split()
        if operations[0] == 'insert':
            insert(int(operations[1]), int(operations[2]))
        elif operations[0] == 'remove':
            remove(int(operations[1]))
        elif operations[0] == 'print':
            printf()
        elif operations[0] == 'append':
            append(int(operations[1]))
        elif operations[0] == 'sort':
            sort()
        elif operations[0] == 'pop':
            pop()
        elif operations[0] == 'reverse':
            reverse()
        else:
            printf()
