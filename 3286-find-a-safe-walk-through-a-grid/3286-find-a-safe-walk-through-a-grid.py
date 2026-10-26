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
    def findSafeWalk(self, grid: List[List[int]], health: int) -> bool:
        m , n = len(grid) , len(grid[0])
        q = Queue()
        health-=grid[0][0]
        if health<=0:
            return False
            
        q.push((0,0,health,0))
        visited = [[-1]*n for _ in range(m)]
        visited[0][0] = health
        directions = [(1,0),(-1,0),(0,1),(0,-1)]


        while q.size()>0:
            r,c,rem_health,steps = q.pop()

            if r==m-1 and c==n-1: 
                if rem_health>0:
                    return True
                else:
                    return False    

            for dr,dc in directions:
                nr = r + dr
                nc = c + dc

                if 0<=nr<m and 0<=nc<n:
                    new_health = rem_health-grid[nr][nc]

                    if new_health<=0:
                        continue

                    if new_health>visited[nr][nc]:
                        visited[nr][nc] = new_health
                        q.push((nr,nc,new_health,steps+1))

        return False                

                      
        