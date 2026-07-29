class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        forward = {}
        backward = {}
        for i in range(len(s)):
            if s[i] not in forward:
                forward[s[i]] = t[i]
            else:
                if forward[s[i]] != t[i]:
                    return False

            if t[i] not in backward:
                backward[t[i]] = s[i]    
            else:
                if backward[t[i]] != s[i]:
                    return False      
                    
        return True