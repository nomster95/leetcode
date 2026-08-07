# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.running_sum = 0
    def inorder_rev(self,root):
        if root is None:
            return

        
        self.inorder_rev(root.right) 
        
        self.running_sum+=root.val
        root.val = self.running_sum
        
        self.inorder_rev(root.left)
        
        
        
        
        

        return root

    def bstToGst(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        self.running_sum = 0
        return self.inorder_rev(root)

        