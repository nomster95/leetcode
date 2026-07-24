"""
# Definition for a Node.
class Node:
    def __init__(self, val: Optional[int] = None, children: Optional[List['Node']] = None):
        self.val = val
        self.children = children
"""
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
    def levelOrder(self, root: 'Node') -> List[List[int]]:
        ans = []
        if(root is None):
            return ans
        queue = Queue()
        
        queue.push(root)
        ans.append([root.val])
        while queue.size()>0:
            l = queue.size()
            level = []
            for i in range(l):
                front = queue.pop()
                for child in front.children:
                    queue.push(child)
                    level.append(child.val)
                  

            if len(level)>0:
                ans.append(level)   

        return ans             

        
        