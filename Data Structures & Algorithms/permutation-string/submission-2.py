class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        l=0
        r=0
        m={}
        
        for i in s1:
            m[i]=m.get(i,0)+1
        c=0
        for r in range(len(s2)):
            print(m)
            if(s2[r] in m ):
                m[s2[r]]=m.get(s2[r],0)-1
                if(m[s2[r]]==0):
                    c+=1
            
            
            while(r-l+1>len(s1)):
                if(s2[l] in m):
                    m[s2[l]]+=1

                    if(m[s2[l]]!=0):
                        c-=1
                    print(c,s2[l])
                l+=1
            if(c==len(s1)):
                return True
            
        return False
            
      
        

