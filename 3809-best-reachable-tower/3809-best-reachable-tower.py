class Solution:
    def bestTower(self, towers: List[List[int]], center: List[int], radius: int) -> List[int]:
        reach = []
        cx = center[0]
        cy = center[1]
        for i in range(len(towers)):
            x = towers[i][0]
            y = towers[i][1]
            if abs(x-cx)+abs(y-cy)<= radius:
                reach.append(towers[i])

        if len(reach)==0:
            return [-1,-1]        

        qf = reach[0][2]
        ans = [reach[0][0],reach[0][1]]
        for i in range(1,len(reach)):
            if reach[i][2]>qf:
                qf = reach[i][2]
                ans = [reach[i][0],reach[i][1]]
            elif reach[i][2]==qf and reach[i][0]<ans[0]:
                qf = reach[i][2]
                ans = [reach[i][0],reach[i][1]]
            elif reach[i][2]==qf and reach[i][0]==ans[0] and reach[i][1]<ans[1]:
                qf = reach[i][2]
                ans = [reach[i][0],reach[i][1]]

        return ans        


