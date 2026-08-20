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

        self.ans.append(root)
        self.preorder(root.left)
        self.preorder(root.right)

    

    def linked(self):
        if not self.ans:
            return
    
        for i in range(len(self.ans)-1):
            
            self.ans[i].left = None
            self.ans[i].right = self.ans[i+1]

        self.ans[-1].left = None
        self.ans[-1].right = None    

        
    
    def flatten(self, root: Optional[TreeNode]) -> None:
        self.ans = []
        self.preorder(root)
        self.linked()
