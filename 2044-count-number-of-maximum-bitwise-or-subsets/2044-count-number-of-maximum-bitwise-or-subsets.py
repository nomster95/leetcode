class Solution:
    def countMaxOrSubsets(self, nums: List[int]) -> int:
        max_or = 0
        n = len(nums)
        for i in nums:
            max_or = max_or | i

        ans = 0
        def backtrack(i,curr_or):
            nonlocal ans
            if i==n:
                if curr_or==max_or:
                    ans+=1
                return

            #dont choose nums[i]
            backtrack(i+1,curr_or)
            #choose nums[i]
            backtrack(i+1,curr_or | nums[i])
            

        backtrack(0,0)
        return ans        



            
        