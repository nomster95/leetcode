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
    def isEvenOddTree(self, root: Optional[TreeNode]) -> bool:
        ans = []
        Odd_even = True
        if(root is None):
            return ans
        queue = Queue()
        
        queue.push(root)
        if root.val%2==0:
            Odd_even = False
        ans.append([root.val])
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
                if len(ans)%2!=0:
                    for i in range(len(level)):
                        if level[i]%2!=0:
                            Odd_even = False
                    level_sort = sorted(level,reverse = True)
                    if level!=level_sort:
                        Odd_even =  False
                    if len(level)!=len(set(level)):
                        Odd_even = False    
                else:
                    for i in range(len(level)):
                        if level[i]%2==0:
                            Odd_even = False

                    level_sor = sorted(level)
                    if level!=level_sor:
                        Odd_even =  False
                    if len(level)!=len(set(level)):
                        Odd_even = False    

                ans.append(level)        

                    
        return Odd_even         
        
        