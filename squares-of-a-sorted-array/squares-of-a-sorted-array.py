class Solution(object):
    def sortedSquares(self, nums):
        #or check for the turning point(if exists) and treat the left half as a reverse sorted array and apply merge sorted arrays.
        arr1 = []
        arr2 = []
        templ = len(nums)
        if(nums[0] == 0 or nums[0] > 0):
            for i in range(templ):
                nums[i] *= nums[i]
            return nums
        elif(nums[templ - 1] <= 0):
            for i in range(templ):
                nums[i] *= nums[i]
            return nums[::-1]
        else:
            f = len(nums) - 1
            i = 0
            while(i< len(nums)):
                if(nums[i] >= 0):
                    f = i
                    break
                i += 1
            for i in range(0,f):
                arr1.append(nums[i] * nums[i])
            for i in range(f,len(nums)):
                arr2.append(nums[i] * nums[i])
            j = 0
            l1 = len(arr1)
            l2 = len(arr2)
            i = len(arr1) - 1
            r = []
            while(i >= 0 and j < l2):
                if(arr1[i] <= arr2[j]):
                    r.append(arr1[i])
                    i -= 1
                else:
                    r.append(arr2[j])
                    j += 1
            if(i >= 0):
                for k in range(i,-1,-1):
                    r.append(arr1[k])
            elif(j < l2):
                for k in range(j, l2):
                    r.append(arr2[k])
            return r
        