class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        n=len(digits)
        c=False
        for i in range(n-1,-1,-1):
            if i==n-1 or c:
                a=digits[i]+1
                if a>9:
                    c=True
                    digits[i]=a%10
                else:
                    c=False
                    digits[i]=a
        if c:
            digits=[1]+digits
        return digits
            