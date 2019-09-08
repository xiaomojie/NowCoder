import sys
a = sys.stdin.readline().strip().split()
index = 0

for i in range(1, len(a)):
    if int(a[i]) < int(a[index]):
        break
    index += 1

# print(index)

left = int(a[index])
index += 2
if index < len(a):
    right = int(a[index])
else:
    right = float("+inf")

# print(left,right)
# print(100 < right)

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
    print(' '.join(a[:index-1] + [str(max_)] + a[index:]))
