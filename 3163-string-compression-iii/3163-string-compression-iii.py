class Solution:
    def compressedString(self, word: str) -> str:
        current_char  = word[0]
        count = 1
        ans = ""

        for i in range(1,len(word)):
            if word[i]==current_char:
                count+=1

            else:
                while  count>9:
                    ans+=f"{9}{current_char}" 
                    count-=9
                ans+=f"{count}{current_char}" 
                current_char = word[i]
                count = 1

        while count>9:
            ans+=f"{9}{current_char}"
            count-=9
        ans+=f"{count}{current_char}" 
        
        return ans    
        
        