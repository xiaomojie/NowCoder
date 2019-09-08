# import sys
# line1 = list(map(int, sys.stdin.readline().strip().split(' ')))
# n = line1[0]
# m = line1[1]
#
# w = list(map(int, sys.stdin.readline().strip().split(' ')))
# v = list(map(int, sys.stdin.readline().strip().split(' ')))
#
# i = min(w) + 1
# while i:
#     money = m
#     for j in range(len(w)):
#         if w[j] < i:
#             money -= (i - w[j])*v[j]
#     if money >= 0:
#         i += 1
#         continue
#     else:
#         print(i - 1)
#         break


# import sys
# line1 = list(map(int, sys.stdin.readline().strip().split(' ')))
# n = line1[0]
# m = line1[1]
#
# w = list(map(int, sys.stdin.readline().strip().split(' ')))
# v = list(map(int, sys.stdin.readline().strip().split(' ')))
#
# i = min(w) + 1
# while i:
#     for j in range(len(w)):
#         if w[j] < i:
#             m -= (i - w[j])*v[j]
#             w[j] += 1
#     if m >= 0:
#         i += 1
#         continue
#     else:
#         print(i - 1)
#         break

# import sys
# line1 = list(map(int, sys.stdin.readline().strip().split(' ')))
# n = line1[0]
# m = line1[1]
#
# w = list(map(int, sys.stdin.readline().strip().split(' ')))
# v = list(map(int, sys.stdin.readline().strip().split(' ')))
#
# map_ = [list(item) for item in zip(w, v)]
# map_.sort()
# j = min(w) + 1
# # while j:
# #     for i in range(len(map_)):
# #         if map_[i][0] < j:
# #             m -= (j - map_[i][0]) * map_[i][1]
# #             map_[i][0] += 1
# #         else:
# #             break
# #     if m >= 0:
# #         j += 1
# #         continue
# #     else:
# #         print(j - 1)
# #         break
# while m >= 0:
#     for i in range(len(map_)):
#         m = m - map_[i][1]
#         map_[i][0] += 1
#         if i < len(map_)-1 and map_[i+1][0] < map_[i][0]:
#             continue
#         else:
#             break
# print(map_[0][0]-1)



# import sys
# line1 = list(map(int, sys.stdin.readline().strip().split(' ')))
# n = line1[0]
# m = line1[1]
#
# w = list(map(int, sys.stdin.readline().strip().split(' ')))
# v = list(map(int, sys.stdin.readline().strip().split(' ')))
#
# map_ = [list(item) for item in zip(w, v)]
# map_.sort()
# j = min(w) + 1
#
# while m >= 0:
#     for i in range(len(map_)):
#         m = m - map_[i][1]
#         map_[i][0] += 1
#         if i < len(map_)-1 and map_[i+1][0] < map_[i][0]:
#             continue
#         else:
#             break
# print(map_[0][0]-1)


import sys
line1 = list(map(int, sys.stdin.readline().strip().split(' ')))
n = line1[0]
m = line1[1]

w = list(map(int, sys.stdin.readline().strip().split(' ')))
v = list(map(int, sys.stdin.readline().strip().split(' ')))

the_max = max(w)
the_min = min(w)



for i in range(n):
    gap = 0
    mid = (the_max + the_min) // 2
    if w[i] < mid:
        gap += (mid - w[i]) * v[i]
    if gap == m:
        ans = mid
        break
    elif gap < m:
        the_min = mid + 1
        ans = mid
    elif gap > m:
        the_max = mid - 1
print(ans)
# map_ = [list(item) for item in zip(w, v)]
# map_.sort()
# j = min(w) + 1
#
# while m >= 0:
#     for i in range(len(map_)):
#         m = m - map_[i][1]
#         map_[i][0] += 1
#         if i < len(map_)-1 and map_[i+1][0] < map_[i][0]:
#             continue
#         else:
#             break
# print(map_[0][0]-1)
