def get_max_substring(s):
    max_length = 0
    start = 0
    d = {}
    for i in range(len(s)):
        if s[i] in d.keys() and start <= d[s[i]]:
            start = d[s[i]] + 1
        else:
            max_length = max(max_length, i - start + 1)
        d[s[i]] = i
    return max_length


print(get_max_substring("pwwkew"))
print(get_max_substring("abcabcbb"))
print(get_max_substring("bbbbb"))


# https://www.jianshu.com/p/b28aa7ea8e5f

# 还可以使用滑窗来做
# def get_max_substring1(s):
#     d = {}
#     max_length = 0
#     i = 0
#     j = 0
#     while i < len(s) and j < len(s):
#         if s[j] in d.keys() and d[s[j]] != -1:
#             d[s[i]] = -1
#             i += 1
#         else:
#             d[s[j]] = 1
#             j += 1
#             max_length = max(max_length, j-i)
#     return max_length
#
# print(get_max_substring1("pwwkew"))
# print(get_max_substring1("abcabcbb"))
# print(get_max_substring1("bbbbb"))
# https://www.cnblogs.com/kkkky/p/7687083.html