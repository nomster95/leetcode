class Solution:
    def sortVowels(self, s: str) -> str:
        index = []
        freq = {}
        s = list(s)
        for i in range(len(s)):
            if s[i] in 'aeiou' and s[i] not in freq:
                freq[s[i]] = 1
                index.append(i)
            elif s[i] in 'aeiou' and s[i] in freq:
                freq[s[i]]+=1
                index.append(i)

        ans = dict(sorted(freq.items() , key = lambda x: x[1] , reverse = True))
        j = 0
        for i in ans:
            while freq[i]!=0:
                s[index[j]] = i
                freq[i]-=1
                j+=1

        return "".join(s)       
       


          
        




        