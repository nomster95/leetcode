class Solution:
    def countDigits(self, num: int) -> int:
        count = 0
        nums = num
        while nums!=0:
            digit = nums%10
            if num%digit==0:
                count+=1

            nums = nums//10

        return count    


        