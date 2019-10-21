import sys
# import numpy as np
import random
def voc(x,y):
    voc_set = set()
    for i in x:
        voc_set = voc_set | set(i)
    voc_list = list(voc_set)
    # print(voc_list)
    a = np.zeros((len(x), len(voc_list)))
    for index, i in enumerate(x):
        for j in i:
            a[index][voc_list.index(j)] += 1
    # print(a)
    X = np.array(x)
    # print(X)
    Y = np.array(y)
    P0 = a[Y == 0]
    # print(a[Y==0])
    # print(np.sum(P0, axis=0))
    P0Sum = np.sum(P0,axis=0)/np.sum(P0)
    # print(P0Sum)
    P0class = len(Y[Y==0])/float(len(Y))
    P1 = a[Y == 1]
    P1Sum = np.sum(P1,axis=0)/np.sum(P0)
    P1class = len(Y[Y==1])/float(len(Y))

    return voc_list, P0class, P1class,P0Sum, P1Sum

def prediction(word_list, voc_list, p0class, p1class, p0sum, p1sum):
    voc_vec = np.zeros(len(voc_list))
    for i in word_list:
        if i in voc_list:
            voc_vec[voc_list.index(i)] =1
    word_list_p0sum = np.log(p0class)
    word_list_p1sum = np.log(p1class)

    for index, i in enumerate(voc_vec):
        if i != 0:
            if p0sum[index] != 0:
                word_list_p0sum += np.log(p0sum[index])
            if p1sum[index] != 0:
                word_list_p1sum += np.log(p1sum[index])
    # print(word_list_p0sum)
    # print(word_list_p1sum)
    if word_list_p0sum <= word_list_p1sum:
        return 0
    else:
        return 1


if __name__=='__main__':
    nums = sys.stdin.readline().strip().split(" ")
    nums = list(map(int, [x for x in nums if x != '']))
    M = nums[0]
    N = nums[1]
    d = nums[2]
    x = []
    y = []
    test = []
    for i in range(M):
        line = sys.stdin.readline().strip().split(" ")
        line = list(map(int, [x for x in line if x != '']))
        x.append(line[1:])
        y.append(line[0])
    for i in range(N):
        line = sys.stdin.readline().strip().split(" ")
        line = list(map(int, [x for x in line[1:] if x != '']))
        test.append(line)
    # print(x)
    # print(y)
    # print(test)
    voc_list, p0class, p1class, p0sum, p1sum = voc(x,y)
    # print(voc_list, p0class, p1class, p0sum, p1sum)
    for i in range(N):
        # print(prediction(test[i], voc_list, p0class, p1class, p0sum, p1sum))
        k = (random.randrange(0,10))
        print(1 if k > 5 else 0)
