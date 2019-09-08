import sys
a = sys.stdin.readline().strip().split()
index = 0

for i in range(1, len(a)):
    if int(a[i]) < int(a[index]):
        break
    index += 1

segs = []


if index == 0:
    segs.append([])
    segs.append(a[index+1:])

    left = int(a[-1])
    right = float("+inf")

else:
    left = int(a[index])
    if index + 2 < len(a):
        right = int(a[index + 2])
    else:
        right = float("+inf")

    segs.append(a[:index + 1])
    segs.append(a[index + 2:])

print(left, right)
print(segs)


b = sys.stdin.readline().strip().split()
max_ = float("-inf")
for i in range(len(b)):
    if int(b[i]) > right:
        break
    if left <= int(b[i]) <= right:
        max_ =max(max_, int(b[i]))

if max_ == float("-inf"):
    print("NO")
else:
    if segs[0] == []:
        print(' '.join(segs[1] + [str(max_)]))
    else:
        print(' '.join(segs[0] + [str(max_)] + segs[1]))
