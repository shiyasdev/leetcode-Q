class Solution(object):
    def removeStars(self, s):
        l = []

        for x in s:
            if x == "*":
                if l:
                    l.pop()
            else:
                l.append(x)
        
        result = "".join(l)
        return result