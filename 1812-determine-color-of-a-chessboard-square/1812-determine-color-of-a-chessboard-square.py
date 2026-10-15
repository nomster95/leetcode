class Solution:
    def squareIsWhite(self, coordinates: str) -> bool:
        black = {'a','c','e','g'}
        char = coordinates[0]
        num = int(coordinates[1])
        if char in black:
            if num%2==0:
                return True
            else:
                return False
        else:
            if num%2==0:
                return False
            else:
                return True                