class Solution:
    def canConstruct(self, s: str, k: int) -> bool:
        freq = {}
        if k>len(s):
            return False

        for x in s:
            if x not in freq:
                freq[x] = 1
            else:
                freq[x]+=1

        count = 0        

        for i in set(s):
            if freq[i]%2!=0:
                count+=1

        if count>k:
            return False
            
        return True            
                            
        