# from collections import defaultdict
#
# # n, k = 4, 3
# # nums = [int(i) for i in '1 7 2 4'.split()]
#
# n, k = 6, 9
# nums = [int(i) for i in
#         '422346306 940894801 696810740 862741861 85835055 313720373'.split()]
#
# remainders = defaultdict(int)
# for num in nums:
#     remainders[num % k] += 1
#
# max_subset, mid, visit = 0, k // 2, defaultdict(lambda: True)
# even_k = True if k % 2 == 0 else False
#
# remainders = dict(remainders)
# for rem, total in remainders.items():
#     if rem == 0 and total > 0:
#         max_subset += 1
#     elif rem == mid:
#         to_be_added = 1 if even_k else max(remainders[mid],
#                                            remainders.get(k - mid, 0))
#         max_subset += to_be_added
#         visit[k - mid] = False
#     elif visit[rem]:
#         max_subset += max(remainders[rem], remainders.get(k - rem, 0))
#         visit[k - rem] = False
#
# print(max_subset)


# n, k = 4, 3
# nums = [int(i) for i in '1 7 2 4'.split()]

n, k = 6, 9
nums = [int(i) for i in
        '422346306 940894801 696810740 862741861 85835055 313720373'.split()]

remainders = {}
for num in nums:
    rem = num % k
    remainders[rem] = remainders.get(rem, 0) + 1

max_subset, mid, visit = 0, k // 2, {}
even_k = True if k % 2 == 0 else False

for rem in remainders.keys():
    if rem == 0 and remainders[0] > 0:
        max_subset += 1
    elif rem == mid:
        to_be_added = 1 if even_k else max(remainders[mid],
                                           remainders.get(k - mid, 0))
        max_subset += to_be_added
        visit[k - mid] = False
    elif visit.get(rem, True):
        max_subset += max(remainders[rem], remainders.get(k - rem, 0))
        visit[k - rem] = False

print(max_subset)
