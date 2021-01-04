from itertools import permutations

n, m = input().split()
v_permutation = list(permutations(n, int(m)))
for i in sorted(permutations(n, int(m))):
    print(''.join(i))

