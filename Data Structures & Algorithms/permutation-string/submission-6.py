class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        
        m={}
        for s in s1:
            m[s]=m.get(s,0)+1

        l=0
        r=0
        sm={}
        k=len(s1)
        while r<len(s2):
            
            if k>0 and r<len(s2):
                sm[s2[r]]=sm.get(s2[r],0)+1
                r+=1
                k-=1
                
            else:
               
                if sm[s2[l]]==1:
                    sm.pop(s2[l])
                   
                else:
                    sm[s2[l]]-=1
                l+=1
                k+=1
            if sm==m:
                return True
        
        return False

            

