from collections import deque
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        result=[]
        queue=deque([root])

        while queue:
            node=queue.popleft()
            result.append(node.val)
            n=len(queue)

            if node.right:
                queue.append(node.right)
            if node.left:
                queue.append(node.left)
            for _ in range(n):
                node=queue.popleft()

                if node.right:
                    queue.append(node.right)
                if node.left:
                    queue.append(node.left)
        return result

            
        
        