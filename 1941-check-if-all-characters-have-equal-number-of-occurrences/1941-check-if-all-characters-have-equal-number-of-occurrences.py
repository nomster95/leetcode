class Solution:
    def areOccurrencesEqual(self, s: str) -> bool:
        freq = {}
        ans = set()
        for i in s:
            if i not in freq:
                freq[i] = 1
            else:
                freq[i]+=1

        for i in freq:
            ans.add(freq[i])

        if len(ans)==1:
            return True
        return False        
                  

              


        