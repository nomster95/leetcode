class Solution:
    def maxScore(self, cardPoints: list[int], k: int) -> int:
        n = len(cardPoints)
        lsum = sum(cardPoints[0:k])
        maxSum = lsum
        rsum = 0
        rindex = n-1
        for i in range(k-1,-1,-1):
            lsum = lsum - cardPoints[i]
            rsum = rsum + cardPoints[rindex]
            rindex-=1

            maxSum = max(maxSum,lsum+rsum)

        return maxSum    


        