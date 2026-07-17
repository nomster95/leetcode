class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        n = len(nums)
        k = k%n
        rotation = nums[-k:] + nums[:-k]
        nums[:] = rotation
        
        