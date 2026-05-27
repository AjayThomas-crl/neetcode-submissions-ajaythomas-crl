class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l=0
        r=0
        m=set()
        a=0

        while(r<len(s) ):
            if(s[r] not in m):
                m.add(s[r])
                a=max(a,r-l+1)
                r+=1
                print(m)
            else:
                print(m)
                while(s[r] in m):
                    m.remove(s[l])
                    l+=1
        return a
