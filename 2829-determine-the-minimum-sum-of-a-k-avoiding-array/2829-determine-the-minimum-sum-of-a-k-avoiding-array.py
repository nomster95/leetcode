class Solution:
    def minimumSum(self, n: int, k: int) -> int:
        seen = set()
        i = 1
        ans = []
        while len(ans)<n:
            if k-i not in seen:
                ans.append(i)

            seen.add(i)
            i+=1    


            
        return sum(ans)        


        