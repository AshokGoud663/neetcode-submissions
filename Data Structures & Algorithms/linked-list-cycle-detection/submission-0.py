# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        temp=head
        dup=set()
        while temp:
            if temp in dup:
                return True
            dup.add(temp)
            temp=temp.next
        return False
        