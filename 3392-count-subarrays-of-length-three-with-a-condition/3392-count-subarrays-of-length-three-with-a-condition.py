class Solution:
    def countSubarrays(self, nums: List[int]) -> int:
        ans = 0
        for i in range(len(nums)):
            for j in range(i,len(nums)):
                arr = nums[i:j+1]
                if len(arr)==3:
                    if arr[0]+arr[2]==arr[1]/2:
                        ans+=1

        return ans                
        