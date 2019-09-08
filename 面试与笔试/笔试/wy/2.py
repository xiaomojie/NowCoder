t = int(input())
for i in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    a = sorted(a, reverse=True)
    if a[0] < a[1] + a[2]:
        print("YES")
    else:
        print("NO")

