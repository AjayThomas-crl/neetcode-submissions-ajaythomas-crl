class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        l=0
        r=0
        a=0
        while(r<len(s)):
            i=l
            j=r 
            m={}
            for x in range (i,j+1):
                
                m[s[x]]=m.get(s[x],0)+1
            p=(r-l+1)-max(m.values())
            if(p<=k):
                a=max(a,r-l+1)
                
                r+=1
                
            else:
                
                l+=1
        return a


            