n = int(input())
a = list(map(int, input().split()))
print(" ".join(map(str, [n+1-i for i in a])))