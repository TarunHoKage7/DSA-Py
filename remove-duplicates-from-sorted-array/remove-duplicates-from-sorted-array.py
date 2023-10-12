class Solution(object):
    def removeDuplicates(self, nums):
        dpval = nums[0]
        apval = nums[0]
        delptr = 1
        actuaptr = 1
        while(actuaptr <= len(nums) - 1):
            if(nums[actuaptr] > apval):
                apval = nums[actuaptr]
                nums[delptr] = apval
                actuaptr += 1
                delptr += 1
                continue
            else:
                actuaptr += 1
                continue
        return delptr