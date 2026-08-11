class Solution:
    def sumOfPrimesInRange(self, n: int) -> int:
        r = 0
        original = n
        ans = 0
        while n!=0:
            div = n%10
            r = r*10 + div
            n = n//10


        for i in range(min(original,r),max(original,r)+1):
            is_prime = True
            if i==1:
                is_prime = False
            for j in range(2,i):
                if i%j==0:
                    is_prime = False

            if is_prime:
                ans+=i

        return ans            

                    





        