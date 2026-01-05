class Solution(object):
    def sumAndMultiply(self, n):
        if n == 0:
            return 0
        t = [ x for x in str(n) if x!= '0' ]
        a = "".join(t)
        w = int(a)
        s = sum(int(i) for i in a)
        return w * s
            
            