class Solution:
    def maxFreq(self, s: str, maxLetters: int, minSize: int, maxSize: int) -> int:
        occur = {}
        freq = {}
        l,r = 0,0
        while r<len(s):
            if s[r] not in freq:
                freq[s[r]] = 1
            else:
                freq[s[r]]+=1

            win_size = r-l+1    

            if win_size>minSize:
                freq[s[l]]-=1
                if freq[s[l]]==0:
                    del freq[s[l]]
                l+=1   

            if r-l+1==minSize and len(freq)<=maxLetters:
                x = s[l:r+1]
                if x not in occur:
                    occur[x] = 1
                else:
                    occur[x]+=1  

            r+=1  

        if len(occur)==0:
            return 0            

        return max(occur.values())        



        