class Solution:
    def queensAttacktheKing(self, queens: list[list[int]], king: list[int]) -> list[list[int]]:
        attackers = []
        kr, kc = king[0],king[1]

        directions = [(-1,-1),(-1,0),(-1,1),
                       (0,-1),       (0,1),
                       (1,-1),(1,0),(1,1)]
                     
        queen_set  = set(map(tuple,queens))       
        for dr,dc in directions:
            r = dr + kr
            c = dc + kc

            while 0<=r<8 and 0<=c<8:
                if (r,c) in queen_set:
                    attackers.append([r,c])
                    break


                r+=dr
                c+=dc

        return attackers             


        
        