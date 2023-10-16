class Solution(object):
    def pivotIndex(self, nums):
        arr1, arr2 = [0],[0]
        for i in range(len(nums) - 1):
            arr1.append(arr1[-1] + nums[i])
        for i in range(len(nums) - 1,0,-1):
            arr2.insert(0, arr2[0] + nums[i])
        print(arr1, arr2)
        for i in range(len(nums)):
            if arr1[i] == arr2[i]:
                return i
        return - 1
        