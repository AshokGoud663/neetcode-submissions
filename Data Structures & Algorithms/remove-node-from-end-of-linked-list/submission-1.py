# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        if n==1 and head.next is None:
            return None
        
        first=head
        second=head
        while n>0:
            first=first.next
            n-=1
        
        if first is None:
            return second.next
        
        while first.next:
            second=second.next
            first=first.next
        
        second.next=second.next.next
        return head


        

        