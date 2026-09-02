class Solution:
    def isValid(self, s: str) -> bool:
        s=deque()
        for i in s:
            if i in "[([":
                s.add(i)
            else:
                if i==s[-1]:
                    s.pop()
                else:
                    return False
        return len(s)==0
        
        