import sys
class Solution:
    def solution(self, equation, x='x'):
        _equation = equation.replace("=", "-(")+")"
        _equation = _equation.replace("x","*x")
        _equation = _equation.replace("+*x","+x")
        _equation = _equation.replace("-*x","-x")
        _equation = _equation.replace("(*x","(x")
        _equation = _equation.strip("*")
        try:
            result = eval(_equation, {x:1j})
            res = - result.real / result.imag
            if int(res) == res:
                return int(res)
            else:
                return -1
        except:
            return  -1

line = str(sys.stdin.readline().strip())
line = line.replace("*", "")
line = line.lower()
print(Solution().solution(line))

