# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:

        def bfs(root, lo=float('-inf'), hi=float('inf')):
            if root == None:
                return True
            if not (lo < root.val < hi):
                return False
            return (bfs(root.left, lo, root.val) and 
                    bfs(root.right, root.val, hi))
        
        return bfs(root)