class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        freq = {}
        for i in s:
            if(i not in freq):
                freq[i] = 1
            else:
                freq[i]+=1

        for i in t:
            if(i in freq):
                freq[i]-=1
            else:
                freq[i] = 1    

        for st in freq:
            if(freq[st] != 0):
                return st               

            


        