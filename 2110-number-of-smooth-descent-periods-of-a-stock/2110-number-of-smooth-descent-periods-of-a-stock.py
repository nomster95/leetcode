class Solution:
    def getDescentPeriods(self, prices: list[int]) -> int:
        count = 0
        descent = 1

        for i in range(1,len(prices)):
            if prices[i] == prices[i-1] - 1:
                descent+=1
            else:
                descent = 1

            count+=descent

        return count + 1            
        