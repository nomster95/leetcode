class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        ans = set()
        l,r = 0,0
        longest = 0
        while(l<=r and r<len(s)):
            if s[r] not in ans:
                ans.add(s[r])
                w = r-l+1
                longest = max(longest,w)
                r+=1
            else:
                ans.remove(s[l])    
                l+=1

        return longest        
        