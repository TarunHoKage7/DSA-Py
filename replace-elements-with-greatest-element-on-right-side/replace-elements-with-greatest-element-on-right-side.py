class Solution(object):
    def replaceElements(self, arr):
        curmax = arr[-1]
        arr[-1] = -1
        for i in range(len(arr) -2, -1, -1):
            if(arr[i] > curmax):
                curmax, arr[i] = arr[i], curmax
            else:
                arr[i] = curmax
        return arr