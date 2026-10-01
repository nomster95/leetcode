class Solution:
    def maximumLengthSubstring(self, s: str) -> int:
        l,r = 0,0
        max_len = 0
        freq = {}
        while r<len(s):
            if s[r] not in freq:
                freq[s[r]] = 1
            else:
                freq[s[r]]+=1

            while freq[s[r]]>2:
                freq[s[l]]-=1
                l+=1

            max_len = max(max_len,r-l+1)
            r+=1

        return max_len            

        