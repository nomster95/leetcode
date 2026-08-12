class Solution:
    def findLUSlength(self, strs: List[str]) -> int:
        ans = -1

        for i in range(len(strs)):
            sub = True
            for j in range(len(strs)):
                if i==j:
                    continue
                candidate = strs[i]
                other = strs[j] 
                p = 0

                for char in other:
                    if p < len(candidate) and candidate[p] == char:
                        p += 1

                if p == len(candidate):
                    sub = False
                    break

            if sub:
                length = len(strs[i])
                ans = max(ans,length)

        return ans    


                    
    

                    

                
            

                  


          

          

                    

        