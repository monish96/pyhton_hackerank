import numpy


if __name__ == '__main__':
    i, j = input().split()
    _twodarray = []
    for x in range(int(i)):
        v_push = map(int, input().split())
        _twodarray.append(list(v_push))
    print(numpy.mean(numpy.array(_twodarray), axis=1))
    print(numpy.var(numpy.array(_twodarray), axis=1))
    print(numpy.std(numpy.array(_twodarray), axis=None))
