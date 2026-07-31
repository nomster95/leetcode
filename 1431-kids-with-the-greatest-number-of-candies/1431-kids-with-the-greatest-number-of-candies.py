class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        n = len(candies)
        ans = [0]*n
        top = max(candies)
        for i in range(n):
            if candies[i]+extraCandies>=top:
                ans[i] = True
            else:
                ans[i] = False

        return ans           
        