class Solution:
    def numberOfSpecialChars(self, word: str) -> int:
        last_lower = {}
        first_upper = {}
        count = 0
        for i,val in enumerate(word):
            if val.islower():
                last_lower[val] = i
            else:
                if val not in first_upper:
                    first_upper[val] = i    

        for x in last_lower:
            if x.upper() in first_upper:
                if last_lower[x]<first_upper[x.upper()]:
                    count+=1

        return count              
             





                    




            
        