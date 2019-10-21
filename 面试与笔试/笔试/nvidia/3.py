import sys
while True:
    try:
        line = sys.stdin.readline().strip().split('.')
        line = line[::-1]
        res = 0
        for j, i in enumerate(line):
            res += 256 ** j * int(i)
        print(res)

        line = int(input())
        res = []
        for i in range(3, -1, -1):
            res.append(str(line//(256**i)%256))
        print('.'.join(res))
    except:
        break
