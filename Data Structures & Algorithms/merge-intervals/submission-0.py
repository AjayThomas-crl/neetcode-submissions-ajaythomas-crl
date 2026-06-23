class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        
        intervals.sort(key=lambda x:x[0])
        res=[]
        prev=intervals[0]
        i=1
        while(i<len(intervals)):
            s1=prev[0]
            e1=prev[1]

            s2=intervals[i][0]
            e2=intervals[i][1]


            if(e1>=s2):
                l=[min(s1,s2),max(e1,e2)]
                res.append(l)
                prev=l
                i+=1
                continue
            res.append(intervals[i])
            i+=1
        return  res
            
            