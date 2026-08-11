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
        self.ans.append(root)
        self.inorder(root.right)

        return root    
    def recoverTree(self, root: Optional[TreeNode]) -> None:
        self.ans = []
        self.inorder(root)
        
        first = None
        second = None
        for i in range(len(self.ans)-1):
            if self.ans[i+1].val<self.ans[i].val:
                if first is None:
                    first = self.ans[i]
                    second = self.ans[i+1]
                else:
                    second = self.ans[i+1]    

        first.val,second.val = second.val,first.val       
                    
                
                
            
                    


       