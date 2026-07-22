class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        premap={i:[] for i in range(numCourses)}

        for c,p in prerequisites:
            premap[c]=premap.get(c)+[p]

        vis=set()
        cycle=set()
        order=[]
        def dfs(i):
            if i in cycle:
                return False
            if i in vis:
                return True
    
            cycle.add(i)
            for pre in premap[i]:
                if not dfs(pre):
                    return False
            vis.add(i)
            cycle.remove(i)
            order.append(i)
            return True
        
        for i in premap:
            if not dfs(i):
                return []
        
        return order
            