class Solution:
    def closestPrimes(self, left: int, right: int) -> List[int]:
        ans = []
        #sieve of erastosthenes
        is_prime = [True]*(right+1)
        is_prime[0] = is_prime[1] = False
        p = 2
        while p*p<=right:
            if is_prime[p]:
                for j in range(p*p,right+1,p):
                    is_prime[j] = False

            p+=1

        for i in range(left,right+1):
            if is_prime[i]:
                ans.append(i)    

       
        if len(ans)<2:
            return [-1,-1]

        min_pair = [ans[-2],ans[-1]]
        min_diff = ans[-1]-ans[-2]
        for i in range(len(ans)-2,0,-1):
            diff = ans[i] - ans[i-1]

            if diff<=min_diff:
                min_diff = diff
                min_pair = [ans[i-1],ans[i]]

        return min_pair                     

           

        