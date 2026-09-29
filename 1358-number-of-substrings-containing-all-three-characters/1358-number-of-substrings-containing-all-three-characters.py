class Solution:
    def numberOfSubstrings(self, s: str) -> int:
        freq = {'a':-1,'b':-1,'c':-1}
        count = 0
        n = len(s)
        for i in range(n):
            freq[s[i]] = i

            if freq['a']!=-1 and freq['b']!=-1 and freq['c']!=-1:
                count = count + (1+ min(freq.values()))

        return count        


            
        