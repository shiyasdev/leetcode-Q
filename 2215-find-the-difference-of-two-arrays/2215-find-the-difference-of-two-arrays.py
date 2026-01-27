class Solution(object):
    def findDifference(self, nums1, nums2):
        f_li = set(nums1)
        s_li = set(nums2)

        res = f_li - s_li
        final = s_li - f_li

        li = []

        li.append(list(res))
        li.append(list(final))

        return li