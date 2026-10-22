class Solution:
    def fourSum(self, nums: list[int], target: int) -> list[list[int]]:
        nums.sort()
        n = len(nums)
        ans = []


        for i in range(n-3):
            if i>0 and nums[i]==nums[i-1]:
                continue
            for j in range(i+1,n-2):
                if j>i+1 and nums[j]==nums[j-1]:
                    continue
                low , high = j+1 , n-1
                while low<high:
                    sums = nums[i] +nums[j] + nums[low] + nums[high]
                    if sums==target:
                        ans.append([nums[i],nums[j],nums[low],nums[high]])
                        low,high = low+1,high-1
                        while low<high and nums[low]==nums[low-1]:
                            low+=1
                        while low<high and nums[high]==nums[high+1]:
                            high-=1
                    elif sums<target:
                        low+=1
                    else:
                        high-=1

        return ans                                    
        
        