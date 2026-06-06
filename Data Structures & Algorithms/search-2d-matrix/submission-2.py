class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m=len(matrix)
        n=len(matrix[0])

        l=0
        r=m*n-2
        while(l<=r):
            mid=(l+r)//2

            ro=mid//m
            c=mid%m
            print(ro)
            if(matrix[ro][c]==target):
                return True
            elif(matrix[ro][c]<target):
                l=mid+1
            else:
                r=mid-1
        
        return False

            