class Solution:
    def minSteps(self, s: str, t: str) -> int:
        ans = 0
        freq1 = {}
        freq2 = {}
        for i in s:
            if i not in freq1:
                freq1[i] = 1
            else:
                freq1[i]+=1

        for i in t:
            if i not in freq2:
                freq2[i]=1
            else:
                freq2[i]+=1

        for ch in set(freq1) | set(freq2):

            diff = abs(freq1.get(ch, 0) - freq2.get(ch, 0))  
            ans+=diff  

        return ans                        
        