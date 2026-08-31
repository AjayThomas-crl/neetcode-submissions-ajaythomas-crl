class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        m={5:0,10:0,20:0}
        for i in bills:
            m[i]+=1
            change=i-5
            if change==0:
                continue
            if change==15:
                if m[5]>=1 and m[10]>=1:
                    m[5]-=1
                    m[10]-=1
                    continue
                elif m[5]>=2:
                    m[5]-=2
                    continue
                else:
                    return False
            elif change==5:
                if m[5]>=1:
                    m[5]-=1
                    continue
                else:
                    return False

                
            
        return True