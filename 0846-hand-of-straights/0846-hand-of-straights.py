class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        if len(hand)%groupSize!=0:
            return False

        hand.sort()
        freq = {}
        for i in hand:
            if i not in freq:
                freq[i] = 1
            else:
                freq[i]+=1

        for i in hand:
            if freq[i]==0:
                continue

            need = freq[i]
            for x in range(i,i+groupSize):
                if freq.get(x,0)<need:
                    return False

                freq[x]-=need

        return True        

        