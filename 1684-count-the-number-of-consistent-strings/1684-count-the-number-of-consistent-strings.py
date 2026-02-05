class Solution(object):
    def countConsistentStrings(self, allowed, words):
        """
        :type allowed: str
        :type words: List[str]
        :rtype: int
        """

        count = 0

        for x in words:
            valid = True
            for i in x:
                if i not in allowed:
                    valid = False
                    break
            if valid:
                count += 1

        return count