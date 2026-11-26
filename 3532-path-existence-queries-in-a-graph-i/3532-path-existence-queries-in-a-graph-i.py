class Solution:
    def pathExistenceQueries(self, n: int, nums: List[int], maxDiff: int, queries: List[List[int]]) -> List[bool]:
        n = len(queries)
        components = [0]*len(nums)
        ans = [False]*n
        comp = 0

        for i in range(len(nums)-1):
            if nums[i+1]-nums[i]>maxDiff:
                comp+=1
            
            components[i+1] = comp




        for i in range(n):
            u = queries[i][0]
            v = queries[i][1]

            if components[u]==components[v]:
                ans[i] = True

        return ans        
                



        