class Solution:
    
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        premap={i:[] for i in range(numCourses)}
        
        for c,p in prerequisites:
            premap[c]=premap.get(c,[])+[p]
        
        vis=set()
        
        def rec(i):
            if i in vis:
                return False
            if not premap[i]:
                return True
            
            vis.add(i)
            for pre in premap[i]:
                if not rec(pre):
                    return False
            vis.remove(i)
            premap[i]=[]
            return True
        
        for i in premap:
            if not rec(i):
                return False
        return True