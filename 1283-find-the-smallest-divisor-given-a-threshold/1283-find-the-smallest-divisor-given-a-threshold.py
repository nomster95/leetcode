class Solution:
    def divison(self,nums,val):
        ans = 0
        for i in range(len(nums)):
            dividend = (nums[i]+val-1)//val
            ans+=dividend

        return ans  

    def smallestDivisor(self, nums: List[int], threshold: int) -> int:
        l = 1
        r = max(nums)
        while l<=r:
            mid = (l+r)//2
            if self.divison(nums,mid)<=threshold:
                r = mid-1
            else:
                l = mid + 1

        return l            
        