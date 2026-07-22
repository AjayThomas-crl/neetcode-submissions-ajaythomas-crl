class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        premap={}

        for c,p in prerequisites:
            premap[c]=premap.get(c,[])+[p]

        order=set()
        vis=set()

        def rec(i):
            if i>numCourses-1:
                return False
            
            d=premap.get(i,[])
            print()
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
                    print(i,pre)
                    
                    premap[i].remove(pre)
                    if not premap[i]:
                        order.add(i)
            
            return True

        for i in range (numCourses):
            
            if not rec(i):
                return []
        
        
        return list(order)