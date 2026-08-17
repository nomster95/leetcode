class Solution:
    def minMoves2(self, nums: List[int]) -> int:
        ops = 0
        

        nums.sort()
        l = 0
        r = len(nums)-1
        mid = (l+r)//2
        while l<=r:

            if nums[l]!=nums[mid]:
                diff = abs(nums[mid]-nums[l])
                ops += diff
                
            l+=1

        return ops        


        