class Solution:
    def countSymmetricIntegers(self, low: int, high: int) -> int:
        ans = 0
        for i in range(low,high+1):
            c = str(i)
            if len(c)%2!=0:
                continue
            mid = len(c)//2
            left_sum = 0
            right_sum = 0
            left_part = c[0:mid]
            right_part = c[mid:]
            for i in range(len(left_part)):
                left_sum+=int(left_part[i])
                right_sum+=int(right_part[i])

            if left_sum==right_sum:
                ans+=1    

        return ans        

            
            
        