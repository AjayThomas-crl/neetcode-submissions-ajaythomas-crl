class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res=[]
        c=0
        o=1
        def rec(s,c,o):
            if o>n or c>n:
                return 
            if c==o and  c==n:
                res.append(s)
            
            if c>o:
                return
            
            
            rec(s+"(",c,o+1)

            s+=")"
            c+=1
            rec(s,c,o)
        
        rec("(",0,1)
        return res



            
