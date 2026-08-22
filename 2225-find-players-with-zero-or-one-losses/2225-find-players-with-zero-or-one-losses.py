class Solution:
    def findWinners(self, matches: List[List[int]]) -> List[List[int]]:
        win = {}
        loss = {}
        winner = []
        loser = []
        for i in matches:
            if i[0] not in win:
                win[i[0]] = 1
            else:
                win[i[0]]+=1

            if i[1] not in loss:
                loss[i[1]]=1
            else:
                loss[i[1]]+=1

        for i in win:
            if i not in loss:
                winner.append(i)

        for i in loss:
            if loss[i]==1:
                loser.append(i) 

        winner.sort()
        loser.sort()           

        return [winner,loser]            



        
        