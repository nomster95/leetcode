class Solution:
    def merge(self, intervals: list[list[int]]) -> list[list[int]]:
        intervals.sort()
        merged = []
        for interval in intervals:
            if not merged or merged[-1][1]<interval[0]:
                merged.append(interval)
            else:
                merged[-1] = [merged[-1][0],max(merged[-1][1],interval[1])]

        return merged            
        