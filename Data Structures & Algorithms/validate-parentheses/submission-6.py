class Solution:
    def isValid(self, s: str) -> bool:
        st=deque()
        m={"(":")","{":"}","[":"]"}
        for i in s:
            if i in "{([":
                st.append(i)
            else:
                if not st or i!=m[st[-1]]:
                    return False
                st.pop()
                    
        return True if len(st)==0 else False
        
        