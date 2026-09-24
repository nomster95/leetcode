class Solution:
    def maximumLength(self, s: str) -> int:
        max_len = -1
        freq = {}
        for i in range(len(s)):
            for j in range(i,len(s)):
                if len(set(s[i:j+1]))==1:
                    if s[i:j+1] not in freq:
                        freq[s[i:j+1]] = 1
                    else:
                        freq[s[i:j+1]]+=1    

        for x in freq:
            if freq[x]>=3:
                max_len = max(max_len,len(x))

        return max_len        


        