class Solution:
    def prime(self,n):

        is_prime = True
        if n<2:
            return False
        for i in range(2,int(sqrt(n))+1):
            if n%i==0:
                is_prime = False
                break

        return is_prime        

    def sumOfLargestPrimes(self, s: str) -> int:
        primes = set()

        for i in range(len(s)):
            for j in range(i,len(s)):
                st = s[i:j+1]
                num = int(st)
                if self.prime(num) == True:
                    primes.add(num)

        if len(primes)==0:
            return 0             



        ans = sorted(primes , reverse = True)
        if len(ans)<3:
            return sum(ans)

        return ans[0]+ans[1] + ans[2]


                


        