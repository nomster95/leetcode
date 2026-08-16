class Solution:
    def countDistinctIntegers(self, nums: List[int]) -> int:
        ans = set(nums)

        for i in nums:
            rev = 0
            while i!=0:
                digit = i%10
                rev = rev*10 + digit
                i = i//10
            ans.add(rev)    

        return len(ans)    
        