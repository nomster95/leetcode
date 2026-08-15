# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def postorder(self,root,target):
        if root is None:
            return 

        root.left = self.postorder(root.left,target)
        root.right = self.postorder(root.right,target)

        if root.left is None and root.right is None:
            if root.val==target:

                root = None

        return root        
    def removeLeafNodes(self, root: Optional[TreeNode], target: int) -> Optional[TreeNode]:
        return self.postorder(root,target)
        