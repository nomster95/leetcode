# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.ans = 0
    def prune(self,root,low,high):
        #base case
        if root is None:
            return

        if root.val<low:
            self.prune(root.right,low,high) 
        elif root.val>high:
            self.prune(root.left,low,high) 
        elif root.val>=low and root.val<=high:
            self.ans+=root.val
            self.prune(root.left,low,high) 
            self.prune(root.right,low,high) 
    

        

        return root

    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        self.ans = 0
        self.prune(root,low,high)
        return self.ans

        