class Solution:
    def maxIceCream(self, costs: list[int], coins: int) -> int:
        costs.sort()
        sums = 0
        bars = 0
        for i in costs:
            if i + sums > coins:
                break

            sums+=i
            bars+=1

        return bars        
        


        