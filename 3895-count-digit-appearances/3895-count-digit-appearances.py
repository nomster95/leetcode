class Solution:
    def countDigitOccurrences(self, nums: list[int], digit: int) -> int:
        ans = 0
        n = len(nums)
        for i in range(n):
            for j in str(nums[i]):
                if j in str(digit):
                    ans+=1

        return ans            
          

        