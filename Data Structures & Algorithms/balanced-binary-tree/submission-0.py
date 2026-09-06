# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        if root is None:
            return True
        found=True
        def bfs(root):
            nonlocal found
            if root is None or not found:
                return 0

            left=bfs(root.left)
            right=bfs(root.right)

            if abs(left - right)>1:
                found=False
                return 0
            
            return 1 +max(left,right)
        bfs(root)
        return found

        