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
        if root is None:
            return

        self.inorder(root.left) 
        self.ans.append(root.val)   
        self.inorder(root.right)

        return root

    def build(self,left,right):
          
        
        #base case:
        if left>right:
            return None


        mid = (left+right)//2
        root = TreeNode(self.ans[mid])
        root.left = self.build(left,mid-1)
        root.right = self.build(mid+1,right)   
        

        return root
    def balanceBST(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        self.ans = []
        self.inorder(root)
        return self.build(0,len(self.ans)-1)
        
        