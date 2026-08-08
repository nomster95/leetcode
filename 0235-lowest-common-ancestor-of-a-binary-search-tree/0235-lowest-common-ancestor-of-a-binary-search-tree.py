# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def __init__(self):
        self.ans = None
    def LCA(self,root,p,q):
        #base case:
        if root is None:
            return 

        #recurisve case    

        if root.val>p.val and root.val>q.val:
            self.LCA(root.left,p,q)  
        elif root.val<p.val and root.val<q.val:
            self.LCA(root.right,p,q)  
        else:
            self.ans = root

        return self.ans    

    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        self.ans = None
        return self.LCA(root,p,q)
        
        