class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        map={}
        for i in range(len(nums)):
            map[nums[i]]=i;

        j=-1
        for i in range (len(nums)):
            need=target-nums[i]
            if(map.get(need)):
                print(map[need])
                return [i,map[need]]
        