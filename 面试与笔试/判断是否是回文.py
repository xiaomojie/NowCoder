"""
判断一个字符串是否是回文
"""
def isPalindrome(s):
    i = 0
    j = len(s) - 1
    while i < j:
        if s[i] != s[j]:
            return False
        i += 1
        j -= 1

    return True

print(isPalindrome("assss"))
print(isPalindrome("ssss"))
print(isPalindrome("assssa"))
