# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def pri(self,head):
        while(head is not None):
            print(head.val,end=" ")
            head=head.next
        print(" ")
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        curr=head
        curr_nxt=None
        prev=None
        while(curr is not None):
            curr_nxt=curr.next
            
            curr.next=prev
            curr=curr_nxt
            
        self.pri(prev)

