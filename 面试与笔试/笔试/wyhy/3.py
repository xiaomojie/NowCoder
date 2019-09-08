n = int(input())
for i in range(n):
    s = input().strip()
    index = []
    for j in range(len(s)):
        if s[j] != "N":
            index.append(j)
    if len(index) < 3:
        print(len(s))
    else:
        if index[0] != 0:
            index = [0] + index
        if index[-1] != len(s) - 1:
            index = index + [len(s) - 1]

        print(index)
        diff = []
        k = 1
        while k < len(index):
            diff.append(index[k] - index[k-1])
            k += 1
        print(diff)
        max_len = 0
        i = 0
        j = 3

        while j <= len(diff):
            max_len = max(max_len, sum(diff[i:j]))
            i += 1
            j += 1
        print(max_len)

'''
4
NNTN
NNNNGGNNNN
NGNNNNGNNNNNNNNSNNNN
NGNNNNGNNNNNNNNSNNNNS
'''