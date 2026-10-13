class Solution:
    def minimumCardPickup(self, cards: list[int]) -> int:
        ans = -1
        freq = {}
        min_dist = float('inf')
        for i in range(len(cards)):
            if cards[i] not in freq:
                freq[cards[i]] = i
            else:
                dist = i - freq[cards[i]] + 1
                freq[cards[i]] = i
                min_dist = min(min_dist,dist)

        if min_dist == float('inf'):
            return -1

        return min_dist            



                
        