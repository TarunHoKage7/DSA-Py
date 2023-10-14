class Solution(object):
    def thirdMax(self, nums):
        nums = list(set(nums))
        ln = len(nums)
        if(ln<3):
            return max(nums)

        if(nums[0] > nums[1] and nums[0] > nums[2]):
            if nums[1] < nums[2]:
                nums[1], nums[2] = nums[2], nums[1]
        elif(nums[1] > nums[0] and nums[1] > nums[2]):
            nums[0], nums[1] = nums[1], nums[0]
            if nums[1] < nums[2]:
                nums[1], nums[2] = nums[2], nums[1]
        else:
            nums[0], nums[2] = nums[2], nums[0]
            if nums[1] < nums[2]:
                nums[1], nums[2] = nums[2], nums[1]

        for i in range(3, ln):
            if(nums[i] < nums[2]):
                continue
            elif(nums[i] > nums[0]):
                nums[2] = nums[1]
                nums[1] = nums[0]
                nums[0] = nums[i]
            elif(nums[i] > nums[1]):
                nums[2] = nums[1]
                nums[1] = nums[i]
            else:
                nums[2] = nums[i]
        
        return nums[2]