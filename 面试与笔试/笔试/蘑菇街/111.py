# # coding=utf-8
# for i in range(1):
#     filename = "{0:03d}.txt".format(i)  # 这样子就可以输出文件名是001～009，然后
#     print filename
#     f = open(filename, 'r')
#     lines = f.readlines()   # lines保存文件中所有的行
#     for line in lines:
#         numbers = list(map(float, line.strip().split(',')))  # 比如说一行有8个数字，以空格分隔，这里会把这8个数字转换成int型放在数组number中[1,2,3,4,5,6,7,8]
#         print(numbers[1])
#
#
# #coding=utf-8
# import cv
#
# f = open("000.txt",'r')
#
# lines = f.readlines()
#
# for line in lines:
#     numbers = list(map(float,line.strip().split(',')))
#     print(numbers)
#     flame = numbers[0]
#     oid = numbers[1]
#     sx1 = numbers[2]
#     sx2=numbers[2]+numbers[4]
#     sy1=numbers[3]
#     sy2=numbers[3]+numbers[5]
#     name = "000001"
#     im = cv.imread("data/000004.png")  # 读取指定路径图片
#     cv2.rectangle(im, (int(sx1), int(sy1)), (int(sx2), int(sy2)), (0, 255, 0), 3)
#     if (sy1 > 10):
#         cv2.putText(im, oid, (int(sx1), int(sy1 - 6)), cv2.FONT_HERSHEY_COMPLEX_SMALL, 0.8, (0, 255, 0))
#     else:
#         cv2.putText(im, oid, (int(sx1), int(sy1 + 15)), cv2.FONT_HERSHEY_COMPLEX_SMALL, 0.8, (0, 255, 0))
#     # cv2.imshow('MultiTracker', frame)#也可以存储
#     cv2.imwrite("image/000000.png", gray)
#     break



#coding=utf-8
import sys

def max_seq(nums):
    dp = [float("-inf")] * len(nums)
    for i in range(len(nums)):
        if i == 0:
            dp[i] = nums[i]
        else:
            dp[i] = dp[i-1] + nums[i]
    max_len = 0
    dic = {}
    for j in range(len(dp)):
        if dp[j] in dic.keys():
            max_len = max(max_len, j - dic[dp[j]])
        else:
            dic[dp[j]] = j
    return max_len

print max_seq([0,-1,1,3,-3])