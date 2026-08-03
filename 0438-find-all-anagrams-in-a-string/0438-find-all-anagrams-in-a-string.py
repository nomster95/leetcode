class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        ans = []
        target = {}
        window = {}
        window_length = len(p)
        l,r = 0,window_length
        for i in p:
            if i not in target:
                target[i] = 1
            else:
                target[i]+=1    
        for i in s[0:window_length]:
            if i not in window:
                window[i] = 1
            else:
                window[i]+=1

        if target==window:
            ans.append(0)

        while r<len(s):
            if s[r] not in window:
                window[s[r]]=1
            else:
                window[s[r]]+=1    
            
            window[s[l]]-=1
            if window[s[l]]==0:
                del window[s[l]]  
            l+=1
            r+=1    
            if window==target:
                ans.append(l)   

        return ans       

            