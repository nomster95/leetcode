class Solution:
    def countEven(self, num: int) -> int:
        ans = 0
        for i in range(1,num+1):
            sums = 0
            while i!=0:
                digit = i%10
                sums+=digit
                i = i//10
            if sums%2==0:
                ans+=1

        return ans            
        