class MinStack:

    def __init__(self):
        self.s=[]
        self.m_s=[]


    def push(self, val: int) -> None:
        self.s.append(val)
        print(val)
        if(len(self.m_s)>0 and val>=self.m_s[-1]):
            self.m_s.append(self.m_s[-1])
        else:
            self.m_s.append(val)

    def pop(self) -> None:
        self.s.pop()
        self.m_s.pop()

        

    def top(self) -> int:
        return self.s[-1]
        

    def getMin(self) -> int:
        return self.m_s[-1]
        
