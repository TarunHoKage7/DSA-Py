class Solution(object):
    def findDisappearedNumbers(self, nums):
        i = 0
        while(i < len(nums)):
            index = nums[i]
            while(index != nums[index - 1]):
                temp = nums[index - 1]
                nums[index - 1] = index
                index = temp
            i += 1
        
        ret = []
        for i in range(len(nums)):
            if(i + 1 != nums[i]):
                ret.append(i + 1)
        
        return ret