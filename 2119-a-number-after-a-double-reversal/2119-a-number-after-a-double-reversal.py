class Solution:
    def isSameAfterReversals(self, num: int) -> bool:
        nums = num
        reverse1 = 0
        while nums!=0:
            digit = nums%10
            reverse1 = reverse1*10 + digit
            nums = nums//10


        reverse2 = 0
        while reverse1!=0:
            digit = reverse1%10
            reverse2 = reverse2*10 + digit
            reverse1 = reverse1//10

        if reverse2==num:
            return True

        return False        





           

        