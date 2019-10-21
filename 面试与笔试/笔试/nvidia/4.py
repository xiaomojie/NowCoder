class Solution:
    def __init__(self):
        self.can = {}
        self.count = 0
    def AddCandidate(self, pCandidateName):

        if not pCandidateName.isalpha():
            return 0
        if pCandidateName in self.can.keys():
            return 0
        self.can[pCandidateName] = 0
        self.count += 1
    def Vote(self, pCandidateName):
        if pCandidateName in self.can.keys():
            self.can[pCandidateName] += 1
    def GetVoteResult(self,pCandidateName):
        if not pCandidateName:
            return None
        return self.can[pCandidateName]
    def clear(self):
        pass


s = Solution()
a = int(input())
b = input().split(' ')
c = int(input())
d = input().split(' ')
for i in range(a):
    s.AddCandidate(b[i])
for j in range(c):
    s.Vote(d[j])
for i in range(a):
    print(b[i] + " : " + str(s.GetVoteResult(b[i])))
print("Invalid : " + str(s.count))



