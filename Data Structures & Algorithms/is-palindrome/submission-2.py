class Solution:
    def isPalindrome(self, s: str) -> bool:
        mstr=s.lower()
        mstr=mstr.replace(" ","")
        
        l=0
        r=len(mstr)-1
        print(mstr)
        while(l<=r):
            if(not mstr[l].isalnum()):
                continue
                l+=1
            if(not mstr[r].isalnum()):
                r-=1
                continue
            if(mstr[l]==mstr[r]):
                l+=1
                r-=1
            else:
                return False
        return True
