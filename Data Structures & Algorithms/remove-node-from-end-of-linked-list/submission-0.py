# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        if n==1 and head.next is None:
            return None
        c=0
        temp=head
        while temp:
            c+=1
            temp=temp.next
        if n==c:
            return head.next
        N=c-n

        temp=head
        while N>1:
            temp=temp.next
            N-=1
        temp.next=temp.next.next
        return head

        