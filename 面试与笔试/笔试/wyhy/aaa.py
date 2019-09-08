import sys

line1 = list(map(int, sys.stdin.readline().strip().split(" ")))
n, m = line1[0], line1[1]
num1 = list(map(int, sys.stdin.readline().strip().split(" ")))
num2 = list(map(int, sys.stdin.readline().strip().split(" ")))
num1.sort()
num2.sort(reverse=True)

cur_sum = m - 1
res = []
diff_i = []
diff_j = []
while cur_sum >= 0:
    if len(diff_i) == len(num1):
        break
    for i in range(len(num1)):
        for j in range(len(num2)):
            if i not in diff_i and j not in diff_j and (num1[i] + num2[j]) % m == cur_sum:
                diff_i.append(i)
                diff_j.append(j)
                res.append(cur_sum)

    cur_sum -= 1
    # print res

print(' '.join([str(i) for i in res]))
