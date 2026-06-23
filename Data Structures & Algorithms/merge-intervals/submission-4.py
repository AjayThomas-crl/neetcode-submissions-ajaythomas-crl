class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        
        intervals.sort(key=lambda x: x[0])
        s=[]
        i=0
        while(i<len(intervals)):
            if s:
                p=s.pop()
                s1=p[0]
                e1=p[1]

                s2=intervals[i][0]
                e2=intervals[i][1]
                print(s1,e1,s2,e2)
                if(e1>=s2):
                    s.append([min(s1,s2),max(e1,e2)])
                    
                else:
                    s.append(p)
                    s.append(intervals[i])
            else:
                s.append(intervals[i])
            i+=1
        return s
        
