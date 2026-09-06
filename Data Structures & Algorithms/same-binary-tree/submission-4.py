# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if p is None and q is None:
            return True
        
        found=True
        def bfs(p,q):
            nonlocal found

            if not found:
                return
            

            if not p and not q:
                return
                
            
            if (p and not q) or (not p and q):
                found=False
                return 
            if p.val!=q.val:
                found=False
                return 
            bfs(p.left,q.left)
            bfs(p.right,q.right)

        bfs(p,q)
        return found

                

        