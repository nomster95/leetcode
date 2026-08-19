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
        if root is None:
            return 

        self.ans.append(root.val)
        self.preorder(root.left) 
        self.preorder(root.right)

        return root   

       


    def checkTree(self, root: Optional[TreeNode]) -> bool:
        self.ans = []
        self.preorder(root)
        if self.ans[0]==sum(self.ans[1:]):
            return True

        return False    

        