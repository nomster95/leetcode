class Solution:
    def minimumRounds(self, tasks: list[int]) -> int:
        freq = {}
        ans = []
        ops = 0
        length = 0
        for i in tasks:
            if i not in freq:
                freq[i] = 1
            else:
                freq[i]+=1

        for j in freq:
            if freq[j]==1:
                return -1
            elif freq[j]%3==0:
                ops+=freq[j]//3
            elif freq[j]%3==1:
                freq[j]-=4
                ops+=2
                ops+=freq[j]//3
            elif freq[j]%3==2:
                freq[j]-=2
                ops+=1
                ops+=freq[j]//3
            

        return ops   
        