class TimeMap:

    def __init__(self):
        self.m={}
        

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.m:
            self.m[key]=[]
        
        self.m[key].append([value,timestamp])
        
    def get(self, key: str, timestamp: int) -> str:
        a=""
        mk=self.m.get(key,[])
        print(mk)
        n=len(mk)
        l=0
        r=n-1
        maxtime=0
        # if(n>0):
        #     for i in mk:
        #         if(i[1]<=timestamp and i[1]>maxtime):
        #             maxtime=i[1]
        #             a=i[0]
        while(n>0 and l<=r):
            mid=(l+r)//2
            if(mk[mid][1]>maxtime and mk[mid][1]<=timestamp):
                a=mk[mid][0]

            if(mk[mid][1]>timestamp):
                r=mid-1
            else:
                l=mid+1

        return a
        
