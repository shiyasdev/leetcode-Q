class Solution(object):
    def differenceOfSum(self, nums):
        t = sum(nums)
        res = 0
        for i in nums:
            for x in str(i):
                res += int(x)
        return abs(t - res)