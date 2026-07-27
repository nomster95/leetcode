class Solution:
    def digitFrequencyScore(self, n: int) -> int:
        score = 0
        for i in str(n):
            score = score + int(i)

        return score    
        
        








        



        