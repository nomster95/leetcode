class Solution:
    def isHappy(self, n: int) -> bool:
        seen = set()
        happy = 0
        while(True):
            if(n==1):
                return True
            elif(n in seen):
                return False
            seen.add(n)
            happy = 0        
            while(n>0):
                sq = n%10
                happy = happy + sq**2
                n = n//10
            n = happy
        