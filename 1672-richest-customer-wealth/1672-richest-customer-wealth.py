class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        ans = []
        for i in accounts:
            cash = sum(i)
            ans.append(cash)

        return max(ans)    
    