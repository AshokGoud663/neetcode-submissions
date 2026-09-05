# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return None
        
        m=0
        def bfs(root):
            nonlocal m

            if root is None:
                return 0
            
            left=bfs(root.left)
            right=bfs(root.right)

            m=max(m,left+right)

            return 1 + max(left,right)

        bfs(root)
        return m
            



        