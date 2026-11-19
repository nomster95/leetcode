class Solution:
    def minRectanglesToCoverPoints(self, points: List[List[int]], w: int) -> int:
        x_axis = [x[0] for x in points]
        x_axis.sort()
        count = 1
        start_x = x_axis[0]
        for i in x_axis:
            if i>start_x+w:
                start_x = i
                count+=1


        return count        

        