class Solution:
    def minSteps(self, s: str, t: str) -> int:
        freq1 = {}
        freq2 = {}
        for i in s:
            if i not in freq1:
                freq1[i]=1
            else:
                freq1[i]+=1

        for i in t:
            if i not in freq2:
                freq2[i]=1
            else:
                freq2[i]+=1

        ans = 0        

        for i in set(t):
            if i in s:

                if freq1[i]<freq2[i]:
                    diff = freq2[i]-freq1[i]
                    ans+=diff
            else:
                ans+=freq2[i]       

        return ans     



                                 

        