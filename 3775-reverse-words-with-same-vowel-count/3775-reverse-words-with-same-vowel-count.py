class Solution:
    def reverseWords(self, s: str) -> str:
        words = s.split()
        vowel1 = 0
        for i in words[0]:
            if i in "aeiou":
                vowel1+=1

        for i in range(1,len(words)):
            vowel_count = 0
            for j in words[i]:
                if j in "aeiou":
                    vowel_count+=1

            if vowel1==vowel_count:
                rev = words[i][::-1]
                words[i] = rev

        return (" ").join(words)        


        