class Solution:
    def numSteps(self, s: str) -> int:
        p2 = 1
        num = 0
        for i in range(len(s)-1,-1,-1):
            if s[i]=="1":
                num = num + p2
            p2 = p2*2

        steps = 0    

        while num>1:
            if num%2!=0:
                num+=1
                steps+=1
            else:
                num = num>>1
                steps+=1     

        return steps           


        