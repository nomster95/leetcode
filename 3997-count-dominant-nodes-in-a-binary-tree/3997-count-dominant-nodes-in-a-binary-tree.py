# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.ans = 0
    def dominant(self,root):
        if root is None:
            return float("-inf")

        
        left_max = self.dominant(root.left)
        right_max = self.dominant(root.right)
        max_value = max(root.val,left_max,right_max)

        if root.val==max_value:
            self.ans+=1

        return max_value    



    def countDominantNodes(self, root: TreeNode | None) -> int:
        self.ans = 0
        self.dominant(root)
        return self.ans
        