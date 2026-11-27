class Solution:
    def minCost(self, colors: str, neededTime: list[int]) -> int:
        n  = len(colors)
        cost = 0
        max_time = neededTime[0]
        for i in range(1,n):
            if colors[i]==colors[i-1]:
                cost+=min(neededTime[i],max_time)
                max_time = max(max_time,neededTime[i])
            else:
                max_time = neededTime[i]
                    
        

        return cost       

        