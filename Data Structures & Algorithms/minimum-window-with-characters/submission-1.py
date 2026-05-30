class Solution:
    def minWindow(self, s: str, t: str) -> str:
        m={}
        for i in t:
            m[i]=m.get(i,0)+1
        l=0
        r=0
        c=0
        m1={}
        for r in range(len(s)):
            if(s[r] in m):
                m[s[r]]-=1
                if(m[s[r]]==0):
                    c+=1

            if(c==len(t)):
                while(s[l] not in m):
                    l+=1
                if(len(s)-l+1>=len(t)):
                    m1[s[l:r+1]]=r-l+1
                    
                    if(s[l] in m):
                        if(m[s[l]]==0):
                            c-=1
                        m[s[l]]+=1

                    l+=1
                    
                else:
                    return s[l:r+1]
        mi=99
        st=""
        print(m1)
        for i,k in m1.items():
            if(k<mi):
                mi=k
                st=i
        
        return st