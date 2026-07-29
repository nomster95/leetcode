class Solution:
    def findAndReplacePattern(self, words: List[str], pattern: str) -> List[str]:
        ans = []
        
        for j in words:
            forward = {}
            backward = {}
            is_valid = True
            for i in range(len(pattern)):
                if pattern[i] not in forward:
                    forward[pattern[i]] = j[i]
                else:
                    if forward[pattern[i]] != j[i]:
                        is_valid = False
                        break

                if j[i] not in backward:
                    backward[j[i]] = pattern[i]    
                else:
                    if backward[j[i]] != pattern[i]:
                        is_valid = False 
                        break     
                    
            if is_valid:
                ans.append(j)

        return ans        