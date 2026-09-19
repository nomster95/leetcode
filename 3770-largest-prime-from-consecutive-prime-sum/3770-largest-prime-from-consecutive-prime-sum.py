class Solution:
    def largestPrime(self, n: int) -> int:
        if n==1:
            return 0

        if n==2:
            return 2    
        primes = []
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
                primes.append(i)


        total = 0
        largest_prime = 2
        prime_set = set(primes)
        for x in primes:
            total+=x
            
            if total > n:
                break

            if total in prime_set:
                largest_prime = total    

        return largest_prime  



                    



            

        