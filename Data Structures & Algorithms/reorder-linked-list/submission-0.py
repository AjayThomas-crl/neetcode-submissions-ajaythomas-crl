# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def pri(self,head: Optional[ListNode]):
        while(head is not None):
            print(head.val, end=" ")
            head=head.next
        print("\n")
    def reorderList(self, head: Optional[ListNode]) -> None:
        
        slow=head
        fast=head.next

        while(fast is not None and fast.next is not None):
            slow=slow.next
            fast=fast.next.next
        print(slow.val)
        p2=slow.next
        slow.next=None
        prev=None
        while(p2 is not None):
            nxt=p2.next
            nxt_prev=p2
            p2.next=prev
            p2=nxt
            prev=nxt_prev
        
        self.pri(prev)

        while(prev is not None):
            head_nxt=head.next
            prev_next=prev.next

            head.next=prev
            prev.next=head_nxt

            head=head_nxt
            prev=prev_next
