# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Queue:
    def __init__(self):
        self.q = []
        self.front = -1

    def push(self,x):
        if self.front == -1:
            self.front = 0
        self.q.append(x)  
    def pop(self):
        if len(self.q) == 0:
            return -1
        x = self.q[self.front]
        self.front+=1
        if(self.front == len(self.q)):
            self.front = -1
            self.q = []  
        return x
    def getFront(self):
        if len(self.q) == 0:
            return -1
        return self.q[self.front]     
    def size(self):
        if len(self.q) == 0:
            return 0
        return len(self.q) - self.front             

class Solution:
    def reverseOddLevels(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        
        if(root is None):
            return root
        queue = Queue()
        
        queue.push(root)
        levelNumber = 0
        while queue.size()>0:
            levelNumber+=1
            l = queue.size()
            level = []
            for i in range(l):
                front = queue.pop()
                if front.left!=None:
                    queue.push(front.left)
                    level.append(front.left)
                if front.right != None:
                    queue.push(front.right)  
                    level.append(front.right)  

            if levelNumber%2!=0:
                i = 0
                j = len(level) - 1
                while i < j:
                    level[i].val, level[j].val = level[j].val, level[i].val
                    i += 1
                    j -= 1


 

        return root        



    
        