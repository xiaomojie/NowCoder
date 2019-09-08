# import sys
# line1 = list(map(int, sys.stdin.readline().strip().split(' ')))
# line2 = list(map(int, sys.stdin.readline().strip().split(' ')))
# line3 = list(map(int, sys.stdin.readline().strip().split(' ')))
#
# n = line1[0]
# m = line1[1]
# d = line1[2]
#
# print(2)

if __name__ == "__main__":
    from copy import copy

    nn, mm, D = map(int, input().strip().split())
    sps = list(map(int, input().strip().split()))
    father = list(map(int, input().strip().split()))

    from collections import defaultdict

    d = defaultdict(list)
    for index, node in enumerate(father):
        d[node].append(index + 2)
        d[index + 2].append(node)

    ress = [0] * (nn + 1)
    for spe in sps:
        vis = [1] + [0] * nn
        vis[spe] = 1
        depth = 0
        ress[spe] = max(ress[spe], depth)
        candis = copy(d[spe])
        while not all(vis):
            depth += 1
            new_candi = []
            for c in candis:
                if not vis[c]:
                    vis[c] = 1
                    ress[c] = max(ress[c], depth)
                    new_candi.extend(d[c])
            candis = new_candi
    res = 0
    for num in ress[1:]:
        if num <= D:
            res += 1
    print(res)