# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.ans = []
    def postorder(self,root):
        #base case
        if root is None:
            return 
        #recursive case
        
        self.postorder(root.left) #left subtree
        self.postorder(root.right)  #right subtree
        self.ans.append(root.val)

    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        self.ans = []
        self.postorder(root)
        return self.ans
        