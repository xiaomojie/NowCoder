import sys
n = int(input().strip())
arr = list(map(int, sys.stdin.readline().strip().split(' ')))

res = 0
tmp = sorted(arr, reverse=True)
end = n
for i in range(n):
    if end > 0:
        index = "".join([str(x) for x in arr[0:end]]).rfind(str(tmp[i]))
        res += tmp[i] * sum(range(index+1,end+1))
        end = index
    else:
        break
    print(i)

print(res%1000000007)
