class Solution:
    def minCost(self, s: str, cost: List[int]) -> int:
        total = sum(cost)
        freq = {}
        for i in range(len(s)):
            if s[i] not in freq:
                freq[s[i]] = cost[i]
            else:
                freq[s[i]]+=cost[i]

        expensive = max(freq.values())
        return total-expensive         
        
        
        
        
        