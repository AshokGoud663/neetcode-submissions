# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return 0
        
        def bfs(root,c):
            if root is None:
                return c
            
            left=bfs(root.left,c)
            right=bfs(root.right,c)

            c=max(1+left,1+right)
            return c
        c=bfs(root,0)
        return c

        