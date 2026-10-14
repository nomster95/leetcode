class Solution:
    def findMinDifference(self, timePoints: list[str]) -> int:
        min_time = float('inf')

        total_time = []
        for i in range(len(timePoints)):
            time = timePoints[i]

            hours = int(time[0])*10 + int(time[1])
            minutes = int(time[3])*10 + int(time[4])

            total = hours*60 + minutes

            total_time.append(total)

        total_time.sort()

        for i in range(1,len(total_time)):
            min_time = min(min_time,total_time[i]-total_time[i-1])   
            gap  = 1440 - total_time[-1] + total_time[0]
            min_time = min(min_time,gap)

        return min_time    





        