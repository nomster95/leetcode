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
    def minimumOperations(self, root: Optional[TreeNode]) -> int:
        ans = 0
        if(root is None):
            return ans
        queue = Queue()
        
        queue.push(root)
        
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

            swap = 0       

            if len(level)>0:
                
                level_sort = sorted(level)
                freq = {}
                for i in range(len(level)):

                    
                    freq[level[i]] = i

                for i in range(len(level)):
                    if level[i]!=level_sort[i]:

                        j = freq[level_sort[i]]
                        val_i = level[i]
                        val_j = level[j]
                        level[i],level[j]=level[j],level[i]
                        swap+=1
                        

                        freq[val_j] = i
                        freq[val_i] = j
                        
            ans+=swap            
                

        return ans          
        