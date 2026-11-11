import random
class Solution:

    def __init__(self, nums: list[int]):
        self.nums = nums
        

    def pick(self, target: int) -> int:
        indices = []
        for i in range(len(self.nums)):
            if self.nums[i]==target:
                indices.append(i)

        return random.choice(indices)    

        


# Your Solution object will be instantiated and called as such:
# obj = Solution(nums)
# param_1 = obj.pick(target)