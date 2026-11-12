# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class BSTIterator:

    def __init__(self, root: TreeNode | None):
        self.root = root
        self.ans = []
        self.index = 0

        def inorder(root):
            if root is None:
                return 

            inorder(root.left)
            self.ans.append(root.val)
            inorder(root.right)

            return root    

        inorder(self.root)    



        

    def next(self) -> int:
        x = self.ans[self.index]
        self.index+=1

        return x

        

    def hasNext(self) -> bool:
        if self.index<len(self.ans):
            return True

        return False   

        


# Your BSTIterator object will be instantiated and called as such:
# obj = BSTIterator(root)
# param_1 = obj.next()
# param_2 = obj.hasNext()