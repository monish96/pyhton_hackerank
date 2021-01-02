"""
print numpy.poly([-1, 1, 1, 10])        #Output : [  1 -11   9  11 -10]

print numpy.roots([1, 0, -1])           #Output : [-1.  1.]

print numpy.polyint([1, 1, 1])          #Output : [ 0.33333333  0.5         1.          0.        ]

print numpy.polyder([1, 1, 1, 1])       #Output : [3 2 1]

print numpy.polyval([1, -2, 0, 2], 4)   #Output : 34

print numpy.polyfit([0,1,-1, 2, -2], [0,1,1, 4, 4], 2)


"""
import numpy


if __name__ == "__main__":
    v_list = list(map(float,input().split()))
    n = int(input())
    print(numpy.polyval(v_list, n))

