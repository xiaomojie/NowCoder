import sys
T = int(input())

for i in range(T):
    res = 0
    max_score = 0
    n = input()
    er = list(map(int, sys.stdin.readline().strip().split(" ")))
    score = [0]
    left = []
    mid = [i for i in er[:2] if i == er[1]]
    right = []
    score.append(score[-1] + len(left)-len(right))
    for item in range(1, len(er)):
        if er[item] > er[item-1]:
            left += mid
            mid = [i for i in right if i == er[item]] + [er[item]]
            left += [i for i in right if i < er[item]]
            right += [i for i in right if i > er[item]]
        if er[item] < er[item-1]:
            right += (mid + [i for i in left if i > er[item]])
            mid = [i for i in left if i == er[item]] + [er[item]]
            left += [i for i in left if i < er[item]]
        score.append(score[-1]+len(left)-len(right))
    print(max(score), score[-1])
