class Node:
    def __init__(self,val=0,next=None):
        self.val=val
        self.next=next
class Solution:
    
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        m={}
        for x in prerequisites:
            if x[1] not in m:
                m[x[1]]=Node(x[1])
            if x[0] not in m:
                m[x[0]]=Node(x[0])
            
            m[x[1]].next=m[x[0]]
            
        slow=m[0]
        fast=m[0].next
        while (fast is not None and slow is not None):
            if (slow==fast):
                return False
            slow=slow.next
            fast=fast.next.next
        return True