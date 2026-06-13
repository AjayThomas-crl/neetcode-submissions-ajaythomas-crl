# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        if(l1 is None):
            return l2
        if(l2 is None):
            return l1

        new=ListNode()
        dummy=ListNode(0,new)
        while(l1 is not None or l2 is not None):
            if(l1 is None):
                s=l2.val
                l2=l2.next
            elif(l2 is None):
                s=l1.val
                l1=l1.next
            else:

                s=l1.val+l2.val
                l1=l1.next
                l2=l2.next
            print(s)
            if(s>9):
                new.next=ListNode(s%10)
                new=new.next
                new.next=ListNode(s//10)
            else:
                new.next=ListNode(s)
            new=new.next
            
        
        return dummy.next.next