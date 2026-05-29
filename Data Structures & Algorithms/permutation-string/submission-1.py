class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        l=0
        r=0
        m={}
        
        for i in s1:
            m[i]=m.get(i,0)+1
        
        for r in range(len(s2)):
            print(m)
            
            m[s2[r]]=m.get(s2[r],0)-1
            
            while(r-l+1>len(s1)):
                if(s2[l] in m):
                    m[s2[l]]+=1
                    print(m[s2[l]])
                l+=1
            p=all(x==0 for x in m.values())
            if(p):
                return True
        return False
            
        # while(r<len(s1)):
        #     if(m[s1[r]]>0):
        #         m[s1[r]]-=1
        #         r+=1
        #     else:
        #         m[s1[l]]+=1
        #         l+=1
        #     if(max(m.values())==0):
        #         return True
        return False

