# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.ans = 0
    def grandpa(self,root,parent,grandparent):
        if root is None:
            return

        
        if grandparent is not None and grandparent.val%2==0:
            self.ans+=root.val

        self.grandpa(root.left,root,parent)    
        self.grandpa(root.right,root,parent)    

        return root


    def sumEvenGrandparent(self, root: Optional[TreeNode]) -> int:
        self.parent = None
        self.grandparent = None
        self.ans = 0
        self.grandpa(root,self.parent,self.grandparent)
        return self.ans
        