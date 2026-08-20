# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def build(self,root,curr_number):
        if root is None:
            return 0

        curr_number = curr_number*10 + root.val
        if root.left is None and root.right is None:
            return curr_number

        return self.build(root.left,curr_number) + self.build(root.right,curr_number)      



    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        return self.build(root,0)
        