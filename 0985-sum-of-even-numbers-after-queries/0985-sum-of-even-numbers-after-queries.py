class Solution:
    def sumEvenAfterQueries(self, nums: List[int], queries: List[List[int]]) -> List[int]:
        ans = [0]*len(queries)
        sums = 0
        for i in nums:
            if i%2==0:
                sums+=i

        for i in range(len(queries)):
            if nums[queries[i][1]]%2==0:
                sums-=nums[queries[i][1]]

            nums[queries[i][1]]+=queries[i][0]
            if nums[queries[i][1]]%2==0:
                sums+=nums[queries[i][1]]

            ans[i]=sums

        return ans





            
        