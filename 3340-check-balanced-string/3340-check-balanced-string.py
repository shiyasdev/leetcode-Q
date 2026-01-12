class Solution(object):
    def isBalanced(self, num):
        even = 0
        odd = 0
        l = len(num)
        for x in range(l):
            d = int(num[x])
            if x % 2 == 0:
                even += d
            else:
                odd += d
        return even == odd