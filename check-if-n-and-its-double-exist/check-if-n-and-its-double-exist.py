class Solution(object):
    def checkIfExist(self, arr):
        ht = {}
        for i in arr:
            if i not in ht:
                ht[i] = 1
            else:
                ht[i] += 1

        for i in arr:
            if(i != i*2):
                if i*2 in ht:
                    return True
            else:
                if ht[i] >= 2:
                    return True
        return False