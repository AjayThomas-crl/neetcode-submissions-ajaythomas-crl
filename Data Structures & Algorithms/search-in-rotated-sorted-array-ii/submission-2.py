class Solution:
    def search(self, nums: List[int], target: int) -> bool:
        
        l=0
        r=len(nums)-1

        while(l<=r):
            mid=(l+r)//2

            if(nums[mid]==target):
                return True
            if(nums[l]==nums[mid]==nums[r]):
                l+=1
                r-=1
            if(nums[mid]<nums[r]):
                if(target<=nums[r] and target>nums[mid]):
                    l=mid+1
                else:
                    r=mid-1
            else:
                if(target<nums[mid] and target>=nums[l]):
                    r=mid-1
                else:
                    l=mid+1
        
        return False