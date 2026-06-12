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
    def rev(self,curr):
        curr_nxt=None
        prev=None
        while(curr is not None):
            curr_nxt=curr.next
            curr.next=prev
            prev=curr
            curr=curr_nxt
        return prev
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        head=self.rev(head)
        
        res=head
        c=1
        prev=None
        while(c!=n):
            prev=head
            head=head.next
            c+=1
        
        if(head is None or prev is None):
            return None
        
        prev.next=head.next
        return self.rev(res)

        

