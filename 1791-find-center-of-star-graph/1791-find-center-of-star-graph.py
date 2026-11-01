class Solution:
    def findCenter(self, edges: list[list[int]]) -> int:
        x,y = edges[0][0:2]
        if x in edges[1]:
            return x
        else:
            return y    

        

        