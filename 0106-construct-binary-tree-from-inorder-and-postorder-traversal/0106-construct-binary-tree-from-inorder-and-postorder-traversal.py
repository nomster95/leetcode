# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def build(self,inorder,postorder):
        #base case
        if len(postorder)==0:
            return None

        #recursive case  
        first = postorder[-1]  
        p = inorder.index(first)
        left_postorder = postorder[:p]
        right_postorder = postorder[p: -1]
        left_inorder = inorder[:p]
        right_inorder = inorder[p+1: ]
        root = TreeNode(first)
        root.left = self.build(left_inorder,left_postorder)
        root.right = self.build(right_inorder,right_postorder)

        return root
    def buildTree(self, inorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        return self.build(inorder,postorder)