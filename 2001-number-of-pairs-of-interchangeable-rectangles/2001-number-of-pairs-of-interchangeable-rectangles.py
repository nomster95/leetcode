class Solution:
    def interchangeableRectangles(self, rectangles: list[list[int]]) -> int:
        freq = {}
        for i in range(len(rectangles)):
            rect_pair = rectangles[i][0]/rectangles[i][1]
            if rect_pair not in freq:
                freq[rect_pair] = 1
            else:
                freq[rect_pair]+=1

        inter = 0
        for i in freq.values():
            inter+= (i*(i-1))//2  

        return inter              

        