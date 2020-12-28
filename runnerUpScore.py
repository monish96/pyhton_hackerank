"""
find the runner up score
===================================================================================
map() function returns a map object(which is an iterator) of the results
after applying the given function to each item of a given iterable (list, tuple etc.)
===================================================================================
"""


def return_runner_up_score(number, array):
    if number > 2:
        # first_max = max(array[0], array[1])
        second_max = min(array[0], array[1])
        if len(array) >= 2:
            if len(array) > 2:
                processed_array = array[0: number]
                z_set = list(processed_array)
                first_max = max(z_set[0], z_set[1])
                second_max = min(z_set[0], z_set[1])
                for i in range(2, len(processed_array)):
                    if processed_array[i] > first_max:
                        second_max = first_max
                        first_max = processed_array[i]
                    elif second_max < processed_array[i] != first_max:
                        second_max = processed_array[i]
                return second_max
            else:
                return second_max
        else:
            return -1


if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())
    print(return_runner_up_score(n, list(set(arr))))
