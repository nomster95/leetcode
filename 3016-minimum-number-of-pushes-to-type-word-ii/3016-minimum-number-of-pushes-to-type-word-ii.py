class Solution:
    def minimumPushes(self, word: str) -> int:
        pushes = 0
        count = 1
        mul = 1
        freq = {}
        for i in word:
            if i not in freq:
                freq[i] = 1
            else:
                freq[i]+=1

        ans = dict(sorted(freq.items() , key=lambda x: x[1] , reverse=True))
        for x in ans:
            mul = ((count-1)//8)+1
            pushes+=(freq[x]*mul)
            count+=1

        return pushes    



                    
        
        