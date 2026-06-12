# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        res=head
        l=head
        r=head
        c=n
        while(c>0):
            r=r.next
            c-=1
        prev=None
        while(r is not None):
            prev=l
            l=l.next
            r=r.next
        # if(l.next is None):
        #     prev.next=None
        # else:
        if(prev is None):
            return None
        prev.next=l.next
        return res