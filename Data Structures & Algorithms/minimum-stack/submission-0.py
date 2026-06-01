class MinStack:

    def __init__(self):
        self.s=[]
        self.stop=-1
        self.m_s=[]
        self.m_top=-1


    def push(self, val: int) -> None:
        self.stop+=1
        self.s.append(val)
        print(val,self.m_top)
        if(self.m_top>-1 and val>=self.m_s[self.m_top]):
            self.m_s.append(self.m_s[self.m_top])
            self.m_top+=1
        else:
            self.m_top+=1
            self.m_s.append(val)

    def pop(self) -> None:
        self.stop-=1
        self.m_top-=1
        return self.s[self.stop+1]

    def top(self) -> int:
        return self.s[self.stop]
        

    def getMin(self) -> int:
        return self.m_s[self.m_top]
        
