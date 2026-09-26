class Solution:
    def minQueenMoves(self, source: list[int], target: list[int]) -> int:

        if source==target:
            return 0
        elif source[0]==target[0] or source[1]==target[1] or source[0]+source[1]==target[0]+target[1] or source[0]-source[1]==target[0]-target[1]:
            

            return 1
        else:
            return 2        
        