class Solution:
    def toGoatLatin(self, sentence: str) -> str:
        words = sentence.split()
        for i in range(len(words)):
            if words[i][0] in "aeiouAEIOU":
                words[i]+="ma"
                words[i]+="a"*(i+1)
            else:  
                new_word = words[i][1:] + words[i][0] + "ma" + "a" * (i + 1)
                words[i] = new_word

        return " ".join(words)            

                


        