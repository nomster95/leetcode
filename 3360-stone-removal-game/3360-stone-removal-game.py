class Solution:
    def canAliceWin(self, n: int) -> bool:
        if n<10:
            return False

        x = n
        sub = 10
        while True:
            if x>=sub:
                x-=sub
                sub-=1
            else:
                break

        if sub%2==0:
            return False
        else:
            return True                

            
            
                
        