class Solution:
    def maximumGroups(self, grades: list[int]) -> int:
        n = len(grades)
        k = 0
        sums = 0
        while sums<=n:
            k+=1
            sums+=k

        return k-1    
    

        