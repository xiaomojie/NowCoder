import sys

class solution:
    def get_ring(self,s):
        current = s[0]
        s.pop(0)
        return self.dfs(current, s)
    def dfs(self, current, s_list):
        if len(s_list) == 0:
            if current[0] == current[-1]:
                return True
            return False
        for index, each in enumerate(s_list):
            if each[0] != current[-1]:
                continue
            s = s_list.pop(index)
            if self.dfs(current[0] + each[-1], s_list):
                return True
            s_list.append(s)
        return False
if __name__ == '__main__':
    s = solution()
    string = sys.stdin.readline()
    string = string.split()
    string = [each[0] + each[-1] for each in string]
    res = s.get_ring(string)
    if res:
        print("true")
    else:
        print("false")