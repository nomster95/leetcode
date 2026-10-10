class Solution:
    def longestContinuousSubstring(self, s: str) -> int:
        max_len = 1
        run = 1
        for i in range(len(s)-1):
            if ord(s[i+1])-ord(s[i])==1:
                run+=1
            else:
                run = 1

            max_len = max(max_len,run)

        return max_len            
        