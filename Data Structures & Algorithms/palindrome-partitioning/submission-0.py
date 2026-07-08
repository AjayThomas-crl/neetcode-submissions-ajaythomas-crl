class Solution:
    
    def partition(self, s: str) -> List[List[str]]:
        def ispalin(s):
            l=0
            r=len(s)-1
            while l<r:
                if not s[l]==s[r]:
                    return False
                l+=1
                r-=1
            return True
        res=[]
        part=[]
        def rec(i):
            if i>=len(s):
                res.append(part.copy())
                return
            for j in range (i,len(s)):
                if ispalin(s[i:j+1]):
                    part.append(s[i:j+1])
                    rec(j+1)
                    part.pop()
                
            
        rec(0)
        return res
        
