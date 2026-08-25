# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.ans = []

    def path(self,root,targetSum,current_path):
        if root is None:
            return self.ans 

        current_path.append(root.val)
        remaining = targetSum - root.val   
        if root.left is None and root.right is None:
            if remaining==0:
                self.ans.append(current_path.copy())  

        self.path(root.left,remaining,current_path) 
        self.path(root.right,remaining,current_path)

        current_path.pop()
        return self.ans
        
        
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        self.ans = []
        current_path = []
        return self.path(root,targetSum,current_path)

        