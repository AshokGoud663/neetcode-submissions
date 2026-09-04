"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if head is None:
            return None
        mapping={}

        temp=head

        while temp:
            mapping[temp]=Node(temp.val)
            temp=temp.next
        
        temp=head

        while temp:
            mapping[temp].next=mapping.get(temp.next)
            mapping[temp].random=mapping.get(temp.random)
            temp=temp.next
        return mapping[head]
        