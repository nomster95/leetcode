class Solution:
    def minChanges(self, s: str) -> int:
        count = 0
        for i in range(0,len(s),2):
            part = s[i:i+2]
            for j in range(len(part)-1):
                if part[j]!=part[j+1]:
                    count+=1


        return count            



        