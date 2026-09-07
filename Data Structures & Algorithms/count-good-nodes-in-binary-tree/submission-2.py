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
            # if not root :
            #     return
            if root.left:

                bfs(root.left,root.left.val if root.left.val >=m else m)
                # if root.val==m:
                #     count+=1
            

            if  root.right:
            
                bfs(root.right,root.right.val if root.right.val >= m else m)
            if root.val==m:
                count+=1
            if not root.left and not root.right:
                return
        bfs(root,root.val)
        return count

        