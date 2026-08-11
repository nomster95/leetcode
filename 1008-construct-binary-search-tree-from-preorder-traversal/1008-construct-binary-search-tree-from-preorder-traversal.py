# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def preorder(self,preorder):
        if len(preorder)==0:
            return None

        root = TreeNode(preorder[0])   
        i = 1
        while i<len(preorder) and preorder[i]<root.val:
            i+=1

        root.left = self.preorder(preorder[1:i])   
        root.right = self.preorder(preorder[i:]) 
        
        return root
    def bstFromPreorder(self, preorder: List[int]) -> Optional[TreeNode]:
        return self.preorder(preorder)
        