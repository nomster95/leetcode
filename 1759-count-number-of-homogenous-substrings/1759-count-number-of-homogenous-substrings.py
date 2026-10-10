class Solution:
    def countHomogenous(self, s: str) -> int:
        count = 0
        run = 1
        mod = 10**9 + 7

        for i in range(len(s)-1):
            if s[i]==s[i+1]:
                run+=1
            else:
                run = 1

            count = (count + run)%mod

        return count+1           

        