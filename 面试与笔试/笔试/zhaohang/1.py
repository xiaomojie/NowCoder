import sys
s = list(sys.stdin.readline().strip())
count = [1]*len(s)

i = 0
while i < len(s):
    if i < len(s) - 1 and s[i] == 'R' and s[i+1] == s[i]: # 0
        count[i] = 0
        i += 1
    elif i > 0 and s[i] == 'L' and s[i] == s[i-1]: # -1
        count[i] = 0
        i += 1
    elif i < len(s) - 1 and s[i] == 'R' and s[i+1] == 'L':
        j = i-1
        while j >= 0 and s[j] == 'R':
            if (i-j) % 2 == 0:
                count[i] += 1
            else:
                count[i+1] += 1
            j -= 1

        j = i + 2
        while j < len(s) and s[j] == 'L':
            if (j-i) % 2 == 0:
                count[i] += 1
            else:
                count[i+1] += 1
            j += 1

        i += 2
    # elif i > 0 and s[i] == 'L' and s[i-1] == 'R':
    #     j = i + 1
    #     while j < len(s) and s[j] == 'L':
    #         if (j-i) % 2 == 0:
    #             count[i] += 1
    #         else:
    #             count[i-1] += 1
    #         j += 1
    #     i += 2
print(' '.join([str(x) for x in count]))