# if __name__ == "__main__":
#     v_list = []
#     n = int(input())
#     v_list = list(map(int, input().split()))
#     v_list = set(v_list[:n])
#     for _ in range(int(input())):
#         try:
#             op_name, value = input().split()
#             if op_name == 'discard':
#                 v_list.discard(value)
#             elif op_name == 'remove':
#                 v_list.discard(value)
#         except ValueError or KeyError:
#             v_list.pop()
#             continue
#     print(v_list)
#

# ==========================================================

# n = int(input())
# s = set(map(int, input().split()))
# for i in range(int(input())):
#     eval('s.{0}({1})'.format(*input().split() + ['']))
#
# print(sum(s))

# =============================================================

n = int(input())
s = set(map(int, input().split()))
d = {"pop": s.pop, "remove": s.remove, "discard": s.discard}
for _ in range(int(input())):
    c = input().split()
    d[c[0]](int(c[1])) if len(c) > 1 else d[c[0]]()
print(sum(s))
