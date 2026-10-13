class Solution:
    def totalFruit(self, fruits: list[int]) -> int:
        l,r = 0,0
        max_len = 0
        freq = {}

        while r<len(fruits):
            if fruits[r] not in freq:
                freq[fruits[r]] = 1
            else:
                freq[fruits[r]]+=1

            while len(freq)>2:
                freq[fruits[l]]-=1
                if freq[fruits[l]]==0:
                    del freq[fruits[l]]
                l+=1

            max_len = max(max_len,r-l+1)
            r+=1


        return max_len                    
        