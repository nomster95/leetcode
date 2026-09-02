# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.ans = []
    def uni(self,root):
        if root is None:
            return

        self.ans.append(root.val)

        self.uni(root.left)
        self.uni(root.right)

        return root     

    def isUnivalTree(self, root: Optional[TreeNode]) -> bool:
        self.ans = []
        self.uni(root)
        sol = set(self.ans)
        if len(sol)==1:
            return True

        return False    


        
        