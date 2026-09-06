# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        lca=False
        address=root
        def bfs(root,p,q):
            nonlocal lca
            nonlocal address
            if lca or not root:
                return
            
            if (p.val<=root.val<=q.val) or (q.val<=root.val<=p.val):
                lca=True
                address=root
                return 
            elif p.val<root.val and q.val<root.val:
                bfs(root.left,p,q)
            else:
                bfs(root.right,p,q)
        bfs(root,p,q)
        return address
        