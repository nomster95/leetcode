class Solution:
    def substr(self,s,k):
        if k<0:
            return 0
        l,r,count = 0,0,0
        vowels = {'a','e','i','o','u'}

        vowel = {}
        cons_count = 0
        last_seen = {v: -1 for v in vowels}

        
        while r<len(s):
            if s[r] in vowels:
                last_seen[s[r]] = r
            else:
                cons_count+=1    
            
            while cons_count>k:
                if s[l] not in vowels:
                    cons_count-=1
                l+=1

            earliest = min(last_seen.values())    

            if earliest>=l:
                count+= earliest - l +1
            r+=1

        return count                           

    def countOfSubstrings(self, word: str, k: int) -> int:
        return self.substr(word,k) - self.substr(word,k-1)
        