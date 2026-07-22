class Solution:
    
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        premap={}
        
        for c,p in prerequisites:
            premap[c]=premap.get(c,[])+[p]
        
            
        
        vis=set()
        
        
        def rec(i):
            if i>numCourses-1 or i in vis:
                return False
            d=premap.get(i,[])
            if not d:
                return True
            vis.add(i)
            for pre in d:
                
                if not rec(pre):
                    return False
                else:
                    print(i,pre)
                    premap[i].remove(pre)
            return True
        return rec(0)