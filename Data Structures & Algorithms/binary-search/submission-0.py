class Solution:
    def search(self, nums: List[int], target: int) -> int:
        mid=int(len(nums)/2)
        print(mid)

        l=0
        if(target<nums[mid]):
            l=0
            r=mid+1
        else:
            l=mid
            r=len(nums)
        
        for i in range(l,r,1):
            print(i,r)
            if(target==nums[i]):
                return i
        
        return -1