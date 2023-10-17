class Solution:
    def dominantIndex(self, nums: List[int]) -> int:
        indmax = 0
        curmax = nums[0]
        curmax2 = -1
        for i in range(0, len(nums)):
            if nums[i] > curmax2:
                if nums[i] > curmax:
                    curmax2, curmax = curmax, nums[i]
                    indmax = i
                elif(i == 0):
                    continue
                else:
                    curmax2 = nums[i]
                
        if curmax2 * 2 <= curmax:
            return indmax
        return -1