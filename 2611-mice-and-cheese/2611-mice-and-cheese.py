class Solution:
    def miceAndCheese(self, reward1: List[int], reward2: List[int], k: int) -> int:
        n = len(reward1)
        total = sum(reward2)
        gain = []
        for i in range(n):
            gain.append(reward1[i]-reward2[i])

        gain.sort(reverse=True)
        for i in range(k):
            total+=gain[i]

        return total        
        