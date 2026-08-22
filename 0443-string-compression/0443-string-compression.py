class Solution:
    def compress(self, chars: List[str]) -> int:
        n = len(chars)
        current_char  = chars[0]
        count = 1
        ans = ""

        for i in range(1,len(chars)):
            if chars[i]==current_char:
                count+=1

            else:
                if count>1:
                    ans+=f"{current_char}{count}"
                else:
                    ans+=f"{current_char}"  

                current_char = chars[i]
                count = 1

        if count>1:
            ans+=f"{current_char}{count}" 
        else:
            ans+=f"{current_char}"       

        for i in range(len(ans)):
            chars[i] = ans[i]

            
            

        
        return len(ans)

 
               

        
        