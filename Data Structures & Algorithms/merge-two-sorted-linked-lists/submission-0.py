# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if (list1==None and list2==None):
            return None
        if(list1==None):
            return list2
        if(list2==None):
            return list1
        if(list1.val<list2.val):
            root=list1
            res=list1
            list1=list1.next
        else:
            root=list2
            res=list2
            list2=list2.next

        while(list1!=None and list2 !=None):
            if(list1.val<list2.val):
                root.next=list1
                list1=list1.next
            else:
                root.next=list2
                list2=list2.next
            root=root.next

        if(list1==None):
            root.next=list2
        else:
            root.next=list1
        return res