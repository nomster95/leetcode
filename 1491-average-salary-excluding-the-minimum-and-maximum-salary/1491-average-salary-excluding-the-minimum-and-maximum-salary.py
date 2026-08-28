class Solution:
    def average(self, salary: List[int]) -> float:
        salary.sort()
        m = len(salary[1:len(salary)-1])
        avg = sum(salary[1:len(salary)-1])/m
        return avg
        