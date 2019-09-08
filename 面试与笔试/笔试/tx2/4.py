import sys
n = int(input())
T = sys.stdin.readline().strip()
m = int(input())
s = []
for i in range(m):
    s.append(sys.stdin.readline().strip())

count = 0
for i in range(m):
    diff = (len(T) % len(s[i]))
    if diff != 0 and T[-diff:-1] not in s[i]:
        continue
    elif s[i] != T[:len(s[i])]:
        continue
    else:
        j = 0
        while j + len(s[i]) - 1 < len(T):
            if T[j:j+len(s[i])] != s[i]:
                break
            j += len(s[i])
        if j + len(s[i]) - 1 >= len(T) and T[j:] in s[i]:
            count += 1
            # print(s[i])
print(count)