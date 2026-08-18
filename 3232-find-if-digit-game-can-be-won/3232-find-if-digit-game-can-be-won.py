class Solution:
    def canAliceWin(self, nums: List[int]) -> bool:
        single_sum = 0
        double_sum = 0
        for i in nums:
            if i<10:
                single_sum+=i
            else:
                double_sum+=i

        if single_sum == double_sum:
            return False

        return True                

        