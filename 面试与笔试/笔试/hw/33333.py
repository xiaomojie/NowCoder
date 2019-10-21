a = "1 3 2 4 3 2"
er = [int(i) for i in a.split()]
score = [0]
left = []
mid = [er[0]]
right = []
score.append(score[-1]+len(left)-len(right))
for item in range(1, len(er)):
    if er[item] > er[item-1]:
        left += mid
        mid = [i for i in right if i == er[item]] + [er[item]]
        left += [i for i in right if i < er[item]]
        right = [i for i in right if i > er[item]]
    if er[item] < er[item-1]:
        right += mid + [i for i in left if i > er[item]]
        mid = [i for i in left if i == er[item]] + [er[item]]
        left = [i for i in left if i < er[item]]
    score.append(score[-1]+len(left)-len(right))
print(max(score), score[-1])