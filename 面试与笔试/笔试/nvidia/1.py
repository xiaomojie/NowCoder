import math
count = 0
for i in range(2020, 10000+1):
    flag = True
    for j in range(2, i):
        if i % j == 0:
            flag = False
            break
    if flag:
        count += 1
print(count)
