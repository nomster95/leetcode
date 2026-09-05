class Solution:
    def validDigit(self, n: int, x: int) -> bool:
        nums = str(n)
        if str(x) in nums and nums[0]!=str(x):
            return True

        return False    



        