class Solution:
    def carFleet(self, t: int, position: List[int], speed: List[int]) -> int:

        pair=[[p,s] for p,s in zip(position,speed)]
        
        pair.sort(key=lambda x:x[0],reverse=True)
        s=deque()
        for i in pair:
            s.append(i)
            if len(s)>1:
                a=s.pop()
                b=s.pop()
                ta=(t-a[0])/a[1]
                tb=(t-b[0])/b[1]
                if ta<=tb:
                    s.append(b)
                else:
                    s.append(b)
                    s.append(a)
        return len(s)