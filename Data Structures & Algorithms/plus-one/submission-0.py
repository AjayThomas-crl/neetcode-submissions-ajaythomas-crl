class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        ans=0
        for i in digits:
            ans=ans*10+i
        ans+=1
        res=[]
        for j in str(ans):
            res.append(int(j))
        
        return res