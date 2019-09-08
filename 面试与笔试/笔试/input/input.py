import sys

'''
求a+b的和,输入格式:
a   b
'''

# for line in sys.stdin:
#     a = line.split('\t')
#     print(a[0] + a[1])

'''
求a+b的和,输入格式:
a
b
'''
# a = input()
# b = input()
# print(a + b)

'''
Input：
3
1 2 3
2 1 3
3 2 1

'''
# n = int(sys.stdin.readline().strip())
# for i in range(n):
#     line = sys.stdin.readline().strip()
#     values = list(map(int, line.split()))
#     print(values)

'''
3
1 2 3
2 3
4
'''
# n = int(sys.stdin.readline().strip())
# for i in range(n):
#     line = sys.stdin.readline().strip()
#     values = list(map(int, line.split()))
#     print(values)

'''
输入一行2 3
'''
a = input().split()
print(a)

a,b,c,d = map(int, input().split())