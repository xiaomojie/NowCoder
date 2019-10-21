import sys
s = []
for i in range(4):
    s.append(input())

DAY = {'A':'MON', 'B':'TUE', 'C':'WED', 'D':'THU', 'E':'FRI', 'F':'SAT', 'G':'SUN'}
hour = {'0':'00', '1':'01', '2':'02','3':'03', '4':'04', '5':'05','6':'06', '7':'07', '8':'08',
        '9':'09', 'A':'10', 'B':'11','C':'12', 'D':'13', 'E':'14','F':'15', 'G':'16', 'H':'17',
        'I':'18', 'J':'19', 'K':'20','L':'21', 'M':'22', 'N':'23'}

count = 0
one = ""
while True:
    if s[0][count] == s[1][count]:
        if one != "":
            hh = s[0][count]
            break
        elif s[0][count] >= 'A' and s[0][count] <= 'G':
            one = s[0][count]
    count += 1
count = 0
while True:
    if s[2][count] == s[3][count] and ('A'<=s[2][count]<='Z' or 'a'<=s[2][count]<='z') and ('A'<=s[3][count]<='Z' or 'a'<=s[3][count]<='z'):
        break
    count += 1

print("%s %s:%02d" %(DAY[one], hour[hh], count))