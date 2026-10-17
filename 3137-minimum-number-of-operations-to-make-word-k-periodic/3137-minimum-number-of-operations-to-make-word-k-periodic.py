class Solution:
    def minimumOperationsToMakeKPeriodic(self, word: str, k: int) -> int:
        freq = {}
        for i in range(0,len(word),k):
            freq[word[i:k+i]] = freq.get(word[i:k+i],0) + 1

        return sum(freq.values()) - max(freq.values())

        