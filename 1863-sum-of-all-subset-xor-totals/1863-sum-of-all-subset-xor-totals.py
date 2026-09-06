class Solution:
    def subsetXORSum(self, nums: List[int]) -> int:
        
        n = len(nums)
        sol = []
        def backtrack(i,curr_xor):
            ans = 0
            if i==n:
                return curr_xor

            ans+=backtrack(i+1,curr_xor)
            
            sol.append(nums[i])
            ans+= backtrack(i+1,curr_xor^nums[i])
            sol.pop()


            return ans

        return backtrack(0,0)
                



        