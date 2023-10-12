class Solution(object):
    def duplicateZeros(self, arr):
        count = 0
        ln = len(arr)
        i = 0
        
        while(i < ln and count < ln): #finding the last index which would be retained
            if(arr[i] == 0):
                count += 2
            else:
                count += 1
            i += 1
        i -= 1  #removing the last iteration of i+1 as it was over before i reached there
        rght = ln - 1 # the pointer at the right end where redacting begins
        
        if (count > ln): #handling a trialing 0
            arr[-1] = 0
            rght -= 1
            i -= 1
            
        
        while(i >= 0): #copying from the right
            arr[rght] = arr[i]
            if(arr[i] == 0):
                arr[rght - 1] = 0
                rght -= 1
            rght -= 1
            i -= 1
            
        return arr