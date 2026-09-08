# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        count=k
        ans=-1
        def bfs(root):
            nonlocal ans
            nonlocal count

            if not root or count<0:
                return

            bfs(root.left)

            count-=1
            if count==0:
                ans=root.val
                return
            bfs(root.right)
                        
            
            
        bfs(root)
        return ans
            
        