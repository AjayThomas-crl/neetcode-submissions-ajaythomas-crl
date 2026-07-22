class Solution:
    
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        premap={}
        
        for c,p in prerequisites:
            premap[c]=premap.get(c,[])+[p]
        
            
        
        vis=set()
        
        print(premap)
        def rec(i):
            if i>numCourses-1:
                return False
            d=premap.get(i,[])
            
            if not d:
                return True
            if i in vis:
                return False
            vis.add(i)

            
            for pre in d:
                print(pre)
                if not rec(pre):
                    return False
                else:
                    premap[i].remove(pre)
                    
            return True
        ans=True
        for i in premap:
            if not rec(i):
                return False
        return True