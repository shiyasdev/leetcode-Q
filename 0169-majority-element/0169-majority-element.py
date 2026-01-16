class Solution(object):
    def majorityElement(self, nums):
        res = {}
        for x in nums:
            if x in res:
                res[x] += 1
            else:
                res[x] = 1
        return max(res,key=res.get)
        