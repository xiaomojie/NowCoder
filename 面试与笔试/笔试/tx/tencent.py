# import sys
# line1 = list(map(int, sys.stdin.readline().strip().split(' ')))
# n = line1[0]
# k = line1[1]
#
#
# h = list(map(int, sys.stdin.readline().strip().split(' ')))
# min_sum = float("inf")
# i = 0
# j = k
# index = 0
# while j <= len(h):
#     if min_sum > sum(h[i:j]):
#         index = i
#         min_sum = min(min_sum, sum(h[i:j]))
#     i += 1
#     j += 1
#
# print(index+1)
# import sys
# line1 = list(map(int, sys.stdin.readline().strip().split(' ')))
# n = line1[0]
# k = line1[1]
#
# h = list(map(int, sys.stdin.readline().strip().split(' ')))
# min_sum = float("inf")
# i = 0
# j = k
# index = 0
# sum_1 = sum(h[i:j])
# i += 1
# j += 1
# while j <= len(h):
#     cur_sum = sum_1 - h[i-1] + h[j-1]
#     if min_sum > cur_sum:
#         index = i
#         min_sum = min(min_sum, cur_sum)
#     i += 1
#     j += 1
#
# print(index+1)

import sys
line1 = list(map(int, sys.stdin.readline().strip().split(' ')))
n = line1[0]
k = line1[1]


h = list(map(int, sys.stdin.readline().strip().split(' ')))
# min_sum = float("inf")
i = 0
j = k-1
index = 1
min_sum = cur_sum = sum(h[i:j+1])
i += 1
j += 1

while j < len(h):
    cur_sum = cur_sum + h[j] - h[i-1]
    if min_sum > cur_sum:
        index = i
        min_sum = cur_sum
    i += 1
    j += 1

print(index+1)
