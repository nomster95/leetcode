# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def postorder(self,root):
        if root is None:
            return

        root.left = self.postorder(root.left)
        root.right = self.postorder(root.right)

        if root.left is None and root.right is None:
            if root.val==0:
                root = None

        return root        


    def pruneTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        return self.postorder(root)
        