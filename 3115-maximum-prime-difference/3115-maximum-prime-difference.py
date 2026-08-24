class Solution:
    def maximumPrimeDifference(self, nums: List[int]) -> int:
        ans = []
        for i in range(len(nums)):
            is_prime = True
            if nums[i]==1:
                is_prime = False
            for j in range(2,nums[i]):    
                if nums[i]%j==0:
                    
                    is_prime = False

            if is_prime:
                ans.append(i)

        return ans[-1] - ans[0]   




        