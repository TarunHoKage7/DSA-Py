class Solution(object):
    def merge(self, a1, m, a2, n):
        #brute force would be to copy nums2 and sort O(nlogn)
        #O(n) space would be easy as well
        ptr = m + n - 1
        p1 = m - 1
        p2 = n - 1
        
        while(ptr >= 0):
            if(p1 >= 0 and p2 >= 0):
                if(a1[p1] >= a2[p2]):
                    a1[ptr] = a1[p1]
                    p1 -= 1
                else:
                    a1[ptr] = a2[p2]
                    p2 -= 1
                ptr -= 1
            elif(p1 < 0):
                while(p2 >= 0):
                    a1[ptr] = a2[p2]
                    p2 -= 1
                    ptr -= 1
            else:
                return a1
        return a1        