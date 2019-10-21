while True:
    try:
        input()
        b = list(input().split())
        input()
        d = list(input().split())
        res = []
        for i in b:
            res.append(d.count(i))
        count = 0
        for i in d:
            if i not in b:
                count += 1
        tmp = []
        for i in range(len(b)):
            s = b[i]+" : "+str(res[i])
            tmp.append(s)
        tmp.append("Invalid : " + str(count))
        for i in tmp:
            print(i)

    except:
        break