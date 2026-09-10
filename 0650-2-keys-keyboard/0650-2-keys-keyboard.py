class Solution:
    def minSteps(self, n: int) -> int:
        ans = 0
        if n==1:
            return 0
            
        x = 2
        while n!=1:
            if n%x==0:
                ans+=x
                n = n//x  
            else:
                x+=1

             

        return ans            






        