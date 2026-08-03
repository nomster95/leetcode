class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        
        count = 0
        vowels = set('aeiou')
        window = s[0:k]
        for i in window:
            if i in vowels:
                count+=1
        l,r = 0,k   
        max_count = count  

        while r<len(s):
            
            if s[r] in vowels:
                count+=1
            if s[l] in vowels:
                count-=1
            max_count = max(max_count,count)    
            l+=1
            r+=1

        return max_count            


        