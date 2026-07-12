class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        m={}
        m[2]=['a','b','c']
        m[3]=['d','e','f']
        m[4]=['g','h','i']
        m[5]=['j','k','l']
        m[6]=['m','n','o']
        m[7]=['p','q','r','s']
        m[8]=['t','u','v']
        m[9]=['w','x','y','z']
        ans=[]
        def dfs(i,s):
            nonlocal ans
            if i==len(s):
                return
            
            ans=permutations(ans,m[int(s[i])])
            dfs(i+1,s)

        def permutations(l1,l2):
            res=[]
            
            if not l1:
                return l2
            print(l1,l2)
            for t in l2:
                for l in l1:
                    
                    r=l+t
                    res.append(r)
            return res
        dfs(0,digits)
        return ans
