# -*- coding:utf-8 -*-
"""
题目描述
请实现一个函数用来匹配包括'.'和'*'的正则表达式。模式中的字符'.'表示任意一个字符，
而'*'表示它前面的字符可以出现任意次（包含0次）。 在本题中，匹配是指字符串的所有
字符匹配整个模式。例如，字符串"aaa"与模式"a.a"和"ab*ac*a"匹配，但是与"aa.a"和"ab*a"均
不匹配
"""
class Solution:
    # s, pattern都是字符串
    def match(self, s, pattern):
        # write code here
        if s is None or pattern is None:
            return False
        return self.match_core(s, pattern)

    def match_core(self, s, pattern):
        # 1. 两者都到尾部，返回True
        if not len(s) and not len(pattern):
            return True
        # 2. 字符串没到尾部，pattern到尾部
        if len(s) and not len(pattern):
            return False
        # 3. 当pattern的下一个字符为*时
        if len(pattern) > 1 and pattern[1] == '*':
            # 4. 如果当前字符匹配或者（当前pattern为.且s没到结尾）
            if len(s) > 0 and (s[0] == pattern[0] or pattern[0] == '.'):
                return self.match_core(s[1:], pattern[2:]) or self.match_core(s[1:], pattern) or \
                       self.match_core(s, pattern[2:])
            else:
                # 5. 当前字符不匹配  当前pattern为.且s到结尾   当前字符不为.
                return self.match_core(s, pattern[2:])
        # 6. 下一个pattern不为*时
        if len(s) > 0 and (s[0] == pattern[0] or pattern[0]=='.'):
            return self.match_core(s[1:], pattern[1:])
        return False


# print(Solution().match("aaa", "a.a"))
print(Solution().match("", "."))