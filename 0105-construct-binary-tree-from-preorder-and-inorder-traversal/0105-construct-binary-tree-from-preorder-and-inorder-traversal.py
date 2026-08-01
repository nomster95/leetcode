# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def build(self,preorder,inorder):
        #base case
        if len(preorder)==0:
            return None

        #recursive case  
        first = preorder[0]  
        p = inorder.index(first)
        left_preorder = preorder[1:p+1]
        right_preorder = preorder[p+1: ]
        left_inorder = inorder[:p]
        right_inorder = inorder[p+1: ]
        root = TreeNode(first)
        root.left = self.build(left_preorder,left_inorder)
        root.right = self.build(right_preorder,right_inorder)

        return root
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        return self.build(preorder,inorder)
        