# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        
        if not subRoot:
            return True
        
        found = False

        def bfs(root):
            nonlocal found

            if not root or found:
                return

            if root.val == subRoot.val:
                if solve(root, subRoot):
                    found = True
                    return

            bfs(root.left)
            bfs(root.right)

        def solve(root, subRoot):
            if not root and not subRoot:
                return True

            if not root or not subRoot:
                return False

            if root.val != subRoot.val:
                return False

            return solve(root.left, subRoot.left) and \
                   solve(root.right, subRoot.right)

        bfs(root)
        return found
             