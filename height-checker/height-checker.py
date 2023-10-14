class Solution(object):
    def heightChecker(self, arr):
        sarr = sorted(arr)
        ret = 0
        for i in range(len(arr)):
            if(sarr[i] != arr[i]):
                ret += 1
        return ret