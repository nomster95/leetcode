class Solution:
    def subtractProductAndSum(self, n: int) -> int:
        product = 1
        addition = 0
        for i in str(n):
            product = product*int(i)
            addition = addition + int(i)

        return product-addition    
        