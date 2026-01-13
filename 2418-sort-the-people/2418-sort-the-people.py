class Solution(object):
    def sortPeople(self, names, heights):
        result = list(zip(heights,names))

        result.sort(reverse=True)
        return [name for height, name in result]
        