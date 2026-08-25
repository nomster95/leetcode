# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def path(self,root,targetSum):
        if root is None:
            return False

        remaining = targetSum - root.val
        if root.left is None and root.right is None:
            return remaining==0    
        
        return self.path(root.left, remaining) or self.path(root.right, remaining)

            





    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        return self.path(root,targetSum)
        