class Solution:
    def maxDistance(self, moves: str) -> int:
        x = 0
        y = 0
        u_score = 0
        for i in moves:
            if i=='U':
                x+=1
            elif i=='D':
                x-=1
            elif i=='R':
                y+=1
            elif i=='L':
                y-=1
            else:
                u_score+=1

        return abs(x)+abs(y)+u_score        


        