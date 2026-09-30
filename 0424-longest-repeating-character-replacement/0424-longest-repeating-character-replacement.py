class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        l,r = 0,0
        freq = {}
        max_len = 0
        max_freq = 0
        while r<len(s):
            if s[r] not in freq:
                freq[s[r]] = 1
            else:
                freq[s[r]]+=1    

            max_freq = max(max_freq,freq[s[r]])
            if (r-l+1)-max_freq>k:
                freq[s[l]]-=1
                l = l+1

            if (r-l+1)-max_freq<=k:
                max_len = max(max_len,r-l+1)

            r+=1

        return max_len            

        