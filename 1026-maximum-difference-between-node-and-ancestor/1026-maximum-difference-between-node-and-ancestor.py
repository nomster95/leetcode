# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diff(self,root,min_value,max_value):
        if root is None:
            return 0

        
        difference = max(abs(root.val - min_value),abs(root.val - max_value)) 
        min_value = min(min_value,root.val)
        max_value = max(max_value,root.val)   
        left = self.diff(root.left,min_value,max_value)
        right = self.diff(root.right,min_value,max_value)

        return max(difference,left,right)

    def maxAncestorDiff(self, root: Optional[TreeNode]) -> int:
        return self.diff(root,root.val,root.val)
        