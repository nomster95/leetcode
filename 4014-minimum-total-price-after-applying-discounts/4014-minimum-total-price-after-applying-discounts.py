class Solution:
    def minPrice(self, prices: list[int], discounts: list[int]) -> float:
        prices.sort()
        discounts.sort()
        
        i = len(prices)-1
        j = len(discounts)-1
        while i>=0 and j>=0:
            discounted = (prices[i]*(100-discounts[j]))/100
            prices[i] = discounted
            i-=1
            j-=1

        return sum(prices)    
        
        
        