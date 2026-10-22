class Solution:
    def threeSumClosest(self, nums: list[int], target: int) -> int:
        nums.sort()
        n = len(nums)
        ans = []
        closest = float('inf')
        for i in range(n-2):
            low , high = i+1 , n-1
            while low<high:
                sums = nums[i] + nums[low] + nums[high]
                new_close = abs(sums-target)
                if new_close<abs(closest-target):
                    closest = sums

                if sums<target:
                    low+=1
                elif sums>target:
                    high-=1
                else:
                    return target    

        return closest               
        