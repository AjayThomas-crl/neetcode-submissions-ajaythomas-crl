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
        
        nxt=None
        prev=None
        while(head is not None):
            nxt=head.next
            
            head.next=prev
            prev=head
            head=head.next
        self.pri(prev)


