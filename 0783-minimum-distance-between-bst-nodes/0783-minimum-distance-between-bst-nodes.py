# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    
    def __init__(self):
        self.ans = []
    def inorder(self,root):

        #base case:
        if root is None:
            return 
        #recursive case:
        self.inorder(root.left) 
        self.ans.append(root.val)   
        self.inorder(root.right)    

        return root
    def minDiffInBST(self, root: Optional[TreeNode]) -> int:
        self.ans = []
        self.inorder(root)
        min_diff = self.ans[-1] - self.ans[0]
        for i in range(len(self.ans)-1):
            min_val = self.ans[i+1]-self.ans[i]
            if min_val<min_diff:
                min_diff = min_val

        return min_diff        
           
        