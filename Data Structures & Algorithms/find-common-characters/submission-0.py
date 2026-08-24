class Solution:
    def commonChars(self, words: List[str]) -> List[str]:
        h={}
        res=[]
        for i in words[0]:
            check=True
            for j in range(1,len(words)):
                if i not in words[j]:
                    check=False
            
            if check:
                res.append(i)
        return res

        