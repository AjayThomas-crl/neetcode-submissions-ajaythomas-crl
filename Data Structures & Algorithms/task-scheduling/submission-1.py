class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        time=0
        m={}
        for t in tasks:
            m[t]=m.get(t,0)-1
        
        mh=[x for x in m.values()]
        heapq.heapify(mh)
        q=deque()
        while(mh or q):
            while(len(q)>0 and q[0][1]==time):
                z=q.popleft()
                heapq.heappush(mh,z[0])
            if (mh):
                p=heapq.heappop(mh)
                if(p+1<0):

                    q.append([p+1,time+n+1])
            time+=1
        return time

