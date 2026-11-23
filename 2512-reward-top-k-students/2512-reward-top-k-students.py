import heapq
class Solution:
    def topStudents(self, positive_feedback: list[str], negative_feedback: list[str], report: list[str], student_id: list[int], k: int) -> list[int]:
        h = []
        positive = set(positive_feedback)
        negative = set(negative_feedback)
        rank = [0]*k

    
        for i in range(len(report)):
            points = 0
            for x in report[i].split(" "):
                if x in positive:
                    points+=3
                elif x in negative:
                    points-=1

            heapq.heappush(h,(-points,student_id[i]))   


        for i in range(k):
            rank[i] = heapq.heappop(h)[1]

        return rank          








        