"""
股票买卖两次的最大获利
"""
import sys
class Solution:
    def max_profit(self, prices):
        minprice = float('inf')
        maxprice = float('-inf')
        maxprofit1 = [0]*len(prices)
        maxprofit2 = [0]*len(prices)
        for i in range(len(prices)):
            if prices[i] < minprice:
                minprice = prices[i]
            else:
                maxprofit1[i] = prices[i] - minprice

        for i in range(len(prices)-1, -1, -1):
            if prices[i] > maxprice:
                maxprice = prices[i]
            else:
                maxprofit2[i] = maxprice - prices[i]

        res = 0
        for i in range(len(prices)):
            # print(maxprofit1[i],maxprofit2[i] )
            res = max(res, max(maxprofit1[:i+1]) + max(maxprofit2[i:]))
        return res

nums = list(map(int, sys.stdin.readline().strip().split(" ")))
print(Solution().max_profit(nums))
