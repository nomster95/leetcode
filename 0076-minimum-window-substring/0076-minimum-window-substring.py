class Solution:
    def minWindow(self, s: str, t: str) -> str:
        freq = {}
        l,r = 0,0
        minLen = float('inf')
        sIndex = -1
        count = 0
        for i in t:
            if i not in freq:
                freq[i] = 1
            else:
                freq[i]+=1

        while r<len(s):
            if s[r] in freq and freq[s[r]]>0:
                count+=1

            if s[r] in freq:    
                freq[s[r]]-=1

            while count==len(t):
                if (r-l+1)<minLen:
                    minLen = r-l+1
                    sIndex = l

                removed = s[l] 

                if removed in freq:   
                    freq[removed]+=1
                    
                    if freq[removed]>0:
                        count-=1

                l+=1

            r+=1    

        if sIndex==-1:
            return ""

        return s[sIndex:sIndex+minLen]                

        