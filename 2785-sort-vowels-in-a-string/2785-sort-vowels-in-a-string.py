class Solution:
    def sortVowels(self, s: str) -> str:
        vowels = []
        vowel = {'a','e','i','o','u'}
        for i in s:
            if i.lower() in vowel:
                vowels.append(i)

        vowels.sort()        

        p = 0 
        ans = "" 
        for i in s:
            if i.lower() in vowel:
                ans+=vowels[p]   
                p+=1

            else:
                ans+=i       

        return ans        

         


              

        