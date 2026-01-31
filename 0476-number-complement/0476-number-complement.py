class Solution(object):
    def findComplement(self, num):
        b = num.bit_length()

        m = (1 << b ) - 1

        return num ^ m
        