class Solution(object):
    def moveZeroes(self, nums):
        zc = 0
        curptr = 0
        for i in nums:
            if i == 0:
                zc += 1
        
        i = 0
        while i < len(nums):
            if(nums[i] != 0):
                nums[curptr] = nums[i]
                curptr += 1
                i += 1
            else:
                i += 1
        
        for i in range(len(nums) - zc, len(nums)):
            nums[i] = 0