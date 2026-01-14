class Solution(object):
    def sortSentence(self, s):
        arr = [""] * len(s.split())

        for w in s.split():
            arr[int(w[-1]) - 1] = w[:-1]

        result = " ".join(arr)
        return result