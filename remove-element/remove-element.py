class Solution(object):
    def removeElement(self, nums, val):
        delptr = len(nums) - 1
        actuaptr = len(nums) - 1

        while(actuaptr >= 0):
            if(nums[actuaptr] == val):
                nums[delptr], nums[actuaptr] = nums[actuaptr], nums[delptr]
                delptr -= 1
                actuaptr -= 1
                print(nums)
                continue
            else:
                actuaptr -= 1
        
        return delptr + 1