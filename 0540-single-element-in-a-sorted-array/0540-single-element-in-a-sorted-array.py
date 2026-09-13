class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        n = len(nums)
        l = 1
        r = len(nums)-2
        if n==1:
            return nums[0]

        if nums[0]!=nums[1]:
            return nums[0]
        if nums[-2]!=nums[-1]:
            return nums[-1]

        while l<=r:
            mid = (l+r)//2
            if nums[mid]!=nums[mid+1] and nums[mid]!=nums[mid-1]:
                return nums[mid]
            else:
                # left half 
                if (mid%2==1 and nums[mid-1]==nums[mid]) or (mid%2==0 and nums[mid+1]==nums[mid]):
                    l = mid+1
                #right half    
                else:
                    r = mid-1 


            
        return -1