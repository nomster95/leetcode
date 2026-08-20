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
    def maxLevelSum(self, root: Optional[TreeNode]) -> int:
        ans = []
        if(root is None):
            return ans
        queue = Queue()
        
        queue.push(root)
        ans.append(root.val)
        while queue.size()>0:
            l = queue.size()
            level = []
            for i in range(l):
                front = queue.pop()
                if front.left!=None:
                    queue.push(front.left)
                    level.append(front.left.val)
                if front.right != None:
                    queue.push(front.right)  
                    level.append(front.right.val)  

            if len(level)>0:
                ans.append(sum(level))

        x = max(ans)
        

        for i in range(len(ans)):
            if ans[i]==x:
                return i+1    
                   

                 


    
        