# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        maxi=float('-inf')
        def bfs(root):
            nonlocal maxi
            if not root:
                return 0
            left=max(0,bfs(root.left))
            right=max(0,bfs(root.right))

            current=left +root.val+right
            maxi=max(maxi,current)
            return max(left,right)+root.val
        bfs(root)
        return maxi 

        