# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.ans = ""

    def preorder(self,root):
        if root is None:
            return

        self.ans+=str(root.val)

        if root.right is not None or root.left is not None:
            self.ans+="("
            self.preorder(root.left)
            self.ans+=")"

        if root.right is not None:
            self.ans+= "("
            self.preorder(root.right)
            self.ans+=")"

              

    def tree2str(self, root: Optional[TreeNode]) -> str:
        self.ans = ""
        self.preorder(root)
        return self.ans
        