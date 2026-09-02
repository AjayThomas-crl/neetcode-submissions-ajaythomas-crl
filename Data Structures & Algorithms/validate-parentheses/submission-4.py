class Solution:
    def isValid(self, s: str) -> bool:
        s=deque()
        m={"(":")","{":"}","[":"]"}
        for i in s:
            if i in "{([":
                s.add(i)
            else:
                if i==m[s[-1]]:
                    s.pop()
                else:
                    return False
        return True if len(s)==0 else False
        
        