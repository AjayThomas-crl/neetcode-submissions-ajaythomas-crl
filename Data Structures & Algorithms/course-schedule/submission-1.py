class Node:
    def __init__(self,val=0,next=None):
        self.val=val
        self.next=next
class Solution:
    
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        m={}
        if numCourses-1 is 0:
            return True
        for x in prerequisites:
            if x[1] not in m:
                m[x[1]]=Node(x[1])
            if x[0] not in m:
                m[x[0]]=Node(x[0])
            
            m[x[1]].next=m[x[0]]
            
        slow=m[numCourses-1]
        fast=m[numCourses-1]
        while (fast is not None and fast.next is not None):
            slow=slow.next
            fast=fast.next.next
            if (slow==fast):
                return False
            
        return True