class Solution(object):
    def findMaxConsecutiveOnes(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        ret = 0
        cur = 0
        for i in nums:
            if(i):
                cur += 1
            else:
                if(cur > ret):
                    ret = cur
                cur = 0
        if(cur > ret):
            ret = cur
        return ret
            