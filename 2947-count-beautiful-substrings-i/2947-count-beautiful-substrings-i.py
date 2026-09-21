class Solution:
    def beautifulSubstrings(self, s: str, k: int) -> int:
        ans = 0
        for i in range(len(s)):
            vowel = 0
            consonant = 0
            for j in range(i,len(s)):
                if s[j] in "aeiou":
                    vowel+=1
                else:
                    consonant+=1

                if vowel==consonant and (vowel*consonant)%k==0:
                    
                    ans+=1

        return ans            




        