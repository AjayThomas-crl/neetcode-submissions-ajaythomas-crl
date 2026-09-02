class Solution:
    def isValid(self, s: str) -> bool:
        st=deque()
        m={"(":")","{":"}","[":"]"}
        for i in s:
            if i in "{([":
                st.append(i)
            else:
                if i==m[st[-1]]:
                    st.pop()
                else:
                    return False
        return True if len(st)==0 else False
        
        