class Solution:
    def maxCount(self, banned: List[int], n: int, maxSum: int) -> int:
        seen = set()
        for i in banned:
            if i<=n:
                seen.add(i)

        sums = 0
        ans = 0
        for i in range(1,n+1):
            if sums + i >maxSum:
                break

            if i not in seen:
                sums+=i
                ans+=1

        return ans        

                            
        