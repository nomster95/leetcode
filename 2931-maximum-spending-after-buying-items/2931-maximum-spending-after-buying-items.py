class Solution:
    def maxSpending(self, values: List[List[int]]) -> int:
        money = 0
        items = []
        m,n = len(values),len(values[0])

        for i in range(m):
            for j in range(n):
                items.append(values[i][j])

        items.sort()
        for x in range(1,(m*n)+1):
            money+=items[x-1]*x

        return money    

        