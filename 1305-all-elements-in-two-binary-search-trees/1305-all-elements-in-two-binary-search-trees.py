# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.ans1 = []
        self.ans2 = []
    def inorder1(self,root1):
        if root1 is None:
            return

        self.inorder1(root1.left)  
        self.ans1.append(root1.val)  
        self.inorder1(root1.right)

        return root1

    def inorder2(self,root2):
        if root2 is None:
            return    

        self.inorder2(root2.left)   
        self.ans2.append(root2.val) 
        self.inorder2(root2.right)

        return root2
    def getAllElements(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> List[int]:
        self.ans1 = []
        self.ans2 = []
        self.inorder1(root1)
        self.inorder2(root2)
        ans = self.ans1 + self.ans2
        ans.sort()
        return ans