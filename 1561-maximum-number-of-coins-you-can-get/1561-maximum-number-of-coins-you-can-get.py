class Solution:
    def maxCoins(self, piles: List[int]) -> int:
        n = len(piles)
        piles.sort()
        coins = 0
        l = 0
        r = len(piles)-2
        while l!=n//3:
            coins+=piles[r]
            l+=1
            r-=2

        return coins    

    
        