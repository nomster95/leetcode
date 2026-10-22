class Solution:
    def triangleNumber(self, nums: list[int]) -> int:
        nums.sort()
        n = len(nums)
        ans = 0
        for i in range(2,n):
            low , high = 0 , i-1
            while low<high:
                if nums[low] + nums[high] > nums[i]:
                    ans+= high-low
                    high-=1
                else:
                    low+=1    
                

        return ans                      
        