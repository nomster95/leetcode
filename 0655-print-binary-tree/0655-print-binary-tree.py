# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__ (self):
        self.height = 0
    def heights(self,root):
        if root is None:

            return 0

        leftHeight = self.heights(root.left)
        rightHeight = self.heights(root.right)

        
        return max(leftHeight,rightHeight)+1

    def build(self,root,row,left,right):
        if root is None:
            return

        mid = (left + right)//2
        self.matrix[row][mid] = str(root.val)

        self.build(root.left,row+1,left,mid-1)
        self.build(root.right,row+1,mid+1,right)







    def printTree(self, root: Optional[TreeNode]) -> List[List[str]]:
        h = self.heights(root)
        rows = h
        cols = (2**h)-1
        matrix = [["" for _ in range(cols)] for _ in range(rows)]
        self.matrix = matrix
        self.build(root,0,0,cols-1)
        return matrix

        
        