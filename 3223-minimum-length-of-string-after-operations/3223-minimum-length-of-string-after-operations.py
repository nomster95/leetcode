class Solution:
    def minimumLength(self, s: str) -> int:
        freq = {}
        for i in s:
            if i not in freq:
                freq[i] = 1
            else:
                freq[i]+=1

        for i in freq:
            if freq[i]>2:
                while freq[i]>2:
                    freq[i]-=2


        return sum(freq.values())            

        