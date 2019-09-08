"""
求一个字符串中的最长回文子串
"""

# 法一：暴力法，求出所有的子串，然后在看每个子串是否是回文 O(n^3)

# 法二：中心法，以每一个字母为中心，向两边扩展，判断是否是回文，要分成奇数和偶数两种情况 O(n^2)

# 法三：动态规划，设状态dp[j][i]表示索引j到索引i的子串是否是回文串，转移方程为：
'''
            true    j == i
dp[j][i] =  s[i] == s[j]  i-j == 1
            s[i] == s[j] and dp[j+1][i-1]   i-j > 1
            
则dp[j][i]为true时表示索引j到索引i形成的子串为回文子串，且子串起点索引为j,长度为i - j + 1。
算法时间复杂度为O(N ^ 2)。
'''
# https://www.jianshu.com/p/c82cada7e5b0

# 法1
def longestPalindrome1(s):
    # s = list(s)
    max_len = 1
    start = 0
    for i in range(len(s)):
        for j in range(i+1, len(s)):
            if list(s[i:j+1]) == list(reversed(s[i:j+1])):
                if j - i + 1 > max_len:
                    max_len = j - i + 1
                    start = i
    return max_len, s[start: start+max_len]

# 法2
def longestPalindrome2(s):
    # 长度为
    max_len = 1
    start = 0
    for i in range(len(s)):
        j = i - 1
        k = i + 1
        while j >= 0 and k < len(s) and s[j] == s[k]:
            if k - j + 1 > max_len:
                start = j
                max_len = k - j + 1

            j -= 1
            k += 1

    for i in range(len(s)):
        j = i
        k = i + 1
        while j >= 0 and k < len(s) and s[j] == s[k]:
            if k - j + 1 > max_len:
                start = j
                max_len = k - j + 1
            j -= 1
            k += 1

    return max_len, s[start:start+max_len]

# 法3
def longestPalindrome(s):
    dp = [[0]*len(s) for i in range(len(s))]
    max_len = 1
    start = 0
    for i in range(len(s)):
        for j in range(i+1):
            if i - j < 2:
                dp[j][i] = (s[i] == s[j])
            else:
                dp[j][i] = (s[i] == s[j] and dp[j+1][i-1])

            if dp[j][i] and i-j+1 > max_len:
                max_len = i-j+1
                start = j
    return max_len, s[start:start+max_len]



print(longestPalindrome("a"))
print(longestPalindrome("aba"))
print(longestPalindrome("abccba"))
print(longestPalindrome("ab"))
print(longestPalindrome("abb"))
print(longestPalindrome("abca"))



