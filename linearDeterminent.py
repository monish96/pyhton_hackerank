import numpy

if __name__ == "__main__":
    v_matrix = []
    for _ in range(int(input())):
        temp = list(map(float, input().split()))
        v_matrix.append(temp)
    print(round(numpy.linalg.det(v_matrix), 2))
