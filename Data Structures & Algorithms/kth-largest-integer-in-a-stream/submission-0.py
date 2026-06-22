class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.k=k
        self.nums=nums

    def sin_down(self,i):
        while(True):
            smallest=i
            left=2*i+1
            right=2*i+2

            if(right<=len(self.nums)-1 and self.nums[right]<self.nums[smallest]):
                smallest=right

            if(left<=len(self.nums)-1 and self.nums[left]<self.nums[smallest]):
                smallest=left
            
            if smallest==i:
                break 

            self.nums[smallest],self.nums[i]=self.nums[i],self.nums[smallest]
            i=smallest

    def haeap(self):
        for i in range (len(self.nums)-1,-1,-1):
            self.sin_down(i)
        

    def add(self, val: int) -> int:
        self.nums.append(val)
        self.haeap()
        while(len(self.nums)>self.k):
            self.nums.pop(0)
        print(self.nums)

        

        
        
        return self.nums[0]
