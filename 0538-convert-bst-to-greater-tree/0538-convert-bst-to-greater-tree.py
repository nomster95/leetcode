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
        #base case
        if root is None:
            return

        #recursive case    
        self.inorder_rev(root.right) #process right

        self.running_sum+=root.val  #process root
        root.val = self.running_sum
        
        self.inorder_rev(root.left)  #process left  

        return root

    
        
    
    def convertBST(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        self.running_sum = 0
        return self.inorder_rev(root)

        