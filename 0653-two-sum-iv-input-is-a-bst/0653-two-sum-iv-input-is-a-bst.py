# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__ (self):
        self.ans = []

    def inorder(self,root):
        if root is None:
            return 

        self.inorder(root.left)
        self.ans.append(root.val)
        self.inorder(root.right)


        return root        

    def findTarget(self, root: Optional[TreeNode], k: int) -> bool:
        self.ans = []
        self.inorder(root)
        seen = set()
        for i in range(len(self.ans)):
            rem = k - self.ans[i]
            if rem in seen:
                return True
            else:
                seen.add(self.ans[i])    
            


        return False        
        