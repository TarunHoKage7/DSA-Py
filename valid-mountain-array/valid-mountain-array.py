class Solution(object):
    def validMountainArray(self, arr):
        tp = 0 #turn point after which it'll check
        i = 1

        if(len(arr) <3):
            return False

        while(tp < 2 and i < len(arr)):
            if(tp == 0):
                if arr[i] < arr [i - 1]:
                    tp += 1
                    if(i == 1):
                        tp += 1
                elif arr[i] == arr [i - 1]:
                    return False
            elif(tp == 1):
                if arr[i] > arr[i - 1]:
                    tp += 1
                elif arr[i] == arr [i - 1]:
                    return False
            i += 1
        if(tp == 1):
            return True
        else:
            return False