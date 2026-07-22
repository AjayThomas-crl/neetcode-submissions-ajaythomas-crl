class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        premap={}

        for c,p in prerequisites:
            premap[c]=premap.get(c,[])+[p]
        order=set()
        vis=set()
        for i in range(numCourses):
            if i not in premap:
                order.add(i)
        

        def rec(i):
            print(i)
            if i>numCourses-1:
                return False
            
            d=premap.get(i,[])
            
            if not d:
                order.add(i)
                return True
            if i in vis:
                return False
            vis.add(i)
            
            for pre in d:
                if not rec(pre):
                    return False
                else:
                    
                    
                    premap[i].remove(pre)
                    if not premap[i]:
                        order.add(i)
                    
            
            return True

        for p in premap:
            
            if not rec(p):
                return []
        for i in range(numCourses):
            if i not in order:
                order.add(i)
        
        
        return list(order)