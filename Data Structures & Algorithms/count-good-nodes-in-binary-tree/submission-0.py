# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        if not root:
            return []
        count=0
        def bfs(root,m):

            nonlocal count

            if not root:
                return
            
            if root.val>=m:
                count+=1
                m=root.val
            
            bfs(root.left,m)

            bfs(root.right,m)
        bfs(root,root.val)
        return count


        