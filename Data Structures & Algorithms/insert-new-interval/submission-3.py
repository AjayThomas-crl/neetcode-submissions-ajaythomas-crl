class Solution:
    def merge(self,intervals):
        s=[]
        i=0
        while(i<len(intervals)):
            if s:
                p=s.pop()
                s1=p[0]
                e1=p[1]

                s2=intervals[i][0]
                e2=intervals[i][1]
                
                if(e1>=s2):
                    s.append([min(s1,s2),max(e1,e2)])
                    
                else:
                    s.append(p)
                    s.append(intervals[i])
            else:
                s.append(intervals[i])
            i+=1
        return s
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        if not intervals:
            return [newInterval]
        intervals=self.merge(intervals)
        res=[]
        for i in range(0,len(intervals),1):
            # if(intervals[i][1]>=newInterval[1]):
            if(newInterval[0]<=intervals[i][0]):
                res.append(newInterval)
            
            res.append(intervals[i])
        print(res)
        return self.merge(res)


        

