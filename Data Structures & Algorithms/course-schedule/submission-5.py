class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        m = {i: [] for i in range(numCourses)}
        vis=set()
        for x in prerequisites:

            if x[0] not in m:
                m[x[0]] = []
            m[x[0]].append(x[1])


        def dfs(node):
            if(node in vis):
                return False
            if not m[node]:
                return True
            vis.add(node)
            
            for x in m[node]:
                if not dfs(x):
                    return False
            vis.remove(node)
            m[node]=[]
            return True

        for i in range (numCourses):
            if not dfs(i):
                return False
        return True 
        
        