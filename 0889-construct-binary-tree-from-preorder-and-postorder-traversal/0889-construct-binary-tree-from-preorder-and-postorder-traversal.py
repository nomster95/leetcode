# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def build(self,preorder,postorder):
        if len(postorder)==0:
            return
        if len(preorder)==1:
            return TreeNode(preorder[0])    

        first = postorder[-1]
        second = preorder[1]
        p = postorder.index(second)    
        left_postorder = postorder[0:p+1]
        right_postorder = postorder[p+1:-1]
        left_preorder = preorder[1:len(left_postorder)+1]
        right_preorder = preorder[len(left_postorder)+1: ]
        root = TreeNode(first)
        root.left = self.build(left_preorder,left_postorder)
        root.right = self.build(right_preorder,right_postorder)

        return root

    def constructFromPrePost(self, preorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        return self.build(preorder,postorder)
        