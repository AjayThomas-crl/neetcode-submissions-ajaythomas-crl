class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        l=0
        r=0
        a=0
        m={}
        m[s[r]]=1
        while(r<len(s)):
            p=(r-l+1)-max(m.values())
            if(p<=k):
                a=max(a,r-l+1)
                r+=1
                if(r<len(s)):
                    m[s[r]]=m.get(s[r],0)+1
            else:
                m[s[l]]-=1
                l+=1
        return a


            