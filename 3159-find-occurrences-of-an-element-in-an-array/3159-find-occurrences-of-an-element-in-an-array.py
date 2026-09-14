class Solution:
    def occurrencesOfElement(self, nums: List[int], queries: List[int], x: int) -> List[int]:
        occurence = []
        for i in range(len(nums)):
            if nums[i]==x:
                occurence.append(i)

        ans = [-1]*len(queries)
        for j in range(len(queries)):
            if queries[j]>len(occurence):
                ans[j] = -1
            else:
                ans[j] = occurence[queries[j]-1]      

        return ans         
        