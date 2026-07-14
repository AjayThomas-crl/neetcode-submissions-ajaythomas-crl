class Solution:
    def isHappy(self, n: int) -> bool:
        
        ma={}
        def rec(n):
            m=n
            h=0
            if n in ma:
                return -1
            while(m>0):
                d=m%10
                h+=d*d
                m=m//10
            ma[n]=h
            return h
        while (True):
            h=rec(n)
            if h==1:
                return True
            elif h==-1:
                return False
            rec(h)
