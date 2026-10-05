class Solution:
    def judgeCircle(self, moves: str) -> bool:
        vertical = 0
        horizontal = 0
        for i in moves:
            if i=="U":
                vertical+=1
            elif i=="D":
                vertical-=1
            elif i=="L":
                horizontal-=1
            else:
                horizontal+=1

        if vertical==0 and horizontal==0:
            return True

        return False
                                
        