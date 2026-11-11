import random
class Solution:

    def __init__(self, nums: list[int]):
        self.nums = nums
        self.arr = nums.copy()
        

    def reset(self) -> list[int]:
        return self.nums
        

    def shuffle(self) -> list[int]:
        random.shuffle(self.arr)
        return self.arr
        


# Your Solution object will be instantiated and called as such:
# obj = Solution(nums)
# param_1 = obj.reset()
# param_2 = obj.shuffle()