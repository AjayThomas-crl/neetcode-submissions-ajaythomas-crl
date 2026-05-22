class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        res=[]
        freq=[[] for _ in range (len(nums)+1)]
        map={}
        for n in nums:
            map[n]=map.get(n,0)+1
        for key,value in map.items():
            freq[value].append(key)

        for i in range(len(freq)-1,0,-1):
            if(freq[i] and k>0):
                while(len(freq[i])>0 and k > 0):
                    res.append(freq[i].pop())
                    k-=1
        print(res) 
        return res       
        


        