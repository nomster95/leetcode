class Solution:
    def findPermutationDifference(self, s: str, t: str) -> int:
        freq1 = {}
        freq2 = {}
        ans = 0
        for i in range(len(s)):
            freq1[s[i]] = i
            freq2[t[i]] = i

        for i in s:
            diff = abs(freq1[i]-freq2[i])
            ans = ans + diff

        return ans    



        


        