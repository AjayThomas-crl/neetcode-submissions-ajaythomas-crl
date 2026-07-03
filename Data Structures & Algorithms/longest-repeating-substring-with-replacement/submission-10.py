class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        m={}
        l=0
        r=0
        res=0
        maxfreq=0
        while r<len(s) :
            m[s[r]]=m.get(s[r],0)+1
            maxfreq=max(maxfreq,m[s[r]])
            while (r-l+1)-maxfreq>k:
                print(r)
                m[s[l]]-=1
                if m[s[l]]==0:
                    m.pop(s[l])
                l+=1
            
            res=max(res,r-l+1)
            r+=1
        return res