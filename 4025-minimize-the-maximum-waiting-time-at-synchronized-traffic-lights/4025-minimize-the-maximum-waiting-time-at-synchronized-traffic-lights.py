class Solution:
    def minPenalty(self, period: int, lights: list[int], arrivalTime: list[int]) -> int:
        maxGreen = max(lights)
        max_penalty = 0
        for i in range(len(arrivalTime)):
            r = arrivalTime[i]%period
            if r>=maxGreen:
                penalty = period-r
                max_penalty = max(max_penalty,penalty) 

        return max_penalty        

        