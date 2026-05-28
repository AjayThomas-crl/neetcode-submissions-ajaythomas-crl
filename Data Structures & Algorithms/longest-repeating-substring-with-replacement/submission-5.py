class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        l=0
        r=1
        a=0
        freq=Counter(s)
        max_c=max(freq,key=freq.get)
        while(r<len(s)):
            if(s[r]==max_c):
                a=max(a,r-l+1)
                r+=1
            elif(k>0):
                a=max(a,r-l+1)
                r+=1
                k-=1
            else:
                if(s[l]!=max_c):
                    k+=1
                l+=1
        return a
                
