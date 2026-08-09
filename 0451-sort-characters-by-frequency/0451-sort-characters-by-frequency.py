class Solution:
    def frequencySort(self, s: str) -> str:
        freq = {}
        sol = ""

        for i in s:
            if i not in freq:
                freq[i] = 1
            else:
                freq[i]+=1
        

        ans = sorted(freq.items(),key = lambda x: x[1] ,reverse = True)
        
        for char,i in ans:
            sol+=char*i

        return sol    
            


    


        