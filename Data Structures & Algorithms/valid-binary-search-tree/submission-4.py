# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        found=True
        def bfs(root,low,high):
            nonlocal found
            if not root or not found:
                return
            
            if root.val<=low or root.val>=high:
                found=False
                return
            
            bfs(root.left,low,root.val)
            bfs(root.right,root.val,high)
        bfs(root,float('-inf'),float('inf'))
        return found
        

            
            
        