class Solution:
    def findPrimePairs(self, n: int) -> List[List[int]]:
        primes = set()
        ans = []
        is_prime = [True]*(n+1)
        is_prime[0] = is_prime[1] = False
        p = 2
        while p*p<=n:
            if is_prime[p]:
                for j in range(p*p,n+1,p):
                    is_prime[j] = False

            p+=1

        for i in range(2,n+1):
            if is_prime[i]:
                primes.add(i)

        for x in range(2,(n//2)+1):
            if x in primes and n-x in primes:
                ans.append([x,n-x])


        return ans        

