# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.res = 0
    def good(self,root,max_val):
        if root is None:
            return 0

        left = self.good(root.left,max(max_val,root.val))
        right = self.good(root.right,max(max_val,root.val))
        self.res = left + right
        if root.val>=max_val:
            self.res+=1

        return self.res        
    def goodNodes(self, root: TreeNode) -> int:
        self.res = 0
        return self.good(root,root.val)
        