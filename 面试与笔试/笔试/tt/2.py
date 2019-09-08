n = int(input().strip())
if n == 0:
    print(0)
else:
    f = [0] * (n + 2)
    f[0] = 1
    f[2] = 1
    # f[4] = 2
    for i in range(4, n+1, 2):
        for j in range(0, i-2 + 1, 2):
            f[i] += f[j] * f[i-2-j]
    print(f[n] % 1000000007)