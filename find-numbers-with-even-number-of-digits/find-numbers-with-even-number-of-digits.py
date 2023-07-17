class Solution(object):
    def findNumbers(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        ret = 0
        for i in nums:
            if not (len(str(i))%2):
                ret += 1
        return ret