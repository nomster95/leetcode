class Solution:
    def maxSumOfSquares(self, num: int, sums: int) -> str:
        if sums>9*num:
            return ""
        
        ans = ""
        while len(ans)!=num:
            digit = min(9,sums)
            ans+=str(digit)
            sums-=digit

        return ans        



        