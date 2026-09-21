class Solution:
    def longestBalanced(self, s: str) -> int:
        max_len = 0
        
        for i in range(len(s)):
            sub_len = 0
            freq = {}
            for j in range(i,len(s)):
                freq[s[j]] = freq.get(s[j], 0) + 1
                if len(set(freq.values()))==1:    

                    max_len = max(max_len,j-i+1) 

        return max_len                        
                        



                


        