class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        carry = 1
        i = len(digits) - 1
        while(i >= 0):
            if (digits[i] + carry == 10):
                carry = 1
                digits[i] = 0
            else:
                digits[i] += 1
                carry = 0
                return digits
            i -= 1
        if(carry):
            digits.insert(0,1)
        return digits