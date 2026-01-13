class Solution(object):
    def reverseWords(self, s):
        result = []

        for x in s.split(" "):
            result.append(x[::-1])

        return " ".join(result)