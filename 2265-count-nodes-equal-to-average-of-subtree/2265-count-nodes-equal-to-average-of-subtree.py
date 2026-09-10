# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.ans = 0
    def average(self,root):
        if root is None:
            return (0,0)

        left_sum , left_count = self.average(root.left) 
        right_sum , right_count = self.average(root.right)

        max_sum = root.val + left_sum  + right_sum
        max_count = 1 + left_count + right_count

        avg = max_sum//max_count
        if avg==root.val:
            self.ans+=1

        return (max_sum,max_count)




    def averageOfSubtree(self, root: TreeNode) -> int:
        self.ans = 0
        self.average(root)
        return self.ans
        