import sys
def solve(eq,var='x'):
    eq1 = eq.replace("=","-(")+")"
    eq1 = eq1.replace("x","*x")
    eq1 = eq1.replace("+*x","+x")
    eq1 = eq1.replace("-*x","-x")
    eq1 = eq1.replace("(*x","(x")
    eq1 = eq1.strip("*")
    # print(eq1)
    try:
        c = eval(eq1,{var:1j})
        res = -c.real/c.imag
        if int(res) == res:
            return int(res)
      # return -c.real/c.imag
        else:
            return -1
    except:
        return  -1

line = str(sys.stdin.readline().strip())
line = line.replace("*", "")
line = line.lower()
# print(line)
print(solve(line))
# test = '10x-2x-8=x+7+4x'
# test = '2x=6'
# print(solve(test))
