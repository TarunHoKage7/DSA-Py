class Solution(object):
    def sortArrayByParity(self, nums):
        actua = 0
        i = 0
        ln = len(nums)
        while(actua < ln):
            if nums[actua]%2 == 0:
                nums[i], nums[actua] = nums[actua], nums[i]
                i += 1
                actua += 1
            else:
                actua += 1
        return nums