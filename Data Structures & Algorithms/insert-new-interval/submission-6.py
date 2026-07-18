class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        if not intervals:
            return [newInterval]
        res=[]
        done =False
        for i in intervals:
            if not done and i[0]>=newInterval[0]:
                res.append(newInterval)
                done=True
                res.append(i)
            else:
                res.append(i)
        if not done:
            res.append(newInterval)
        
        i=1
        q=deque()
        q.append(res[0])
        res1=[]
        while(i<len(res)):
            if q[-1][1]>= res[i][0]:
                p=q.pop()
                q.append([min(p[0],res[i][0]),max(p[1],res[i][1])])
            else:
                q.append(res[i])
            i+=1
        
        while q:
            res1.append(q.popleft())
        return res1
