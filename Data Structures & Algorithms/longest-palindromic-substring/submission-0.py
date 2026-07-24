class Solution:
    def longestPalindrome(self, s: str) -> str:
        r=len(s)
        i=0
        malen=0
        ma=""
        while (i<len(s)):
            l=i
            r=i
            while l>-1 and r<len(s) and s[l]==s[r]:
                if (r-l+1)>malen:
                    malen=r-l+1
                    ma=s[l:r+1]
                l-=1
                r+=1
            l=i
            r=i+1
            while l>-1 and r<len(s) and s[l]==s[r]:
                if (r-l+1)>malen:
                    malen=r-l+1
                    ma=s[l:r+1]
                l-=1
                r+=1

            i+=1
        return ma
        