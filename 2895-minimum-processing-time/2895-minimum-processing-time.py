class Solution:
    def minProcessingTime(self, processorTime: List[int], tasks: List[int]) -> int:
        tasks.sort()
        processorTime.sort(reverse=True)
        j = 0
        max_time = 0
        for i in range(3,len(tasks),4):
            max_time = max(max_time,processorTime[j]+tasks[i])
            j+=1

        return max_time    






        