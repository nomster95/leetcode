class Solution:
    def beautySum(self, s: str) -> int:
        ans = 0
        for i in range(len(s)):
            freq = {}
            for j in range(i,len(s)):
                if s[j] not in freq:
                    freq[s[j]] = 1
                else:
                    freq[s[j]]+=1

                ans+=max(freq.values())-min(freq.values())

        return ans            



        