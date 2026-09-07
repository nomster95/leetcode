class Solution:
    def matchPlayersAndTrainers(self, players: List[int], trainers: List[int]) -> int:
        n = len(players)
        m = len(trainers)
        l,r = 0,0
        players.sort()
        trainers.sort()
        while l<n and r<m:
            if trainers[r]>=players[l]:
                r+=1
                l+=1
            else:
                r+=1    

        return l     
        
        