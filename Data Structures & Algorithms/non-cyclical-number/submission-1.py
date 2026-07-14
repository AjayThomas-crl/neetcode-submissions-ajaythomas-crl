class Solution:
    def isHappy(self, n: int) -> bool:
        ma={}
        def rec(n):
            m=n
            h=0
            if n in ma:
                return False
            while(m>0):
                d=m%10
                h+=d*d
                m=m//10
            ma[n]=h
            if h==1:
                return True
            return rec(h)
        return rec(n)
        
