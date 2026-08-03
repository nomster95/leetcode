class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        k = len(s1)
        window = s2[:k]
        l,r = 0,k
        target = {}
        windows = {}
        for i in s1:
            if i not in target:
                target[i] = 1
            else:
                target[i]+=1
        for i in window:
            if i not in windows:
                windows[i] = 1
            else:
                windows[i]+=1
        if target == windows:
            return True

        while r<len(s2):
            if s2[r] not in windows:
                windows[s2[r]] = 1
            else:
                windows[s2[r]]+=1
            windows[s2[l]]-=1
            if windows[s2[l]]==0:
                del windows[s2[l]]     
            if target==windows:
                return True
            l+=1
            r+=1
        return False                                          
        