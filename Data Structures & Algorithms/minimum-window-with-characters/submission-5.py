class Solution:
    def minWindow(self, s: str, t: str) -> str:
        m={}
        for i in t:
            m[i]=m.get(i,0)+1
        
        wm={}

        l=0
        r=0
        need=len(m)
        have=0
        ans_length=len(s)+1
        ans_strt=-1
    
        for r in range(len(s)):
            if(s[r] in m):
                wm[s[r]]=wm.get(s[r],0)+1
                if(wm[s[r]]==m[s[r]]):
                    have+=1

            while(have==need):
                if(r-l+1<ans_length):
                    ans_length=r-l+1
                    ans_strt=l
                
                if(s[l] in m):
                    wm[s[l]]-=1
                    if(wm[s[l]]<m[s[l]]):
                        have-=1
                l+=1
        return "" if(ans_strt==-1) else s[ans_strt:ans_strt+ans_length]


            