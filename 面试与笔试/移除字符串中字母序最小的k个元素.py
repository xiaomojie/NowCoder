#coding=utf-8
# 移除字符串中字母序最小的k个元素
def remove_str(s, k):
    if not s:
        return s
    sorted_s = sorted(s)
    d = {}
    for i in range(k):
        if sorted_s[i] in d:
            d[sorted_s[i]] += 1
        else:
            d[sorted_s[i]] = 1
    res = []
    for i in range(len(s)):
        if s[i] in d.keys()and d[s[i]]!=0:
            d[s[i]] -= 1
        else:
            res.append(s[i])
    return ''.join(res)

