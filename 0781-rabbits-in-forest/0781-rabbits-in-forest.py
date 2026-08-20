class Solution:
    def numRabbits(self, answers: List[int]) -> int:
        freq = {}
        rabbits = 0
        for i in answers:
            group_size = i+1
            if i not in freq:
                freq[i] = 0
            
            if freq[i]==0:
                rabbits+=group_size

            freq[i]+=1

            if freq[i]==group_size:
                freq[i] = 0

        return rabbits            


        


        
        