# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lca(self,root,p,q):
        if root is None or root==p or root==q:
            return root

        left = self.lca(root.left,p,q)
        right = self.lca(root.right,p,q)

        if right is None:
            return left
        elif left is None:
            return right
        else:
            return root      


    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        return self.lca(root,p,q)
        