"""
# Definition for a Node.
class Node:
    def __init__(self, val: Optional[int] = None, children: Optional[List['Node']] = None):
        self.val = val
        self.children = children
"""

class Solution:
    def __init__(self):
        self.ans = []
    def preorders(self,root):
        #base case
        if root is None:
            return 
        #recursive case
        
        for child in root.children:

            self.preorders(child) 
        self.ans.append(root.val)    
        

    def postorder(self, root: 'Node') -> List[int]:
        self.ans = []
        self.preorders(root)
        return self.ans
    
    
        