# coding=utf-8
# 本题为考试多行输入输出规范示例，无需提交，不计分。


import sys

if __name__ == "__main__":

    line = sys.stdin.readline().strip()
    arr = list(map(int, line.split()))
    a = arr[0]
    b = arr[1]

    low = 0
    high = a

    while low < high:
        mid = (low + high) / 2
        if abs(pow(mid, b) - a) <= float(0.000001):
            print("%.6f" % mid)
            break
        elif pow(mid, b) < a:
            low = mid
        else:
            high = mid