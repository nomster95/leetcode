class Solution:
    def minSwaps(self, nums: list[int]) -> int:
        min_swaps = float('inf')
        ones = 0
        zeroes = 0
        for i in nums:
            if i==1:
                ones+=1

        arr = nums + nums[:ones]
        for i in nums[:ones]:
            if i==0:
                zeroes+=1

        min_swaps = min(min_swaps,zeroes)
        r = ones
        l = 0
        while r<len(arr)-1:
            if arr[r]==0:
                zeroes+=1

            if arr[l]==0:
                zeroes-=1

            min_swaps = min(min_swaps,zeroes)
            l+=1
            r+=1

        return min_swaps            


        