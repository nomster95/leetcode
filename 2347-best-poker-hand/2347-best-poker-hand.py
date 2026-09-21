class Solution:
    def bestHand(self, ranks: list[int], suits: list[str]) -> str:
        freq = {}
        for i in ranks:
            if i not in freq:
                freq[i] = 1
            else:
                freq[i]+=1    
            

        if len(set(suits))==1:
            return "Flush"

        three_of_a_kind = False
        pair = False
        high = False    



        for j in freq:
            if freq[j]>=3:
                three_of_a_kind = True
            elif freq[j]>=2:
                pair = True  
            elif freq[i]==1:
                high = True   

        if three_of_a_kind:
            return "Three of a Kind"
        elif pair:
            return "Pair"
        elif high:
            return "High Card"        



        