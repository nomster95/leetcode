class Solution:
    def sumOddLengthSubarrays(self, arr: list[int]) -> int:
        ans = 0
        for i in range(len(arr)):
            for j in range(i,len(arr)):
                nums = arr[i:j+1]
                if len(nums)%2!=0:
                    ans+=sum(nums)

        return ans            
        