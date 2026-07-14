class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        l=0
        res=[]
        i=0
        j=0
        while i<len(nums1) and j<len(nums2):
            if nums1[i]<nums2[j]:
                res.append(nums1[i])
                i+=1
            else:
                res.append(nums2[j])
                j+=1
            
        if i>=len(nums1):
            res=res+nums2[j:]
        elif j>=len(nums2):
            res=res+nums1[i:]
        median=0
        
        no=len(res)
        if no%2==0:
            
            median=float((res[no//2-1]+res[no//2])/2)
        else:
            median=float(res[no//2])
        return median
        