class Solution:
    def xorGame(self, nums: list[int]) -> bool:
        xor = 0
        n = len(nums)
        for i in nums:
            xor^=i

        if xor==0:
            return True
        else:
            if n%2==0:
                return True
            else:
                return False          
        