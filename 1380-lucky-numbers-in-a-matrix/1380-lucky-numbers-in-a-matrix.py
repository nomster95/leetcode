class Solution:
    def luckyNumbers(self, matrix: List[List[int]]) -> List[int]:
       
        maximum = set()
        minimum = set()
        lucky = []
        for i in matrix:
            minimum.add(min(i))

        for i in zip(*matrix):
            maximum.add(max(i))

        common = maximum.intersection(minimum)
        for i in common:
            lucky.append(i)

        return lucky         

                
            

        