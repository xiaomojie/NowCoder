s = input()
s_list = s.split()
s_min = s_list[-1]
s_new = ""
for i in s_list[0]:
    if i in s_min:
        s_new += "*"
    else:
        s_new += i
print(s_new)