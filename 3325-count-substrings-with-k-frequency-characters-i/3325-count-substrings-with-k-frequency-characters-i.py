class Solution:
    def numberOfSubstrings(self, s: str, k: int) -> int:
        ans = 0
        for i in range(len(s)):
            freq = {}
            for j in range(i,len(s)):
                if s[j] not in freq:
                    freq[s[j]] = 1
                else:
                    freq[s[j]]+=1

                if freq[s[j]]>=k:
                    ans+= len(s)-j
                    break
                        

                
        return ans            

        
        