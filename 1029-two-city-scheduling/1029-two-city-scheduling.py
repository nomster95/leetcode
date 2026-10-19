class Solution:
    def twoCitySchedCost(self, costs: list[list[int]]) -> int:
        n = len(costs)
        total_cost = 0
        diff = []
        for i in range(n):
            total_cost+=costs[i][0]
            cost = costs[i][1]-costs[i][0]
            diff.append(cost)

        diff.sort()
        for i in range(n//2):
            total_cost+=diff[i]

        return total_cost        
        
        