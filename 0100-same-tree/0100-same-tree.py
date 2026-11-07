# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def same(self,root1,root2):
        if root1 is None and root2 is None:
            return True

        if (root1 and not root2) or (root2 and not root1):
            return False 

        if root1.val!=root2.val:
            return False

        return self.same(root1.left,root2.left) and self.same(root1.right,root2.right)
       

    def isSameTree(self, p: TreeNode | None, q: TreeNode | None) -> bool:
        return self.same(p,q)


        