class Solution:
    def maxPoints(self, technique1: List[int], technique2: List[int], k: int) -> int:
        n = len(technique1)
        total = sum(technique1)
        diff = []
        for i in range(n):
            diff.append(technique2[i]-technique1[i])

        diff.sort(reverse=True)
        for i in range(n-k):
            if diff[i]>0:
                total+=diff[i]

        return total        

        