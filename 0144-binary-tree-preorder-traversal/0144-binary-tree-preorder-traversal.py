# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.ans = []
    def preorder(self,root):
        #base case
        if root is None:
            return 
        #recursive case
        self.ans.append(root.val)
        self.preorder(root.left) #left subtree
        self.preorder(root.right)  #right subtree

    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        self.ans = []
        self.preorder(root)
        return self.ans