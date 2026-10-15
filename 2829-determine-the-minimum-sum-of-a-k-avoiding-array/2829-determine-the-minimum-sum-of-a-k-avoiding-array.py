class Solution:
    def minimumSum(self, n: int, k: int) -> int:
        seen = set()
        i = 1
        ans = 0
        counter = 0
        while counter<n:
            if k-i not in seen:
                ans+=i
                counter+=1

            seen.add(i)
            i+=1    


            
        return ans     


        