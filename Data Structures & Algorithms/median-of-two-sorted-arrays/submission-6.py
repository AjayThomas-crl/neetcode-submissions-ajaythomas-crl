class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        A,B=nums1,nums2
        if len(A)<len(B):
            A,B=B,A
        
        l=0
        r=len(A)-1
        n=len(B)+len(A)
        half=(len(A)+len(B))//2
        
        while (l<=r):
            mid=(l+r)//2
            restmid=half-mid-2

            lA=A[mid] if mid>=0 else float("-inf")
            rA=A[mid+1] if ( mid+1)<len(A) else float("inf")
            lB=B[restmid] if restmid>=0 else float("-inf")
            rB=B[restmid+1] if ( restmid+1)<len(B) else float("inf")

            if (lA<=rB  and lB<=rA):
                if n%2==0:
                    return (min(A[mid+1],B[restmid+1])+max(A[mid],B[restmid]))/2
                else:
                    return min(A[mid+1],B[restmid+1])
            elif A[mid]>B[restmid]:
                r=mid-1
            else:
                l=mid+1