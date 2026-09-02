# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        data=list()
        temp=head
        while temp:
            data.append(temp)
            temp=temp.next
        l=0
        h=len(data)-1
        dummy=ListNode(-1)
        curr=dummy
        while l<h:
            curr.next=data[l]
            curr=curr.next
            curr.next=data[h]
            curr=curr.next
            l+=1
            h-=1
        if l==h:
            curr.next=data[l]
            curr=curr.next
        curr.next=None
        # return dummy.next


        