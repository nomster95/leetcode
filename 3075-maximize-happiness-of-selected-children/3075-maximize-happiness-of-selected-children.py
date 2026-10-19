class Solution:
    def maximumHappinessSum(self, happiness: List[int], k: int) -> int:
        happiness.sort(reverse=True)
        score = 0
        down  = 1
        for i in range(k):
            if happiness[i]<0:
                break

            score+=happiness[i]
            if i+1<len(happiness):
                happiness[i+1] = happiness[i+1]-down
                down+=1

        return score    



        