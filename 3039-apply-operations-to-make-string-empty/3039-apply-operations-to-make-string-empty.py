class Solution:
    def lastNonEmptyString(self, s: str) -> str:
        ans = ""
        freq = {}
        last = {}
        for i,ch in enumerate(s):
            last[ch]=i

        for i in s:
            if i not in freq:
                freq[i] = 1
            else:
                freq[i]+=1

        max_freq = max(freq.values())
        for j,x in enumerate(s):
            if freq[x]==max_freq and last[x]==j:

                ans+=x

        return ans        




        