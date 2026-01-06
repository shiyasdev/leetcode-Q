class Solution(object):
    def reverse(self, x):
        s = -1 if x < 0 else 1
        x = abs(x)

        rn = int(str(x)[::-1]) * s

        if rn < -2**31 or rn > 2**31 - 1:
            return 0
        
        return rn

        
        