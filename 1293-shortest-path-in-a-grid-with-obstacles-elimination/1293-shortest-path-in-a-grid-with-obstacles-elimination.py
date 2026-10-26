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
    def shortestPath(self, grid: list[list[int]], k: int) -> int:
        m , n = len(grid) , len(grid[0])
        q = Queue()
        q.push((0,0,k,0))
        visited = [[-1]*n for _ in range(m)]
        visited[0][0] = k
        directions = [(1,0),(-1,0),(0,1),(0,-1)]


        while q.size()>0:
            r,c,remaining_k,steps = q.pop()

            if r==m-1 and c==n-1: 
                return steps

            for dr,dc in directions:
                nr = r + dr
                nc = c + dc

                if 0<=nr<m and 0<=nc<n:
                    new_k = remaining_k-grid[nr][nc]

                    if new_k<0:
                        continue

                    if new_k>visited[nr][nc]:
                        visited[nr][nc] = new_k
                        q.push((nr,nc,new_k,steps+1))

        return -1                    
        