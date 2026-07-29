class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        r = s.split()
        if len(pattern)!=len(r):
            return False
        forward = {}
        backward = {}
        for i in range(len(pattern)):
            if pattern[i] not in forward:
                forward[pattern[i]] = r[i]
            else:
                if forward[pattern[i]] != r[i]:
                    return False

            if r[i] not in backward:
                backward[r[i]] = pattern[i]    
            else:
                if backward[r[i]] != pattern[i]:
                    return False

        return True                   
        