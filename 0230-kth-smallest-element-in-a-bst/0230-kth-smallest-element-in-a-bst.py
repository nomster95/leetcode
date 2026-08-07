# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.ans = []
    def inorder(self,root):
        #base case
        if root is None:
            return

        #recursive case
        self.inorder(root.left)    
        self.ans.append(root.val)
        self.inorder(root.right)
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        self.ans = []
        self.inorder(root)
        return self.ans[k-1]

        