class Solution:
    def differenceOfSum(self, nums: List[int]) -> int:
        ele_sum = 0
        dig_sum = 0
        for i in nums:
            ele_sum = ele_sum+i
            rev = 0
            while i!=0:
                digit = i%10
                rev = rev + digit
                i = i//10

            dig_sum = dig_sum + rev

        return abs(ele_sum-dig_sum)        

        