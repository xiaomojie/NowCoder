# 不对   有问题，还没写完
class Solution:
    def max_sub_sum(self, nums):
        if not nums:
            return 0
        res = [nums[0]]
        flag = True
        max_sum = nums[0]
        i = 1
        while i < len(nums):
            j = i
            if flag:
                while res[-1] - nums[j] > 0:
                    j += 1
                if i == j-1:
                    cur_max = nums[i]
                else:
                    cur_max = max(nums[i:j])
                res.append(cur_max)
                max_sum += cur_max
                flag = not flag
                i = j
            else:
                i += 1
                continue

        return max_sum

print(Solution().max_sub_sum([4,3,8,5,3,8]))
