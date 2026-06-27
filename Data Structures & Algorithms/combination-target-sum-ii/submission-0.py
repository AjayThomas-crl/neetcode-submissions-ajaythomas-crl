class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        cur=[]
        res=[]
        def rec(i,s):
            if s==target:
                res.append(cur.copy())
                return
            if i>=len(candidates) or s>target:
                return
            
            cur.append(candidates[i])
            rec(i+1,s+candidates[i])
            cur.pop()
            while(i+1<len(candidates) and candidates[i]==candidates[i+1]):
                i+=1
            rec(i+1,s)

        rec(0,0)
        return res
